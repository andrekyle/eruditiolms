from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
from flask_migrate import Migrate
from urllib.parse import urlparse
from functools import wraps
from werkzeug.utils import secure_filename
import json

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Curated model answers for the SAQA 118792 AISD course (staff-only page).
# Imported at module load so that Vercel's bundler always includes the file.
try:
    from _saqa_aisd_answers import LAB_ANSWERS as SAQA_LAB_ANSWERS
except Exception:  # pragma: no cover — fall back to empty dict if missing
    SAQA_LAB_ANSWERS = {}

app = Flask(__name__)

# Make sure the instance folder exists — used for the SQLite DB AND the
# persisted secret key below. On read-only hosts (e.g. Vercel serverless
# functions where /var/task is read-only) this can fail; ignore in that case
# and rely on env-based SECRET_KEY + external DATABASE_URL.
try:
    os.makedirs(app.instance_path, exist_ok=True)
except OSError:
    pass

# SECRET_KEY: prefer env var; otherwise persist a generated key to
# instance/.secret_key so logged-in sessions survive app restarts.
# (Previously we used os.urandom() on every boot, which invalidated every
# session cookie and forced everyone to log in again.)
def _load_or_create_secret_key():
    env_key = os.environ.get('SECRET_KEY')
    if env_key:
        return env_key
    key_path = os.path.join(app.instance_path, '.secret_key')
    try:
        if os.path.exists(key_path):
            with open(key_path, 'r', encoding='utf-8') as f:
                k = f.read().strip()
                if k:
                    return k
        k = os.urandom(32).hex()
        with open(key_path, 'w', encoding='utf-8') as f:
            f.write(k)
        try:
            os.chmod(key_path, 0o600)
        except Exception:
            pass
        return k
    except Exception:
        # Fall back to ephemeral key if we can't write to disk.
        return os.urandom(32).hex()

app.config['SECRET_KEY'] = _load_or_create_secret_key()

# Database: prefer DATABASE_URL (e.g. Supabase Postgres), fall back to local SQLite.
# For the SQLite fallback we use an ABSOLUTE path under the instance folder so
# the same lms.db is used no matter what cwd the app is launched from.
_default_sqlite_path = os.path.join(app.instance_path, 'lms.db').replace('\\', '/')
# `or` (not `.get(default)`) so that DATABASE_URL="" is treated as unset.
_db_url = os.environ.get('DATABASE_URL') or f'sqlite:///{_default_sqlite_path}'
# SQLAlchemy 1.4+ requires postgresql:// scheme (not postgres://)
if _db_url.startswith('postgres://'):
    _db_url = _db_url.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = _db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Pooled Postgres (Supabase pgbouncer/pooler) drops idle connections; enable
# pre-ping + short recycle so SQLAlchemy never hands out a dead connection.
if _db_url.startswith('postgresql'):
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_pre_ping': True,
        'pool_recycle': 280,
        'pool_size': 5,
        'max_overflow': 5,
        'connect_args': {'connect_timeout': 10, 'keepalives': 1,
                         'keepalives_idle': 30, 'keepalives_interval': 10,
                         'keepalives_count': 3},
    }

# Optional Supabase client config (for storage/auth/REST features)
app.config['SUPABASE_URL'] = os.environ.get('SUPABASE_URL')
app.config['SUPABASE_KEY'] = os.environ.get('SUPABASE_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = None

# Models
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('student_id', 'course_id'),)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255))
    is_teacher = db.Column(db.Boolean, default=False)
    is_superadmin = db.Column(db.Boolean, default=False)
    # Canonical role: 'superuser' | 'admin' | 'teacher' | 'student'
    role = db.Column(db.String(20), default='student', nullable=False)
    full_name = db.Column(db.String(120))
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    bio = db.Column(db.Text)
    phone = db.Column(db.String(40))
    location = db.Column(db.String(120))
    avatar_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    enrollments = db.relationship('Enrollment', backref='student', lazy=True)
    courses = db.relationship('Course', backref='teacher', lazy=True)
    student_progress = db.relationship('StudentProgress', backref='student', lazy=True)
    quiz_responses = db.relationship('QuizResponse', backref='student', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Role helpers — keep is_teacher / is_superadmin in sync with role
    @property
    def is_superuser(self):
        return self.role == 'superuser'
    @property
    def is_admin(self):
        return self.role == 'admin'
    @property
    def is_student(self):
        return self.role == 'student'
    def apply_role(self, role):
        """Set role and derive legacy boolean flags."""
        role = (role or 'student').lower()
        if role not in {'superuser', 'admin', 'teacher', 'student'}:
            role = 'student'
        self.role = role
        # Permissions matrix:
        #  superuser → full power (admin + teach)
        #  admin     → user/site management only (no teaching)
        #  teacher   → can create courses, cannot manage users
        #  student   → can enroll only
        self.is_superadmin = role in {'superuser', 'admin'}
        self.is_teacher = role in {'superuser', 'teacher'}

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    badge_url = db.Column(db.String(255))
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    lessons = db.relationship('Lesson', backref='course', lazy=True, cascade='all, delete-orphan')
    quizzes = db.relationship('Quiz', backref='course', lazy=True, cascade='all, delete-orphan')
    enrollments = db.relationship('Enrollment', backref='course', lazy=True, cascade='all, delete-orphan')
    student_progress = db.relationship('StudentProgress', backref='course', lazy=True, cascade='all, delete-orphan')

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False, default='')
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    # Content type: 'lesson' (read), 'video' (watch), 'task' (submit), 'exam' (quiz)
    content_type = db.Column(db.String(20), nullable=False, default='lesson')
    video_url = db.Column(db.String(500))
    task_instructions = db.Column(db.Text)
    # Teacher/admin-only model answer for practical labs & tasks.
    # Rendered on /teacher/lab-answers; never shown to students.
    model_answer = db.Column(db.Text)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=True)
    order = db.Column(db.Integer, default=0)
    points = db.Column(db.Float, default=1.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    exam_quiz = db.relationship('Quiz', foreign_keys=[quiz_id])
    completions = db.relationship('LessonCompletion', backref='lesson', lazy=True, cascade='all, delete-orphan')
    submissions = db.relationship('TaskSubmission', backref='lesson', lazy=True, cascade='all, delete-orphan')


class LessonCompletion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('student_id', 'lesson_id'),)


class TaskSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    submission_text = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    grade = db.Column(db.Float)
    feedback = db.Column(db.Text)


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    questions = db.relationship('Question', backref='quiz', lazy=True, cascade='all, delete-orphan')
    quiz_responses = db.relationship('QuizResponse', backref='quiz', lazy=True, cascade='all, delete-orphan')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    question_type = db.Column(db.String(50), nullable=False)  # multiple_choice, true_false, matching, drag_and_drop, image_drag_drop
    question_html = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))  # URL to the uploaded image
    points = db.Column(db.Float, default=1.0)
    feedback = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    options = db.relationship('QuestionOption', backref='question', lazy=True, cascade='all, delete-orphan')
    student_responses = db.relationship('QuestionResponse', backref='question', lazy=True, cascade='all, delete-orphan')

class QuestionOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    option_html = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer)
    matching_answer = db.Column(db.Text)
    drag_zone = db.Column(db.String(50))  # For drag and drop questions: source or target
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class QuestionResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_response_id = db.Column(db.Integer, db.ForeignKey('quiz_response.id'), nullable=False)
    points = db.Column(db.Float)
    is_correct = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    selected_options = db.relationship('QuestionOption', secondary='question_response_option', backref='responses')

class QuestionResponseOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    response_id = db.Column(db.Integer, db.ForeignKey('question_response.id'), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('question_option.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class QuizResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    points = db.Column(db.Float)
    total_points = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    question_responses = db.relationship('QuestionResponse', backref='quiz_response', lazy=True, cascade='all, delete-orphan')

class StudentProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    points_earned = db.Column(db.Float, default=0)
    total_points = db.Column(db.Float, default=0)
    last_activity = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('student_id', 'course_id'),)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def requires_superadmin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_superadmin:
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

def requires_superuser(f):
    """Stricter than requires_superadmin: only the top-tier Super User role."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or (current_user.role or '') != 'superuser':
            flash('Only a Super User can perform that action.', 'danger')
            return redirect(url_for('manage_users') if current_user.is_authenticated else url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def requires_staff(f):
    """Allow teachers, admins and superusers (any non-student role)."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        ok = False
        if current_user.is_authenticated:
            role = (getattr(current_user, 'role', '') or '').lower()
            ok = (role in {'teacher', 'admin', 'superuser'}
                  or current_user.is_teacher
                  or current_user.is_superadmin)
        if not ok:
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('index') if current_user.is_authenticated else url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def auto_enroll_teacher(user):
    """Ensure a teacher (or admin/superuser) is enrolled in every course.
    Creates any missing Enrollment rows. Safe to call repeatedly."""
    if not user or user.role not in ('teacher', 'admin', 'superuser'):
        return 0
    existing = {e.course_id for e in Enrollment.query.filter_by(student_id=user.id).all()}
    added = 0
    for c in Course.query.all():
        if c.id in existing:
            continue
        db.session.add(Enrollment(student_id=user.id, course_id=c.id))
        added += 1
    if added:
        db.session.commit()
    return added

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember', False)
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user, remember=remember)
            auto_enroll_teacher(user)
            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('auth/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = (request.form.get('username') or '').strip()
        email = (request.form.get('email') or '').strip()
        password = request.form.get('password') or ''
        is_teacher = bool(request.form.get('is_teacher'))

        if not username or not email or not password:
            flash('Username, email and password are required.', 'danger')
        elif len(password) < 6:
            flash('Password must be at least 6 characters.', 'danger')
        elif User.query.filter_by(username=username).first():
            flash('That username is already taken.', 'danger')
        elif User.query.filter_by(email=email).first():
            flash('That email is already in use.', 'danger')
        else:
            u = User(username=username, email=email, full_name=username)
            u.apply_role('teacher' if is_teacher else 'student')
            u.set_password(password)
            db.session.add(u)
            db.session.commit()
            login_user(u)
            auto_enroll_teacher(u)
            flash('Account created. Welcome!', 'success')
            return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/manage/users')
@login_required
@requires_superadmin
def manage_users():
    users = User.query.all()
    return render_template('admin/manage_users.html', users=users)

@app.route('/manage/users/create', methods=['GET', 'POST'])
@login_required
@requires_superuser
def create_user():
    if request.method == 'POST':
        username = (request.form.get('username') or '').strip()
        email    = (request.form.get('email') or '').strip()
        password = request.form.get('password') or ''
        first    = (request.form.get('first_name') or '').strip()
        last     = (request.form.get('last_name') or '').strip()
        role     = (request.form.get('role') or 'student').strip().lower()

        if not username or not email or not password:
            flash('Username, email and password are required.', 'danger')
        elif role not in {'superuser', 'admin', 'teacher', 'student'}:
            flash('Invalid role.', 'danger')
        elif User.query.filter_by(username=username).first():
            flash('That username is already taken.', 'danger')
        elif User.query.filter_by(email=email).first():
            flash('That email is already in use.', 'danger')
        else:
            u = User(username=username, email=email,
                     first_name=first, last_name=last,
                     full_name=(first + ' ' + last).strip() or username)
            u.apply_role(role)
            u.set_password(password)
            db.session.add(u)
            db.session.commit()
            flash(f'User "{username}" created.', 'success')
            return redirect(url_for('manage_users'))

    return render_template('users/create.html')

@app.route('/manage/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
@requires_superuser
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        username = (request.form.get('username') or '').strip()
        email    = (request.form.get('email') or '').strip()
        first    = (request.form.get('first_name') or '').strip()
        last     = (request.form.get('last_name') or '').strip()
        phone    = (request.form.get('phone') or '').strip()
        location = (request.form.get('location') or '').strip()
        bio      = (request.form.get('bio') or '').strip()
        role     = (request.form.get('role') or user.role or 'student').strip().lower()
        new_password     = request.form.get('new_password') or ''
        confirm_password = request.form.get('confirm_password') or ''
        current_password = request.form.get('current_password') or ''

        if not username or not email:
            flash('Username and email are required.', 'danger')
        elif role not in {'superuser', 'admin', 'teacher', 'student'}:
            flash('Invalid role.', 'danger')
        elif username != user.username and User.query.filter_by(username=username).first():
            flash('That username is already taken.', 'danger')
        elif email != user.email and User.query.filter_by(email=email).first():
            flash('That email is already in use.', 'danger')
        else:
            # Prevent a Super User from demoting themselves (would lock out admin).
            if user.id == current_user.id and role != 'superuser':
                flash("You can't change your own role away from Super User.", 'warning')
                return render_template('users/edit.html', user=user)

            # Avatar upload (optional)
            avatar_file = request.files.get('avatar')
            if avatar_file and avatar_file.filename:
                allowed_ext = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
                ext = avatar_file.filename.rsplit('.', 1)[-1].lower() if '.' in avatar_file.filename else ''
                if ext not in allowed_ext:
                    flash('Avatar must be a PNG, JPG, GIF, or WEBP image.', 'danger')
                    return render_template('users/edit.html', user=user)
                filename = secure_filename(f"avatar_{user.id}_{int(datetime.utcnow().timestamp())}.{ext}")
                upload_path = os.path.join(app.static_folder, 'uploads', 'avatars')
                try:
                    os.makedirs(upload_path, exist_ok=True)
                    avatar_file.save(os.path.join(upload_path, filename))
                    user.avatar_url = url_for('static', filename=f'uploads/avatars/{filename}')
                except OSError:
                    # Read-only filesystem (e.g. Vercel serverless).
                    flash('Avatar upload is disabled in this environment; other changes were saved.', 'warning')

            # Remove avatar if requested
            if request.form.get('remove_avatar') == '1':
                user.avatar_url = None

            # Password change (optional). Super User can reset without knowing the current one.
            if new_password or confirm_password:
                if new_password != confirm_password:
                    flash('New passwords do not match.', 'danger')
                    return render_template('users/edit.html', user=user)
                if len(new_password) < 4:
                    flash('New password is too short.', 'danger')
                    return render_template('users/edit.html', user=user)
                user.set_password(new_password)

            user.username = username
            user.email = email
            user.first_name = first
            user.last_name = last
            user.full_name = (first + ' ' + last).strip() or username
            user.phone = phone
            user.location = location
            user.bio = bio
            user.apply_role(role)
            db.session.commit()
            flash(f'User "{username}" updated.', 'success')
            return redirect(url_for('manage_users'))

    return render_template('users/edit.html', user=user)

@app.route('/manage/users/<int:user_id>/delete', methods=['POST'])
@login_required
@requires_superuser
def delete_user(user_id):
    if user_id == current_user.id:
        flash("You can't delete your own account.", 'warning')
        return redirect(url_for('manage_users'))
    user = User.query.get_or_404(user_id)
    # Protect superusers from being deleted by anyone (only allowed via DB).
    if user.role == 'superuser':
        flash("Super users cannot be deleted from the UI.", 'danger')
        return redirect(url_for('manage_users'))
    # Block deletion of users that own content (would cascade-fail otherwise).
    if user.courses:
        flash(f'Cannot delete "{user.username}" \u2014 they own {len(user.courses)} course(s). Reassign first.', 'danger')
        return redirect(url_for('manage_users'))
    name = user.username

    # Manually clean up related rows (no DB cascade configured).
    # Quiz responses -> question responses -> question response options
    qrs = QuizResponse.query.filter_by(user_id=user.id).all()
    for qr in qrs:
        for qresp in QuestionResponse.query.filter_by(quiz_response_id=qr.id).all():
            QuestionResponseOption.query.filter_by(response_id=qresp.id).delete(synchronize_session=False)
            db.session.delete(qresp)
        db.session.delete(qr)
    # Stray question responses (defensive)
    for qresp in QuestionResponse.query.filter_by(user_id=user.id).all():
        QuestionResponseOption.query.filter_by(response_id=qresp.id).delete(synchronize_session=False)
        db.session.delete(qresp)
    # Lesson completions, task submissions, student progress, enrollments
    LessonCompletion.query.filter_by(student_id=user.id).delete(synchronize_session=False)
    TaskSubmission.query.filter_by(student_id=user.id).delete(synchronize_session=False)
    StudentProgress.query.filter_by(student_id=user.id).delete(synchronize_session=False)
    Enrollment.query.filter_by(student_id=user.id).delete(synchronize_session=False)
    db.session.flush()

    db.session.delete(user)
    db.session.commit()
    flash(f'User "{name}" deleted.', 'success')
    return redirect(url_for('manage_users'))

@app.route('/user/<int:user_id>/change-password', methods=['GET', 'POST'])
@login_required
def change_password(user_id):
    # Only allow users to change their own password or superadmin to change any password
    if user_id != current_user.id and not current_user.is_superadmin:
        flash('You do not have permission to change this password.', 'danger')
        return redirect(url_for('index'))
    
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        
        if user_id == current_user.id and not user.check_password(current_password):
            flash('Current password is incorrect.', 'danger')
        elif new_password != confirm_password:
            flash('New passwords do not match.', 'danger')
        else:
            user.set_password(new_password)
            db.session.commit()
            flash('Password updated successfully.', 'success')
            return redirect(url_for('index'))
    
    return render_template('auth/change_password.html', user=user)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = current_user
    if request.method == 'POST':
        username = (request.form.get('username') or '').strip()
        email = (request.form.get('email') or '').strip()
        first_name = (request.form.get('first_name') or '').strip()
        last_name = (request.form.get('last_name') or '').strip()
        bio = (request.form.get('bio') or '').strip()
        phone = (request.form.get('phone') or '').strip()
        location = (request.form.get('location') or '').strip()
        new_password = request.form.get('new_password') or ''
        confirm_password = request.form.get('confirm_password') or ''
        current_password = request.form.get('current_password') or ''

        if not username or not email:
            flash('Username and email are required.', 'danger')
            return render_template('profile.html', user=user)

        # Uniqueness checks (only if changed)
        if username != user.username and User.query.filter_by(username=username).first():
            flash('That username is already taken.', 'danger')
            return render_template('profile.html', user=user)
        if email != user.email and User.query.filter_by(email=email).first():
            flash('That email is already in use.', 'danger')
            return render_template('profile.html', user=user)

        # Avatar upload (optional)
        avatar_file = request.files.get('avatar')
        if avatar_file and avatar_file.filename:
            allowed_ext = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
            ext = avatar_file.filename.rsplit('.', 1)[-1].lower() if '.' in avatar_file.filename else ''
            if ext not in allowed_ext:
                flash('Avatar must be a PNG, JPG, GIF, or WEBP image.', 'danger')
                return render_template('profile.html', user=user)
            filename = secure_filename(f"avatar_{user.id}_{int(datetime.utcnow().timestamp())}.{ext}")
            upload_path = os.path.join(app.static_folder, 'uploads', 'avatars')
            try:
                os.makedirs(upload_path, exist_ok=True)
                avatar_file.save(os.path.join(upload_path, filename))
                user.avatar_url = url_for('static', filename=f'uploads/avatars/{filename}')
            except OSError:
                # Read-only filesystem (e.g. Vercel serverless). Skip the
                # upload but let the rest of the profile update proceed.
                flash('Avatar upload is disabled in this environment; other changes were saved.', 'warning')

        # Remove avatar if requested
        if request.form.get('remove_avatar') == '1':
            user.avatar_url = None

        # Password change (optional) — only triggered when the user actually
        # enters a new password. Browser autofill of the current password field
        # should not force a password change.
        if new_password or confirm_password:
            if not user.check_password(current_password):
                flash('Current password is incorrect.', 'danger')
                return render_template('profile.html', user=user)
            if new_password != confirm_password:
                flash('New passwords do not match.', 'danger')
                return render_template('profile.html', user=user)
            if len(new_password) < 4:
                flash('New password is too short.', 'danger')
                return render_template('profile.html', user=user)
            user.set_password(new_password)

        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.full_name = (first_name + ' ' + last_name).strip()
        user.bio = bio
        user.phone = phone
        user.location = location
        db.session.commit()
        flash('Your profile has been updated.', 'success')
        return redirect(url_for('profile'))

    return render_template('profile.html', user=user)

@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_superadmin:
        # Superadmin sees every course in the system.
        courses = Course.query.all()
        enrolled_courses = []
    elif current_user.is_teacher:
        # Teachers see every course they're enrolled in (auto-enrolled into all by default).
        # Falls back to owned courses if (somehow) not enrolled anywhere.
        courses = [e.course for e in current_user.enrollments]
        if not courses:
            courses = Course.query.filter_by(teacher_id=current_user.id).all()
        enrolled_courses = []
    else:
        # Students see enrolled courses and available courses separately
        enrolled_courses = [enrollment.course for enrollment in current_user.enrollments]
        courses = Course.query.filter(
            ~Course.id.in_([c.id for c in enrolled_courses])
        ).all()

    # Calculate course statistics
    course_stats = {}
    all_courses = courses + ([] if current_user.is_teacher else enrolled_courses)

    # Pre-fetch this user's lesson completions and quiz responses once
    my_completed_lesson_ids = {
        c.lesson_id for c in LessonCompletion.query.filter_by(student_id=current_user.id).all()
    }
    my_quiz_responses = QuizResponse.query.filter_by(user_id=current_user.id).all()
    # Best (highest %) attempt per quiz_id
    best_by_quiz = {}
    attempts_by_quiz = {}
    for qr in my_quiz_responses:
        attempts_by_quiz[qr.quiz_id] = attempts_by_quiz.get(qr.quiz_id, 0) + 1
        pct = (qr.points / qr.total_points * 100.0) if qr.total_points else 0.0
        prev = best_by_quiz.get(qr.quiz_id)
        if prev is None or pct > prev['percent']:
            best_by_quiz[qr.quiz_id] = {
                'percent': pct,
                'points': qr.points or 0,
                'total_points': qr.total_points or 0,
                'taken_at': qr.created_at,
                'response_id': qr.id,
            }

    for course in all_courses:
        lessons = list(course.lessons)
        lessons_total = len(lessons)
        lessons_done = sum(1 for l in lessons if l.id in my_completed_lesson_ids)
        percent = int(round((lessons_done / lessons_total) * 100)) if lessons_total else 0

        quiz_results = []
        for quiz in course.quizzes:
            best = best_by_quiz.get(quiz.id)
            quiz_results.append({
                'id': quiz.id,
                'title': quiz.title,
                'attempts': attempts_by_quiz.get(quiz.id, 0),
                'best_percent': int(round(best['percent'])) if best else None,
                'best_points': best['points'] if best else None,
                'total_points': best['total_points'] if best else None,
                'taken_at': best['taken_at'] if best else None,
                'best_response_id': best['response_id'] if best else None,
            })

        course_stats[course.id] = {
            'student_count': len(course.enrollments),
            'quiz_count': len(course.quizzes),
            'lessons_total': lessons_total,
            'lessons_done': lessons_done,
            'percent': percent,
            'quiz_results': quiz_results,
        }

    # Distinct students across all teacher courses (don't double-count multi-enrollments,
    # and exclude teachers/admins who are auto-enrolled into every course).
    if current_user.is_teacher or current_user.is_superadmin:
        candidate_ids = {e.student_id for c in courses for e in c.enrollments}
        if candidate_ids:
            student_rows = User.query.filter(
                User.id.in_(candidate_ids),  # type: ignore[attr-defined]
                User.role == 'student',  # type: ignore[attr-defined]
            ).all()
            active_student_count = len(student_rows)
        else:
            active_student_count = 0
    else:
        active_student_count = 0

    return render_template('dashboard.html',
                         courses=courses,
                         enrolled_courses=enrolled_courses,
                         course_stats=course_stats,
                         active_student_count=active_student_count)

REPORT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CalendarResults')

@app.route('/report/')
@app.route('/report/<path:filename>')
@login_required
def report(filename='index.html'):
    """Serve the static CalendarResults report bundle."""
    full = os.path.normpath(os.path.join(REPORT_DIR, filename))
    if not full.startswith(os.path.normpath(REPORT_DIR)):
        abort(404)
    if not os.path.exists(full):
        abort(404)
    return send_from_directory(REPORT_DIR, filename)

@app.route('/my/results')
@login_required
def my_results():
    """A university-style transcript page listing every quiz attempt for the current user, grouped by course."""
    responses = (QuizResponse.query
                 .filter_by(user_id=current_user.id)
                 .order_by(QuizResponse.created_at.desc())
                 .all())

    # Group all attempts by (course_id, quiz_id)
    by_quiz = {}   # quiz_id -> list of attempts (newest first)
    quiz_meta = {} # quiz_id -> {quiz, course}
    for r in responses:
        quiz = Quiz.query.get(r.quiz_id)
        if not quiz:
            continue
        quiz_meta.setdefault(quiz.id, {'quiz': quiz, 'course': quiz.course})
        by_quiz.setdefault(quiz.id, []).append(r)

    # Build per-course summary
    courses_data = {}  # course_id -> {course, quizzes: [...], totals}
    for quiz_id, meta in quiz_meta.items():
        course = meta['course']
        quiz = meta['quiz']
        attempts = by_quiz[quiz_id]
        # Best attempt
        def _pct(a):
            return (a.points / a.total_points * 100.0) if a.total_points else 0.0
        best = max(attempts, key=_pct)
        best_pct = _pct(best)
        latest = attempts[0]  # already ordered desc
        quiz_entry = {
            'quiz_id': quiz.id,
            'title': quiz.title,
            'attempts_count': len(attempts),
            'best_points': best.points or 0,
            'best_total': best.total_points or 0,
            'best_percent': best_pct,
            'best_grade': _letter_grade(best_pct),
            'best_response_id': best.id,
            'latest_taken_at': latest.created_at,
            'attempts': [
                {
                    'response_id': a.id,
                    'points': a.points or 0,
                    'total': a.total_points or 0,
                    'percent': _pct(a),
                    'grade': _letter_grade(_pct(a)),
                    'taken_at': a.created_at,
                } for a in attempts
            ],
        }
        cd = courses_data.setdefault(course.id, {
            'course': course,
            'quizzes': [],
        })
        cd['quizzes'].append(quiz_entry)

    # Compute per-course aggregate (average of best attempts, weighted by total_points)
    course_rows = []
    for cid, cd in courses_data.items():
        sum_best = sum(q['best_points'] for q in cd['quizzes'])
        sum_total = sum(q['best_total'] for q in cd['quizzes'])
        avg_pct = (sum_best / sum_total * 100.0) if sum_total else 0.0
        course_rows.append({
            'course': cd['course'],
            'quizzes': sorted(cd['quizzes'], key=lambda q: q['title'].lower()),
            'sum_best': sum_best,
            'sum_total': sum_total,
            'avg_percent': avg_pct,
            'avg_grade': _letter_grade(avg_pct),
        })
    course_rows.sort(key=lambda c: c['course'].title.lower())

    # Overall (cumulative) average across all quizzes attempted
    overall_best = sum(c['sum_best'] for c in course_rows)
    overall_total = sum(c['sum_total'] for c in course_rows)
    overall_pct = (overall_best / overall_total * 100.0) if overall_total else 0.0
    total_attempts = sum(len(by_quiz[qid]) for qid in by_quiz)

    return render_template('my_results.html',
                           course_rows=course_rows,
                           overall_best=overall_best,
                           overall_total=overall_total,
                           overall_pct=overall_pct,
                           overall_grade=_letter_grade(overall_pct),
                           total_attempts=total_attempts,
                           quizzes_taken=len(quiz_meta))


def _letter_grade(pct):
    if pct >= 85: return 'A'
    if pct >= 75: return 'B'
    if pct >= 65: return 'C'
    if pct >= 55: return 'D'
    if pct >= 50: return 'E'
    return 'F'


def _about_html_for(course):
    """Return a topical 'About this course' HTML body based on the course title."""
    _t = (course.title or '').lower()
    if '1z0' in _t or 'oracle' in _t or 'java' in _t:
        _p = 'style="font-size:1.0625rem;line-height:1.65;color:#3F3F3F;margin:0 0 12px;"'
        _h2 = 'style="font-size:1.375rem;font-weight:600;color:#101828;margin:28px 0 10px;"'
        _ul = 'style="font-size:1.0625rem;line-height:1.65;color:#3F3F3F;margin:0 0 18px 1.25rem;padding:0;"'
        _row = 'style="padding:14px 0;border-bottom:1px solid #E5E5E5;"'
        return (
            '<div style="display:flex;gap:48px;flex-wrap:wrap;align-items:flex-start;">'
              '<div style="flex:1 1 60%;min-width:300px;">'
                '<h1 style="font-size:2.5rem;font-weight:400;color:#7A7A7A;line-height:1.15;margin:0 0 28px;letter-spacing:-0.01em;">OCA \u2013 Oracle Certified Associate, Java SE 8 Programmer I (1Z0-808)</h1>'
                f'<h2 {_h2}>Java Basics</h2>'
                f'<ul {_ul}>'
                  '<li>Define the scope of variables</li>'
                  '<li>Define the structure of a Java class</li>'
                  '<li>Create executable Java applications with a main method; run a Java program from the command line; produce console output</li>'
                  '<li>Import other Java packages to make them accessible in your code</li>'
                  '<li>Compare and contrast the features and components of Java such as: platform independence, object orientation, encapsulation, etc.</li>'
                '</ul>'
                f'<h2 {_h2}>Working With Java Data Types</h2>'
                f'<ul {_ul}>'
                  '<li>Declare and initialize variables (including casting of primitive data types)</li>'
                  '<li>Differentiate between object reference variables and primitive variables</li>'
                  '<li>Know how to read or write to object fields</li>'
                  '<li>Explain an Object\u2019s Lifecycle (creation, \u201cdereference by reassignment\u201d and garbage collection)</li>'
                  '<li>Develop code that uses wrapper classes such as Boolean, Double, and Integer</li>'
                '</ul>'
                f'<h2 {_h2}>Using Operators and Decision Constructs</h2>'
                f'<ul {_ul}>'
                  '<li>Use Java operators; use parentheses to override operator precedence</li>'
                  '<li>Test equality between Strings and other objects using <code>==</code> and <code>equals()</code></li>'
                  '<li>Create if and if/else and ternary constructs</li>'
                  '<li>Use a switch statement</li>'
                '</ul>'
                f'<h2 {_h2}>Creating and Using Arrays</h2>'
                f'<ul {_ul}>'
                  '<li>Declare, instantiate, initialize and use a one-dimensional array</li>'
                  '<li>Declare, instantiate, initialize and use multi-dimensional arrays</li>'
                '</ul>'
                f'<h2 {_h2}>Using Loop Constructs</h2>'
                f'<ul {_ul}>'
                  '<li>Create and use while loops</li>'
                  '<li>Create and use for loops including the enhanced for loop</li>'
                  '<li>Create and use do/while loops</li>'
                  '<li>Compare loop constructs</li>'
                  '<li>Use break and continue</li>'
                '</ul>'
                f'<h2 {_h2}>Working with Methods and Encapsulation</h2>'
                f'<ul {_ul}>'
                  '<li>Create methods with arguments and return values; including overloaded methods</li>'
                  '<li>Apply the <code>static</code> keyword to methods and fields</li>'
                  '<li>Create and overload constructors; differentiate between default and user defined constructors</li>'
                  '<li>Apply access modifiers</li>'
                  '<li>Apply encapsulation principles to a class</li>'
                  '<li>Determine the effect upon object references and primitive values when they are passed into methods that change the values</li>'
                '</ul>'
                f'<h2 {_h2}>Working with Inheritance</h2>'
                f'<ul {_ul}>'
                  '<li>Describe inheritance and its benefits</li>'
                  '<li>Develop code that makes use of polymorphism; develop code that overrides methods; differentiate between the type of a reference and the type of an object</li>'
                  '<li>Determine when casting is necessary</li>'
                  '<li>Use <code>super</code> and <code>this</code> to access objects and constructors</li>'
                  '<li>Use abstract classes and interfaces</li>'
                '</ul>'
                f'<h2 {_h2}>Handling Exceptions</h2>'
                f'<ul {_ul}>'
                  '<li>Differentiate among checked exceptions, unchecked exceptions, and Errors</li>'
                  '<li>Create a try-catch block and determine how exceptions alter normal program flow</li>'
                  '<li>Describe the advantages of Exception handling</li>'
                  '<li>Create and invoke a method that throws an exception</li>'
                  '<li>Recognize common exception classes (such as <code>NullPointerException</code>, <code>ArithmeticException</code>, <code>ArrayIndexOutOfBoundsException</code>, <code>ClassCastException</code>)</li>'
                '</ul>'
                f'<h2 {_h2}>Working with Selected classes from the Java API</h2>'
                f'<ul {_ul}>'
                  '<li>Manipulate data using the <code>StringBuilder</code> class and its methods</li>'
                  '<li>Create and manipulate Strings</li>'
                  '<li>Create and manipulate calendar data using classes from <code>java.time.LocalDateTime</code>, <code>java.time.LocalDate</code>, <code>java.time.LocalTime</code>, <code>java.time.format.DateTimeFormatter</code>, <code>java.time.Period</code></li>'
                  '<li>Declare and use an <code>ArrayList</code> of a given type</li>'
                  '<li>Write a simple Lambda expression that consumes a Lambda Predicate expression</li>'
                '</ul>'
                f'<h2 {_h2}>Assume the following:</h2>'
                f'<ul {_ul}>'
                  '<li><strong>Missing package and import statements:</strong> If sample code does not include package or import statements, and the question does not explicitly refer to these missing statements, then assume that all sample code is in the same package, or import statements exist to support them.</li>'
                  '<li><strong>No file or directory path names for classes:</strong> If a question does not state the file names or directory locations of classes, then assume one of the following, whichever will enable the code to compile and run: all classes are in one file, or each class is contained in a separate file and all files are in one directory.</li>'
                  '<li><strong>Unintended line breaks:</strong> Sample code might have unintended line breaks. If you see a line of code that looks like it has wrapped, and this creates a situation where the wrapping is significant (for example, a quoted String literal has wrapped), assume that the wrapping is an extension of the same line, and the line does not contain a hard carriage return that would cause a compilation failure.</li>'
                  '<li><strong>Code fragments:</strong> A code fragment is a small section of source code that is presented without its context. Assume that all necessary supporting code exists and that the supporting environment fully supports the correct compilation and execution of the code shown and its omitted environment.</li>'
                  '<li><strong>Descriptive comments:</strong> Take descriptive comments, such as \u201csetter and getters go here,\u201d at face value. Assume that correct code exists, compiles, and runs successfully to create the described effect.</li>'
                '</ul>'
              '</div>'
              '<div style="flex:0 0 280px;min-width:240px;font-size:1rem;line-height:1.5;color:#3F3F3F;">'
                f'<div {_row}><strong>Provider:</strong> Oracle</div>'
                f'<div {_row}><strong>Level:</strong> Associate</div>'
                f'<div {_row}><strong>Delivery Channel:</strong> Pearson VUE</div>'
                f'<div {_row}><strong>Mode:</strong> Online &amp; In-person</div>'
                f'<div {_row}><strong>Cost:</strong> From USD 245</div>'
                f'<div {_row}><strong>Language:</strong> English</div>'
              '</div>'
            '</div>'
        )
    if 'power bi' in _t or 'pl-300' in _t:
        return (
            '<p>This course prepares you for the <strong>Microsoft Power BI Data Analyst (PL-300)</strong> certification.</p>'
            '<p>You will learn how to connect to data sources, clean and transform data with Power Query, model data with DAX, and design interactive reports and dashboards in Power BI Desktop and the Power BI Service.</p>'
        )
    if 'az-900' in _t or 'azure fundamentals' in _t:
        return (
            '<p>This course prepares you for the <strong>Microsoft Azure Fundamentals (AZ-900)</strong> certification.</p>'
            '<p>You will learn core cloud concepts, the main Azure services (compute, networking, storage, databases), Azure pricing and support, and the basics of governance, security, privacy, and compliance in the Azure cloud.</p>'
        )
    if 'az-' in _t or 'azure' in _t:
        return (
            '<p>This course introduces you to <strong>Microsoft Azure</strong> \u2014 Microsoft\u2019s cloud platform.</p>'
            '<p>You will explore the main Azure services, learn how to deploy and manage resources, and understand how Azure is used in modern cloud solutions.</p>'
        )
    if 'sql' in _t:
        return (
            '<p>This course covers <strong>SQL</strong> \u2014 the standard language for working with relational databases.</p>'
            '<p>You will learn how to write queries with <code>SELECT</code>, filter and sort results, combine tables with joins, aggregate data, and modify records safely. By the end you\u2019ll be able to answer real business questions directly from a database.</p>'
        )
    if 'aws' in _t:
        return (
            '<p>This course introduces you to <strong>Amazon Web Services (AWS)</strong> and prepares you for the <strong>AWS Certified Cloud Practitioner</strong> exam.</p>'
            '<p>You will learn AWS core services (EC2, S3, RDS, IAM, VPC), the AWS Well-Architected Framework, pricing and billing, and security best practices in the cloud.</p>'
        )
    if 'gcp' in _t or 'google cloud' in _t:
        return (
            '<p>This course introduces you to <strong>Google Cloud Platform (GCP)</strong>.</p>'
            '<p>You will learn the core GCP services for compute, storage, networking, and data, and how organizations use Google Cloud to build and run modern applications.</p>'
        )
    if 'pcap' in _t or 'python' in _t:
        return (
            '<div style="display:flex;gap:48px;flex-wrap:wrap;align-items:flex-start;">'
              '<div style="flex:1 1 60%;min-width:300px;">'
                '<h1 style="font-size:2.5rem;font-weight:400;color:#7A7A7A;line-height:1.15;margin:0 0 28px;letter-spacing:-0.01em;">PCAP \u2013 Certified Associate Python Programmer certification</h1>'
                '<p style="font-size:1.0625rem;line-height:1.65;color:#3F3F3F;margin:0 0 18px;"><em>PCAP\u2122 \u2013 Certified Associate Python Programmer</em> certification is a professional credential that measures your ability to accomplish coding tasks related to the <strong>basics of programming in the Python language</strong> and the fundamental notions and techniques used in <strong>object-oriented programming</strong>.</p>'
                '<p style="font-size:1.0625rem;line-height:1.65;color:#3F3F3F;margin:0 0 18px;"><em>PCAP \u2013 Certified Associate Python Programmer</em> certification shows that the individual is familiar with <strong>general computer programming concepts</strong> like conditional execution, loops, Python programming language syntax, semantics, and the runtime environment, as well as with <strong>general coding techniques</strong> and the <strong>object-oriented approach</strong>.</p>'
                '<p style="font-size:1.0625rem;line-height:1.65;color:#3F3F3F;margin:0 0 18px;">Becoming PCAP certified ensures that the individual is fully acquainted with all the primary means provided by Python 3 to enable her/him to start her/his own studies, and to open a path to the developer\u2019s career.</p>'
              '</div>'
              '<div style="flex:0 0 280px;min-width:240px;font-size:1rem;line-height:1.5;color:#3F3F3F;">'
                '<div style="padding:14px 0;border-bottom:1px solid #E5E5E5;"><strong>Provider:</strong> Python Institute</div>'
                '<div style="padding:14px 0;border-bottom:1px solid #E5E5E5;"><strong>Level:</strong> Associate</div>'
                '<div style="padding:14px 0;border-bottom:1px solid #E5E5E5;"><strong>Delivery Channel:</strong> TestNow &amp; Pearson VUE</div>'
                '<div style="padding:14px 0;border-bottom:1px solid #E5E5E5;"><strong>Mode:</strong> Online</div>'
                '<div style="padding:14px 0;border-bottom:1px solid #E5E5E5;"><strong>Cost:</strong> From USD 295</div>'
                '<div style="padding:14px 0;border-bottom:1px solid #E5E5E5;"><strong>Language:</strong> English (TestNow\u2122, Pearson VUE), Spanish (TestNow\u2122), Japanese (TestNow\u2122)</div>'
              '</div>'
            '</div>'
        )
    if (' ai ' in f' {_t} ') or 'artificial intelligence' in _t or 'machine learning' in _t:
        return (
            '<p>This course introduces you to <strong>Artificial Intelligence and Machine Learning</strong>.</p>'
            '<p>You will learn what AI and ML are, how machines learn from data, the main types of learning (supervised, unsupervised, reinforcement), and where AI is used in the real world today.</p>'
        )
    return (
        f'<p>Welcome to <strong>{course.title}</strong>.</p>'
        '<p>This course will guide you through the key concepts step by step. Each lesson builds on the previous one, and you can track your progress as you go.</p>'
    )


def _seed_starter_lessons(course):
    """Add the standard 4 starter lessons (Welcome / Video / Task / Exam) to a course.
    Skips silently if the course already has lessons."""
    if course.lessons:
        return

    # Pick a topical intro video based on the course title so a Power BI course
    # doesn't show a Python video, etc.
    _t = (course.title or '').lower()
    if '1z0' in _t or 'oracle' in _t or 'java' in _t:
        intro_video = 'https://www.youtube.com/embed/eIrMbAQSU34'  # Java in 100 seconds
    elif 'power bi' in _t or 'pl-300' in _t:
        intro_video = 'https://www.youtube.com/embed/TmhQCQr_DCA'  # Power BI in 100 seconds
    elif 'az-900' in _t or 'azure fundamentals' in _t:
        intro_video = 'https://www.youtube.com/embed/NKEFWyqJ5XA'  # Adam Marczak — AZ-900 Episode 1: Course Introduction
    elif 'az-' in _t or 'azure' in _t:
        intro_video = 'https://www.youtube.com/embed/IFpKngfH7Hs'  # Azure in 100 seconds
    elif 'sql' in _t:
        intro_video = 'https://www.youtube.com/embed/zsjvFFKOm3c'  # SQL in 100 seconds
    elif 'aws' in _t:
        intro_video = 'https://www.youtube.com/embed/a9__D53WsUs'  # AWS in 100 seconds
    elif 'gcp' in _t or 'google cloud' in _t:
        intro_video = 'https://www.youtube.com/embed/4D3X6Xl5c_0'  # GCP in 100 seconds
    elif 'pcap' in _t or 'python' in _t:
        intro_video = 'https://www.youtube.com/embed/x7X9w_GIm1s'  # Python in 100 seconds
    elif (' ai ' in f' {_t} ') or 'artificial intelligence' in _t or 'machine learning' in _t:
        intro_video = 'https://www.youtube.com/embed/PeMlggyqz0Y'  # Machine Learning in 100 seconds
    else:
        intro_video = 'https://www.youtube.com/embed/x7X9w_GIm1s'

    # Build a topical "About this course" body so the first lesson is actually
    # useful, rather than a generic "Welcome — replace this" placeholder.
    about_html = _about_html_for(course)

    starter_quiz = Quiz(
        course_id=course.id,
        title=f'{course.title} \u2014 Final Exam',
        description='Short exam covering the starter lessons.',
    )
    db.session.add(starter_quiz)
    db.session.flush()

    db.session.add_all([
        Lesson(
            course_id=course.id,
            title='About this course',
            content=about_html,
            content_type='lesson',
            order=1,
            points=1.0,
        ),
        Lesson(
            course_id=course.id,
            title='Lesson 1: Watch \u2014 Intro Video',
            content='<p>Replace this with your own intro video.</p>',
            content_type='video',
            video_url=intro_video,
            order=2,
            points=1.0,
        ),
        Lesson(
            course_id=course.id,
            title='Lesson 2: Task \u2014 Your First Submission',
            content='',
            content_type='task',
            task_instructions='<p>Replace these instructions with the task you want students to complete.</p>',
            order=3,
            points=2.0,
        ),
        Lesson(
            course_id=course.id,
            title='Lesson 3: Exam',
            content='',
            content_type='exam',
            quiz_id=starter_quiz.id,
            order=4,
            points=5.0,
        ),
    ])


def _save_course_image(course, image_file):
    """Save an uploaded course image to /static/uploads/courses and set course.image_url.
    Returns True if a file was saved, False otherwise."""
    if not image_file or not image_file.filename:
        return False
    allowed_ext = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    ext = image_file.filename.rsplit('.', 1)[-1].lower() if '.' in image_file.filename else ''
    if ext not in allowed_ext:
        flash('Course image must be a PNG, JPG, GIF, or WEBP file.', 'danger')
        return False
    filename = secure_filename(
        f"course_{course.id}_{int(datetime.utcnow().timestamp())}.{ext}"
    )
    upload_path = os.path.join(app.static_folder, 'uploads', 'courses')
    os.makedirs(upload_path, exist_ok=True)
    image_file.save(os.path.join(upload_path, filename))
    course.image_url = url_for('static', filename=f'uploads/courses/{filename}')
    return True


def _save_course_badge(course, badge_file):
    """Save an uploaded course badge to /static/uploads/badges and set course.badge_url.
    Returns True if a file was saved, False otherwise."""
    if not badge_file or not badge_file.filename:
        return False
    allowed_ext = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}
    ext = badge_file.filename.rsplit('.', 1)[-1].lower() if '.' in badge_file.filename else ''
    if ext not in allowed_ext:
        flash('Course badge must be a PNG, JPG, GIF, WEBP, or SVG file.', 'danger')
        return False
    filename = secure_filename(
        f"badge_{course.id}_{int(datetime.utcnow().timestamp())}.{ext}"
    )
    upload_path = os.path.join(app.static_folder, 'uploads', 'badges')
    os.makedirs(upload_path, exist_ok=True)
    badge_file.save(os.path.join(upload_path, filename))
    course.badge_url = url_for('static', filename=f'uploads/badges/{filename}')
    return True


@app.route('/course/create', methods=['POST'])
@login_required
def create_course():
    if not current_user.is_teacher:
        flash('Only teachers can create courses.', 'danger')
        return redirect(url_for('index'))
    
    title = request.form.get('title')
    description = request.form.get('description')
    image_url_field = (request.form.get('image_url') or '').strip()
    
    if not title:
        flash('Course title is required.', 'danger')
        return redirect(url_for('index'))
    
    course = Course(
        title=title,
        description=description,
        teacher_id=current_user.id
    )
    
    db.session.add(course)
    db.session.flush()  # need course.id for filename

    # Optional image upload (file beats URL)
    image_file = request.files.get('image')
    saved = _save_course_image(course, image_file)
    if not saved and image_url_field:
        course.image_url = image_url_field

    # Seed the standard 4 starter lessons so every course has the same structure
    _seed_starter_lessons(course)

    db.session.commit()
    
    flash('Course created successfully!', 'success')
    return redirect(url_for('view_course', course_id=course.id))

@app.route('/course/<int:course_id>')
@login_required
def view_course(course_id):
    course = Course.query.get_or_404(course_id)
    
    # Check if the user has access to this course
    if not current_user.is_teacher and not any(e.student_id == current_user.id for e in course.enrollments):
        flash('You do not have access to this course.', 'danger')
        return redirect(url_for('index'))
    
    # Get all students not enrolled in this course if user is teacher
    available_students = []
    if current_user.is_teacher:
        enrolled_student_ids = [e.student_id for e in course.enrollments]
        available_students = User.query.filter(
            User.is_teacher == False,
            ~User.id.in_(enrolled_student_ids)
        ).all()
    
    return render_template('course/view_course.html', 
                          course=course, 
                          available_students=available_students)

@app.route('/course/<int:course_id>/enroll', methods=['POST'])
@login_required
def enroll_students(course_id):
    if not (current_user.is_teacher or current_user.is_superadmin):
        flash('Only a teacher, administrator, or super user can enroll students.', 'error')
        return redirect(url_for('view_course', course_id=course_id))
    
    course = Course.query.get_or_404(course_id)
    student_ids = request.form.getlist('student_ids[]')
    
    for student_id in student_ids:
        # Check if enrollment already exists
        enrollment = Enrollment.query.filter_by(
            student_id=student_id,
            course_id=course_id
        ).first()
        
        if not enrollment:
            enrollment = Enrollment(student_id=student_id, course_id=course_id)
            db.session.add(enrollment)
    
    try:
        db.session.commit()
        flash('Students enrolled successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error enrolling students.', 'error')
    
    return redirect(url_for('view_course', course_id=course_id))

@app.route('/course/<int:course_id>/unenroll/<int:student_id>', methods=['POST'])
@login_required
def unenroll_student(course_id, student_id):
    if not (current_user.is_teacher or current_user.is_superadmin):
        flash('Only a teacher, administrator, or super user can unenroll students.', 'error')
        return redirect(url_for('view_course', course_id=course_id))
    
    enrollment = Enrollment.query.filter_by(
        student_id=student_id,
        course_id=course_id
    ).first_or_404()
    
    try:
        db.session.delete(enrollment)
        db.session.commit()
        flash('Student unenrolled successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error unenrolling student.', 'error')
    
    return redirect(url_for('view_course', course_id=course_id))


@app.route('/course/<int:course_id>/student/<int:student_id>')
@login_required
def view_student_progress(course_id, student_id):
    # Teachers/superadmins can view any student's progress for their course;
    # a student may always view their own progress page.
    if not (
        current_user.is_teacher
        or current_user.is_superadmin
        or current_user.id == student_id
    ):
        flash('You do not have permission to view this page.', 'danger')
        return redirect(url_for('view_course', course_id=course_id))

    course = Course.query.get_or_404(course_id)
    student = User.query.get_or_404(student_id)
    enrollment = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first_or_404()

    lessons = Lesson.query.filter_by(course_id=course_id).order_by(Lesson.order).all()
    lesson_ids = [l.id for l in lessons]
    completed_ids = set()
    submissions = []
    if lesson_ids:
        completed_ids = {
            c.lesson_id for c in LessonCompletion.query.filter(
                LessonCompletion.student_id == student_id,
                LessonCompletion.lesson_id.in_(lesson_ids),
            ).all()
        }
        submissions = TaskSubmission.query.filter(
            TaskSubmission.student_id == student_id,
            TaskSubmission.lesson_id.in_(lesson_ids),
        ).all()
    submissions_by_lesson = {s.lesson_id: s for s in submissions}

    progress = StudentProgress.query.filter_by(student_id=student_id, course_id=course_id).first()
    quiz_responses = (QuizResponse.query
                      .join(Quiz, Quiz.id == QuizResponse.quiz_id)
                      .filter(QuizResponse.user_id == student_id, Quiz.course_id == course_id)
                      .order_by(QuizResponse.created_at.desc()).all())

    total_lessons = len(lessons)
    completed_lessons = sum(1 for l in lessons if l.id in completed_ids)
    pct = int((completed_lessons / total_lessons) * 100) if total_lessons else 0

    # Points: derive from the actual course content rather than the running
    # StudentProgress accumulator (which only reflects graded quizzes/tasks
    # and starts at 0/0 until the first submission is graded).
    total_points = sum((l.points or 0) for l in lessons)
    points_earned = sum((l.points or 0) for l in lessons if l.id in completed_ids)
    # Add any explicit task grades that exceed the lesson's base point value.
    for s in submissions:
        if s.grade is None:
            continue
        lesson = next((l for l in lessons if l.id == s.lesson_id), None)
        if not lesson:
            continue
        base = lesson.points or 0
        # If a grade was awarded and the lesson wasn't already counted as complete,
        # count the grade. If it was complete, prefer the larger of base/grade.
        if lesson.id in completed_ids:
            points_earned += max(0, float(s.grade) - base)
        else:
            points_earned += float(s.grade)
    points_pct = int((points_earned / total_points) * 100) if total_points else 0

    return render_template(
        'course/student_progress.html',
        course=course, student=student, enrollment=enrollment,
        lessons=lessons, completed_ids=completed_ids,
        submissions_by_lesson=submissions_by_lesson,
        progress=progress, quiz_responses=quiz_responses,
        total_lessons=total_lessons, completed_lessons=completed_lessons, pct=pct,
        points_earned=points_earned, total_points=total_points, points_pct=points_pct,
    )

@app.route('/course/<int:course_id>/edit', methods=['POST'])
@login_required
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    
    # The course's teacher can edit; superadmin can edit any course.
    is_owner = current_user.is_teacher and current_user.id == course.teacher_id
    if not (is_owner or current_user.is_superadmin):
        flash('You do not have permission to edit this course.', 'danger')
        return redirect(url_for('index'))
    
    title = request.form.get('title')
    description = request.form.get('description')
    
    if not title:
        flash('Course title is required.', 'danger')
        return redirect(url_for('view_course', course_id=course_id))
    
    course.title = title
    course.description = description

    # Image handling: uploaded file > URL field > remove flag > leave as-is
    image_file = request.files.get('image')
    saved = _save_course_image(course, image_file)
    if not saved:
        image_url_field = (request.form.get('image_url') or '').strip()
        if image_url_field:
            course.image_url = image_url_field
        elif request.form.get('remove_image') == '1':
            course.image_url = None

    # Badge handling: uploaded file > URL field > remove flag > leave as-is
    badge_file = request.files.get('badge')
    badge_saved = _save_course_badge(course, badge_file)
    if not badge_saved:
        badge_url_field = (request.form.get('badge_url') or '').strip()
        if badge_url_field:
            course.badge_url = badge_url_field
        elif request.form.get('remove_badge') == '1':
            course.badge_url = None

    db.session.commit()
    
    flash('Course updated successfully!', 'success')
    return redirect(url_for('view_course', course_id=course_id))


@app.route('/course/<int:course_id>/delete', methods=['POST'])
@login_required
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)

    # The course's creator can delete it; superadmin can delete any course.
    is_owner = current_user.is_teacher and current_user.id == course.teacher_id
    if not (is_owner or current_user.is_superadmin):
        flash('Only the teacher who created this course (or a superadmin) can delete it.', 'danger')
        return redirect(url_for('index'))

    title = course.title
    try:
        db.session.delete(course)
        db.session.commit()
        flash(f'Course "{title}" deleted.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting course: {e}', 'danger')

    return redirect(url_for('index'))

@app.route('/course/<int:course_id>/quiz/create', methods=['GET', 'POST'])
@login_required
def create_quiz(course_id):
    course = Course.query.get_or_404(course_id)

    # Allow the course owner (teacher) or any superadmin/admin to create quizzes
    is_owner = current_user.is_teacher and current_user.id == course.teacher_id
    if not (is_owner or current_user.is_superadmin):
        flash('You do not have permission to create quizzes for this course.', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        
        if not title:
            flash('Quiz title is required.', 'danger')
            return redirect(url_for('create_quiz', course_id=course_id))
        
        quiz = Quiz(
            title=title,
            description=description,
            course_id=course_id
        )
        
        db.session.add(quiz)
        db.session.commit()
        
        flash('Quiz created successfully!', 'success')
        return redirect(url_for('view_quiz', quiz_id=quiz.id))
    
    return render_template('quiz/create_quiz.html', course=course)

@app.route('/quiz/<int:quiz_id>/delete', methods=['POST'])
@login_required
def delete_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    course = Course.query.get(quiz.course_id)

    # Allow course owner or any superadmin/admin to delete
    is_owner = current_user.is_teacher and current_user.id == course.teacher_id
    if not (is_owner or current_user.is_superadmin):
        flash('You do not have permission to delete this quiz.', 'danger')
        return redirect(url_for('index'))
    
    # Delete all questions and their options first
    for question in quiz.questions:
        QuestionOption.query.filter_by(question_id=question.id).delete()
    Question.query.filter_by(quiz_id=quiz_id).delete()
    
    # Delete the quiz
    db.session.delete(quiz)
    db.session.commit()
    
    flash('Quiz deleted successfully!', 'success')
    return redirect(url_for('view_course', course_id=course.id))

@app.route('/quiz/<int:quiz_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    course = Course.query.get(quiz.course_id)

    # Allow course owner or any superadmin/admin to edit
    is_owner = current_user.is_teacher and current_user.id == course.teacher_id
    if not (is_owner or current_user.is_superadmin):
        flash('You do not have permission to edit this quiz.', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        
        if not title:
            flash('Quiz title is required.', 'danger')
            return redirect(url_for('edit_quiz', quiz_id=quiz_id))
        
        quiz.title = title
        quiz.description = description
        db.session.commit()
        
        flash('Quiz updated successfully!', 'success')
        return redirect(url_for('view_quiz', quiz_id=quiz_id))
    
    return render_template('quiz/edit_quiz.html', quiz=quiz)

@app.route('/quiz/<int:quiz_id>/add_question', methods=['GET', 'POST'])
@login_required
def add_question(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    
    if request.method == 'POST':
        question_type = request.form.get('question_type')
        question_text = request.form.get('question_text')
        points = request.form.get('points', type=float)
        feedback = request.form.get('feedback')
        
        # Check if there's an image uploaded for image-based questions
        image_url = None
        if 'question_image' in request.files and request.files['question_image'].filename:
            image_file = request.files['question_image']
            # Create unique filename
            filename = secure_filename(f"question_{quiz_id}_{int(datetime.utcnow().timestamp())}_{image_file.filename}")
            # Save to static/uploads folder
            upload_path = os.path.join(app.static_folder, 'uploads')
            os.makedirs(upload_path, exist_ok=True)
            image_file.save(os.path.join(upload_path, filename))
            image_url = url_for('static', filename=f'uploads/{filename}')
        
        # Save the question with image URL if available
        question = Question(
            quiz_id=quiz_id,
            question_type=question_type,
            question_html=question_text,
            image_url=image_url,
            points=points,
            feedback=feedback
        )
        db.session.add(question)
        db.session.commit()  # Commit to get the question ID
        
        if question_type == 'image_drag_drop':
            # Process image zones and drag items
            drag_items = request.form.getlist('drag_items[]')
            zone_x = request.form.getlist('zone_x[]', type=int)
            zone_y = request.form.getlist('zone_y[]', type=int)
            zone_width = request.form.getlist('zone_width[]', type=int)
            zone_height = request.form.getlist('zone_height[]', type=int)
            
            # Create draggable items
            for i, item_text in enumerate(drag_items):
                option = QuestionOption(
                    question_id=question.id,
                    option_html=item_text,
                    order=i,
                    is_correct=True,  # All items are correct in their proper zones
                    drag_zone="item"
                )
                db.session.add(option)
            
            # Create target zones on the image
            for i in range(len(zone_x)):
                zone_data = {
                    "x": zone_x[i],
                    "y": zone_y[i],
                    "width": zone_width[i],
                    "height": zone_height[i],
                    "target_item": i  # Which item should be placed in this zone
                }
                
                option = QuestionOption(
                    question_id=question.id,
                    option_html=json.dumps(zone_data),
                    order=i,
                    drag_zone="zone"
                )
                db.session.add(option)
        
        elif question_type == 'drag_and_drop':
            # Handle regular drag and drop (existing code)
            drag_items = request.form.getlist('drag_items[]')
            drag_zones = request.form.getlist('drag_zones[]')
            
            for i, (item_text, zone) in enumerate(zip(drag_items, drag_zones)):
                option = QuestionOption(
                    question_id=question.id,
                    option_html=item_text,
                    drag_zone=zone,
                    order=i
                )
                db.session.add(option)
        
        # Handle other question types...
        
        db.session.commit()
        flash('Question added successfully!', 'success')
        return redirect(url_for('view_quiz', quiz_id=quiz_id))
    
    return render_template('quiz/add_question.html', quiz=quiz)

@app.route('/quiz/<int:quiz_id>/view')
@login_required
def view_quiz(quiz_id):
    # This page added nothing actionable. Redirect to a useful page:
    # teachers go to the editor, students go straight to taking the quiz.
    quiz = Quiz.query.get_or_404(quiz_id)
    if current_user.is_teacher:
        return redirect(url_for('edit_quiz', quiz_id=quiz.id))
    return redirect(url_for('take_quiz', quiz_id=quiz.id))

@app.route('/quiz/<int:quiz_id>/take', methods=['GET', 'POST'])
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    
    if request.method == 'POST':
        earned_points = 0
        total_points = 0
        
        # Create quiz response
        quiz_response = QuizResponse(
            user_id=current_user.id,
            quiz_id=quiz_id
        )
        db.session.add(quiz_response)
        
        for question in quiz.questions:
            total_points += question.points
            
            # Handle different question types
            if question.question_type == 'image_drag_drop':
                # Get answers for image drag and drop
                answers = request.form.getlist(f'question_{question.id}_positions[]')
                correct_count = 0
                total_items = len(answers)
                
                # Get the zones
                zones = QuestionOption.query.filter_by(
                    question_id=question.id, 
                    drag_zone='zone'
                ).order_by(QuestionOption.order).all()
                
                # Process each dropped item's position
                for i, position_data in enumerate(answers):
                    if position_data:
                        try:
                            position = json.loads(position_data)
                            zone_data = json.loads(zones[i].option_html) if i < len(zones) else None
                            
                            if zone_data:
                                # Check if item is in correct zone
                                if (position['x'] >= zone_data['x'] and 
                                    position['x'] <= zone_data['x'] + zone_data['width'] and
                                    position['y'] >= zone_data['y'] and 
                                    position['y'] <= zone_data['y'] + zone_data['height']):
                                    correct_count += 1
                        except (ValueError, TypeError, json.JSONDecodeError):
                            continue
                
                # Calculate points
                if total_items > 0:
                    question_points = (correct_count / total_items) * question.points
                    earned_points += question_points
                    
            elif question.question_type == 'drag_and_drop':
                # Handle regular drag and drop (existing code)
                answers = request.form.getlist(f'question_{question.id}_answers[]')
                correct_count = 0
                total_items = len(answers)
                
                for i, answer in enumerate(answers):
                    if answer:
                        try:
                            option_id = int(answer)
                            option = QuestionOption.query.get(option_id)
                            if option and option.order == i:
                                correct_count += 1
                        except (ValueError, TypeError):
                            continue
                
                if total_items > 0:
                    question_points = (correct_count / total_items) * question.points
                    earned_points += question_points

            elif question.question_type == 'multiple_choice':
                # Multi-select: all correct options must be checked and no incorrect ones.
                selected_ids = set()
                for val in request.form.getlist(f'question_{question.id}[]'):
                    try:
                        selected_ids.add(int(val))
                    except (ValueError, TypeError):
                        continue
                correct_ids = {o.id for o in question.options if o.is_correct}
                incorrect_ids = {o.id for o in question.options if not o.is_correct}
                q_points = 0
                if correct_ids:
                    correct_hits = len(selected_ids & correct_ids)
                    wrong_hits = len(selected_ids & incorrect_ids)
                    raw = (correct_hits - wrong_hits) / len(correct_ids)
                    ratio = max(0.0, min(1.0, raw))
                    q_points = ratio * question.points
                    earned_points += q_points
                qr = QuestionResponse(
                    question_id=question.id,
                    user_id=current_user.id,
                    quiz_response=quiz_response,
                    points=q_points,
                    is_correct=(selected_ids == correct_ids)
                )
                db.session.add(qr)
                db.session.flush()
                for opt_id in selected_ids:
                    db.session.add(QuestionResponseOption(response_id=qr.id, option_id=opt_id))

            elif question.question_type in ('single_choice', 'true_false'):
                val = request.form.get(f'question_{question.id}')
                selected_id = None
                is_correct = False
                q_points = 0
                if val:
                    try:
                        selected_id = int(val)
                        opt = QuestionOption.query.get(selected_id)
                        if opt and opt.question_id == question.id and opt.is_correct:
                            q_points = question.points
                            earned_points += q_points
                            is_correct = True
                    except (ValueError, TypeError):
                        selected_id = None
                qr = QuestionResponse(
                    question_id=question.id,
                    user_id=current_user.id,
                    quiz_response=quiz_response,
                    points=q_points,
                    is_correct=is_correct
                )
                db.session.add(qr)
                db.session.flush()
                if selected_id is not None:
                    db.session.add(QuestionResponseOption(response_id=qr.id, option_id=selected_id))

        quiz_response.points = earned_points
        quiz_response.total_points = total_points
        db.session.commit()
        
        # Update student progress
        update_student_progress(current_user.id, quiz.course_id, earned_points, total_points)
        
        flash('Quiz submitted successfully!', 'success')
        return redirect(url_for('view_quiz_result', quiz_id=quiz_id, response_id=quiz_response.id))
    
    return render_template('quiz/take_quiz.html', quiz=quiz)

@app.route('/quiz/<int:quiz_id>/result/<int:response_id>')
@login_required
def view_quiz_result(quiz_id, response_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    quiz_response = QuizResponse.query.get_or_404(response_id)
    
    # Security check: only allow viewing own results or if teacher
    if quiz_response.user_id != current_user.id and not current_user.is_teacher:
        flash('You do not have permission to view these results.', 'danger')
        return redirect(url_for('view_quiz', quiz_id=quiz_id))
    
    return render_template('quiz/view_quiz_result.html', quiz=quiz, quiz_response=quiz_response)


# =====================================================================
# Lesson content routes — students do lessons, watch videos,
# complete tasks, and take exams.
# =====================================================================

def _student_can_access_lesson(lesson):
    """Returns True if current_user may view the lesson."""
    if not current_user.is_authenticated:
        return False
    if current_user.is_teacher or current_user.is_superadmin:
        return True
    return any(e.student_id == current_user.id for e in lesson.course.enrollments)


def _is_lesson_completed(lesson_id, student_id):
    return LessonCompletion.query.filter_by(
        lesson_id=lesson_id, student_id=student_id
    ).first() is not None


@app.route('/course/<int:course_id>/lessons')
@login_required
def list_lessons(course_id):
    course = Course.query.get_or_404(course_id)
    if not (current_user.is_teacher or current_user.is_superadmin
            or any(e.student_id == current_user.id for e in course.enrollments)):
        flash('You do not have access to this course.', 'danger')
        return redirect(url_for('index'))

    lessons = sorted(course.lessons, key=lambda l: (l.order or 0, l.id))
    completed_ids = set()
    if not current_user.is_teacher:
        completed_ids = {c.lesson_id for c in LessonCompletion.query.filter_by(
            student_id=current_user.id).all()}
    return render_template('lesson/list.html',
                           course=course,
                           lessons=lessons,
                           completed_ids=completed_ids)


@app.route('/lesson/<int:lesson_id>')
@login_required
def view_lesson(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    if not _student_can_access_lesson(lesson):
        flash('You do not have access to this lesson.', 'danger')
        return redirect(url_for('index'))

    submission = None
    if lesson.content_type == 'task' and not current_user.is_teacher:
        submission = TaskSubmission.query.filter_by(
            lesson_id=lesson.id, student_id=current_user.id
        ).order_by(TaskSubmission.submitted_at.desc()).first()

    completed = _is_lesson_completed(lesson.id, current_user.id)

    # Auto-mark passive lesson types (reading / video) as completed the first
    # time the user opens them, so progress reflects navigation through the
    # course. Tasks and exams still require an explicit submission.
    if (not completed
            and lesson.content_type in ('lesson', 'video')
            and _student_can_access_lesson(lesson)):
        try:
            db.session.add(LessonCompletion(
                student_id=current_user.id, lesson_id=lesson.id
            ))
            db.session.commit()
            try:
                update_student_progress(
                    current_user.id, lesson.course_id,
                    lesson.points or 0, lesson.points or 0
                )
            except Exception:
                db.session.rollback()
            completed = True
        except Exception:
            db.session.rollback()

    # Build sidebar outline + prev/next navigation
    all_lessons = sorted(lesson.course.lessons, key=lambda l: (l.order or 0, l.id))
    completed_ids = {c.lesson_id for c in LessonCompletion.query.filter_by(
        student_id=current_user.id).all()}
    try:
        idx = next(i for i, l in enumerate(all_lessons) if l.id == lesson.id)
    except StopIteration:
        idx = 0
    prev_lesson = all_lessons[idx - 1] if idx > 0 else None
    next_lesson = all_lessons[idx + 1] if idx < len(all_lessons) - 1 else None
    total_lessons = len(all_lessons)
    completed_count = len([l for l in all_lessons if l.id in completed_ids])

    return render_template('lesson/view.html',
                           lesson=lesson,
                           course=lesson.course,
                           submission=submission,
                           completed=completed,
                           all_lessons=all_lessons,
                           completed_ids=completed_ids,
                           prev_lesson=prev_lesson,
                           next_lesson=next_lesson,
                           lesson_index=idx + 1,
                           total_lessons=total_lessons,
                           completed_count=completed_count)


@app.route('/lesson/<int:lesson_id>/complete', methods=['POST'])
@login_required
def complete_lesson(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    if not _student_can_access_lesson(lesson):
        flash('You cannot complete this lesson.', 'danger')
        return redirect(url_for('view_lesson', lesson_id=lesson_id))

    if not _is_lesson_completed(lesson.id, current_user.id):
        completion = LessonCompletion(
            student_id=current_user.id, lesson_id=lesson.id
        )
        db.session.add(completion)
        try:
            db.session.commit()
            update_student_progress(
                current_user.id, lesson.course_id,
                lesson.points or 0, lesson.points or 0
            )
            flash('Marked as complete.', 'success')
        except Exception:
            db.session.rollback()
            flash('Could not mark complete.', 'danger')
    return redirect(url_for('view_lesson', lesson_id=lesson_id))


@app.route('/lesson/<int:lesson_id>/task', methods=['POST'])
@login_required
def submit_task(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    if not _student_can_access_lesson(lesson) or current_user.is_teacher:
        flash('You cannot submit this task.', 'danger')
        return redirect(url_for('view_lesson', lesson_id=lesson_id))
    if lesson.content_type != 'task':
        flash('This lesson is not a task.', 'warning')
        return redirect(url_for('view_lesson', lesson_id=lesson_id))

    text = (request.form.get('submission_text') or '').strip()
    if not text:
        flash('Submission cannot be empty.', 'warning')
        return redirect(url_for('view_lesson', lesson_id=lesson_id))

    submission = TaskSubmission(
        student_id=current_user.id,
        lesson_id=lesson.id,
        submission_text=text,
    )
    db.session.add(submission)

    if not _is_lesson_completed(lesson.id, current_user.id):
        db.session.add(LessonCompletion(
            student_id=current_user.id, lesson_id=lesson.id
        ))
        try:
            db.session.commit()
            update_student_progress(
                current_user.id, lesson.course_id,
                lesson.points or 0, lesson.points or 0
            )
        except Exception:
            db.session.rollback()
            flash('Could not save submission.', 'danger')
            return redirect(url_for('view_lesson', lesson_id=lesson_id))
    else:
        db.session.commit()

    flash('Task submitted.', 'success')
    return redirect(url_for('view_lesson', lesson_id=lesson_id))


@app.route('/lesson/<int:lesson_id>/exam')
@login_required
def take_lesson_exam(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    if not _student_can_access_lesson(lesson):
        flash('You do not have access to this exam.', 'danger')
        return redirect(url_for('index'))
    if lesson.content_type != 'exam' or not lesson.quiz_id:
        flash('No exam attached to this lesson.', 'warning')
        return redirect(url_for('view_lesson', lesson_id=lesson_id))
    return redirect(url_for('take_quiz', quiz_id=lesson.quiz_id))


def update_student_progress(student_id, course_id, earned_points, total_points):
    progress = StudentProgress.query.filter_by(
        student_id=student_id,
        course_id=course_id
    ).first()
    
    if not progress:
        # Create new progress record with initial values
        progress = StudentProgress(
            student_id=student_id,
            course_id=course_id,
            points_earned=0,  # Initialize to 0
            total_points=0    # Initialize to 0
        )
        db.session.add(progress)
    
    # Ensure points_earned and total_points are not None
    if progress.points_earned is None:
        progress.points_earned = 0
    if progress.total_points is None:
        progress.total_points = 0
    
    # Now safely add the points
    progress.points_earned += float(earned_points)
    progress.total_points += float(total_points)
    progress.last_activity = datetime.utcnow()
    progress.updated_at = datetime.utcnow()
    
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error updating student progress: {str(e)}")
        raise

@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@app.context_processor
def inject_asset_version():
    """Cache-buster: rebuilds whenever style.css (or its peers) is edited.
    Use as ?v={{ asset_v }} on <link>/<script> tags in templates."""
    try:
        candidates = [
            os.path.join(app.static_folder, 'css', 'style.css'),
            os.path.join(app.static_folder, 'css', 'rich-editor.css'),
            os.path.join(app.static_folder, 'js', 'icons-shim.js'),
        ]
        latest = max(os.path.getmtime(p) for p in candidates if os.path.exists(p))
        return {'asset_v': str(int(latest))}
    except Exception:
        return {'asset_v': '0'}

def init_db():
    with app.app_context():
        # Destructive reset only when explicitly requested via env var.
        # Default is OFF for all backends so app restarts never wipe data.
        # To intentionally reset locally, run with: $env:INIT_DB_RESET='1'
        is_sqlite = app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite')
        reset_db = os.environ.get('INIT_DB_RESET', '0') == '1'
        seed_demo = os.environ.get('INIT_DB_SEED', '1') == '1'

        # Persistence sanity log — confirm we're not wiping data on every boot.
        try:
            uri = app.config['SQLALCHEMY_DATABASE_URI']
            shown = uri.split('@')[-1] if '@' in uri else uri  # hide credentials
            print(f"[init_db] using DB: {shown}")
            print(f"[init_db] INIT_DB_RESET={'ON (DESTRUCTIVE)' if reset_db else 'off'} "
                  f"INIT_DB_SEED={'on' if seed_demo else 'off'}")
        except Exception:
            pass

        if reset_db:
            db.drop_all()
        db.create_all()

        # Lightweight migration: ensure new optional columns exist on already-deployed tables.
        try:
            with db.engine.begin() as conn:
                dialect = db.engine.dialect.name
                if dialect == 'sqlite':
                    cols = [row[1] for row in conn.exec_driver_sql("PRAGMA table_info(course)")]
                    if 'image_url' not in cols:
                        conn.exec_driver_sql("ALTER TABLE course ADD COLUMN image_url VARCHAR(255)")
                    if 'badge_url' not in cols:
                        conn.exec_driver_sql("ALTER TABLE course ADD COLUMN badge_url VARCHAR(255)")
                else:
                    conn.exec_driver_sql(
                        "ALTER TABLE course ADD COLUMN IF NOT EXISTS image_url VARCHAR(255)"
                    )
                    conn.exec_driver_sql(
                        "ALTER TABLE course ADD COLUMN IF NOT EXISTS badge_url VARCHAR(255)"
                    )
        except Exception as e:
            print(f"[migration] course.image_url ensure failed: {e}")

        # Ensure lesson.model_answer exists (teacher/admin-only lab answer key).
        try:
            with db.engine.begin() as conn:
                dialect = db.engine.dialect.name
                if dialect == 'sqlite':
                    cols = [row[1] for row in conn.exec_driver_sql("PRAGMA table_info(lesson)")]
                    if 'model_answer' not in cols:
                        conn.exec_driver_sql("ALTER TABLE lesson ADD COLUMN model_answer TEXT")
                else:
                    conn.exec_driver_sql(
                        "ALTER TABLE lesson ADD COLUMN IF NOT EXISTS model_answer TEXT"
                    )
        except Exception as e:
            print(f"[migration] lesson.model_answer ensure failed: {e}")

        # Reconcile legacy User.is_teacher / is_superadmin booleans with the
        # canonical role string. Older rows could be out of sync, which would
        # hide staff-only nav links from real admins/teachers.
        try:
            fixed = 0
            for u in User.query.all():
                role = (u.role or 'student').lower()
                want_super = role in {'superuser', 'admin'}
                want_teach = role in {'superuser', 'teacher'}
                if bool(u.is_superadmin) != want_super or bool(u.is_teacher) != want_teach:
                    u.is_superadmin = want_super
                    u.is_teacher = want_teach
                    fixed += 1
            if fixed:
                db.session.commit()
                print(f"[migration] reconciled role flags on {fixed} user(s)")
        except Exception as e:
            print(f"[migration] role-flag reconcile failed: {e}")

        # Ensure every video lesson has a topical video matching its course title.
        # We update lessons whose video_url is missing OR still the generic
        # "Python in 100 seconds" placeholder. Manually-set videos pointing at
        # something else are left alone.
        try:
            placeholder = 'https://www.youtube.com/embed/x7X9w_GIm1s'
            topical = [
                (('1z0', 'oracle', 'java'),       'https://www.youtube.com/embed/eIrMbAQSU34'),
                (('power bi', 'pl-300'),          'https://www.youtube.com/embed/TmhQCQr_DCA'),
                (('az-900', 'azure fundamentals'),
                                                  'https://www.youtube.com/embed/NKEFWyqJ5XA'),
                (('az-', 'azure'),                'https://www.youtube.com/embed/IFpKngfH7Hs'),
                (('aws',),                        'https://www.youtube.com/embed/a9__D53WsUs'),
                (('gcp', 'google cloud'),         'https://www.youtube.com/embed/4D3X6Xl5c_0'),
                (('sql',),                        'https://www.youtube.com/embed/zsjvFFKOm3c'),
                (('pcap', 'python'),              'https://www.youtube.com/embed/x7X9w_GIm1s'),
                (('ai', 'artificial intelligence', 'machine learning'),
                                                  'https://www.youtube.com/embed/PeMlggyqz0Y'),
            ]
            import re
            def _topical_for(title_lower):
                # 'ai' must be a whole word so we don't match 'training', 'maintain', etc.
                tokens = set(re.findall(r"[a-z0-9-]+", title_lower))
                for keys, url in topical:
                    for k in keys:
                        if ' ' in k or '-' in k:
                            if k in title_lower:
                                return url
                        elif k == 'ai':
                            if 'ai' in tokens:
                                return url
                        else:
                            if k in title_lower:
                                return url
                return placeholder  # fallback

            # All URLs that our seeder has ever auto-assigned — safe to overwrite
            # because they were never user-chosen.
            seeded_urls = {placeholder} | {url for _, url in topical}

            video_lessons = Lesson.query.filter_by(content_type='video').all()
            changed = 0
            for ln in video_lessons:
                title = (ln.course.title or '').lower() if ln.course else ''
                want = _topical_for(title)
                current = (ln.video_url or '').strip()
                if not current or current in seeded_urls:
                    if ln.video_url != want:
                        ln.video_url = want
                        changed += 1
            if changed:
                db.session.commit()
                print(f"[migration] retargeted {changed} video lesson(s) to topical content")
        except Exception as e:
            print(f"[migration] intro-video backfill failed: {e}")

        # Rename the seeded "Lesson 1: Welcome" placeholder to "About this course"
        # and replace its generic body with a topical course overview. Also refresh
        # bodies that match a previously-seeded short version. User-edited intros
        # are left untouched.
        try:
            old_title = 'Lesson 1: Welcome'
            seeded_body_token = 'Use this lesson to introduce your course.'
            # Markers that identify content we previously auto-seeded and can safely overwrite.
            prior_seeded_markers = (
                'This course prepares you for the <strong>PCAP',
                'This course prepares you for the <strong>Oracle',
                'This course prepares you for the <strong>Microsoft Power BI',
                'This course prepares you for the <strong>Microsoft Azure Fundamentals',
                'This course introduces you to <strong>Microsoft Azure</strong>',
                'This course covers <strong>SQL</strong>',
                'This course introduces you to <strong>Amazon Web Services',
                'This course introduces you to <strong>Google Cloud Platform',
                'This course introduces you to <strong>Artificial Intelligence',
                'In this course you will learn the basics.',
                'This course will guide you through the key concepts step by step.',
                '<h2>PCAP',
                '<h2>PCAP \u2013 Certified Associate Python Programmer',
            )
            candidates = Lesson.query.filter(
                Lesson.content_type == 'lesson',
                Lesson.title.in_([old_title, 'About this course'])
            ).all()
            changed = 0
            for ln in candidates:
                body = ln.content or ''
                is_stale = (
                    seeded_body_token in body
                    or body.strip() == ''
                    or any(m in body for m in prior_seeded_markers)
                )
                if not is_stale:
                    continue
                new_body = _about_html_for(ln.course) if ln.course else body
                if ln.title != 'About this course' or new_body != body:
                    ln.title = 'About this course'
                    ln.content = new_body
                    changed += 1
            if changed:
                db.session.commit()
                print(f"[migration] refreshed {changed} 'About this course' lesson(s)")
        except Exception as e:
            print(f"[migration] about-lesson backfill failed: {e}")

        # Renumber seeded lesson titles so they start at 1 (the About lesson
        # is the first item but no longer carries a "Lesson N:" prefix).
        try:
            rename_map = {
                'Lesson 2: Watch \u2014 Intro Video': 'Lesson 1: Watch \u2014 Intro Video',
                'Lesson 3: Task \u2014 Your First Submission': 'Lesson 2: Task \u2014 Your First Submission',
                'Lesson 4: Exam': 'Lesson 3: Exam',
                'Lesson 2: Watch \u2014 Python in 100 seconds': 'Lesson 1: Watch \u2014 Python in 100 seconds',
                'Lesson 3: Task \u2014 Hello, World!': 'Lesson 2: Task \u2014 Hello, World!',
            }
            changed = 0
            for old, new in rename_map.items():
                rows = Lesson.query.filter_by(title=old).all()
                for ln in rows:
                    ln.title = new
                    changed += 1
            if changed:
                db.session.commit()
                print(f"[migration] renumbered {changed} lesson title(s) to start at 1")
        except Exception as e:
            print(f"[migration] lesson renumber backfill failed: {e}")

        # Skip seeding if users already exist (avoids duplicate seed on remote DB)
        if User.query.first() is not None:
            return
        if not seed_demo:
            return

        # Create a superadmin account
        superadmin = User(
            username='admin',
            email='admin@example.com',
            is_teacher=True,
            is_superadmin=True
        )
        superadmin.set_password('admin')
        
        # Create a test teacher account
        teacher = User(
            username='teacher',
            email='teacher@example.com',
            is_teacher=True,
            is_superadmin=False
        )
        teacher.set_password('password')
        
        # Create a test student account
        student = User(
            username='student',
            email='student@example.com',
            is_teacher=False,
            is_superadmin=False
        )
        student.set_password('password')
        
        db.session.add(superadmin)
        db.session.add(teacher)
        db.session.add(student)
        db.session.commit()

        # ---- Demo content: course + lessons of each type ----
        demo_course = Course(
            title='Intro to Python',
            description='A short demo course showcasing every lesson type.',
            teacher_id=teacher.id,
        )
        db.session.add(demo_course)
        db.session.flush()

        db.session.add(Enrollment(
            student_id=student.id, course_id=demo_course.id
        ))

        demo_quiz = Quiz(
            course_id=demo_course.id,
            title='Final Exam — Python Basics',
            description='Short exam covering the demo lessons.',
        )
        db.session.add(demo_quiz)
        db.session.flush()

        q = Question(
            quiz_id=demo_quiz.id,
            question_type='multiple_choice',
            question_html='<p>What does <code>print()</code> do?</p>',
            points=1.0,
        )
        db.session.add(q)
        db.session.flush()
        db.session.add_all([
            QuestionOption(question_id=q.id, option_html='Outputs text to the console', is_correct=True, order=1),
            QuestionOption(question_id=q.id, option_html='Sends data to a printer', is_correct=False, order=2),
            QuestionOption(question_id=q.id, option_html='Creates a new variable', is_correct=False, order=3),
        ])

        db.session.add_all([
            Lesson(
                course_id=demo_course.id,
                title='Lesson 1: Welcome',
                content='<p>Welcome to <strong>Intro to Python</strong>! '
                        'In this course you will learn the basics.</p>',
                content_type='lesson',
                order=1,
                points=1.0,
            ),
            Lesson(
                course_id=demo_course.id,
                title='Lesson 1: Watch — Python in 100 seconds',
                content='<p>Watch this short overview of Python.</p>',
                content_type='video',
                video_url='https://www.youtube.com/embed/x7X9w_GIm1s',
                order=2,
                points=1.0,
            ),
            Lesson(
                course_id=demo_course.id,
                title='Lesson 2: Task — Hello, World!',
                content='',
                content_type='task',
                task_instructions='<p>Write a Python program that prints '
                                  '<code>Hello, World!</code> and paste it below.</p>',
                order=3,
                points=2.0,
            ),
            Lesson(
                course_id=demo_course.id,
                title='Lesson 3: Exam',
                content='',
                content_type='exam',
                quiz_id=demo_quiz.id,
                order=4,
                points=5.0,
            ),
        ])
        db.session.commit()

# ---------------------------------------------------------------------------
# Teacher / Administrator: Lab Answer Key (SAQA 118792 AISD only)
# ---------------------------------------------------------------------------
# A single page listing the practical labs of the SAQA 118792 AISD course
# with the curated model answers from ``_saqa_aisd_answers.LAB_ANSWERS``.
# Visible only to teachers and administrators — students never see the link
# or the page.

@app.route('/teacher/lab-answers')
@login_required
@requires_staff
def lab_answers():
    from _saqa_aisd_answers import LAB_TITLES, LAB_LESSON_HINTS

    course = (Course.query
              .filter(Course.title.ilike('%SAQA 118792%'))
              .first())

    # Build the list straight from the curated answers dict so the page works
    # even if the SAQA course hasn't been built into the DB yet. When matching
    # lesson rows exist, attach them so we can link to the student-facing page.
    course_lessons = sorted(course.lessons,
                            key=lambda l: (l.order or 0, l.id)) if course else []

    def _find_lesson(hint):
        h = hint.lower()
        for l in course_lessons:
            if 'practical lab' in (l.title or '').lower() and h in (l.title or '').lower():
                return l
        return None

    labs = []
    for n in sorted(SAQA_LAB_ANSWERS.keys()):
        labs.append({
            'order':       n,
            'title':       LAB_TITLES.get(n, f'Lab {n}'),
            'lesson':      _find_lesson(LAB_LESSON_HINTS.get(n, '')),
            'answer_html': SAQA_LAB_ANSWERS[n],
        })

    return render_template(
        'teacher/lab_answers.html',
        course=course,
        labs=labs,
    )


if __name__ == '__main__':
    init_db()  # Initialize database on startup
    app.run(debug=True)
