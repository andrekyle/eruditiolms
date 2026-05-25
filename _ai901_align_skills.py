"""Align AI-901 (Azure AI Fundamentals — AI-900 syllabus) lessons with the
official Skills Measured (as of May 2, 2025). Appends a 'Skills measured —
covered in this lesson' block to each content lesson so students can see
which exam bullets the lesson maps to. Idempotent.

Mapping:
  L3 (id 101) Principles of Responsible AI               -> Area 1 (Responsible AI)
  L4 (id 103) AI Model Components and Configurations     -> Area 2 (ML principles)
  L5 (id 105) AI Workloads and Capabilities              -> Area 1 (Workload identification)
  L6 (id 107) Generative AI Apps and Agents with Foundry -> Area 5 (Generative AI)
  L7 (id 109) Text and Speech Solutions with Foundry     -> Area 4 (NLP)
  L8 (id 111) Vision and Information Extraction          -> Area 3 (Computer Vision)
"""
from app import app, db, Lesson

COURSE_ID = 6

MARKER_START = "<!-- AI900_SKILLS_MAPPING:START -->"
MARKER_END = "<!-- AI900_SKILLS_MAPPING:END -->"

SUBSKILLS = {
    101: (
        "1. Describe Artificial Intelligence workloads and considerations "
        "(15–20%) — Responsible AI",
        [
            ("Identify guiding principles for responsible AI", [
                "Describe considerations for fairness in an AI solution",
                "Describe considerations for reliability and safety in an AI solution",
                "Describe considerations for privacy and security in an AI solution",
                "Describe considerations for inclusiveness in an AI solution",
                "Describe considerations for transparency in an AI solution",
                "Describe considerations for accountability in an AI solution",
            ]),
        ],
    ),
    103: (
        "2. Describe fundamental principles of machine learning on Azure (15–20%)",
        [
            ("Identify common machine learning techniques", [
                "Identify regression machine learning scenarios",
                "Identify classification machine learning scenarios",
                "Identify clustering machine learning scenarios",
                "Identify features of deep learning techniques",
                "Identify features of the Transformer architecture",
            ]),
            ("Describe core machine learning concepts", [
                "Identify features and labels in a dataset for machine learning",
                "Describe how training and validation datasets are used in machine learning",
            ]),
            ("Describe Azure Machine Learning capabilities", [
                "Describe capabilities of automated machine learning (AutoML)",
                "Describe data and compute services for data science and machine learning",
                "Describe model management and deployment capabilities in Azure Machine Learning",
            ]),
        ],
    ),
    105: (
        "1. Describe Artificial Intelligence workloads and considerations "
        "(15–20%) — Workload identification",
        [
            ("Identify features of common AI workloads", [
                "Identify computer vision workloads",
                "Identify natural language processing workloads",
                "Identify document processing workloads",
                "Identify features of generative AI workloads",
            ]),
        ],
    ),
    107: (
        "5. Describe features of generative AI workloads on Azure (20–25%)",
        [
            ("Identify features of generative AI solutions", [
                "Identify features of generative AI models",
                "Identify common scenarios for generative AI",
                "Identify responsible AI considerations for generative AI",
            ]),
            ("Identify generative AI services and capabilities in Microsoft Azure", [
                "Describe features and capabilities of Azure AI Foundry",
                "Describe features and capabilities of Azure OpenAI service",
                "Describe features and capabilities of the Azure AI Foundry model catalog",
            ]),
        ],
    ),
    109: (
        "4. Describe features of Natural Language Processing (NLP) workloads on Azure "
        "(15–20%)",
        [
            ("Identify features of common NLP workload scenarios", [
                "Identify features and uses for key phrase extraction",
                "Identify features and uses for entity recognition",
                "Identify features and uses for sentiment analysis",
                "Identify features and uses for language modeling",
                "Identify features and uses for speech recognition and synthesis",
                "Identify features and uses for translation",
            ]),
            ("Identify Azure tools and services for NLP workloads", [
                "Describe capabilities of the Azure AI Language service",
                "Describe capabilities of the Azure AI Speech service",
            ]),
        ],
    ),
    111: (
        "3. Describe features of computer vision workloads on Azure (15–20%)",
        [
            ("Identify common types of computer vision solution", [
                "Identify features of image classification solutions",
                "Identify features of object detection solutions",
                "Identify features of optical character recognition (OCR) solutions",
                "Identify features of facial detection and facial analysis solutions",
            ]),
            ("Identify Azure tools and services for computer vision tasks", [
                "Describe capabilities of the Azure AI Vision service",
                "Describe capabilities of the Azure AI Face detection service",
            ]),
        ],
    ),
}


def build_mapping_html(area_title: str, groups: list[tuple[str, list[str]]]) -> str:
    parts = [
        MARKER_START,
        '<hr>',
        '<div class="ai900-skills-mapping">',
        '<h3>Skills measured &mdash; covered in this lesson</h3>',
        f'<p><strong>Functional group:</strong> {area_title}</p>',
        '<p class="text-muted">Source: Microsoft official '
        '<a href="https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-900" '
        'target="_blank" rel="noopener">AI-900 study guide</a> '
        '(skills measured as of May 2, 2025).</p>',
    ]
    for group_title, bullets in groups:
        parts.append(f'<h4>{group_title}</h4>')
        parts.append('<ul>')
        parts.extend(f'  <li>{b}</li>' for b in bullets)
        parts.append('</ul>')
    parts.append('</div>')
    parts.append(MARKER_END)
    return "\n".join(parts)


def strip_existing(html: str) -> str:
    if MARKER_START not in html:
        return html.rstrip()
    start = html.find(MARKER_START)
    end = html.find(MARKER_END)
    if end == -1:
        return html[:start].rstrip()
    return (html[:start] + html[end + len(MARKER_END):]).rstrip()


def main() -> None:
    with app.app_context():
        for lid, (area_title, groups) in SUBSKILLS.items():
            lesson = db.session.get(Lesson, lid)
            if lesson is None:
                print(f"  (lesson {lid} not found)")
                continue
            base = strip_existing(lesson.content or "")
            block = build_mapping_html(area_title, groups)
            lesson.content = f"{base}\n\n{block}\n"
            print(f"  refreshed skills mapping on lesson {lid}: {lesson.title!r}")
        db.session.commit()
        print("Done.")


if __name__ == "__main__":
    main()
