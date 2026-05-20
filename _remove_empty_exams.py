"""Find and delete empty/legacy exam lessons across all courses.
An empty exam lesson = content_type='exam' AND linked quiz has 0 questions."""
from app import app, db, Lesson, Quiz, Course, QuestionResponse, QuestionResponseOption, QuizResponse

with app.app_context():
    courses = Course.query.order_by(Course.id).all()
    to_delete = []  # (lesson, quiz_or_None)
    for c in courses:
        ls = Lesson.query.filter_by(course_id=c.id).order_by(Lesson.order).all()
        for L in ls:
            if L.content_type != 'exam':
                continue
            q = db.session.get(Quiz, L.quiz_id) if L.quiz_id else None
            qcnt = len(q.questions) if q else 0
            if qcnt == 0:
                to_delete.append((c, L, q))

    if not to_delete:
        print('Nothing to delete')
    else:
        print('Empty exam lessons to delete:')
        for c, L, q in to_delete:
            print(f'  course={c.id} {c.title!r}  lesson_id={L.id} order={L.order} title={L.title!r} quiz_id={L.quiz_id} qcnt=0')

    print('\nApplying deletions...')
    for c, L, q in to_delete:
        # Delete the lesson first (FK to quiz)
        db.session.delete(L)
        db.session.flush()
        if q is not None:
            # Make sure no other lesson references this quiz
            other = Lesson.query.filter_by(quiz_id=q.id).first()
            if other:
                print(f'  SKIP quiz#{q.id} delete (still referenced by lesson id={other.id})')
            else:
                # Clean any quiz_responses (should be none if no questions, but be safe)
                for qr in QuizResponse.query.filter_by(quiz_id=q.id).all():
                    for qresp in QuestionResponse.query.filter_by(quiz_response_id=qr.id).all():
                        QuestionResponseOption.query.filter_by(response_id=qresp.id).delete(synchronize_session=False)
                        db.session.delete(qresp)
                    db.session.delete(qr)
                db.session.delete(q)
        print(f'  deleted lesson_id={L.id} (course {c.id})')
    db.session.commit()
    print(f'\nTotal deleted: {len(to_delete)} lessons')
