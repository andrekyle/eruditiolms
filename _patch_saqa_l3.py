"""One-off: update the Analytical Thinking lesson content in Supabase."""
import os
import sys
from app import app, db
from app import Lesson  # type: ignore

# Reload the lesson module to pick up the new HTML
from _saqa_aisd_authoring.lesson03_analytical_thinking import LESSON_HTML

with app.app_context():
    target = Lesson.query.get(200)
    if target is None:
        print("Lesson not found"); sys.exit(1)
    print(f"Updating lesson id={target.id} title={target.title!r}")
    target.content = LESSON_HTML
    db.session.commit()
    print("Done. Length:", len(LESSON_HTML))
