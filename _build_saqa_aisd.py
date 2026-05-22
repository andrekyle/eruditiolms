"""Build the SAQA 118792 AI Software Developer course.

For the existing course "SAQA 118792: Occupational Certificate: Artificial
Intelligence Software Developer", this script:
- Keeps the course row (id preserved)
- Updates description if needed
- Preserves / refreshes the About lesson at order 1
- Deletes any other existing lessons/quizzes for this course
- For each of 10 lessons:
    * inserts content lesson
    * inserts hands-on practical lesson
    * inserts quiz + exam wrapper
- Inserts a 30-question Final Exam at the end

Idempotent: re-running fully rebuilds (preserves only the course row).
Reads modules from _saqa_aisd_authoring/.
"""
import importlib
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent
AUTH = WORKSPACE / "_saqa_aisd_authoring"
sys.path.insert(0, str(AUTH))

from app import app, db, Course, Lesson, Quiz, Question, QuestionOption  # noqa: E402

import _spec as spec_mod  # noqa: E402
import final_exam as final_mod  # noqa: E402

# Import the canonical About HTML straight from the original create script
sys.path.insert(0, str(WORKSPACE))
from _create_saqa_aisd import ABOUT_HTML, COURSE_TITLE, COURSE_DESCRIPTION  # noqa: E402


_QTYPE_ALIASES = {
    'multiple_choice': 'multiple_choice', 'mc': 'multiple_choice', 'multi': 'multiple_choice',
    'true_false': 'true_false', 'tf': 'true_false', 'truefalse': 'true_false',
}


def normalize_question(q, label, i):
    """Returns a 4-tuple (qtype, qhtml, opts, feedback). Accepts qtype aliases mc/tf."""
    if not isinstance(q, tuple):
        raise AssertionError(f'{label} q{i}: question must be a tuple, got {type(q)}')
    if len(q) == 4 and isinstance(q[0], str) and q[0].lower() in _QTYPE_ALIASES:
        qtype = _QTYPE_ALIASES[q[0].lower()]
        return (qtype, q[1], q[2], q[3])
    if len(q) == 3:
        qhtml, opts, fb = q
        qtype = 'true_false' if len(opts) == 2 else 'multiple_choice'
        return (qtype, qhtml, opts, fb)
    raise AssertionError(f'{label} q{i}: unrecognised question tuple shape len={len(q)}')


def validate_questions(qs, min_count, label):
    assert isinstance(qs, list), f'{label}: not a list'
    assert len(qs) >= min_count, f'{label}: expected at least {min_count} questions, got {len(qs)}'
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


def insert_content_lesson(course_id, order, title, html, content_type='lesson'):
    lesson = Lesson(
        title=title, content=html, course_id=course_id,
        content_type=content_type, order=order, points=1.0,
    )
    db.session.add(lesson)
    db.session.flush()
    print(f'  +lesson  id={lesson.id} order={order} {title!r}')
    return lesson


def insert_quiz_with_exam_wrapper(course_id, order_start, title, description, questions):
    """Insert a Quiz + exam-wrapper Lesson. Returns next order to use."""
    quiz = Quiz(course_id=course_id, title=title, description=description)
    db.session.add(quiz)
    db.session.flush()
    for i, (qtype, qhtml, opts, fb) in enumerate(questions, start=1):
        question = Question(
            quiz_id=quiz.id,
            question_html=qhtml,
            question_type=qtype,
            points=1.0,
            feedback=fb,
        )
        db.session.add(question)
        db.session.flush()
        for j, (otxt, ok) in enumerate(opts):
            db.session.add(QuestionOption(
                question_id=question.id,
                option_html=otxt,
                is_correct=bool(ok),
                order=j,
            ))
    print(f'  +quiz    id={quiz.id} {len(questions)} questions')
    el = Lesson(
        title=title, content='', course_id=course_id,
        content_type='exam', quiz_id=quiz.id,
        order=order_start, points=1.0,
    )
    db.session.add(el)
    db.session.flush()
    print(f'  +exam    id={el.id} order={order_start}')
    return order_start + 1


def main():
    print('--- Validating authored data ---')
    loaded = {}
    for entry in spec_mod.LESSONS:
        mod = importlib.import_module(entry['module'])
        assert isinstance(mod.LESSON_HTML, str) and len(mod.LESSON_HTML) > 1000, f'{entry["module"]}: LESSON_HTML too short ({len(mod.LESSON_HTML)})'
        assert isinstance(mod.PRACTICAL_HTML, str) and len(mod.PRACTICAL_HTML) > 800, f'{entry["module"]}: PRACTICAL_HTML too short ({len(mod.PRACTICAL_HTML)})'
        qs = validate_questions(list(mod.QUESTIONS), 8, entry['module'])
        loaded[entry['module']] = {
            'lesson_html': mod.LESSON_HTML,
            'practical_html': mod.PRACTICAL_HTML,
            'questions': qs,
        }
        print(f'  OK {entry["module"]} (L={len(mod.LESSON_HTML)}, P={len(mod.PRACTICAL_HTML)}, {len(qs)} Qs)')
    final_qs = validate_questions(list(final_mod.QUESTIONS), 30, 'final_exam')
    print(f'  OK final_exam ({len(final_qs)} Qs)')

    with app.app_context():
        course = Course.query.filter(Course.title.like('SAQA 118792%')).first()
        if not course:
            print('No SAQA 118792 course found. Run _create_saqa_aisd.py first.')
            return
        print(f'\nFound course id={course.id} title={course.title!r}')
        course.title = COURSE_TITLE
        course.description = COURSE_DESCRIPTION

        existing_lessons = Lesson.query.filter_by(course_id=course.id).all()
        existing_quizzes = Quiz.query.filter_by(course_id=course.id).all()
        print(f'Deleting {len(existing_lessons)} existing lessons, {len(existing_quizzes)} existing quizzes...')
        for l in existing_lessons:
            db.session.delete(l)
        for q in existing_quizzes:
            db.session.delete(q)
        db.session.flush()

        about = insert_content_lesson(course.id, 1, 'About this course', ABOUT_HTML)

        next_order = 2
        for entry in spec_mod.LESSONS:
            print(f'\n[{entry["module"]}] {entry["title"]}')
            data = loaded[entry['module']]
            insert_content_lesson(course.id, next_order, entry['title'], data['lesson_html'])
            next_order += 1
            insert_content_lesson(
                course.id, next_order,
                entry['title'].split(' \u2014 ')[0] + ' \u2014 Practical Lab',
                data['practical_html'],
            )
            next_order += 1
            next_order = insert_quiz_with_exam_wrapper(
                course_id=course.id,
                order_start=next_order,
                title=entry['title'] + ' \u2014 Quiz',
                description=entry['quiz_desc'],
                questions=data['questions'],
            )

        print('\n[final_exam] Final Exam (30 questions)')
        final_intro_html = (
            '<h2>Final Exam \u2014 Integrated Summative Assessment</h2>'
            '<p>This 30-question cumulative practice exam mirrors the QCTO / MICT SETA '
            'External Integrated Summative Assessment (EISA) for SAQA 118792.</p>'
            '<p>It draws proportionally from all 10 lesson modules and synthesises the '
            'three Work Experience Modules: <strong>WM-01</strong> AI Solution Design '
            'Interpretation and Development, <strong>WM-02</strong> AI Solution '
            'Performance Testing, and <strong>WM-03</strong> AI Solution Deployment, '
            'Modification and Improvement.</p>'
            '<p>Aim for at least 70% and review every answer\u2019s feedback. Allow '
            'approximately 60&ndash;90 minutes.</p>'
        )
        insert_content_lesson(course.id, next_order, 'Final Exam \u2014 Introduction', final_intro_html)
        next_order += 1
        insert_quiz_with_exam_wrapper(
            course_id=course.id,
            order_start=next_order,
            title=spec_mod.FINAL_EXAM_TITLE,
            description=spec_mod.FINAL_EXAM_DESC,
            questions=final_qs,
        )

        db.session.commit()
        print('\nCommitted.')


if __name__ == '__main__':
    main()
