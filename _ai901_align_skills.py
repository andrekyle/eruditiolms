"""Align AI-901 lessons with the official Microsoft AI-901 skills measured
(as of April 15, 2026). Appends a 'Skills measured — covered in this lesson'
block to each content lesson, replacing any earlier AI-900 mapping. Idempotent.

Mapping:
  L3 (id 101) Principles of Responsible AI               -> Area 1 / Responsible AI
  L4 (id 103) AI Model Components and Configurations     -> Area 1 / Model components
  L5 (id 105) AI Workloads and Capabilities              -> Area 1 / AI workloads
  L6 (id 107) Generative AI Apps and Agents with Foundry -> Area 2 / Gen AI apps & agents
  L7 (id 109) Text and Speech Solutions with Foundry     -> Area 2 / Text & speech
  L8 (id 111) Vision and Information Extraction          -> Area 2 / Vision + info extraction
"""
from app import app, db, Lesson

COURSE_ID = 6

# Strip both old and new markers so re-runs replace whatever is there.
LEGACY_MARKERS = [
    ("<!-- AI900_SKILLS_MAPPING:START -->", "<!-- AI900_SKILLS_MAPPING:END -->"),
]
MARKER_START = "<!-- AI901_SKILLS_MAPPING:START -->"
MARKER_END = "<!-- AI901_SKILLS_MAPPING:END -->"

SUBSKILLS = {
    101: (
        "1. Identify AI concepts and capabilities (40–45%) — Responsible AI",
        [
            ("Describe principles of responsible AI", [
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
        "1. Identify AI concepts and capabilities (40–45%) — AI model components",
        [
            ("Identify AI model components and configurations", [
                "Describe how generative AI models work",
                "Identify an appropriate AI model, based on capabilities",
                "Identify appropriate model deployment options and configuration parameters",
            ]),
        ],
    ),
    105: (
        "1. Identify AI concepts and capabilities (40–45%) — AI workloads",
        [
            ("Identify AI workloads", [
                "Identify scenarios for common AI workloads, including generative and agentic "
                "AI, text analysis, speech, computer vision, and information extraction",
                "Describe common text analysis techniques, including keyword extraction, "
                "entity detection, sentiment analysis, and summarization",
                "Identify features and capabilities of speech recognition and speech synthesis",
                "Identify features and capabilities of computer vision and image-generation models",
                "Identify techniques to extract information from text, images, audio, and videos",
            ]),
        ],
    ),
    107: (
        "2. Implement AI solutions by using Microsoft Foundry (55–60%) — "
        "Generative AI apps and agents",
        [
            ("Implement generative AI apps and agents by using Foundry", [
                "Create effective system and user prompts for generative AI models",
                "Deploy a model and interact with it in the Foundry portal",
                "Create a lightweight chat client application by using the Foundry SDK",
                "Create and test a single-agent solution in the Foundry portal",
                "Create a lightweight client application for an agent",
            ]),
        ],
    ),
    109: (
        "2. Implement AI solutions by using Microsoft Foundry (55–60%) — "
        "Text and speech",
        [
            ("Implement AI solutions for text and speech by using Foundry", [
                "Build a lightweight application that includes text analysis",
                "Respond to spoken prompts by using a deployed multimodal model",
                "Build a lightweight application by using Azure Speech in Foundry Tools",
            ]),
        ],
    ),
    111: (
        "2. Implement AI solutions by using Microsoft Foundry (55–60%) — "
        "Vision, image generation, and information extraction",
        [
            ("Implement AI solutions with computer vision and image-generation "
             "capabilities by using Foundry", [
                "Interpret visual input in prompts by using a deployed multimodal model",
                "Create new visual outputs by using generative models",
                "Build a lightweight application that includes vision capabilities",
            ]),
            ("Implement AI solutions for information extraction by using Foundry", [
                "Extract information from documents and forms by using Azure Content Understanding in Foundry Tools",
                "Extract information from images by using Content Understanding",
                "Extract information from audio and video by using Content Understanding",
                "Build a lightweight application with information extraction capabilities by using Content Understanding",
            ]),
        ],
    ),
}


def build_mapping_html(area_title: str, groups: list[tuple[str, list[str]]]) -> str:
    parts = [
        MARKER_START,
        '<hr>',
        '<div class="ai901-skills-mapping">',
        '<h3>Skills measured &mdash; covered in this lesson</h3>',
        f'<p><strong>Functional group:</strong> {area_title}</p>',
        '<p class="text-muted">Source: Microsoft official '
        '<a href="https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901" '
        'target="_blank" rel="noopener">AI-901 study guide</a> '
        '(skills measured as of April 15, 2026).</p>',
    ]
    for group_title, bullets in groups:
        parts.append(f'<h4>{group_title}</h4>')
        parts.append('<ul>')
        parts.extend(f'  <li>{b}</li>' for b in bullets)
        parts.append('</ul>')
    parts.append('</div>')
    parts.append(MARKER_END)
    return "\n".join(parts)


def strip_block(html: str, start: str, end: str) -> str:
    if start not in html:
        return html
    s = html.find(start)
    e = html.find(end)
    if e == -1:
        return html[:s].rstrip()
    return (html[:s] + html[e + len(end):]).rstrip()


def strip_existing(html: str) -> str:
    out = html or ""
    for start, end in LEGACY_MARKERS:
        out = strip_block(out, start, end)
    out = strip_block(out, MARKER_START, MARKER_END)
    return out.rstrip()


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
            print(f"  refreshed AI-901 skills mapping on lesson {lid}: {lesson.title!r}")
        db.session.commit()
        print("Done.")


if __name__ == "__main__":
    main()
