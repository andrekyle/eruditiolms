"""Append the curated study-resources list to the GH-300 About lesson.
Idempotent: replaces any prior Study resources section content.
"""
import re
from app import app, db, Lesson

EXTRA_HTML = """
<h2>Study resources</h2>
<p>We recommend that you train and get hands-on experience before you take the exam. We offer self-study options and classroom training as well as links to documentation, community sites, and videos.</p>

<p>The official study guide is the right starting point, but treat it as a map, not the territory. The January 2026 revision added <strong>Agent Mode</strong>, <strong>Sub-Agents</strong>, <strong>MCP workflows</strong>, <strong>Spaces</strong>, and <strong>Spark</strong>. Make sure you are on the current version before you study anything else.</p>

<ul>
  <li><strong>GitHub Learn&rsquo;s official certification page</strong> has a free practice exam. Take it early, not at the end. Use it to surface your gaps, not to confirm you are ready.</li>
  <li><strong>The actual GitHub docs at <a href="https://docs.github.com" target="_blank" rel="noopener">docs.github.com</a></strong>. Read the technical documentation on privacy, content exclusions, and enterprise controls &mdash; the documentation pages, not the blog posts or feature announcements. The exam draws on the docs.</li>
  <li><strong><a href="https://github.com/timothywarner-org" target="_blank" rel="noopener">timothywarner-org</a> on GitHub</strong> is actively maintained, updated to April 2026. It includes a quick-reference cheat sheet, practice prompt files, and a Copilot study agent you can run inside VS Code. Worth cloning.</li>
  <li><strong>The GitHub Community certification prep thread</strong> has sample questions and answers in the discussion itself. Useful for checking your understanding of specific concepts.</li>
  <li><strong>freeCodeCamp&rsquo;s GitHub Foundations course</strong> (Andrew Brown, on YouTube) is not GH-300 specific but covers the GitHub fundamentals well if yours are rusty. Nine hours, free.</li>
</ul>

<h3>Is the GH-300 worth doing if you are already a senior practitioner?</h3>
""".strip()


def main():
    app.app_context().push()
    lesson = Lesson.query.filter_by(id=86).first()
    if lesson is None:
        raise SystemExit('GH-300 About lesson (id=86) not found')
    html = lesson.content or ''
    # Replace from "<h2>Study resources</h2>" to end (or end of doc).
    pattern = re.compile(r'<h2>\s*Study resources\s*</h2>.*\Z', re.I | re.S)
    if pattern.search(html):
        new_html = pattern.sub(EXTRA_HTML, html).rstrip() + '\n'
        action = 'replaced'
    else:
        new_html = html.rstrip() + '\n\n' + EXTRA_HTML + '\n'
        action = 'appended'
    lesson.content = new_html
    db.session.commit()
    print(f'{action} Study resources section on lesson id={lesson.id}')


if __name__ == '__main__':
    main()
