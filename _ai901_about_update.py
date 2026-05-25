"""Replace the AI-901 'About this course' lesson body with a summary of the
official Microsoft study guide for Exam AI-901: Azure AI Fundamentals
(skills measured as of April 15, 2026). Idempotent.
"""
from app import app, db, Lesson

LESSON_ID = 21

CONTENT = """
<h2>Study Guide Summary — Exam AI-901: Microsoft Azure AI Fundamentals</h2>

<p>This About page summarizes the official Microsoft <em>Study Guide for Exam AI-901</em>
(skills measured as of <strong>April 15, 2026</strong>). The exam validates that you can
identify core AI concepts and capabilities, and that you can build lightweight
AI solutions on Azure using <strong>Microsoft Foundry</strong>.</p>

<h3>Purpose</h3>
<p>AI-901 awards the Microsoft Certified: <strong>Azure AI Fundamentals</strong>
credential. A scaled score of <strong>700 or greater</strong> is required to pass.
Most questions cover <strong>generally available (GA)</strong> features, though commonly
used Preview features may also appear.</p>

<h3>Audience profile</h3>
<p>You are at the beginning of your career in AI solution development. For this exam you
should have:</p>
<ul>
  <li>Conceptual knowledge of <strong>AI solutions in Azure</strong>.</li>
  <li>The foundational technical skills to work with those solutions.</li>
  <li>Knowledge of <strong>Python</strong> coding syntax and basic programming techniques.</li>
  <li>Familiarity with <strong>Azure resources</strong>.</li>
</ul>

<h3>Skills measured at a glance</h3>
<table class="table table-bordered table-striped">
  <thead>
    <tr><th>Functional area</th><th>Weight</th></tr>
  </thead>
  <tbody>
    <tr><td>Identify AI concepts and capabilities</td><td>40&ndash;45%</td></tr>
    <tr><td>Implement AI solutions by using Microsoft Foundry</td><td>55&ndash;60%</td></tr>
  </tbody>
</table>

<h3>1. Identify AI concepts and capabilities (40&ndash;45%)</h3>

<h4>Describe principles of responsible AI</h4>
<ul>
  <li>Considerations for <strong>fairness</strong>.</li>
  <li>Considerations for <strong>reliability and safety</strong>.</li>
  <li>Considerations for <strong>privacy and security</strong>.</li>
  <li>Considerations for <strong>inclusiveness</strong>.</li>
  <li>Considerations for <strong>transparency</strong>.</li>
  <li>Considerations for <strong>accountability</strong>.</li>
</ul>

<h4>Identify AI model components and configurations</h4>
<ul>
  <li>Describe how <strong>generative AI models</strong> work.</li>
  <li>Identify an appropriate <strong>AI model</strong>, based on capabilities.</li>
  <li>Identify appropriate <strong>model deployment options</strong> and configuration
  parameters.</li>
</ul>

<h4>Identify AI workloads</h4>
<ul>
  <li>Identify scenarios for common AI workloads &mdash; <strong>generative and agentic
  AI</strong>, <strong>text analysis</strong>, <strong>speech</strong>,
  <strong>computer vision</strong>, and <strong>information extraction</strong>.</li>
  <li>Common <strong>text analysis</strong> techniques: keyword extraction, entity
  detection, sentiment analysis, summarization.</li>
  <li>Features and capabilities of <strong>speech recognition</strong> and
  <strong>speech synthesis</strong>.</li>
  <li>Features and capabilities of <strong>computer vision</strong> and
  <strong>image-generation</strong> models.</li>
  <li>Techniques to <strong>extract information</strong> from text, images, audio, and
  videos.</li>
</ul>

<h3>2. Implement AI solutions by using Microsoft Foundry (55&ndash;60%)</h3>

<h4>Implement generative AI apps and agents by using Foundry</h4>
<ul>
  <li>Create effective <strong>system and user prompts</strong> for generative AI models.</li>
  <li><strong>Deploy a model</strong> and interact with it in the Foundry portal.</li>
  <li>Create a lightweight <strong>chat client application</strong> by using the Foundry SDK.</li>
  <li>Create and test a <strong>single-agent</strong> solution in the Foundry portal.</li>
  <li>Create a lightweight <strong>client application for an agent</strong>.</li>
</ul>

<h4>Implement AI solutions for text and speech by using Foundry</h4>
<ul>
  <li>Build a lightweight application that includes <strong>text analysis</strong>.</li>
  <li>Respond to <strong>spoken prompts</strong> by using a deployed multimodal model.</li>
  <li>Build a lightweight application by using <strong>Azure Speech in Foundry Tools</strong>.</li>
</ul>

<h4>Implement AI solutions with computer vision and image-generation capabilities by using Foundry</h4>
<ul>
  <li>Interpret <strong>visual input in prompts</strong> by using a deployed multimodal model.</li>
  <li>Create new <strong>visual outputs</strong> by using generative models.</li>
  <li>Build a lightweight application that includes <strong>vision capabilities</strong>.</li>
</ul>

<h4>Implement AI solutions for information extraction by using Foundry</h4>
<ul>
  <li>Extract information from <strong>documents and forms</strong> by using
  <em>Azure Content Understanding</em> in Foundry Tools.</li>
  <li>Extract information from <strong>images</strong> by using Content Understanding.</li>
  <li>Extract information from <strong>audio and video</strong> by using Content Understanding.</li>
  <li>Build a lightweight application with <strong>information extraction capabilities</strong>
  by using Content Understanding.</li>
</ul>

<h3>Recommended study resources</h3>
<ul>
  <li><strong>Microsoft Learn</strong> &mdash; self-paced learning paths and modules for
  AI-901, plus instructor-led courses.</li>
  <li><strong>Documentation</strong> &mdash; Anomaly Detector, Language Understanding,
  Azure Machine Learning, Computer Vision, Natural Language Processing technology,
  Azure Bot Service, Speech to Text, Speech Translation.</li>
  <li><strong>Practice Assessment</strong> &mdash; free, on Microsoft Learn.</li>
  <li><strong>Exam sandbox</strong> &mdash; explore the exam UI before test day.</li>
  <li><strong>Community</strong> &mdash; Microsoft Q&amp;A, the Artificial Intelligence and
  Machine Learning Hub, and the Microsoft Learn show <em>The AI Show</em>.</li>
  <li><strong>Hands-on practice</strong> &mdash; build small demos in
  <em>Microsoft Foundry</em> (portal, SDK, agents, Foundry Tools, and Content Understanding).</li>
</ul>

<h3>Exam logistics worth knowing</h3>
<ul>
  <li>The English version of the exam is updated first; localized versions follow about
  <strong>eight weeks</strong> later.</li>
  <li>If your preferred language is unavailable, you can request an extra
  <strong>30 minutes</strong>.</li>
  <li><strong>Accommodations</strong> are available for assistive devices, extra time, or
  other modifications.</li>
  <li>Microsoft associate, expert, and specialty certifications expire annually and are
  renewed via a free assessment on Microsoft Learn.</li>
  <li>You can connect your <strong>Microsoft Learn profile</strong> to schedule and renew
  exams and to share or print your certificates.</li>
</ul>

<p class="text-muted"><em>Source: Microsoft official Study Guide for Exam AI-901
&mdash; skills measured as of April 15, 2026 (last updated 04/15/2026).</em></p>
""".strip()


def main() -> None:
    with app.app_context():
        lesson = db.session.get(Lesson, LESSON_ID)
        if lesson is None:
            raise SystemExit(f"Lesson {LESSON_ID} not found")
        lesson.content = CONTENT
        db.session.commit()
        print(f"Updated lesson {lesson.id} '{lesson.title}' ({len(CONTENT)} chars).")


if __name__ == "__main__":
    main()
