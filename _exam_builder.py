"""Shared builder for 50-question final exams across all courses.

Each per-cert data module defines:
    EXAM_TITLE     = '...'
    LESSON_TITLE   = '...'
    COURSE_LIKE    = 'SQL LIKE pattern matching Course.title'
    DESCRIPTION    = 'short description'
    QUESTIONS      = [
        ("<p>...</p>", [("opt", True/False) x4], "feedback"),
        ... 50 total ...
    ]
    LEGACY_EXAM_TITLES   = [...]   # optional, quizzes to remove
    LEGACY_LESSON_TITLES = [...]   # optional, lessons to remove
"""
from app import app, db, Course, Lesson, Quiz, Question, QuestionOption


def build(data_mod):
    EXAM_TITLE   = data_mod.EXAM_TITLE
    LESSON_TITLE = data_mod.LESSON_TITLE
    COURSE_LIKE  = data_mod.COURSE_LIKE
    DESCRIPTION  = getattr(data_mod, 'DESCRIPTION', '50-question final practice exam.')
    QUESTIONS    = data_mod.QUESTIONS
    LEGACY_EXAM_TITLES   = getattr(data_mod, 'LEGACY_EXAM_TITLES', [])
    LEGACY_LESSON_TITLES = getattr(data_mod, 'LEGACY_LESSON_TITLES', [])

    assert len(QUESTIONS) == 50, f'{COURSE_LIKE}: expected 50 questions, got {len(QUESTIONS)}'
    for i, (qh, opts, fb) in enumerate(QUESTIONS, 1):
        assert len(opts) == 4, f'Q{i}: must have 4 options'
        assert sum(1 for _, c in opts if c) == 1, f'Q{i}: must have exactly 1 correct option'

    with app.app_context():
        course = Course.query.filter(Course.title.like(COURSE_LIKE)).first()
        if not course:
            raise SystemExit(f'no course matches LIKE {COURSE_LIKE!r}')
        print(f'course: id={course.id} title={course.title!r}')

        # Clean legacy variants
        for old_title in LEGACY_LESSON_TITLES:
            old_lesson = Lesson.query.filter_by(course_id=course.id, title=old_title).first()
            if old_lesson:
                db.session.delete(old_lesson)
                print(f'  deleted legacy lesson: {old_title!r}')
        for old_qtitle in LEGACY_EXAM_TITLES:
            old_quiz = Quiz.query.filter_by(course_id=course.id, title=old_qtitle).first()
            if old_quiz:
                for q in list(old_quiz.questions):
                    db.session.delete(q)
                db.session.delete(old_quiz)
                print(f'  deleted legacy quiz: {old_qtitle!r}')
        db.session.flush()

        # Upsert quiz
        quiz = Quiz.query.filter_by(course_id=course.id, title=EXAM_TITLE).first()
        if quiz:
            for q in list(quiz.questions):
                db.session.delete(q)
            db.session.flush()
            print(f'  reusing quiz id={quiz.id}, cleared old questions')
        else:
            quiz = Quiz(course_id=course.id, title=EXAM_TITLE, description=DESCRIPTION)
            db.session.add(quiz)
            db.session.flush()
            print(f'  created quiz id={quiz.id}')

        for qh, opts, fb in QUESTIONS:
            q = Question(
                quiz_id=quiz.id,
                question_type='multiple_choice',
                question_html=qh,
                points=1.0,
                feedback=fb,
            )
            db.session.add(q)
            db.session.flush()
            for i, (oh, is_correct) in enumerate(opts):
                db.session.add(QuestionOption(
                    question_id=q.id, option_html=oh, is_correct=is_correct, order=i,
                ))

        # Upsert exam lesson at a new trailing order
        lesson = Lesson.query.filter_by(course_id=course.id, title=LESSON_TITLE).first()
        max_order = db.session.query(db.func.max(Lesson.order)).filter(
            Lesson.course_id == course.id
        ).scalar() or 0
        new_order = max_order + 1

        if lesson:
            lesson.quiz_id = quiz.id
            lesson.content_type = 'exam'
            lesson.order = new_order
            print(f'  updated existing lesson id={lesson.id} order={new_order}')
        else:
            lesson = Lesson(
                course_id=course.id,
                title=LESSON_TITLE,
                content=f'<p>{DESCRIPTION}</p>',
                content_type='exam',
                quiz_id=quiz.id,
                order=new_order,
                points=1.0,
            )
            db.session.add(lesson)
            print(f'  created new lesson order={new_order}')

        db.session.commit()
        print(f'DONE. course_id={course.id} quiz_id={quiz.id} questions=50 lesson_order={new_order}')
