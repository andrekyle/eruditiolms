from app import app, db, Course, Lesson, Quiz
with app.app_context():
    C = db.session.get(Course, 1)
    print('Course:', C.id, C.title)
    ls = Lesson.query.filter_by(course_id=1).order_by(Lesson.order).all()
    for L in ls:
        qid = L.quiz_id or ''
        qcnt = ''
        if L.quiz_id:
            Q = db.session.get(Quiz, L.quiz_id)
            qcnt = ' qs=' + str(len(Q.questions))
        cl = len(L.content or '')
        print('  ord=%2d id=%3d type=%-12s quiz=%s contentlen=%d title=%r%s' % (L.order, L.id, L.content_type, qid, cl, L.title, qcnt))
