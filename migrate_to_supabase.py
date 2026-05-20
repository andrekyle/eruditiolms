"""One-shot migration: copy courses (and lessons/quizzes/questions/options)
from the local SQLite DB into whatever DATABASE_URL is currently set to
(e.g. Supabase Postgres).

Usage (PowerShell):
    $env:DATABASE_URL = "postgresql://...supabase.../postgres?sslmode=require"
    python migrate_to_supabase.py

- Re-points every course.teacher_id to the admin user on the target DB.
- Skips rows whose primary key already exists on the target.
- Re-enrolls admin (and any other existing teachers/admins) in every course.
"""
import os
import sqlite3
import sys

# Ensure we use the env DATABASE_URL (Supabase), not the local SQLite default.
if not os.environ.get('DATABASE_URL'):
    print('ERROR: set $env:DATABASE_URL to your Supabase Postgres URL first.')
    sys.exit(1)

from app import (
    app, db, User, Course, Lesson, Quiz, Question, QuestionOption,
    auto_enroll_teacher,
)

LOCAL_DB = os.path.join(os.path.dirname(__file__), 'instance', 'lms.db')
if not os.path.exists(LOCAL_DB):
    print(f'ERROR: local SQLite DB not found at {LOCAL_DB}')
    sys.exit(1)


def fetch_all(conn, table):
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {table}')
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def main():
    src = sqlite3.connect(LOCAL_DB)
    src.row_factory = sqlite3.Row

    with app.app_context():
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print('ERROR: no admin user on target DB. Create one first.')
            sys.exit(1)

        # ---- Courses ----
        existing_course_ids = {c.id for c in Course.query.all()}
        added_courses = 0
        for row in fetch_all(src, 'course'):
            if row['id'] in existing_course_ids:
                continue
            c = Course(
                id=row['id'],
                title=row['title'],
                description=row.get('description'),
                image_url=row.get('image_url'),
                badge_url=row.get('badge_url'),
                teacher_id=admin.id,  # re-point to target admin
            )
            db.session.add(c)
            added_courses += 1
        db.session.commit()
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
            ))
            added_quizzes += 1
        db.session.commit()
        print(f'Quizzes added: {added_quizzes}')

        # ---- Lessons ----
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
                order=row.get('order') or 0,
                points=row.get('points') or 1.0,
            ))
            added_lessons += 1
        db.session.commit()
        print(f'Lessons added: {added_lessons}')

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
                points=row.get('points') or 1.0,
                feedback=row.get('feedback'),
            ))
            added_questions += 1
        db.session.commit()
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
                order=row.get('order'),
                matching_answer=row.get('matching_answer'),
                drag_zone=row.get('drag_zone'),
            ))
            added_options += 1
        db.session.commit()
        print(f'Question options added: {added_options}')

        # ---- Reset Postgres sequences so future inserts don't collide ----
        try:
            from sqlalchemy import text
            for tbl in ('course', 'lesson', 'quiz', 'question', 'question_option'):
                db.session.execute(text(
                    f"SELECT setval(pg_get_serial_sequence('{tbl}', 'id'),"
                    f" COALESCE((SELECT MAX(id) FROM {tbl}), 1))"
                ))
            db.session.commit()
            print('Postgres id sequences synced.')
        except Exception as e:
            print(f'(sequence sync skipped: {e})')

        # ---- Auto-enroll admin + any existing teachers/admins in every course ----
        total_added = 0
        for u in User.query.filter(User.role.in_(['teacher', 'admin', 'superuser'])).all():
            total_added += auto_enroll_teacher(u)
        print(f'Enrollments added for staff users: {total_added}')

    src.close()
    print('Migration complete.')


if __name__ == '__main__':
    main()
