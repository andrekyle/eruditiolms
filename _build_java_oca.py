"""Build the 1Z0-808 OCA Java SE 8 Programmer I course.

Replaces the polluted Java course (id 3) with:
- Updated title/description
- Refreshed About lesson at order 1
- 9 topic content lessons + 9 quizzes + 9 exam lessons (orders 2..19)
- 25-question Final Exam quiz + exam lesson (orders 20, 21)

Reads data modules from _java_oca_authoring/.
Idempotent: deletes old lessons/quizzes (cascades) then rebuilds.
"""
import importlib
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent
AUTH = WORKSPACE / "_java_oca_authoring"
sys.path.insert(0, str(AUTH))

from app import app, db, Course, Lesson, Quiz, Question, QuestionOption  # noqa: E402

import about as about_mod  # noqa: E402
import _spec as spec_mod  # noqa: E402
import final_exam as final_mod  # noqa: E402

OLD_COURSE_TITLE_LIKE = '%Java%'
NEW_COURSE_TITLE = '1Z0-808: Oracle Certified Associate, Java SE 8 Programmer I'
NEW_COURSE_DESC = (
    'Prepare for the Oracle Certified Associate, Java SE 8 Programmer I (1Z0-808) exam. '
    'Nine lessons cover every official objective \u2014 Java basics, data types, operators, '
    'arrays, loops, methods and encapsulation, inheritance, exceptions, and selected '
    'classes from the Java API \u2014 each followed by an 8-question quiz, with a '
    '25-question cumulative final exam to simulate test conditions.'
)


def validate_questions(qs, expected_count, label):
    assert isinstance(qs, list), f'{label}: not a list'
    assert len(qs) == expected_count, f'{label}: expected {expected_count} questions, got {len(qs)}'
    for i, q in enumerate(qs):
        assert isinstance(q, tuple) and len(q) == 3, f'{label} q{i}: expected 3-tuple, got {type(q).__name__} len {len(q) if isinstance(q,tuple) else "?"}'
        qhtml, opts, fb = q
        assert isinstance(qhtml, str) and qhtml.strip(), f'{label} q{i}: bad question_html'
        assert isinstance(opts, list) and len(opts) == 4, f'{label} q{i}: need 4 options'
        correct = sum(1 for o in opts if o[1])
        assert correct == 1, f'{label} q{i}: need exactly 1 correct, got {correct}'
        for j, o in enumerate(opts):
            assert isinstance(o, tuple) and len(o) == 2, f'{label} q{i} opt{j}: bad option tuple'
            assert isinstance(o[0], str) and o[0].strip(), f'{label} q{i} opt{j}: bad option_html'
        assert isinstance(fb, str), f'{label} q{i}: bad feedback'


def insert_quiz_with_lesson(course_id, order_start, title, description, lesson_html, questions):
    """Insert (or replace) content lesson, quiz with questions, and exam lesson.
    Returns next free order."""
    # Content lesson
    cl = Lesson(
        title=title,
        content=lesson_html,
        course_id=course_id,
        content_type='lesson',
        order=order_start,
        points=1.0,
    )
    db.session.add(cl)
    db.session.flush()
    print(f'  +lesson  id={cl.id} order={order_start} {title!r}')

    # Quiz
    quiz_title = f'Quiz: {title}'
    quiz = Quiz(course_id=course_id, title=quiz_title, description=description)
    db.session.add(quiz)
    db.session.flush()
    for qhtml, opts, fb in questions:
        q = Question(
            quiz_id=quiz.id, question_type='multiple_choice',
            question_html=qhtml, points=1.0, feedback=fb,
        )
        db.session.add(q)
        db.session.flush()
        for i, (ohtml, correct) in enumerate(opts):
            db.session.add(QuestionOption(
                question_id=q.id, option_html=ohtml,
                is_correct=bool(correct), order=i,
            ))
    print(f'  +quiz    id={quiz.id} {len(questions)} questions')

    # Exam lesson linked to quiz
    exam_order = order_start + 1
    el = Lesson(
        title=quiz_title,
        content='',
        course_id=course_id,
        content_type='exam',
        quiz_id=quiz.id,
        order=exam_order,
        points=1.0,
    )
    db.session.add(el)
    db.session.flush()
    print(f'  +exam    id={el.id} order={exam_order} {quiz_title!r}')

    return exam_order + 1


def main():
    # Validate authored content before touching the DB
    print('--- Validating authored data ---')
    for entry in spec_mod.LESSONS:
        mod = importlib.import_module(entry['module'])
        assert isinstance(mod.LESSON_HTML, str) and len(mod.LESSON_HTML) > 500, f'{entry["module"]}: short LESSON_HTML'
        validate_questions(mod.QUESTIONS, 8, entry['module'])
        print(f'  OK {entry["module"]} ({len(mod.LESSON_HTML)} chars HTML, 8 Qs)')
    validate_questions(final_mod.QUESTIONS, 25, 'final_exam')
    print('  OK final_exam (25 Qs)')

    with app.app_context():
        course = Course.query.filter(Course.title.ilike(OLD_COURSE_TITLE_LIKE)).first()
        if not course:
            print('No Java course found.')
            return
        print(f'\nFound course id={course.id} title={course.title!r}')

        # Update course title/description
        course.title = NEW_COURSE_TITLE
        course.description = NEW_COURSE_DESC

        # Delete every existing lesson and quiz for this course (cascades clean up
        # questions, options, responses, progress thanks to relationship cascades).
        existing_lessons = Lesson.query.filter_by(course_id=course.id).all()
        existing_quizzes = Quiz.query.filter_by(course_id=course.id).all()
        print(f'Deleting {len(existing_lessons)} existing lessons, {len(existing_quizzes)} existing quizzes...')
        for l in existing_lessons:
            db.session.delete(l)
        for q in existing_quizzes:
            db.session.delete(q)
        db.session.flush()

        # 1. About lesson at order 1
        about_lesson = Lesson(
            title='About this course',
            content=about_mod.ABOUT_HTML,
            course_id=course.id,
            content_type='lesson',
            order=1,
            points=1.0,
        )
        db.session.add(about_lesson)
        db.session.flush()
        print(f'\n+about   id={about_lesson.id} order=1')

        # 2..19: nine topic blocks
        next_order = 2
        for entry in spec_mod.LESSONS:
            print(f'\n[{entry["module"]}] {entry["title"]}')
            mod = importlib.import_module(entry['module'])
            next_order = insert_quiz_with_lesson(
                course_id=course.id,
                order_start=next_order,
                title=entry['title'],
                description=entry['quiz_desc'],
                lesson_html=mod.LESSON_HTML,
                questions=mod.QUESTIONS,
            )

        # 20..21: Final Exam
        print('\n[final_exam] Final Exam (25 questions)')
        final_lesson_html = (
            '<h2>Final Exam \u2014 1Z0-808 cumulative practice test</h2>'
            '<p>This 25-question cumulative exam draws from all nine objectives of the '
            'Oracle Certified Associate, Java SE 8 Programmer I exam. Allow yourself about '
            '60 minutes and aim for at least 70% to be comfortable with the real exam\u2019s '
            '65% pass mark.</p>'
            '<p>Topics covered: Java basics, data types, operators and decisions, arrays, '
            'loops, methods and encapsulation, inheritance, exceptions, and selected classes '
            'from the Java API (StringBuilder, String, java.time, ArrayList, lambdas).</p>'
        )
        insert_quiz_with_lesson(
            course_id=course.id,
            order_start=next_order,
            title='Final Exam \u2014 1Z0-808 cumulative practice test',
            description='25 cumulative questions across all nine OCA objectives. Pass mark suggestion: 70%.',
            lesson_html=final_lesson_html,
            questions=final_mod.QUESTIONS,
        )

        db.session.commit()
        print('\nCommitted.')


if __name__ == '__main__':
    main()
