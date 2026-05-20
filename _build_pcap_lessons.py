"""Parse 6 PCAP lesson agent outputs and update lesson content + quiz questions."""
import os
import re
import sys
from app import app, db, Lesson, Quiz, Question, QuestionOption, QuestionResponse, QuestionResponseOption

BASE = r'c:\Users\hp\AppData\Roaming\Code\User\workspaceStorage\25f723a0a07d7e81c8ab2371048eef31\GitHub.copilot-chat\chat-session-resources\7cdafd4c-d586-4bc9-9b47-be8b70ffb17b'

# (lesson_order, agent_folder)
SPEC = [
    (4,  'toolu_vrtx_01Vjdujigoi6wTcc4aVtzksR__vscode-1779257269740'),  # L3 Modules+Packages
    (6,  'toolu_vrtx_01LocPiA8Ga9Zhu6k5Agry62__vscode-1779257269741'),  # L4 Exceptions
    (8,  'toolu_vrtx_01VVwehN2GbGv8DiMcEjS7Zo__vscode-1779257269742'),  # L5 Strings
    (10, 'toolu_vrtx_013AwpcxnjCdBfFZCVk9KFrs__vscode-1779257269743'),  # L6 OOP Part A
    (12, 'toolu_vrtx_0167idEdQfj4hwCZuwDCZxVd__vscode-1779257269744'),  # L7 OOP Part B
    (14, 'toolu_vrtx_015wRBNkcq6eJduFeMugJNNg__vscode-1779257269745'),  # L8 Miscellaneous
]

COURSE_ID = 1


def parse(path):
    text = open(path, 'r', encoding='utf-8').read()
    mh = re.search(r'===LESSON_HTML_START===\s*(.*?)\s*===LESSON_HTML_END===', text, re.DOTALL)
    mq = re.search(r'===QUESTIONS_START===\s*(.*?)\s*===QUESTIONS_END===', text, re.DOTALL)
    if not mh or not mq:
        raise RuntimeError(f'{path}: missing markers')
    lesson_html = mh.group(1).strip()
    ns = {}
    exec(compile(mq.group(1), path, 'exec'), ns)
    qs = ns.get('QUESTIONS')
    if not isinstance(qs, list):
        raise RuntimeError(f'{path}: QUESTIONS not a list')
    return lesson_html, qs


def main():
    with app.app_context():
        results = []
        for order, folder in SPEC:
            path = os.path.join(BASE, folder, 'content.txt')
            try:
                lesson_html, qs = parse(path)
            except Exception as e:
                print(f'L{order} PARSE FAIL: {e}')
                results.append((order, False, str(e)))
                continue

            if len(qs) < 8:
                print(f'L{order} FAIL: only {len(qs)} questions')
                results.append((order, False, f'count={len(qs)}'))
                continue
            qs = qs[:8]

            ok = True
            for i, item in enumerate(qs, 1):
                if not (isinstance(item, tuple) and len(item) == 3):
                    print(f'L{order} Q{i} bad tuple len {len(item) if isinstance(item, tuple) else "?"}')
                    ok = False; break
                qh, opts, fb = item
                if len(opts) != 4 or sum(1 for _, c in opts if c) != 1:
                    print(f'L{order} Q{i} bad options: correct={sum(1 for _, c in opts if c)} count={len(opts)}')
                    ok = False; break
            if not ok:
                results.append((order, False, 'bad questions'))
                continue

            lesson = Lesson.query.filter_by(course_id=COURSE_ID, order=order).first()
            if not lesson:
                print(f'L{order} FAIL: lesson not found')
                results.append((order, False, 'no lesson'))
                continue

            exam_lesson = Lesson.query.filter_by(course_id=COURSE_ID, order=order + 1).first()
            if not exam_lesson or not exam_lesson.quiz_id:
                print(f'L{order} FAIL: companion exam lesson at order {order+1} has no quiz')
                results.append((order, False, 'no quiz'))
                continue
            quiz = db.session.get(Quiz, exam_lesson.quiz_id)

            lesson.content = lesson_html

            # Wipe student responses first (FK NOT NULL prevents cascading)
            for q in list(quiz.questions):
                resps = QuestionResponse.query.filter_by(question_id=q.id).all()
                for r in resps:
                    QuestionResponseOption.query.filter_by(response_id=r.id).delete(synchronize_session=False)
                    db.session.delete(r)
            db.session.flush()

            for q in list(quiz.questions):
                db.session.delete(q)
            db.session.flush()

            for qh, opts, fb in qs:
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

            db.session.commit()
            print(f'L{order} OK  lesson_id={lesson.id} ({lesson.title!r}) content_len={len(lesson_html)} quiz#{quiz.id} qs=8')
            results.append((order, True, 'ok'))

        print('\n=== SUMMARY ===')
        for o, ok, msg in results:
            print(f'  L{o}: {"OK" if ok else "FAIL"} ({msg})')
        sys.exit(0 if all(r[1] for r in results) else 1)


if __name__ == '__main__':
    main()
