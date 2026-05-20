"""Strip duplicate lesson-title headers.

The lesson template renders Lesson.title as an <h1>. Many lesson contents
also begin with <h1> or <h2> of the same title, producing a visual duplicate.
This script removes the FIRST leading heading whose text matches the lesson
title (whitespace/case-insensitive). Idempotent.
"""
import re
from app import app, db, Lesson, Course


def normalize(s: str) -> str:
    s = re.sub(r'<[^>]+>', '', s or '')          # strip tags
    s = re.sub(r'&[a-zA-Z#0-9]+;', ' ', s)        # crude entity strip
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s


LEADING_H_RE = re.compile(
    r'^\s*(?:<p>\s*)?(<h[12]\b[^>]*>(.*?)</h[12]>)\s*',
    re.I | re.S,
)


def strip_duplicate(title: str, html: str) -> tuple[str, bool]:
    if not html:
        return html, False
    target = normalize(title)
    # also accept the title with leading "Lesson N:" / "Lesson N -" stripped
    subtitle = re.sub(r'^lesson\s+\d+\s*[:\-\u2014]\s*', '', target)
    m = LEADING_H_RE.match(html)
    if not m:
        return html, False
    heading_text = normalize(m.group(2))
    if heading_text != target and heading_text != subtitle:
        return html, False
    return html[m.end():].lstrip(), True


def main():
    app.app_context().push()
    changed = 0
    for course in Course.query.order_by(Course.id).all():
        for lesson in Lesson.query.filter_by(course_id=course.id).order_by(Lesson.order).all():
            new_html, did = strip_duplicate(lesson.title, lesson.content or '')
            if did:
                lesson.content = new_html
                changed += 1
                print(f'  stripped from lesson id={lesson.id} ({course.title[:25]} | {lesson.title[:60]})')
    db.session.commit()
    print(f'\nDone. Stripped duplicate heading from {changed} lesson(s).')


if __name__ == '__main__':
    main()
