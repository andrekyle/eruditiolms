"""Fill in the placeholder 'Lesson 2: Task -- Your First Submission' task instructions
for the five courses where it is still the default stub. Idempotent: re-running
just rewrites the task_instructions field to the curated text below."""
from app import app, db, Course, Lesson

TASK_STYLE = """
<style>
  .task-h{font-size:1.15rem;font-weight:600;margin:18px 0 8px;}
  .task-p{font-size:1rem;line-height:1.65;margin:0 0 12px;}
  .task-ul,.task-ol{font-size:1rem;line-height:1.65;margin:0 0 14px 1.25rem;padding:0;}
  .task-callout{background:rgba(127,127,127,.10);padding:12px 16px;border-radius:6px;margin:14px 0;}
</style>
"""

TASKS = {
    'PCAP \u2013 Certified Associate Python Programmer': """
<p class="task-p">Welcome to your first hands-on task. You will write a short Python program that practises the fundamentals every PCAP candidate needs: input, variables, simple control flow and string formatting.</p>

<h3 class="task-h">What to build</h3>
<p class="task-p">Write a script called <code>greet.py</code> that:</p>
<ol class="task-ol">
  <li>Asks the user for their <strong>name</strong> and <strong>year of birth</strong>.</li>
  <li>Computes their age this year (assume the current year is <code>2026</code>; do not import <code>datetime</code>).</li>
  <li>Prints exactly one of the following, depending on age:
    <ul class="task-ul">
      <li><code>Hello, NAME &mdash; you are AGE this year.</code></li>
      <li>If <code>AGE &lt; 0</code> or <code>AGE &gt; 130</code>, print <code>Invalid year of birth.</code> and exit.</li>
    </ul>
  </li>
</ol>

<h3 class="task-h">Constraints</h3>
<ul class="task-ul">
  <li>Use only built-ins &mdash; no third-party packages.</li>
  <li>The script must run end-to-end with <code>python greet.py</code> on Python 3.10+.</li>
  <li>Use an f-string for the final output.</li>
</ul>

<div class="task-callout"><strong>Submit:</strong> upload <code>greet.py</code> along with a short text note (1&ndash;2 sentences) describing one Python concept the task helped you practise.</div>
""",

    'AZ-900: Microsoft Azure Fundamentals': """
<p class="task-p">In this first task you will explore the Azure Portal and document one resource &mdash; no production deployment, no real spend required.</p>

<h3 class="task-h">What to do</h3>
<ol class="task-ol">
  <li>Sign in to the <strong>Azure free account</strong> or the <strong>Azure Portal</strong> sandbox provided by Microsoft Learn.</li>
  <li>Open the <em>Create a resource</em> blade and start (but do <strong>not</strong> deploy) a <strong>Storage account</strong>.</li>
  <li>Take a screenshot of the <em>Review + create</em> page showing region, redundancy, performance tier and estimated cost.</li>
  <li>Write a short report (200&ndash;300 words) that answers:
    <ul class="task-ul">
      <li>Which Azure <strong>region</strong> did you choose and why?</li>
      <li>Which <strong>redundancy option</strong> (LRS / ZRS / GRS / RA-GRS) did the wizard default to, and what is the trade-off between cost and availability for each?</li>
      <li>Which <strong>shared-responsibility</strong> items belong to you and which to Microsoft for a storage account?</li>
    </ul>
  </li>
</ol>

<div class="task-callout"><strong>Submit:</strong> the screenshot plus the short report (PDF or DOCX). Make sure no subscription IDs or personal email addresses are visible.</div>
""",

    'PL-300: Microsoft Power BI Data Analyst Associate': """
<p class="task-p">Your first task is a small end-to-end Power BI Desktop exercise: connect to data, clean it in Power Query, model it and produce a single-page report.</p>

<h3 class="task-h">Dataset</h3>
<p class="task-p">Use the public <strong>Financial Sample</strong> Excel file shipped with Power BI (Help &rarr; Sample data) or any CSV with at least one date column and one numeric measure.</p>

<h3 class="task-h">Steps</h3>
<ol class="task-ol">
  <li>Import the dataset into <strong>Power BI Desktop</strong>.</li>
  <li>In <strong>Power Query</strong>, change types correctly, remove obvious nulls, and rename one column.</li>
  <li>Create one explicit <strong>DAX measure</strong>, e.g. <code>Total&nbsp;Sales = SUM(financials[Sales])</code>.</li>
  <li>Build a one-page report containing:
    <ul class="task-ul">
      <li>One <strong>card</strong> visual showing your measure.</li>
      <li>One <strong>bar / column</strong> visual broken down by a categorical column.</li>
      <li>One <strong>line</strong> visual over time.</li>
      <li>A <strong>slicer</strong> on a single field.</li>
    </ul>
  </li>
</ol>

<div class="task-callout"><strong>Submit:</strong> the <code>.pbix</code> file <em>and</em> one screenshot of the finished page. Briefly note (3&ndash;4 sentences) which transformation you applied in Power Query and why.</div>
""",

    'DP-300: Microsoft Azure Database Administrator Associate': """
<p class="task-p">For your first task you will provision an Azure SQL Database (Basic tier or serverless, low cost) and run a few baseline administration commands.</p>

<h3 class="task-h">Steps</h3>
<ol class="task-ol">
  <li>In the Azure Portal, deploy an <strong>Azure SQL Database</strong> on a new logical server. Use the <em>Basic</em> tier or <em>Serverless General Purpose, 1 vCore, auto-pause 1&nbsp;hour</em>.</li>
  <li>Configure the server firewall to allow your client IP.</li>
  <li>Connect with <strong>Azure Data Studio</strong> or <strong>SSMS</strong> and run, capturing the output of each:
    <ul class="task-ul">
      <li><code>SELECT @@VERSION;</code></li>
      <li><code>SELECT name, state_desc FROM sys.databases;</code></li>
      <li><code>SELECT TOP&nbsp;5 * FROM sys.dm_db_resource_stats ORDER BY end_time DESC;</code></li>
    </ul>
  </li>
  <li>Document (1 paragraph) which <strong>service tier</strong> you chose, the <strong>backup retention</strong> default, and how you would <strong>pause</strong> compute to save money in a serverless database.</li>
</ol>

<div class="task-callout"><strong>Submit:</strong> screenshots of the three query outputs plus the short report. <strong>Delete the SQL server after you are done</strong> to avoid charges.</div>
""",

    'AI-900: Microsoft Azure AI Fundamentals': """
<p class="task-p">Your first task is a no-code experiment with <strong>Azure AI Vision</strong> in the Vision Studio sandbox.</p>

<h3 class="task-h">Steps</h3>
<ol class="task-ol">
  <li>Open <strong>Vision Studio</strong> at <code>portal.vision.cognitive.azure.com</code> and sign in with an Azure free account.</li>
  <li>Pick the <em>Image Analysis &rarr; Add captions to images</em> demo.</li>
  <li>Upload <strong>three</strong> images of your own (no faces of identifiable people). Try one easy scene, one cluttered scene and one abstract / artistic image.</li>
  <li>Record, for each image:
    <ul class="task-ul">
      <li>The <strong>auto-generated caption</strong>.</li>
      <li>The <strong>confidence score</strong>.</li>
      <li>One <strong>tag</strong> you find surprising &mdash; correct <em>or</em> wrong.</li>
    </ul>
  </li>
  <li>In 150&ndash;200 words, answer: which Microsoft <strong>responsible AI principle</strong> (fairness, reliability &amp; safety, privacy &amp; security, inclusiveness, transparency, accountability) was most relevant for your three images, and why?</li>
</ol>

<div class="task-callout"><strong>Submit:</strong> a single PDF containing the three captioned screenshots and your short reflection.</div>
""",
}

TARGET_TITLE = 'Lesson 2: Task \u2014 Your First Submission'


def run():
    with app.app_context():
        changed = 0
        for course_title, body in TASKS.items():
            course = Course.query.filter_by(title=course_title).first()
            if not course:
                print(f'skip: course not found -> {course_title}')
                continue
            lesson = Lesson.query.filter_by(course_id=course.id, title=TARGET_TITLE).first()
            if not lesson:
                print(f'skip: task lesson not found in {course_title}')
                continue
            lesson.content_type = 'task'
            lesson.task_instructions = TASK_STYLE + body.strip() + '\n'
            print(f'updated lesson {lesson.id} ({course.title})')
            changed += 1
        db.session.commit()
        print(f'done. {changed} lesson(s) updated.')


if __name__ == '__main__':
    run()
