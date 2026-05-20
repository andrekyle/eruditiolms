"""Strip a leading H1/H2/H3 from Lesson.content when its text matches Lesson.title.

The lesson view renders lesson.title as an <h1> already, so duplicate titles in
the HTML body produce stacked headers.
"""
import re
from app import app, db, Lesson


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip().lower()


def strip_leading_title(html: str, title: str):
    if not html:
        return html, False
    # Skip optional leading whitespace and comments
    m = re.match(r"\s*(?:<!--.*?-->\s*)*<(h[1-3])\b[^>]*>(.*?)</\1>\s*", html, re.DOTALL | re.IGNORECASE)
    if not m:
        return html, False
    if norm(m.group(2)) != norm(title):
        return html, False
    return html[m.end():], True


def main():
    with app.app_context():
        changed = 0
        for L in Lesson.query.all():
            new, did = strip_leading_title(L.content or "", L.title or "")
            if did:
                # Recurse: in case the body had TWO duplicate headings (e.g. h1+h2)
                while True:
                    new2, did2 = strip_leading_title(new, L.title)
                    if not did2:
                        break
                    new = new2
                L.content = new
                changed += 1
                print(f"stripped duplicate title from lesson {L.id}: {L.title!r}")
        db.session.commit()
        print(f"done. updated {changed} lessons.")


if __name__ == "__main__":
    main()
