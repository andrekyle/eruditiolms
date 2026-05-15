from flask import Flask, render_template, request, redirect, url_for, flash, session
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

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or os.urandom(24).hex()

# Database: prefer DATABASE_URL (e.g. Supabase Postgres), fall back to local SQLite
_db_url = os.environ.get('DATABASE_URL', 'sqlite:///lms.db')
# SQLAlchemy 1.4+ requires postgresql:// scheme (not postgres://)
if _db_url.startswith('postgres://'):
    _db_url = _db_url.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = _db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
    password_hash = db.Column(db.String(128))
    is_teacher = db.Column(db.Boolean, default=False)
    is_superadmin = db.Column(db.Boolean, default=False)
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

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
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
    
    questions = db.relationship('Question', backref='quiz', lazy=True)

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
    student_responses = db.relationship('QuestionResponse', backref='question', lazy=True)

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
    question_responses = db.relationship('QuestionResponse', backref='quiz_response', lazy=True)

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
            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('auth/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/manage/users')
@login_required
@requires_superadmin
def manage_users():
    users = User.query.all()
    return render_template('admin/manage_users.html', users=users)

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
            os.makedirs(upload_path, exist_ok=True)
            avatar_file.save(os.path.join(upload_path, filename))
            user.avatar_url = url_for('static', filename=f'uploads/avatars/{filename}')

        # Remove avatar if requested
        if request.form.get('remove_avatar') == '1':
            user.avatar_url = None

        # Password change (optional)
        if new_password or confirm_password or current_password:
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
    if current_user.is_authenticated:
        if current_user.is_teacher:
            # Teachers see their own courses
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
        for course in all_courses:
            course_stats[course.id] = {
                'student_count': len(course.enrollments),
                'quiz_count': len(course.quizzes)
            }
        
        return render_template('dashboard.html', 
                             courses=courses, 
                             enrolled_courses=enrolled_courses, 
                             course_stats=course_stats)
    return render_template('index.html')

@app.route('/course/create', methods=['POST'])
@login_required
def create_course():
    if not current_user.is_teacher:
        flash('Only teachers can create courses.', 'danger')
        return redirect(url_for('index'))
    
    title = request.form.get('title')
    description = request.form.get('description')
    
    if not title:
        flash('Course title is required.', 'danger')
        return redirect(url_for('index'))
    
    course = Course(
        title=title,
        description=description,
        teacher_id=current_user.id
    )
    
    db.session.add(course)
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
    if not current_user.is_teacher:
        flash('Only teachers can enroll students.', 'error')
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
    if not current_user.is_teacher:
        flash('Only teachers can unenroll students.', 'error')
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

@app.route('/course/<int:course_id>/edit', methods=['POST'])
@login_required
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    
    # Check if the user is the teacher of this course
    if not current_user.is_teacher or current_user.id != course.teacher_id:
        flash('You do not have permission to edit this course.', 'danger')
        return redirect(url_for('index'))
    
    title = request.form.get('title')
    description = request.form.get('description')
    
    if not title:
        flash('Course title is required.', 'danger')
        return redirect(url_for('view_course', course_id=course_id))
    
    course.title = title
    course.description = description
    db.session.commit()
    
    flash('Course updated successfully!', 'success')
    return redirect(url_for('view_course', course_id=course_id))

@app.route('/course/<int:course_id>/quiz/create', methods=['GET', 'POST'])
@login_required
def create_quiz(course_id):
    course = Course.query.get_or_404(course_id)
    
    # Check if the user is the teacher of this course
    if not current_user.is_teacher or current_user.id != course.teacher_id:
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
    
    # Check if the user is the teacher of this course
    if not current_user.is_teacher or current_user.id != course.teacher_id:
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
    
    # Check if the user is the teacher of this course
    if not current_user.is_teacher or current_user.id != course.teacher_id:
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
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template('quiz/view_quiz.html', quiz=quiz)

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
                    
            # Handle other question types...
                
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

    completed = (not current_user.is_teacher
                 and _is_lesson_completed(lesson.id, current_user.id))

    return render_template('lesson/view.html',
                           lesson=lesson,
                           course=lesson.course,
                           submission=submission,
                           completed=completed)


@app.route('/lesson/<int:lesson_id>/complete', methods=['POST'])
@login_required
def complete_lesson(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    if not _student_can_access_lesson(lesson) or current_user.is_teacher:
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

def init_db():
    with app.app_context():
        # Destructive reset only when explicitly requested via env var.
        # Defaults to True for SQLite (dev convenience) and False otherwise (safe for Postgres/Supabase).
        is_sqlite = app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite')
        reset_default = '1' if is_sqlite else '0'
        reset_db = os.environ.get('INIT_DB_RESET', reset_default) == '1'
        seed_demo = os.environ.get('INIT_DB_SEED', '1') == '1'

        if reset_db:
            db.drop_all()
        db.create_all()

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
                title='Lesson 2: Watch — Python in 100 seconds',
                content='<p>Watch this short overview of Python.</p>',
                content_type='video',
                video_url='https://www.youtube.com/embed/x7X9w_GIm1s',
                order=2,
                points=1.0,
            ),
            Lesson(
                course_id=demo_course.id,
                title='Lesson 3: Task — Hello, World!',
                content='',
                content_type='task',
                task_instructions='<p>Write a Python program that prints '
                                  '<code>Hello, World!</code> and paste it below.</p>',
                order=3,
                points=2.0,
            ),
            Lesson(
                course_id=demo_course.id,
                title='Lesson 4: Exam',
                content='',
                content_type='exam',
                quiz_id=demo_quiz.id,
                order=4,
                points=5.0,
            ),
        ])
        db.session.commit()

if __name__ == '__main__':
    init_db()  # Initialize database on startup
    app.run(debug=True)
