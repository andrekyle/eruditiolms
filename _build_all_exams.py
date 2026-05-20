"""Parse 6 agent outputs and build 50-question final exams for each course."""
import os
import re
import sys
import types

# Map cert -> (agent_content_path, COURSE_LIKE, EXAM_TITLE, LESSON_TITLE, DESCRIPTION)
BASE = r'c:\Users\hp\AppData\Roaming\Code\User\workspaceStorage\25f723a0a07d7e81c8ab2371048eef31\GitHub.copilot-chat\chat-session-resources\7cdafd4c-d586-4bc9-9b47-be8b70ffb17b'

CERTS = [
    {
        'key': 'pcap',
        'content': os.path.join(BASE, 'toolu_vrtx_01J3i53fqubD7LfhFTWsNC6X__vscode-1779257269685', 'content.txt'),
        'course_like': 'PCAP%',
        'exam_title':   'Final Exam \u2014 PCAP-31-03 Practice (50 Questions)',
        'lesson_title': 'Final Exam: PCAP-31-03 Practice (50 Questions)',
        'description':  '50-question practice exam simulating the Python Institute PCAP-31-03 certification: modules and packages, exceptions, strings and list comprehensions, OOP, and miscellaneous (generators, files, closures).',
    },
    {
        'key': '1z0_808',
        'content': os.path.join(BASE, 'toolu_vrtx_01HB7oUg9Y24QmkcKbFubvGW__vscode-1779257269686', 'content.txt'),
        'course_like': '1Z0-808%',
        'exam_title':   'Final Exam \u2014 1Z0-808 Practice (50 Questions)',
        'lesson_title': 'Final Exam: 1Z0-808 Practice (50 Questions)',
        'description':  '50-question practice exam simulating the Oracle Certified Associate, Java SE 8 Programmer I (1Z0-808): basics, data types, operators, arrays, loops, methods/encapsulation, inheritance, exceptions, and selected Java API classes.',
    },
    {
        'key': 'pl_300',
        'content': os.path.join(BASE, 'toolu_vrtx_014etjWdWuEHRerqSdWtRYwX__vscode-1779257269687', 'content.txt'),
        'course_like': 'PL-300%',
        'exam_title':   'Final Exam \u2014 PL-300 Practice (50 Questions)',
        'lesson_title': 'Final Exam: PL-300 Practice (50 Questions)',
        'description':  '50-question practice exam simulating the Microsoft PL-300 Power BI Data Analyst Associate: prepare data, model data (DAX), visualize/analyze, and deploy and maintain assets.',
    },
    {
        'key': 'dp_300',
        'content': os.path.join(BASE, 'toolu_vrtx_01Rh24jsoavToBA7SXyMLhbj__vscode-1779257269688', 'content.txt'),
        'course_like': 'DP-300%',
        'exam_title':   'Final Exam \u2014 DP-300 Practice (50 Questions)',
        'lesson_title': 'Final Exam: DP-300 Practice (50 Questions)',
        'description':  '50-question practice exam simulating the Microsoft DP-300 Azure Database Administrator Associate: plan and implement data platform resources, security, monitoring and optimization, automation, and HADR.',
    },
    {
        'key': 'ai_901',
        'content': os.path.join(BASE, 'toolu_vrtx_01BSosCb5N5R2E1aBGe1XkU7__vscode-1779257269689', 'content.txt'),
        'course_like': 'AI-9%',
        'exam_title':   'Final Exam \u2014 AI-900/AI-901 Practice (50 Questions)',
        'lesson_title': 'Final Exam: AI-900/AI-901 Practice (50 Questions)',
        'description':  '50-question practice exam simulating the Microsoft Azure AI Fundamentals (AI-900 / AI-901), aligned to the Skills Measured as of April 15, 2026: AI concepts (Responsible AI, model components, AI workloads) and Microsoft Foundry implementation (Generative AI agents, Text/Speech, Vision/Image generation, Content Understanding).',
    },
    {
        'key': 'gh_300',
        'content': os.path.join(BASE, 'toolu_vrtx_01865QrXyoHQthLJY3pNTxAP__vscode-1779257269690', 'content.txt'),
        'course_like': 'GH-300%',
        'exam_title':   'Final Exam \u2014 GH-300 Practice (50 Questions)',
        'lesson_title': 'Final Exam: GH-300 Practice (50 Questions)',
        'description':  '50-question practice exam simulating the GitHub Copilot certification (GH-300): Responsible AI, plans and features, how Copilot handles data, prompt engineering, developer use cases, testing, and privacy/context exclusions.',
    },
]


def extract_block(text: str) -> str:
    m = re.search(r'===QUESTIONS_START===\s*(.*?)\s*===QUESTIONS_END===', text, re.DOTALL)
    if not m:
        raise RuntimeError('markers not found')
    body = m.group(1)
    # The body should begin with `QUESTIONS = [` and end with `]`
    return body


def load_questions(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    body = extract_block(text)
    ns = {}
    exec(compile(body, path, 'exec'), ns)
    qs = ns.get('QUESTIONS')
    if not isinstance(qs, list):
        raise RuntimeError(f'{path}: QUESTIONS not a list')
    return qs


def main():
    # Lazy import after parsing so we don't initialize the app if parsing fails
    from _exam_builder import build

    results = []
    for cert in CERTS:
        print(f'\n=== {cert["key"]} ===')
        try:
            qs = load_questions(cert['content'])
            print(f'  parsed {len(qs)} questions')
        except Exception as e:
            print(f'  PARSE ERROR: {e}')
            results.append((cert['key'], False, str(e)))
            continue

        if len(qs) < 50:
            print(f'  WARNING: expected >=50, got {len(qs)} -- skipping')
            results.append((cert['key'], False, f'count={len(qs)}'))
            continue
        if len(qs) > 50:
            print(f'  trimming {len(qs)} -> 50')
            qs = qs[:50]

        # Build a synthetic module for the builder
        mod = types.ModuleType(f'_exam_data_{cert["key"]}')
        mod.EXAM_TITLE   = cert['exam_title']
        mod.LESSON_TITLE = cert['lesson_title']
        mod.COURSE_LIKE  = cert['course_like']
        mod.DESCRIPTION  = cert['description']
        mod.QUESTIONS    = qs
        mod.LEGACY_EXAM_TITLES   = []
        mod.LEGACY_LESSON_TITLES = []

        try:
            build(mod)
            results.append((cert['key'], True, 'ok'))
        except Exception as e:
            print(f'  BUILD ERROR: {e}')
            results.append((cert['key'], False, str(e)))

    print('\n=== SUMMARY ===')
    for k, ok, msg in results:
        print(f'  {k}: {"OK" if ok else "FAIL"} ({msg})')
    failed = [r for r in results if not r[1]]
    sys.exit(0 if not failed else 1)


if __name__ == '__main__':
    main()
