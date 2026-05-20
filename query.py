from app import app, db, Lesson
with app.app_context():
    rows = Lesson.query.filter(
        (Lesson.title.like("%Welcome%")) | (Lesson.content.like("%In this course you will learn the basics%"))
    ).all()
    print("total:", len(rows))
    for ln in rows:
        ct = (ln.course.title if ln.course else "(no course)")
        body = (ln.content or "").replace(chr(10)," ")[:200]
        print(f"{ln.id} | {ln.course_id} | {ct} | {ln.content_type} | {ln.order} | {ln.title} | {body}")
