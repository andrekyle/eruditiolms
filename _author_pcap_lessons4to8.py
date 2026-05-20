"""Author PCAP Lessons 4-8 + their quizzes; bump the Final Exam to the end.
Idempotent: re-running updates existing rows in place.
"""
import importlib
import re
import sys

from app import app, db, Course, Lesson, Quiz, Question, QuestionOption

COURSE_TITLE_LIKE = 'PCAP%'
FINAL_EXAM_TITLE = 'Lesson 4: Final Exam'

# (lesson_number, topic, quiz_description, data_module_name)
SPEC = [
    (4, 'Control Flow \u2014 Conditionals and Loops',
     'Practise conditionals, loops, ranges, break/continue and common control-flow pitfalls.',
     '_pcap_data_l4'),
    (5, 'Functions',
     'Check your understanding of Python functions, parameters, scope, recursion and lambdas.',
     '_pcap_data_l5'),
    (6, 'Data Collections \u2014 Lists, Tuples, Dictionaries and Sets',
     'Practise lists, tuples, dictionaries, sets, comprehensions and reference vs copy semantics.',
     '_pcap_data_l6'),
    (7, 'Strings and String Methods',
     'Check your understanding of string immutability, slicing, methods and formatting.',
     '_pcap_data_l7'),
    (8, 'Modules, Packages, Files and Exceptions',
     'Practise imports, file I/O, the with statement and Python\'s exception machinery.',
     '_pcap_data_l8'),
]


CODE_BLOCK_RE = re.compile(
    r'(<pre><code class="language-python">)(.*?)(</code></pre>)',
    flags=re.DOTALL,
)


def escape_code_blocks(html: str) -> str:
    """Escape `<` `>` `&` inside <pre><code class="language-python"> blocks so that
    raw Python operators like `< 5` or `>= 18` render correctly in the browser.
    Leaves the rest of the markup untouched.
    """
    def _esc(m):
        inner = m.group(2)
        # Order matters: escape & first to avoid double-escaping
        inner = (inner
                 .replace('&', '&amp;')
                 .replace('<', '&lt;')
                 .replace('>', '&gt;'))
        return m.group(1) + inner + m.group(3)
    return CODE_BLOCK_RE.sub(_esc, html)


def upsert():
    with app.app_context():
        course = Course.query.filter(Course.title.like(COURSE_TITLE_LIKE)).first()
        if not course:
            print('PCAP course not found.')
            return

        # Temporarily push Final Exam out of the way so new lessons can claim 6..15
        final = Lesson.query.filter_by(course_id=course.id, title=FINAL_EXAM_TITLE).first()
        if final:
            final.order = 999
            db.session.flush()
            print(f'parked final exam lesson {final.id} at order 999')
        else:
            print('NOTE: Final Exam lesson not found by title; will not be repositioned.')

        next_order = 6
        for num, topic, qdesc, modname in SPEC:
            # Re-import so changes during the same run are picked up
            if modname in sys.modules:
                data = importlib.reload(sys.modules[modname])
            else:
                data = importlib.import_module(modname)

            lesson_html = escape_code_blocks(data.LESSON_HTML)
            questions = data.QUESTIONS

            ltitle = f'Lesson {num}: {topic}'
            qtitle = f'Lesson {num} Quiz \u2014 {topic}'

            # --- Content lesson ---
            lesson = Lesson.query.filter_by(course_id=course.id, title=ltitle).first()
            if lesson:
                lesson.content = lesson_html
                lesson.content_type = 'lesson'
                lesson.order = next_order
                lesson.points = 1.0
                print(f'updated content lesson {lesson.id} ({ltitle}) order={next_order}')
            else:
                lesson = Lesson(
                    title=ltitle, content=lesson_html, course_id=course.id,
                    content_type='lesson', order=next_order, points=1.0,
                )
                db.session.add(lesson)
                db.session.flush()
                print(f'inserted content lesson {lesson.id} ({ltitle}) order={next_order}')
            next_order += 1

            # --- Quiz ---
            quiz = Quiz.query.filter_by(course_id=course.id, title=qtitle).first()
            if not quiz:
                quiz = Quiz(course_id=course.id, title=qtitle, description=qdesc)
                db.session.add(quiz)
                db.session.flush()
                print(f'  inserted quiz {quiz.id}')
            else:
                quiz.description = qdesc
                for q in list(quiz.questions):
                    db.session.delete(q)
                db.session.flush()
                print(f'  rebuilt quiz {quiz.id}')

            for qtype, qhtml, opts, feedback in questions:
                q = Question(
                    quiz_id=quiz.id, question_type=qtype, question_html=qhtml,
                    points=1.0, feedback=feedback,
                )
                db.session.add(q)
                db.session.flush()
                for i, (ohtml, correct) in enumerate(opts):
                    db.session.add(QuestionOption(
                        question_id=q.id, option_html=ohtml,
                        is_correct=bool(correct), order=i,
                    ))

            # --- Exam-as-lesson ---
            exam = Lesson.query.filter_by(
                course_id=course.id, title=qtitle, content_type='exam',
            ).first()
            if exam:
                exam.quiz_id = quiz.id
                exam.order = next_order
                exam.points = 1.0
                print(f'  updated exam lesson {exam.id} order={next_order}')
            else:
                exam = Lesson(
                    title=qtitle, content='', course_id=course.id,
                    content_type='exam', quiz_id=quiz.id,
                    order=next_order, points=1.0,
                )
                db.session.add(exam)
                db.session.flush()
                print(f'  inserted exam lesson {exam.id} order={next_order}')
            next_order += 1

        # Place Final Exam at the very end
        if final:
            final.order = next_order
            print(f'restored final exam lesson {final.id} to order {next_order}')

        db.session.commit()
        print('done.')


if __name__ == '__main__':
    upsert()
