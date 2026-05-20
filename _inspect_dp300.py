from app import app, db, Course, Lesson, User
app.app_context().push()
c = Course.query.get(5)
print('Course:', c.title)
print('Description:', (c.description or '')[:400])
print('Image:', c.image_url)
print('Badge:', c.badge_url)
print('Teacher:', c.teacher_id)
print()
ls = Lesson.query.filter_by(course_id=5).order_by(Lesson.order).limit(4).all()
for l in ls:
    preview = (l.content or '')[:300]
    print('  L%d id=%d type=%s | %s' % (l.order, l.id, l.content_type, l.title))
    print('    preview:', preview)
    print('    video_url:', l.video_url)
    print('    task:', (l.task_instructions or '')[:200])
    print('    quiz_id:', l.quiz_id, 'points:', l.points)
    print()
print('admin teacher id:', User.query.filter_by(username='admin').first().id)
