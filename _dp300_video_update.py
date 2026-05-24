"""Update DP-300 intro video lesson with an embeddable official Microsoft video.

The previous video_url ('IFpKngfH7Hs') returned "Video unavailable".
This script points Lesson id=18 at the official Microsoft Developer
"Data Exposed" episode focused on preparing for Exam DP-300.

Idempotent — safe to re-run.
"""
from app import app, db, Lesson

VIDEO_ID = "TIIqoDon_r4"
EMBED_URL = f"https://www.youtube.com/embed/{VIDEO_ID}"

CONTENT_HTML = """
<p>
  This episode of <strong>Data Exposed</strong> on the official Microsoft Developer
  channel walks through what to expect from
  <strong>Exam DP-300: Administering Microsoft Azure SQL Solutions</strong> and the
  <strong>Azure Database Administrator Associate</strong> certification &mdash; the skills
  measured, who the exam is for, and how to plan your preparation.
</p>
<p>
  Use this as your orientation video, then work through the lessons in this course
  alongside the official
  <a href="https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300"
     target="_blank" rel="noopener">Microsoft DP-300 study guide</a> and the
  <a href="https://learn.microsoft.com/en-us/training/courses/dp-300t00"
     target="_blank" rel="noopener">DP-300T00 learning path on Microsoft Learn</a>.
</p>
""".strip()


def main() -> None:
    with app.app_context():
        lesson = db.session.get(Lesson, 18)
        if lesson is None:
            raise SystemExit("Lesson id=18 not found")
        lesson.video_url = EMBED_URL
        lesson.content = CONTENT_HTML
        db.session.commit()
        print(f"Updated lesson {lesson.id} ('{lesson.title}') -> {EMBED_URL}")


if __name__ == "__main__":
    main()
