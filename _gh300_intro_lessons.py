"""Add GH-300 Lesson 1 (intro video) and Lesson 2 (first task). Idempotent."""
from app import app, db, Course, Lesson

COURSE_TITLE_LIKE = 'GH-300%'

VIDEO_TITLE = 'Lesson 1: Watch \u2014 Intro Video'
VIDEO_URL = 'https://www.youtube.com/embed/Fi3AJZZregI'
VIDEO_CONTENT = (
    '<p>Watch this short introduction to GitHub Copilot before starting the rest of the course. '
    'It covers what Copilot is, where it runs (IDE, CLI, GitHub.com), and the high-level workflow '
    'you will practise in the lessons that follow.</p>'
)

TASK_TITLE = 'Lesson 2: Task \u2014 Your First Submission'
TASK_STYLE = """
<style>
  .task-h{font-size:1.15rem;font-weight:600;margin:18px 0 8px;}
  .task-p{font-size:1rem;line-height:1.65;margin:0 0 12px;}
  .task-ul,.task-ol{font-size:1rem;line-height:1.65;margin:0 0 14px 1.25rem;padding:0;}
  .task-callout{background:rgba(127,127,127,.10);padding:12px 16px;border-radius:6px;margin:14px 0;}
</style>
"""
TASK_BODY = """
<p class="task-p">Your first task is a hands-on Copilot warm-up: install Copilot, write a tiny script with its help, and reflect briefly on what the AI did well and where you had to steer it.</p>

<h3 class="task-h">Prerequisites</h3>
<ul class="task-ul">
  <li>A GitHub account with an active Copilot subscription (Individual, Business, or Enterprise &mdash; the free trial is fine).</li>
  <li><strong>Visual Studio Code</strong> with the <em>GitHub Copilot</em> and <em>GitHub Copilot Chat</em> extensions installed and signed in.</li>
</ul>

<h3 class="task-h">Steps</h3>
<ol class="task-ol">
  <li>Create a new empty folder and open it in VS Code. Add a single file <code>word_count.py</code>.</li>
  <li>At the top of the file, write a comment describing what you want, for example:
    <code># Read a text file path from argv[1] and print the number of words, lines, and characters.</code>
    Let Copilot suggest the implementation inline. Accept, edit, or reject suggestions until the script works.</li>
  <li>Open <strong>Copilot Chat</strong> and ask it to <code>/tests</code> &mdash; generate at least <strong>three</strong> unit tests for your function (use <code>pytest</code> or <code>unittest</code>). Run the tests and make them pass.</li>
  <li>Ask Copilot Chat to <code>/explain</code> one block of the code it wrote and paste the explanation into a short reflection file <code>REFLECTION.md</code>.</li>
  <li>In the same <code>REFLECTION.md</code>, answer in 150&ndash;250 words:
    <ul class="task-ul">
      <li>Which suggestion did you <strong>accept as-is</strong>, and why was it good?</li>
      <li>Which suggestion did you <strong>reject or rewrite</strong>, and what was wrong with it (hallucinated API, wrong style, insecure, etc.)?</li>
      <li>Which Copilot feature (inline completion, Chat, <code>/tests</code>, <code>/explain</code>) gave you the most value for this task?</li>
    </ul>
  </li>
</ol>

<div class="task-callout"><strong>Submit:</strong> a zip containing <code>word_count.py</code>, your tests file, and <code>REFLECTION.md</code>. Do not commit your Copilot subscription token or any secrets &mdash; this task uses only public, non-sensitive code.</div>
"""


def run():
    with app.app_context():
        course = Course.query.filter(Course.title.like(COURSE_TITLE_LIKE)).first()
        if not course:
            print(f'{COURSE_TITLE_LIKE} not found.')
            return

        # Video lesson at order=2
        video = Lesson.query.filter_by(course_id=course.id, title=VIDEO_TITLE).first()
        if video:
            video.content = VIDEO_CONTENT
            video.content_type = 'video'
            video.video_url = VIDEO_URL
            video.order = 2
            video.points = 1.0
            print(f'updated video lesson {video.id}')
        else:
            video = Lesson(
                course_id=course.id, title=VIDEO_TITLE,
                content=VIDEO_CONTENT, content_type='video',
                video_url=VIDEO_URL, order=2, points=1.0,
            )
            db.session.add(video)
            db.session.flush()
            print(f'inserted video lesson {video.id}')

        # Task lesson at order=3
        task = Lesson.query.filter_by(course_id=course.id, title=TASK_TITLE).first()
        task_instr = TASK_STYLE + TASK_BODY.strip() + '\n'
        if task:
            task.content = ''
            task.content_type = 'task'
            task.task_instructions = task_instr
            task.order = 3
            task.points = 2.0
            print(f'updated task lesson {task.id}')
        else:
            task = Lesson(
                course_id=course.id, title=TASK_TITLE,
                content='', content_type='task',
                task_instructions=task_instr, order=3, points=2.0,
            )
            db.session.add(task)
            db.session.flush()
            print(f'inserted task lesson {task.id}')

        db.session.commit()
        print('done.')


if __name__ == '__main__':
    run()
