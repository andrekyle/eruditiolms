"""Normalize <table> markup in Lesson.content:
- If a table lacks <thead>, the first <tr> that contains any <th> becomes
  <thead><tr>...</tr></thead>; remaining <tr> rows are wrapped in <tbody>.
- Idempotent: tables already containing <thead> are left alone.
"""
import re
from app import app, db, Lesson, Course

TABLE_RE = re.compile(r'(<table\b[^>]*>)(.*?)(</table>)', re.I | re.S)
TR_RE = re.compile(r'<tr\b[^>]*>.*?</tr>', re.I | re.S)


def normalize_table(open_tag: str, inner: str, close_tag: str) -> str:
    if re.search(r'<thead\b', inner, re.I):
        return open_tag + inner + close_tag
    trs = TR_RE.findall(inner)
    if not trs:
        return open_tag + inner + close_tag
    # find first TR with a <th>
    header_idx = None
    for i, tr in enumerate(trs):
        if re.search(r'<th\b', tr, re.I):
            header_idx = i
            break
    if header_idx is None:
        # No header row; wrap everything in <tbody>
        body = '\n'.join(trs)
        return f'{open_tag}\n<tbody>\n{body}\n</tbody>\n{close_tag}'
    header_tr = trs[header_idx]
    body_trs = trs[:header_idx] + trs[header_idx + 1:]
    body = '\n'.join(body_trs)
    parts = [open_tag, '\n<thead>\n', header_tr, '\n</thead>']
    if body:
        parts.append('\n<tbody>\n' + body + '\n</tbody>')
    parts.append('\n' + close_tag)
    return ''.join(parts)


def fix_html(html: str) -> tuple[str, int]:
    count = 0

    def repl(m):
        nonlocal count
        open_tag, inner, close_tag = m.group(1), m.group(2), m.group(3)
        new = normalize_table(open_tag, inner, close_tag)
        if new != open_tag + inner + close_tag:
            count += 1
        return new

    new_html = TABLE_RE.sub(repl, html)
    return new_html, count


def main():
    app.app_context().push()
    total_tables_fixed = 0
    total_lessons_changed = 0
    for course in Course.query.order_by(Course.id).all():
        for lesson in Lesson.query.filter_by(course_id=course.id).order_by(Lesson.order).all():
            html = lesson.content or ''
            if '<table' not in html.lower():
                continue
            new_html, n = fix_html(html)
            if n > 0:
                lesson.content = new_html
                total_tables_fixed += n
                total_lessons_changed += 1
                print(f'  fixed {n} table(s) in lesson id={lesson.id} ({course.title[:30]} | {lesson.title[:50]})')
    db.session.commit()
    print(f'\nDone. {total_tables_fixed} table(s) normalized across {total_lessons_changed} lesson(s).')


if __name__ == '__main__':
    main()
