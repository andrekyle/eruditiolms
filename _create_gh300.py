"""Create the GH-300: GitHub Copilot course with an About lesson.

Idempotent: re-running updates the course title/description and the
About lesson's content rather than creating duplicates.
"""
from app import app, db, Course, Lesson

COURSE_TITLE = 'GH-300: GitHub Copilot'
COURSE_DESCRIPTION = (
    'GitHub Copilot certification (GH-300). Learn to use GitHub Copilot responsibly '
    'and effectively across the IDE, CLI, chat, and agent modes; understand data '
    'handling, prompt engineering, and privacy controls.'
)
TEACHER_ID = 1

ABOUT_TITLE = 'About this course'
ABOUT_HTML = """
<h2>Purpose of this document</h2>
<p>This study guide should help you understand what to expect on the exam and includes a summary of the topics the exam might cover and links to additional resources. The information and materials in this document should help you focus your studies as you prepare for the exam.</p>

<table>
  <thead>
    <tr>
      <th>Useful links</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>How to earn the certification</td><td>Some certifications only require passing one exam, while others require passing multiple exams.</td></tr>
    <tr><td>Certification renewal</td><td>Microsoft associate, expert, and specialty certifications expire annually. You can renew by passing a free online assessment on Microsoft Learn.</td></tr>
    <tr><td>Your Microsoft Learn profile</td><td>Connecting your certification profile to Microsoft Learn allows you to schedule and renew exams and share and print certificates.</td></tr>
    <tr><td>Exam scoring and score reports</td><td>A score of 700 or greater is required to pass.</td></tr>
    <tr><td>Exam sandbox</td><td>You can explore the exam environment by visiting our exam sandbox.</td></tr>
    <tr><td>Request accommodations</td><td>If you use assistive devices, require extra time, or need modification to any part of the exam experience, you can request an accommodation.</td></tr>
  </tbody>
</table>

<h2>About the exam</h2>
<p>Some exams are localized into other languages, and those are updated approximately eight weeks after the English version is updated. While Microsoft makes every effort to update localized versions as noted, there may be times when the localized versions of an exam are not updated on this schedule. Other available languages are listed in the Schedule Exam section of the Exam Details webpage. If the exam isn't available in your preferred language, you can request an additional 30 minutes to complete the exam.</p>

<blockquote><strong>Note:</strong> The bullets that follow each of the skills measured are intended to illustrate how we are assessing that skill. Related topics may be covered in the exam.</blockquote>

<blockquote><strong>Note:</strong> Most questions cover features that are general availability (GA). The exam may contain questions on Preview features if those features are commonly used.</blockquote>

<h2>Skills measured as of January 2026</h2>

<h3>Audience profile</h3>
<p>Candidates for this exam should possess expertise in using GitHub Copilot to improve software development productivity, quality, and security. This includes responsible AI use, prompt engineering, Copilot features across various plans, and privacy safeguards. Candidates should also be familiar with GitHub fundamentals and have experience with one or more programming languages.</p>

<h3>Skills at a glance</h3>
<ul>
  <li>Use GitHub Copilot responsibly (15&ndash;20%)</li>
  <li>Use GitHub Copilot features (25&ndash;30%)</li>
  <li>GitHub Copilot features (25&ndash;30%)</li>
  <li>Understand GitHub Copilot data and architecture (10&ndash;15%)</li>
  <li>Apply prompt engineering and context crafting (10&ndash;15%)</li>
  <li>Improve developer productivity with GitHub Copilot (10&ndash;15%)</li>
  <li>Configure privacy, content exclusions, and safeguards (10&ndash;15%)</li>
</ul>

<h2>Use GitHub Copilot responsibly (15&ndash;20%)</h2>
<h3>Understand responsible AI principles</h3>
<ul>
  <li>Describe risks and limitations of Generative AI tools</li>
  <li>Describe ethical and responsible AI usage</li>
  <li>Identify potential harms and mitigation strategies of AI usage</li>
</ul>
<h3>Validate and operate AI tools</h3>
<ul>
  <li>Explain the need to validate AI output</li>
  <li>Identify how to operate GitHub Copilot responsibly</li>
</ul>

<h2>Use GitHub Copilot features (25&ndash;30%)</h2>
<h3>Use GitHub Copilot in the IDE</h3>
<ul>
  <li>Enable Copilot in the IDE</li>
  <li>Trigger Copilot through inline suggestions, chat, CLI, and Plan Mode</li>
  <li>Exclude specific files or repositories (app knowledge)</li>
</ul>
<h3>Use GitHub Copilot CLI</h3>
<ul>
  <li>Define GitHub Copilot CLI and how it benefits developers</li>
  <li>Identify the steps for installing GitHub Copilot CLI</li>
  <li>Describe key GitHub Copilot CLI features and commands</li>
  <li>Use GitHub Copilot CLI interactively and in sessions</li>
  <li>Generate scripts and manage files with GitHub Copilot CLI</li>
</ul>
<h3>Use GitHub Copilot features and capabilities</h3>
<ul>
  <li>Use Agent Mode, Edit Mode, and MCP for enhanced development and workflows; manage Agent Sessions and delegate tasks to Sub-Agents for optimized context usage</li>
  <li>Use Copilot for code review and coding assistance</li>
  <li>Utilize Spaces, Spark, Pull Request summaries, and customizable review standards via instructions files</li>
  <li>Understand the limits, options, feedback, and commands of GitHub Copilot Chat; include prompt file reuse for consistent responses</li>
</ul>
<h3>Manage organization-wide settings and policies</h3>
<ul>
  <li>Configure organization-wide policy management; enable Copilot Code Review policies and manage feature availability across IDEs and github.com</li>
  <li>Utilize audit log events</li>
  <li>Manage subscriptions using the REST API</li>
</ul>

<h2>Understand GitHub Copilot data and architecture (10&ndash;15%)</h2>
<h3>Describe data handling and flow</h3>
<ul>
  <li>Explain data usage, flow, and sharing</li>
  <li>Describe input processing and prompt building</li>
  <li>Explain proxy filtering and post-processing</li>
</ul>
<h3>Understand lifecycle and limitations</h3>
<ul>
  <li>Visualize code suggestion lifecycle</li>
  <li>Describe limitations of LLMs and Copilot</li>
</ul>

<h2>Apply prompt engineering and context crafting (10&ndash;15%)</h2>
<h3>Craft effective prompts</h3>
<ul>
  <li>Describe prompt structure and context</li>
  <li>Understand how context is determined</li>
  <li>Use zero-shot and few-shot prompting</li>
  <li>Apply best practices for prompt crafting</li>
</ul>
<h3>Engineer prompts for performance</h3>
<ul>
  <li>Explain prompt engineering principles</li>
  <li>Describe prompt process flow and chat history usage</li>
</ul>

<h2>Improve developer productivity with GitHub Copilot (10&ndash;15%)</h2>
<h3>Enhance productivity and code quality</h3>
<ul>
  <li>Use Copilot for code generation, refactoring, and documentation</li>
  <li>Accelerate learning and reduce context switching</li>
  <li>Generate sample data and modernize legacy code</li>
</ul>
<h3>Support testing and security</h3>
<ul>
  <li>Generate unit and integration tests</li>
  <li>Identify edge cases and write assertions</li>
  <li>Suggest security improvements and performance optimizations</li>
</ul>

<h2>Configure privacy, content exclusions, and safeguards (10&ndash;15%)</h2>
<h3>Manage privacy settings and exclusions</h3>
<ul>
  <li>Configure content exclusions and editor settings</li>
  <li>Describe ownership and limitations of outputs</li>
</ul>
<h3>Apply safeguards and troubleshoot</h3>
<ul>
  <li>Enable duplication detection and security warnings</li>
  <li>Resolve issues with suggestions and exclusions</li>
</ul>

<h2>Study resources</h2>
<p>We recommend that you train and get hands-on experience before you take the exam. We offer self-study options and classroom training as well as links to documentation, community sites, and videos.</p>
""".strip()


def main():
    app.app_context().push()
    course = Course.query.filter(Course.title.like('GH-300%')).first()
    if course is None:
        course = Course(
            title=COURSE_TITLE,
            description=COURSE_DESCRIPTION,
            teacher_id=TEACHER_ID,
        )
        db.session.add(course)
        db.session.flush()
        print(f'created course id={course.id}: {course.title}')
    else:
        course.title = COURSE_TITLE
        course.description = COURSE_DESCRIPTION
        print(f'updated existing course id={course.id}: {course.title}')

    about = Lesson.query.filter_by(course_id=course.id, title=ABOUT_TITLE).first()
    if about is None:
        about = Lesson(
            course_id=course.id,
            title=ABOUT_TITLE,
            content=ABOUT_HTML,
            content_type='lesson',
            order=1,
            points=1.0,
        )
        db.session.add(about)
        db.session.flush()
        print(f'  created About lesson id={about.id}')
    else:
        about.content = ABOUT_HTML
        about.content_type = 'lesson'
        about.order = 1
        print(f'  updated About lesson id={about.id}')

    db.session.commit()
    print('done.')


if __name__ == '__main__':
    main()
