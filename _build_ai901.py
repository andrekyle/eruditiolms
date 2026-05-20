"""Build AI-901 (Microsoft Azure AI Fundamentals).

- Renames the AI-900 course to AI-901 (title + slug-ish description).
- Replaces the About lesson with the April 15, 2026 Skills Measured study guide.
- Parses 6 author-agent outputs (L3..L8), writes _ai901_data_l{N}.py modules.
- Upserts content lessons + quizzes + exam lessons orders 4..15, with
  the legacy "Lesson 3: Exam" placeholder parked then restored at order 16.

Idempotent.
"""
import ast
import importlib
import re
import sys
from pathlib import Path

from app import app, db, Course, Lesson, Quiz, Question, QuestionOption

WORKSPACE = Path(__file__).resolve().parent

AGENT = Path(r"c:\Users\hp\AppData\Roaming\Code\User\workspaceStorage\25f723a0a07d7e81c8ab2371048eef31\GitHub.copilot-chat\chat-session-resources\7cdafd4c-d586-4bc9-9b47-be8b70ffb17b")

# (lesson_number, topic, quiz_description, agent_output_path)
SPEC = [
    (3, "Principles of Responsible AI",
     "Practise the six Microsoft Responsible AI principles \u2014 fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.",
     AGENT / "toolu_vrtx_013LJazAFxWvdxvW7MsGct4g__vscode-1779227169377" / "content.txt"),
    (4, "AI Model Components and Configurations",
     "Practise how generative models work, choosing an appropriate model, Foundry deployment options, and configuration parameters such as temperature, top_p, max_tokens, and content filters.",
     AGENT / "toolu_vrtx_01GvJRQLBCwV7ujwe5BfeS1A__vscode-1779227169378" / "content.txt"),
    (5, "AI Workloads and Capabilities",
     "Practise common AI workloads \u2014 generative and agentic AI, text analysis, speech, computer vision, and information extraction \u2014 and the Azure AI services that implement them.",
     AGENT / "toolu_vrtx_01VmoyJCyNyohk8ZCH5MGXPN__vscode-1779227169379" / "content.txt"),
    (6, "Generative AI Apps and Agents with Foundry",
     "Practise authoring system and user prompts, deploying a model in the Foundry portal, building a chat client with the Foundry SDK, and creating single-agent solutions with the Azure AI Agent Service.",
     AGENT / "toolu_vrtx_017qkQsBWyT3cevnzosJC8ty__vscode-1779227169380" / "content.txt"),
    (7, "Text and Speech Solutions with Foundry",
     "Practise building text-analysis apps with Azure AI Language, speech-to-text and text-to-speech apps with Azure AI Speech, and responding to spoken prompts with a multimodal model.",
     AGENT / "toolu_vrtx_011NrWwJDqMMygLiEttAzDBi__vscode-1779227169381" / "content.txt"),
    (8, "Vision and Information Extraction with Foundry",
     "Practise multimodal vision prompts, image generation with DALL\u00b7E 3 / gpt-image-1, and information extraction from documents, images, audio, and video with Azure AI Content Understanding.",
     AGENT / "toolu_vrtx_01Q82DaMfwCmXjedpHSuseSb__vscode-1779227169382" / "content.txt"),
]

OLD_COURSE_TITLE_LIKE = 'AI-9%'
NEW_COURSE_TITLE = 'AI-901: Microsoft Azure AI Fundamentals'
NEW_COURSE_DESC = (
    'Build a solid foundation in AI on Azure with Microsoft Foundry. This AI-901 course '
    'covers responsible AI principles, generative and agentic AI workloads, choosing and '
    'deploying models, and hands-on implementation of text, speech, vision, and information '
    'extraction solutions using Azure AI services and the Foundry SDK.'
)
FINAL_EXAM_TITLE = 'Lesson 3: Exam'

ABOUT_HTML = """
<h2>Purpose of this course</h2>
<p>This course prepares you for the <strong>Microsoft Certified: Azure AI Fundamentals (AI-901)</strong> exam, refreshed on <strong>April 15, 2026</strong>. It is organised around the official <em>Skills measured</em> outline so every lesson and quiz maps directly to an exam objective.</p>

<h3>Useful links</h3>
<table>
  <thead><tr><th>Topic</th><th>Link</th></tr></thead>
  <tbody>
    <tr><td>Exam skills outline (current)</td><td><a href="https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-900" target="_blank" rel="noopener">Study guide for AI-901</a></td></tr>
    <tr><td>Certification page</td><td><a href="https://learn.microsoft.com/credentials/certifications/azure-ai-fundamentals/" target="_blank" rel="noopener">Azure AI Fundamentals certification</a></td></tr>
    <tr><td>Microsoft Foundry</td><td><a href="https://learn.microsoft.com/azure/ai-foundry/" target="_blank" rel="noopener">Azure AI Foundry documentation</a></td></tr>
    <tr><td>Free Azure sandbox</td><td><a href="https://learn.microsoft.com/training/modules/create-account-azure/" target="_blank" rel="noopener">Create an Azure free account</a></td></tr>
    <tr><td>Microsoft Q&amp;A</td><td><a href="https://learn.microsoft.com/answers/" target="_blank" rel="noopener">Microsoft Q&amp;A</a></td></tr>
  </tbody>
</table>

<h2>About the exam</h2>
<blockquote><p><strong>Note:</strong> The passing score is <strong>700</strong> on a 1\u20131000 scale. Scores are reported as a scaled total; you don\u2019t need to pass each section independently, but the weighting below shows where the questions concentrate.</p></blockquote>
<blockquote><p><strong>Note:</strong> The exam is updated periodically. The version this course tracks is the one published on <em>April 15, 2026</em>. If the official skills outline changes, individual lessons in this course will be refreshed to match.</p></blockquote>

<h2>Skills measured as of April 15, 2026</h2>

<h3>Audience profile</h3>
<p>As a candidate for this Microsoft Certification, you are at the beginning of your career in AI solution development. You should have:</p>
<ul>
  <li>Conceptual knowledge of AI solutions in Azure and the foundational technical skills to work with them.</li>
  <li>Familiarity with <strong>Python</strong> coding syntax and basic programming techniques.</li>
  <li>Familiarity with <strong>Azure resources</strong> (subscriptions, resource groups, deployments).</li>
</ul>

<h3>Skills at a glance</h3>
<table>
  <thead><tr><th>Domain</th><th>Weight</th></tr></thead>
  <tbody>
    <tr><td>Identify AI concepts and capabilities</td><td>40\u201345%</td></tr>
    <tr><td>Implement AI solutions by using Microsoft Foundry</td><td>55\u201360%</td></tr>
  </tbody>
</table>

<h2>Domain 1 \u2014 Identify AI concepts and capabilities (40\u201345%)</h2>

<h3>Describe principles of Responsible AI</h3>
<ul>
  <li>Describe considerations for <strong>fairness</strong> in an AI solution</li>
  <li>Describe considerations for <strong>reliability and safety</strong> in an AI solution</li>
  <li>Describe considerations for <strong>privacy and security</strong> in an AI solution</li>
  <li>Describe considerations for <strong>inclusiveness</strong> in an AI solution</li>
  <li>Describe considerations for <strong>transparency</strong> in an AI solution</li>
  <li>Describe considerations for <strong>accountability</strong> in an AI solution</li>
</ul>

<h3>Identify AI model components and configurations</h3>
<ul>
  <li>Describe how generative AI models work</li>
  <li>Identify an appropriate AI model, based on capabilities</li>
  <li>Identify appropriate model deployment options and configuration parameters</li>
</ul>

<h3>Identify AI workloads</h3>
<ul>
  <li>Identify scenarios for common AI workloads, including generative and agentic AI, text analysis, speech, computer vision, and information extraction</li>
  <li>Describe common text analysis techniques, including keyword extraction, entity detection, sentiment analysis, and summarization</li>
  <li>Identify features and capabilities of speech recognition and speech synthesis</li>
  <li>Identify features and capabilities of computer vision and image-generation models</li>
  <li>Identify techniques to extract information from text, images, audio, and videos</li>
</ul>

<h2>Domain 2 \u2014 Implement AI solutions by using Microsoft Foundry (55\u201360%)</h2>

<h3>Implement generative AI apps and agents by using Foundry</h3>
<ul>
  <li>Create effective system and user prompts for generative AI models</li>
  <li>Deploy a model and interact with it in the Foundry portal</li>
  <li>Create a lightweight chat client application by using the Foundry SDK</li>
  <li>Create and test a single-agent solution in the Foundry portal</li>
  <li>Create a lightweight client application for an agent</li>
</ul>

<h3>Implement AI solutions for text and speech by using Foundry</h3>
<ul>
  <li>Build a lightweight application that includes text analysis</li>
  <li>Respond to spoken prompts by using a deployed multimodal model</li>
  <li>Build a lightweight application by using Azure Speech in Foundry Tools</li>
</ul>

<h3>Implement AI solutions with computer vision and image-generation capabilities by using Foundry</h3>
<ul>
  <li>Interpret visual input in prompts by using a deployed multimodal model</li>
  <li>Create new visual outputs by using generative models</li>
  <li>Build a lightweight application that includes vision capabilities</li>
</ul>

<h3>Implement AI solutions for information extraction by using Foundry</h3>
<ul>
  <li>Extract information from documents and forms by using Azure Content Understanding in Foundry Tools</li>
  <li>Extract information from images by using Content Understanding</li>
  <li>Extract information from audio and video by using Content Understanding</li>
  <li>Build a lightweight application with information extraction capabilities by using Content Understanding</li>
</ul>

<h2>How this course is aligned</h2>
<table>
  <thead><tr><th>Lesson</th><th>Title</th><th>Skills measured area</th></tr></thead>
  <tbody>
    <tr><td>L3</td><td>Principles of Responsible AI</td><td>Domain 1 \u2014 Responsible AI principles</td></tr>
    <tr><td>L4</td><td>AI Model Components and Configurations</td><td>Domain 1 \u2014 Model components &amp; configuration</td></tr>
    <tr><td>L5</td><td>AI Workloads and Capabilities</td><td>Domain 1 \u2014 AI workloads</td></tr>
    <tr><td>L6</td><td>Generative AI Apps and Agents with Foundry</td><td>Domain 2 \u2014 Generative AI apps and agents</td></tr>
    <tr><td>L7</td><td>Text and Speech Solutions with Foundry</td><td>Domain 2 \u2014 Text and Speech</td></tr>
    <tr><td>L8</td><td>Vision and Information Extraction with Foundry</td><td>Domain 2 \u2014 Vision, image generation &amp; Content Understanding</td></tr>
  </tbody>
</table>

<h2>Study resources</h2>
<table>
  <thead><tr><th>Resource</th><th>Where to find it</th></tr></thead>
  <tbody>
    <tr><td>Self-paced learning paths</td><td><a href="https://learn.microsoft.com/training/browse/?roles=ai-engineer&amp;levels=beginner" target="_blank" rel="noopener">Microsoft Learn \u2014 AI training</a></td></tr>
    <tr><td>Azure AI Foundry</td><td><a href="https://learn.microsoft.com/azure/ai-foundry/" target="_blank" rel="noopener">Azure AI Foundry docs</a></td></tr>
    <tr><td>Azure AI Language</td><td><a href="https://learn.microsoft.com/azure/ai-services/language-service/" target="_blank" rel="noopener">Azure AI Language docs</a></td></tr>
    <tr><td>Azure AI Speech</td><td><a href="https://learn.microsoft.com/azure/ai-services/speech-service/" target="_blank" rel="noopener">Azure AI Speech docs</a></td></tr>
    <tr><td>Azure AI Vision</td><td><a href="https://learn.microsoft.com/azure/ai-services/computer-vision/" target="_blank" rel="noopener">Azure AI Vision docs</a></td></tr>
    <tr><td>Azure AI Content Understanding</td><td><a href="https://learn.microsoft.com/azure/ai-services/content-understanding/" target="_blank" rel="noopener">Content Understanding docs</a></td></tr>
    <tr><td>Community</td><td><a href="https://techcommunity.microsoft.com/category/artificial-intelligence" target="_blank" rel="noopener">AI &amp; Machine Learning Hub</a></td></tr>
    <tr><td>Videos</td><td><a href="https://learn.microsoft.com/shows/ai-show/" target="_blank" rel="noopener">The AI Show</a></td></tr>
  </tbody>
</table>
""".strip()


def parse_agent_output(text: str):
    m_q = re.search(r'^\s*===QUESTIONS===\s*$', text, flags=re.MULTILINE)
    m_e = re.search(r'^\s*===END===\s*$', text, flags=re.MULTILINE)
    m_l = re.search(r'^\s*===LESSON_HTML===\s*$', text, flags=re.MULTILINE)
    if not (m_l and m_q and m_e):
        raise ValueError("missing markers")

    lesson_html = text[m_l.end():m_q.start()].strip()
    lesson_html = re.sub(r'\n?\s*===LESSON_HTML===\s*$', '', lesson_html).strip()

    questions_src = text[m_q.end():m_e.start()].strip()
    questions = ast.literal_eval(questions_src)
    if not isinstance(questions, list) or len(questions) != 8:
        raise ValueError(f"expected list of 8 questions, got {type(questions).__name__}")
    for i, q in enumerate(questions):
        if not (isinstance(q, tuple) and len(q) == 4):
            raise ValueError(f"q{i}: expected 4-tuple (qhtml, opts, points, feedback), got len={len(q)}")
        qhtml, opts, points, fb = q
        if not isinstance(qhtml, str):
            raise ValueError(f"q{i}: qhtml not str")
        if not isinstance(opts, list) or len(opts) != 4:
            raise ValueError(f"q{i}: need exactly 4 options, got {len(opts)}")
        if sum(int(o[1]) for o in opts) != 1:
            raise ValueError(f"q{i}: need exactly 1 correct option, got marks={[o[1] for o in opts]}")

    return lesson_html, questions_src, questions


CODE_BLOCK_RE = re.compile(
    r'(<pre><code class="language-[a-zA-Z0-9_-]+">)(.*?)(</code></pre>)',
    flags=re.DOTALL,
)


def escape_code_blocks(html: str) -> str:
    def _esc(m):
        inner = m.group(2)
        inner = inner.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        return m.group(1) + inner + m.group(3)
    return CODE_BLOCK_RE.sub(_esc, html)


def write_data_modules():
    for num, topic, _qdesc, path in SPEC:
        text = path.read_text(encoding='utf-8')
        lesson_html, questions_src, _ = parse_agent_output(text)
        safe_html = lesson_html.replace('"""', '\\"\\"\\"')
        out = WORKSPACE / f"_ai901_data_l{num}.py"
        body = (
            '# Auto-generated by _build_ai901.py\n'
            f'LESSON_HTML = """\n{safe_html}\n"""\n\n'
            f'QUESTIONS = {questions_src}\n'
        )
        out.write_text(body, encoding='utf-8')
        modname = out.stem
        if modname in sys.modules:
            importlib.reload(sys.modules[modname])
        else:
            importlib.import_module(modname)
        print(f"wrote {out.name}  (lesson {len(lesson_html)} chars, {len(questions_src)} qsrc chars)")


def upsert():
    with app.app_context():
        course = Course.query.filter(Course.title.like(OLD_COURSE_TITLE_LIKE)).first()
        if not course:
            print('AI-9xx course not found.')
            return

        # Rename to AI-901 and update description
        if course.title != NEW_COURSE_TITLE:
            print(f'renaming course {course.id}: {course.title!r} -> {NEW_COURSE_TITLE!r}')
            course.title = NEW_COURSE_TITLE
        course.description = NEW_COURSE_DESC

        # Update About lesson (the first "lesson" type with title 'About this course')
        about = Lesson.query.filter_by(course_id=course.id, title='About this course').first()
        if about:
            about.content = ABOUT_HTML
            about.content_type = 'lesson'
            print(f'updated About lesson {about.id}')

        final = Lesson.query.filter_by(course_id=course.id, title=FINAL_EXAM_TITLE).first()
        if final:
            final.order = 999
            db.session.flush()
            print(f'parked legacy exam lesson {final.id} at order 999')

        next_order = 4
        for num, topic, qdesc, _path in SPEC:
            modname = f'_ai901_data_l{num}'
            data = importlib.reload(sys.modules[modname]) if modname in sys.modules else importlib.import_module(modname)
            lesson_html = escape_code_blocks(data.LESSON_HTML)
            questions = data.QUESTIONS

            ltitle = f'Lesson {num}: {topic}'
            qtitle = f'Lesson {num} Quiz \u2014 {topic}'

            lesson = Lesson.query.filter_by(course_id=course.id, title=ltitle).first()
            if lesson:
                lesson.content = lesson_html
                lesson.content_type = 'lesson'
                lesson.order = next_order
                lesson.points = 1.0
                print(f'updated content lesson {lesson.id} ({ltitle}) order={next_order}')
            else:
                lesson = Lesson(
                    title=ltitle, content=lesson_html, course_id=course.id,
                    content_type='lesson', order=next_order, points=1.0,
                )
                db.session.add(lesson)
                db.session.flush()
                print(f'inserted content lesson {lesson.id} ({ltitle}) order={next_order}')
            next_order += 1

            quiz = Quiz.query.filter_by(course_id=course.id, title=qtitle).first()
            if not quiz:
                quiz = Quiz(course_id=course.id, title=qtitle, description=qdesc)
                db.session.add(quiz)
                db.session.flush()
                print(f'  inserted quiz {quiz.id}')
            else:
                quiz.description = qdesc
                for q in list(quiz.questions):
                    db.session.delete(q)
                db.session.flush()
                print(f'  rebuilt quiz {quiz.id}')

            for qhtml, opts, _points, feedback in questions:
                q = Question(
                    quiz_id=quiz.id, question_type='multiple_choice',
                    question_html=qhtml, points=1.0, feedback=feedback,
                )
                db.session.add(q)
                db.session.flush()
                for i, (ohtml, correct) in enumerate(opts):
                    db.session.add(QuestionOption(
                        question_id=q.id, option_html=ohtml,
                        is_correct=bool(correct), order=i,
                    ))

            exam = Lesson.query.filter_by(
                course_id=course.id, title=qtitle, content_type='exam',
            ).first()
            if exam:
                exam.quiz_id = quiz.id
                exam.order = next_order
                exam.points = 1.0
                print(f'  updated exam lesson {exam.id} order={next_order}')
            else:
                exam = Lesson(
                    title=qtitle, content='', course_id=course.id,
                    content_type='exam', quiz_id=quiz.id,
                    order=next_order, points=1.0,
                )
                db.session.add(exam)
                db.session.flush()
                print(f'  inserted exam lesson {exam.id} order={next_order}')
            next_order += 1

        if final:
            final.order = next_order
            print(f'restored legacy exam lesson {final.id} to order {next_order}')

        db.session.commit()
        print('done.')


if __name__ == '__main__':
    print('--- Writing data modules ---')
    write_data_modules()
    print('--- Upserting into DB ---')
    upsert()
