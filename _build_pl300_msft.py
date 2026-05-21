"""Build the PL-300 Microsoft Power BI Data Analyst course.

Replaces the polluted PL-300 course (id 5, currently filled with DP-300 content) with:
- Updated title/description
- Fresh About lesson at order 1
- 9 topic content lessons + 9 quizzes + 9 exam-wrapper lessons (orders 2..19)
- 25-question Final Exam (orders 20, 21)

Reads data modules from _pl300_authoring/.
Idempotent: deletes old lessons/quizzes (cascades) then rebuilds.
"""
import importlib
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent
AUTH = WORKSPACE / "_pl300_authoring"
sys.path.insert(0, str(AUTH))

from app import app, db, Course, Lesson, Quiz, Question, QuestionOption  # noqa: E402

import about as about_mod  # noqa: E402
import _spec as spec_mod  # noqa: E402
import final_exam as final_mod  # noqa: E402

OLD_COURSE_TITLE_LIKE = '%PL-300%'
NEW_COURSE_TITLE = 'PL-300: Microsoft Power BI Data Analyst'
NEW_COURSE_DESC = (
    'Prepare for the Microsoft PL-300 Power BI Data Analyst exam. Nine lessons cover '
    'every official objective \u2014 preparing data with Power Query, modelling with star '
    'schemas, writing DAX, optimising model performance, building reports and '
    'visualisations, enhancing reports for storytelling, applying AI and advanced '
    'analytics, and deploying assets in the Power BI service \u2014 each followed by an '
    '8-question quiz, with a 25-question cumulative final exam to simulate test conditions.'
)


def normalize_question(q, label, i):
    """Returns a 4-tuple (qtype, qhtml, opts, feedback)."""
    if isinstance(q, tuple) and len(q) == 3:
        qhtml, opts, fb = q
        qtype = 'true_false' if len(opts) == 2 else 'multiple_choice'
        return (qtype, qhtml, opts, fb)
    if isinstance(q, tuple) and len(q) == 4:
        if isinstance(q[0], str) and isinstance(q[1], str) and isinstance(q[2], list):
            return (q[0], q[1], q[2], q[3])
        if isinstance(q[0], str) and isinstance(q[1], list):
            qhtml, opts, _points, fb = q
            qtype = 'true_false' if len(opts) == 2 else 'multiple_choice'
            return (qtype, qhtml, opts, fb)
    raise AssertionError(f'{label} q{i}: unrecognised tuple shape, types={[type(x).__name__ for x in q] if isinstance(q, tuple) else type(q).__name__}')


def validate_questions(qs, expected_count, label):
    assert isinstance(qs, list), f'{label}: not a list'
    assert len(qs) == expected_count, f'{label}: expected {expected_count} questions, got {len(qs)}'
    normalised = []
    for i, q in enumerate(qs):
        qtype, qhtml, opts, fb = normalize_question(q, label, i)
        assert isinstance(qhtml, str) and qhtml.strip(), f'{label} q{i}: bad question_html'
        assert isinstance(opts, list) and len(opts) in (2, 4), f'{label} q{i}: need 2 or 4 options, got {len(opts)}'
        correct = sum(1 for o in opts if o[1])
        assert correct == 1, f'{label} q{i}: need exactly 1 correct, got {correct}'
        for j, o in enumerate(opts):
            assert isinstance(o, tuple) and len(o) == 2, f'{label} q{i} opt{j}: bad option tuple'
            assert isinstance(o[0], str) and o[0].strip(), f'{label} q{i} opt{j}: bad option_html'
        assert isinstance(fb, str), f'{label} q{i}: bad feedback'
        normalised.append((qtype, qhtml, opts, fb))
    return normalised


def insert_quiz_with_lesson(course_id, order_start, title, description, lesson_html, questions):
    """Insert content lesson, quiz with questions, and exam lesson. Return next free order."""
    cl = Lesson(
        title=title, content=lesson_html, course_id=course_id,
        content_type='lesson', order=order_start, points=1.0,
    )
    db.session.add(cl)
    db.session.flush()
    print(f'  +lesson  id={cl.id} order={order_start} {title!r}')

    quiz_title = f'Quiz: {title}'
    quiz = Quiz(course_id=course_id, title=quiz_title, description=description)
    db.session.add(quiz)
    db.session.flush()
    for qtype, qhtml, opts, fb in questions:
        q = Question(
            quiz_id=quiz.id, question_type=qtype,
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

    exam_order = order_start + 1
    el = Lesson(
        title=quiz_title, content='', course_id=course_id,
        content_type='exam', quiz_id=quiz.id,
        order=exam_order, points=1.0,
    )
    db.session.add(el)
    db.session.flush()
    print(f'  +exam    id={el.id} order={exam_order}')

    return exam_order + 1


def main():
    print('--- Validating authored data ---')
    normalised = {}
    for entry in spec_mod.LESSONS:
        mod = importlib.import_module(entry['module'])
        assert isinstance(mod.LESSON_HTML, str) and len(mod.LESSON_HTML) > 500, f'{entry["module"]}: short LESSON_HTML'
        normalised[entry['module']] = validate_questions(mod.QUESTIONS, 8, entry['module'])
        print(f'  OK {entry["module"]} ({len(mod.LESSON_HTML)} chars HTML, 8 Qs)')
    normalised['final_exam'] = validate_questions(final_mod.QUESTIONS, 25, 'final_exam')
    print('  OK final_exam (25 Qs)')

    with app.app_context():
        course = Course.query.filter(Course.title.ilike(OLD_COURSE_TITLE_LIKE)).first()
        if not course:
            print('No PL-300 course found.')
            return
        print(f'\nFound course id={course.id} title={course.title!r}')

        course.title = NEW_COURSE_TITLE
        course.description = NEW_COURSE_DESC

        existing_lessons = Lesson.query.filter_by(course_id=course.id).all()
        existing_quizzes = Quiz.query.filter_by(course_id=course.id).all()
        print(f'Deleting {len(existing_lessons)} existing lessons, {len(existing_quizzes)} existing quizzes...')
        for l in existing_lessons:
            db.session.delete(l)
        for q in existing_quizzes:
            db.session.delete(q)
        db.session.flush()

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
                questions=normalised[entry['module']],
            )

        print('\n[final_exam] Final Exam (25 questions)')
        final_lesson_html = (
            '<h2>Final Exam \u2014 PL-300 cumulative practice test</h2>'
            '<p>This 25-question cumulative exam draws proportionally from all four '
            'official PL-300 domains: Prepare the data, Model the data, Visualize and '
            'analyze the data, and Deploy and maintain assets.</p>'
            '<p>Allow yourself about 50&ndash;60 minutes and aim for at least 75% to feel '
            'comfortable with the real exam\u2019s 700/1000 pass mark.</p>'
        )
        insert_quiz_with_lesson(
            course_id=course.id,
            order_start=next_order,
            title='Final Exam \u2014 PL-300 cumulative practice test',
            description='25 cumulative questions covering all four PL-300 domains. Pass mark suggestion: 75%.',
            lesson_html=final_lesson_html,
            questions=normalised['final_exam'],
        )

        db.session.commit()
        print('\nCommitted.')


if __name__ == '__main__':
    main()
