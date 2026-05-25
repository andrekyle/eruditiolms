"""Replace the AI-901 'About this course' lesson body with a summary of the
official Microsoft study guide for Exam AI-900: Azure AI Fundamentals
(skills measured as of May 2, 2025). Idempotent.
"""
from app import app, db, Lesson

LESSON_ID = 21

CONTENT = """
<h2>Study Guide Summary — Exam AI-900: Microsoft Azure AI Fundamentals</h2>

<p>This About page summarizes the official Microsoft <em>Study Guide for Exam AI-900</em>
(skills measured as of <strong>May 2, 2025</strong>). Although this course is branded
<strong>AI-901</strong>, it follows the AI-900 syllabus end-to-end so you can use it to
prepare for the Microsoft Certified: <strong>Azure AI Fundamentals</strong> credential.</p>

<h3>Purpose</h3>
<p>AI-900 validates foundational knowledge of <strong>machine learning</strong> and
<strong>artificial intelligence</strong> concepts and the Azure services that implement
them. A scaled score of <strong>700 or greater</strong> is required to pass.</p>

<h3>Audience profile</h3>
<p>The exam is open to candidates from both technical and non-technical backgrounds.
Data-science or software-engineering experience is <em>not</em> required, but you will
benefit from awareness of:</p>
<ul>
  <li>Basic <strong>cloud concepts</strong>.</li>
  <li><strong>Client&ndash;server applications</strong>.</li>
</ul>
<p>AI-900 is useful preparation for role-based certifications such as
<em>Azure Data Scientist Associate</em> and <em>Azure AI Engineer Associate</em>, but it
is not a prerequisite for any of them.</p>

<h3>Skills measured at a glance</h3>
<table class="table table-bordered table-striped">
  <thead>
    <tr><th>Functional area</th><th>Weight</th></tr>
  </thead>
  <tbody>
    <tr><td>Describe Artificial Intelligence workloads and considerations</td><td>15&ndash;20%</td></tr>
    <tr><td>Describe fundamental principles of machine learning on Azure</td><td>15&ndash;20%</td></tr>
    <tr><td>Describe features of computer vision workloads on Azure</td><td>15&ndash;20%</td></tr>
    <tr><td>Describe features of Natural Language Processing (NLP) workloads on Azure</td><td>15&ndash;20%</td></tr>
    <tr><td>Describe features of generative AI workloads on Azure</td><td>20&ndash;25%</td></tr>
  </tbody>
</table>

<h3>1. AI workloads and considerations (15&ndash;20%)</h3>
<ul>
  <li><strong>Identify features of common AI workloads:</strong> computer vision, natural
  language processing, document processing, and generative AI.</li>
  <li><strong>Guiding principles for Responsible AI:</strong> fairness, reliability and
  safety, privacy and security, inclusiveness, transparency, and accountability.</li>
</ul>

<h3>2. Fundamental principles of machine learning on Azure (15&ndash;20%)</h3>
<ul>
  <li><strong>Common ML techniques:</strong> regression, classification, clustering,
  deep learning, and the <em>Transformer</em> architecture.</li>
  <li><strong>Core ML concepts:</strong> features vs. labels in a dataset; the role of
  training and validation datasets.</li>
  <li><strong>Azure Machine Learning capabilities:</strong> automated machine learning
  (AutoML); data and compute services for data science; and model management and
  deployment.</li>
</ul>

<h3>3. Computer vision workloads on Azure (15&ndash;20%)</h3>
<ul>
  <li><strong>Common solution types:</strong> image classification, object detection,
  optical character recognition (OCR), and facial detection and analysis.</li>
  <li><strong>Azure tools and services:</strong> <em>Azure AI Vision</em> and
  <em>Azure AI Face</em>.</li>
</ul>

<h3>4. Natural Language Processing on Azure (15&ndash;20%)</h3>
<ul>
  <li><strong>Common NLP scenarios:</strong> key phrase extraction, entity recognition,
  sentiment analysis, language modeling, speech recognition and synthesis, and
  translation.</li>
  <li><strong>Azure tools and services:</strong> <em>Azure AI Language</em> and
  <em>Azure AI Speech</em>.</li>
</ul>

<h3>5. Generative AI workloads on Azure (20&ndash;25%)</h3>
<ul>
  <li><strong>Features of generative AI solutions:</strong> generative model features,
  common business scenarios, and responsible-AI considerations specific to generative
  AI (e.g., grounding, hallucinations, content safety).</li>
  <li><strong>Azure generative AI services:</strong> <em>Azure AI Foundry</em>,
  <em>Azure OpenAI Service</em>, and the <em>Azure AI Foundry model catalog</em>.</li>
</ul>

<h3>Key updates since the previous version (May 2, 2025)</h3>
<ul>
  <li><em>Identify features of common AI workloads</em> &mdash; <strong>major</strong> change
  (now explicitly includes document processing and generative AI).</li>
  <li><em>Describe fundamental principles of machine learning on Azure</em> &mdash; weight
  <strong>decreased</strong>.</li>
  <li><em>Identify common machine learning techniques</em> &mdash; minor (adds Transformer
  architecture).</li>
  <li><em>Describe features of generative AI workloads on Azure</em> &mdash; weight
  <strong>increased</strong>.</li>
  <li><em>Identify capabilities of Azure OpenAI Service</em> renamed to
  <em>Identify generative AI services and capabilities in Microsoft Azure</em> &mdash;
  <strong>major</strong> change (adds Azure AI Foundry + model catalog).</li>
</ul>

<h3>Recommended study resources</h3>
<ul>
  <li><strong>Microsoft Learn</strong> &mdash; self-paced learning paths and modules for
  AI-900, plus instructor-led courses.</li>
  <li><strong>Documentation</strong> &mdash; Azure Machine Learning, Azure AI Vision and
  Face, Azure AI Language, Azure AI Speech, Azure OpenAI, and Azure AI Foundry.</li>
  <li><strong>Practice Assessment</strong> &mdash; free, on Microsoft Learn.</li>
  <li><strong>Exam sandbox</strong> &mdash; explore the exam UI before test day.</li>
  <li><strong>Community</strong> &mdash; Microsoft Q&amp;A, the AI &amp; Machine Learning
  Hub, and the Microsoft Learn show <em>The AI Show</em>.</li>
  <li><strong>Hands-on practice</strong> &mdash; build small demos in Azure AI Foundry,
  Azure OpenAI playground, Vision Studio, Language Studio, and Azure ML Studio.</li>
</ul>

<h3>Exam logistics worth knowing</h3>
<ul>
  <li>The English version of the exam is updated first; localized versions follow about
  <strong>eight weeks</strong> later.</li>
  <li>If your preferred language is unavailable, you can request an extra
  <strong>30 minutes</strong>.</li>
  <li>Most questions cover <strong>GA</strong> features, but commonly used
  <strong>Preview</strong> features may appear.</li>
  <li><strong>Accommodations</strong> are available for assistive devices, extra time, or
  other modifications.</li>
  <li>Microsoft associate, expert, and specialty certifications expire annually and are
  renewed via a free assessment on Microsoft Learn.</li>
</ul>

<p class="text-muted"><em>Source: Microsoft official Study Guide for Exam AI-900 &mdash;
skills measured as of May 2, 2025; document last updated 05/05/2025.</em></p>
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
