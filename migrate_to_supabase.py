# pyright: reportCallIssue=false
"""One-shot migration: copy all user-generated data from the local SQLite DB
into whatever DATABASE_URL is currently set to (e.g. Supabase Postgres).

Tables migrated (in FK-safe order):
    user, course, quiz, question, question_option, lesson,
    enrollment, lesson_completion, task_submission, student_progress,
    quiz_response, question_response, question_response_option.

Behaviour:
- Skips users that already exist on the target (matched by username/email/id).
- Skips other rows whose primary key already exists on the target.
- Preserves ids, timestamps, and password hashes where possible.
- scrypt password hashes are replaced with a pbkdf2 temp password
  (Vercel's runtime often lacks OpenSSL scrypt support). Affected users
  are written to `migration_temp_passwords.txt`.
- Wraps everything in a single transaction; rolls back on failure.
- Resets Postgres id sequences after a successful run.
- Re-enrols admins/teachers/superusers in every course.

Usage (PowerShell):
    $env:DATABASE_URL = "postgresql://...supabase.../postgres?sslmode=require"
    python migrate_to_supabase.py

Optional env vars:
    MIGRATION_TEMP_PASSWORD   override the default temp password ("ChangeMe2026!")
    MIGRATION_DRY_RUN=1       roll back at the end instead of committing
"""
import os
import sqlite3
import sys
from datetime import datetime

from werkzeug.security import generate_password_hash

if not os.environ.get('DATABASE_URL'):
    print('ERROR: set $env:DATABASE_URL to your Supabase Postgres URL first.')
    sys.exit(1)

from app import (
    app, db, User, Course, Lesson, Quiz, Question, QuestionOption,
    Enrollment, LessonCompletion, TaskSubmission, StudentProgress,
    QuizResponse, QuestionResponse, QuestionResponseOption,
    auto_enroll_teacher,
)

LOCAL_DB = os.path.join(os.path.dirname(__file__), 'instance', 'lms.db')
if not os.path.exists(LOCAL_DB):
    print(f'ERROR: local SQLite DB not found at {LOCAL_DB}')
    sys.exit(1)

TEMP_PASSWORD = os.environ.get('MIGRATION_TEMP_PASSWORD', 'ChangeMe2026!')
DRY_RUN = os.environ.get('MIGRATION_DRY_RUN') == '1'
TEMP_PASSWORDS_FILE = os.path.join(
    os.path.dirname(__file__), 'migration_temp_passwords.txt'
)


def fetch_all(conn, table):
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM "{table}"')
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def _parse_dt(value):
    """SQLite returns datetimes as ISO strings; Postgres wants real datetimes."""
    if value is None or isinstance(value, datetime):
        return value
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value)
        except ValueError:
            try:
                return datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    return value


def _opt_float(value, default=None):
    """Return float(value) preserving 0.0; only fall back when value is None."""
    return default if value is None else float(value)


def _opt_int(value, default=None):
    return default if value is None else int(value)


def main():
    src = sqlite3.connect(LOCAL_DB)
    src.row_factory = sqlite3.Row

    with app.app_context():
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print('ERROR: no admin user on target DB. Create one first.')
            sys.exit(1)

        try:
            # ---- Users ----
            # Build a local-id -> target-id map so we can remap FKs (student_id,
            # user_id, teacher_id) on rows whose owner already exists on the
            # target under a different id.
            target_users = User.query.all()
            target_by_username = {u.username: u for u in target_users}
            target_by_email = {u.email: u for u in target_users}
            existing_user_ids = {u.id for u in target_users}
            user_id_map = {}  # local id -> target id
            added_users = 0
            skipped_users = 0
            temp_password_users = []
            for row in fetch_all(src, 'user'):
                uname = row.get('username')
                email = row.get('email')
                existing = target_by_username.get(uname) or target_by_email.get(email)
                if existing is not None:
                    user_id_map[row['id']] = existing.id
                    skipped_users += 1
                    continue
                if row['id'] in existing_user_ids:
                    # id collision with an unrelated user; let Postgres assign new id
                    new_id = None
                else:
                    new_id = row['id']
                src_hash = row.get('password_hash') or ''
                if src_hash.startswith('scrypt:') or not src_hash:
                    password_hash = generate_password_hash(
                        TEMP_PASSWORD, method='pbkdf2:sha256'
                    )
                    temp_password_users.append(uname)
                else:
                    password_hash = src_hash
                u = User(
                    id=new_id,
                    username=uname,
                    email=email,
                    password_hash=password_hash,
                    full_name=row.get('full_name'),
                    first_name=row.get('first_name'),
                    last_name=row.get('last_name'),
                    bio=row.get('bio'),
                    phone=row.get('phone'),
                    location=row.get('location'),
                    avatar_url=row.get('avatar_url'),
                    created_at=_parse_dt(row.get('created_at')),
                    updated_at=_parse_dt(row.get('updated_at')),
                )
                u.apply_role(row.get('role') or 'student')
                db.session.add(u)
                db.session.flush()  # need u.id for the map
                user_id_map[row['id']] = u.id
                added_users += 1
            db.session.flush()
            print(f'Users added: {added_users} (skipped existing: {skipped_users})')
            if temp_password_users:
                with open(TEMP_PASSWORDS_FILE, 'w', encoding='utf-8') as f:
                    f.write(f'# Generated {datetime.utcnow().isoformat()}Z\n')
                    f.write(f'# Temporary password: {TEMP_PASSWORD}\n')
                    f.write('# These users had scrypt hashes (unsupported on Vercel)\n')
                    f.write('# and were reset. Ask them to change passwords on first login.\n')
                    for name in temp_password_users:
                        f.write(name + '\n')
                print(
                    f'  {len(temp_password_users)} user(s) got a temp password. '
                    f'List written to {TEMP_PASSWORDS_FILE}'
                )

            def map_uid(local_id):
                """Translate a local user id to its target-db equivalent."""
                if local_id is None:
                    return None
                return user_id_map.get(local_id, local_id)

            # ---- Courses ----
            existing_course_ids = {c.id for c in Course.query.all()}
            added_courses = 0
            for row in fetch_all(src, 'course'):
                if row['id'] in existing_course_ids:
                    continue
                db.session.add(Course(
                    id=row['id'],
                    title=row['title'],
                    description=row.get('description'),
                    image_url=row.get('image_url'),
                    badge_url=row.get('badge_url'),
                    teacher_id=admin.id,  # re-point to target admin
                    created_at=_parse_dt(row.get('created_at')),
                    updated_at=_parse_dt(row.get('updated_at')),
                ))
                added_courses += 1
            db.session.flush()
            print(f'Courses added: {added_courses}')

            # ---- Quizzes ----
            existing_quiz_ids = {q.id for q in Quiz.query.all()}
            added_quizzes = 0
            for row in fetch_all(src, 'quiz'):
                if row['id'] in existing_quiz_ids:
                    continue
                db.session.add(Quiz(
                    id=row['id'],
                    course_id=row['course_id'],
                    title=row['title'],
                    description=row.get('description'),
                    created_at=_parse_dt(row.get('created_at')),
                    updated_at=_parse_dt(row.get('updated_at')),
                ))
                added_quizzes += 1
            db.session.flush()
            print(f'Quizzes added: {added_quizzes}')

            # ---- Questions ----
            existing_question_ids = {q.id for q in Question.query.all()}
            added_questions = 0
            for row in fetch_all(src, 'question'):
                if row['id'] in existing_question_ids:
                    continue
                db.session.add(Question(
                    id=row['id'],
                    quiz_id=row['quiz_id'],
                    question_type=row['question_type'],
                    question_html=row['question_html'],
                    image_url=row.get('image_url'),
                    points=_opt_float(row.get('points'), 1.0),
                    feedback=row.get('feedback'),
                    created_at=_parse_dt(row.get('created_at')),
                    updated_at=_parse_dt(row.get('updated_at')),
                ))
                added_questions += 1
            db.session.flush()
            print(f'Questions added: {added_questions}')

            # ---- Question options ----
            existing_option_ids = {o.id for o in QuestionOption.query.all()}
            added_options = 0
            for row in fetch_all(src, 'question_option'):
                if row['id'] in existing_option_ids:
                    continue
                db.session.add(QuestionOption(
                    id=row['id'],
                    question_id=row['question_id'],
                    option_html=row['option_html'],
                    is_correct=bool(row.get('is_correct')),
                    order=_opt_int(row.get('order')),
                    matching_answer=row.get('matching_answer'),
                    drag_zone=row.get('drag_zone'),
                    created_at=_parse_dt(row.get('created_at')),
                ))
                added_options += 1
            db.session.flush()
            print(f'Question options added: {added_options}')

            # ---- Lessons (depend on Course & Quiz) ----
            existing_lesson_ids = {l.id for l in Lesson.query.all()}
            added_lessons = 0
            for row in fetch_all(src, 'lesson'):
                if row['id'] in existing_lesson_ids:
                    continue
                db.session.add(Lesson(
                    id=row['id'],
                    title=row['title'],
                    content=row.get('content') or '',
                    course_id=row['course_id'],
                    content_type=row.get('content_type') or 'lesson',
                    video_url=row.get('video_url'),
                    task_instructions=row.get('task_instructions'),
                    quiz_id=row.get('quiz_id'),
                    order=_opt_int(row.get('order'), 0),
                    points=_opt_float(row.get('points'), 1.0),
                    created_at=_parse_dt(row.get('created_at')),
                ))
                added_lessons += 1
            db.session.flush()
            print(f'Lessons added: {added_lessons}')

            # ---- Enrollments (skip duplicates by id or (student_id, course_id)) ----
            existing_enrol = {
                (e.student_id, e.course_id) for e in Enrollment.query.all()
            }
            existing_enrol_ids = {e.id for e in Enrollment.query.all()}
            added_enrol = 0
            for row in fetch_all(src, 'enrollment'):
                mapped_student = map_uid(row.get('student_id'))
                key = (mapped_student, row.get('course_id'))
                if key in existing_enrol or row['id'] in existing_enrol_ids:
                    continue
                db.session.add(Enrollment(
                    id=row['id'],
                    student_id=map_uid(row['student_id']),
                    course_id=row['course_id'],
                    created_at=_parse_dt(row.get('created_at')),
                    updated_at=_parse_dt(row.get('updated_at')),
                ))
                added_enrol += 1
            db.session.flush()
            print(f'Enrollments added: {added_enrol}')

            # ---- Lesson completions ----
            existing_lc = {
                (lc.student_id, lc.lesson_id) for lc in LessonCompletion.query.all()
            }
            existing_lc_ids = {lc.id for lc in LessonCompletion.query.all()}
            added_lc = 0
            for row in fetch_all(src, 'lesson_completion'):
                mapped_student = map_uid(row.get('student_id'))
                key = (mapped_student, row.get('lesson_id'))
                if key in existing_lc or row['id'] in existing_lc_ids:
                    continue
                db.session.add(LessonCompletion(
                    id=row['id'],
                    student_id=map_uid(row['student_id']),
                    lesson_id=row['lesson_id'],
                    completed_at=_parse_dt(row.get('completed_at')),
                ))
                added_lc += 1
            db.session.flush()
            print(f'Lesson completions added: {added_lc}')

            # ---- Task submissions ----
            existing_ts_ids = {t.id for t in TaskSubmission.query.all()}
            added_ts = 0
            for row in fetch_all(src, 'task_submission'):
                if row['id'] in existing_ts_ids:
                    continue
                db.session.add(TaskSubmission(
                    id=row['id'],
                    student_id=map_uid(row['student_id']),
                    lesson_id=row['lesson_id'],
                    submission_text=row.get('submission_text') or '',
                    submitted_at=_parse_dt(row.get('submitted_at')),
                    grade=_opt_float(row.get('grade')),
                    feedback=row.get('feedback'),
                ))
                added_ts += 1
            db.session.flush()
            print(f'Task submissions added: {added_ts}')

            # ---- Student progress ----
            existing_sp = {
                (s.student_id, s.course_id) for s in StudentProgress.query.all()
            }
            existing_sp_ids = {s.id for s in StudentProgress.query.all()}
            added_sp = 0
            for row in fetch_all(src, 'student_progress'):
                mapped_student = map_uid(row.get('student_id'))
                key = (mapped_student, row.get('course_id'))
                if key in existing_sp or row['id'] in existing_sp_ids:
                    continue
                db.session.add(StudentProgress(
                    id=row['id'],
                    student_id=map_uid(row['student_id']),
                    course_id=row['course_id'],
                    points_earned=_opt_float(row.get('points_earned'), 0.0),
                    total_points=_opt_float(row.get('total_points'), 0.0),
                    last_activity=_parse_dt(row.get('last_activity')),
                    created_at=_parse_dt(row.get('created_at')),
                    updated_at=_parse_dt(row.get('updated_at')),
                ))
                added_sp += 1
            db.session.flush()
            print(f'Student progress added: {added_sp}')

            # ---- Quiz responses ----
            existing_qr_ids = {r.id for r in QuizResponse.query.all()}
            added_qr = 0
            for row in fetch_all(src, 'quiz_response'):
                if row['id'] in existing_qr_ids:
                    continue
                db.session.add(QuizResponse(
                    id=row['id'],
                    user_id=map_uid(row['user_id']),
                    quiz_id=row['quiz_id'],
                    points=_opt_float(row.get('points')),
                    total_points=_opt_float(row.get('total_points')),
                    created_at=_parse_dt(row.get('created_at')),
                ))
                added_qr += 1
            db.session.flush()
            print(f'Quiz responses added: {added_qr}')

            # ---- Question responses ----
            existing_qresp_ids = {r.id for r in QuestionResponse.query.all()}
            added_qresp = 0
            for row in fetch_all(src, 'question_response'):
                if row['id'] in existing_qresp_ids:
                    continue
                db.session.add(QuestionResponse(
                    id=row['id'],
                    question_id=row['question_id'],
                    user_id=map_uid(row['user_id']),
                    quiz_response_id=row['quiz_response_id'],
                    points=_opt_float(row.get('points')),
                    is_correct=bool(row.get('is_correct')),
                    created_at=_parse_dt(row.get('created_at')),
                ))
                added_qresp += 1
            db.session.flush()
            print(f'Question responses added: {added_qresp}')

            # ---- Question response options (join table) ----
            existing_qro_ids = {r.id for r in QuestionResponseOption.query.all()}
            added_qro = 0
            for row in fetch_all(src, 'question_response_option'):
                if row['id'] in existing_qro_ids:
                    continue
                db.session.add(QuestionResponseOption(
                    id=row['id'],
                    response_id=row['response_id'],
                    option_id=row['option_id'],
                    created_at=_parse_dt(row.get('created_at')),
                ))
                added_qro += 1
            db.session.flush()
            print(f'Question response options added: {added_qro}')

            if DRY_RUN:
                db.session.rollback()
                print('DRY RUN — all changes rolled back.')
            else:
                db.session.commit()

                # ---- Reset Postgres id sequences ----
                try:
                    from sqlalchemy import text
                    for tbl in (
                        'user', 'course', 'lesson', 'quiz', 'question',
                        'question_option', 'enrollment', 'lesson_completion',
                        'task_submission', 'student_progress',
                        'quiz_response', 'question_response',
                        'question_response_option',
                    ):
                        db.session.execute(text(
                            f'SELECT setval(pg_get_serial_sequence(\'"{tbl}"\', \'id\'),'
                            f' COALESCE((SELECT MAX(id) FROM "{tbl}"), 1))'
                        ))
                    db.session.commit()
                    print('Postgres id sequences synced.')
                except Exception as e:
                    db.session.rollback()
                    print(f'WARNING: sequence sync failed: {e}')

                # ---- Auto-enrol staff in every course ----
                total_added = 0
                staff = User.query.filter(
                    User.role.in_(['teacher', 'admin', 'superuser'])  # type: ignore[attr-defined]
                ).all()
                for u in staff:
                    total_added += auto_enroll_teacher(u)
                print(f'Enrollments added for staff users: {total_added}')

        except Exception:
            db.session.rollback()
            raise

    src.close()
    print('Migration complete.' if not DRY_RUN else 'Dry run complete (no changes saved).')


if __name__ == '__main__':
    main()
