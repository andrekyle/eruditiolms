"""Replace PCAP About lesson (id=1) with PCAP-31-03 Skills Measured outline."""
from app import app, db, Lesson

HTML = """
<h2>About this course</h2>
<p>This course prepares you for the <strong>PCAP &mdash; Certified Associate in Python Programming</strong> certification (exam code <strong>PCAP-31-03</strong>), administered by the <a href="https://pythoninstitute.org/pcap" target="_blank" rel="noopener">OpenEDG Python Institute</a>. It is designed for learners who already know the basics of Python and want to move from beginner (PCEP level) to associate-level skills in modules, exceptions, strings, OOP, and Python's standard tooling.</p>

<h3>Useful links</h3>
<table class="table">
  <thead><tr><th>Resource</th><th>Link</th></tr></thead>
  <tbody>
    <tr><td>Official PCAP page</td><td><a href="https://pythoninstitute.org/pcap" target="_blank" rel="noopener">pythoninstitute.org/pcap</a></td></tr>
    <tr><td>Exam syllabus (PCAP-31-03)</td><td><a href="https://pythoninstitute.org/pcap-exam-syllabus" target="_blank" rel="noopener">PCAP-31-03 exam syllabus</a></td></tr>
    <tr><td>Schedule the exam</td><td><a href="https://pythoninstitute.org/locate-test-center" target="_blank" rel="noopener">OpenEDG / Pearson VUE test centers</a></td></tr>
    <tr><td>Free study course (PCAP)</td><td><a href="https://edube.org/" target="_blank" rel="noopener">edube.org &mdash; PCAP: Programming Essentials in Python</a></td></tr>
  </tbody>
</table>

<h3>About the exam</h3>
<blockquote class="blockquote">
  <p><strong>Note:</strong> The information in this section reflects the <strong>PCAP-31-03</strong> exam syllabus published by the OpenEDG Python Institute. Always cross-check the latest details on the official syllabus page before scheduling.</p>
</blockquote>
<ul>
  <li><strong>Exam code:</strong> PCAP-31-03</li>
  <li><strong>Format:</strong> Single-choice and multiple-choice items, drag-and-drop, gap-fill, code-fill, code-insertion, and sort questions</li>
  <li><strong>Number of questions:</strong> 40</li>
  <li><strong>Duration:</strong> 65 minutes exam time + 10 minutes NDA/tutorial (75 minutes total)</li>
  <li><strong>Passing score:</strong> 70%</li>
  <li><strong>Language:</strong> English</li>
  <li><strong>Python version targeted:</strong> Python 3.x</li>
  <li><strong>Delivery:</strong> OpenEDG Testing Service or Pearson VUE testing centers (online proctored option available)</li>
</ul>

<h3>Audience profile</h3>
<p>This certification is for candidates who can already write and run simple Python programs (typically PCEP level) and want to demonstrate intermediate Python proficiency, including object-oriented design, robust error handling, advanced string processing, modular code organization, and familiar standard-library idioms. It is well suited to junior developers, automation engineers, data professionals, and students preparing for further certifications such as PCPP-32-1.</p>

<h3>Skills at a glance</h3>
<table class="table">
  <thead><tr><th>Module</th><th>Topic area</th><th>Weight</th></tr></thead>
  <tbody>
    <tr><td>1</td><td>Modules and Packages</td><td>12%</td></tr>
    <tr><td>2</td><td>Exceptions</td><td>14%</td></tr>
    <tr><td>3</td><td>Strings</td><td>18%</td></tr>
    <tr><td>4</td><td>Object-Oriented Programming</td><td>34%</td></tr>
    <tr><td>5</td><td>Miscellaneous (Generators, Closures, File I/O, Standard Library)</td><td>22%</td></tr>
  </tbody>
</table>

<h3>Module 1 &mdash; Modules and Packages (12%)</h3>
<ul>
  <li>Import variants: <code>import</code>, <code>from &hellip; import</code>, <code>import &hellip; as</code>, <code>from &hellip; import *</code></li>
  <li>Conditional imports and selective imports</li>
  <li>Using <code>dir()</code> and the <code>__name__</code> variable (top-level vs imported module)</li>
  <li>Standard modules: <code>math</code>, <code>random</code>, <code>platform</code></li>
  <li>Designing and building your own modules; the role of <code>__pycache__</code></li>
  <li>Packages and subpackages: <code>__init__.py</code>, package hierarchy, dotted-path imports</li>
  <li>PIP basics: installing, listing, upgrading, and removing third-party packages</li>
</ul>

<h3>Module 2 &mdash; Exceptions (14%)</h3>
<ul>
  <li>Defensive vs exception-driven programming styles</li>
  <li>The <code>try / except / else / finally</code> blocks and their execution order</li>
  <li>Multiple <code>except</code> branches and exception ordering (specific to general)</li>
  <li>Raising exceptions with <code>raise</code> and re-raising the current exception</li>
  <li><code>assert</code> statements and their typical use</li>
  <li>The built-in exception hierarchy (<code>BaseException</code>, <code>Exception</code>, <code>ArithmeticError</code>, <code>LookupError</code>, etc.)</li>
  <li>Creating user-defined exception classes; carrying extra context via attributes</li>
</ul>

<h3>Module 3 &mdash; Strings (18%)</h3>
<ul>
  <li>Character encoding fundamentals: ASCII, Unicode, UTF-8; <code>ord()</code> and <code>chr()</code></li>
  <li>Strings as immutable sequences; indexing, slicing, concatenation, repetition, membership</li>
  <li>Iterating over strings; comparing strings; lexicographic vs numeric ordering</li>
  <li>String methods: <code>upper</code>, <code>lower</code>, <code>title</code>, <code>capitalize</code>, <code>swapcase</code>, <code>strip</code>/<code>lstrip</code>/<code>rstrip</code>, <code>split</code>, <code>join</code>, <code>replace</code>, <code>find</code>/<code>index</code>, <code>startswith</code>/<code>endswith</code>, <code>count</code>, <code>isalpha</code>/<code>isdigit</code>/<code>isalnum</code></li>
  <li>Formatting output with <code>%</code>, <code>str.format()</code>, and f-strings; conversion specifiers and field width</li>
  <li>Sorting strings and sorting lists of strings (<code>sorted</code>, <code>list.sort</code>, <code>key=</code>)</li>
</ul>

<h3>Module 4 &mdash; Object-Oriented Programming (34%)</h3>
<ul>
  <li>The OOP mindset: classes vs instances, attributes vs methods, state vs behavior</li>
  <li>Defining classes: <code>class</code> statement, <code>__init__</code>, <code>self</code>, instance vs class variables</li>
  <li>Instance methods, the implicit <code>self</code> argument, and method invocation</li>
  <li>Access conventions: public, single-underscore (<code>_x</code>), and name-mangled (<code>__x</code>) attributes</li>
  <li>Inheritance, single vs multiple inheritance, <code>super()</code>, and the Method Resolution Order (MRO)</li>
  <li>Polymorphism, method overriding, and duck typing</li>
  <li>Introspection: <code>__dict__</code>, <code>__name__</code>, <code>__module__</code>, <code>__bases__</code>, <code>__mro__</code>, <code>isinstance()</code>, <code>issubclass()</code>, <code>hasattr()</code>, <code>getattr()</code>, <code>setattr()</code></li>
  <li>Special methods: <code>__str__</code>, <code>__repr__</code>, <code>__len__</code>, comparison/arithmetic dunders</li>
  <li>Exceptions as classes &mdash; the exception hierarchy, custom exception classes, <code>args</code> attribute, chaining</li>
</ul>

<h3>Module 5 &mdash; Miscellaneous (22%)</h3>
<ul>
  <li>List comprehensions, including conditional and nested forms</li>
  <li>Lambda expressions, <code>map()</code>, <code>filter()</code>, and <code>functools.reduce()</code></li>
  <li>Closures and the <code>nonlocal</code> keyword; understanding the LEGB scope rule</li>
  <li>Generators and the <code>yield</code> statement; generator expressions vs list comprehensions</li>
  <li>File handling: <code>open()</code>, modes (<code>r</code>, <code>w</code>, <code>a</code>, <code>x</code>, <code>b</code>, <code>t</code>, <code>+</code>), text vs binary, <code>with</code> blocks</li>
  <li>Reading and writing files line by line, by chunks, and as a whole</li>
  <li>The <code>os</code> module: working directory, paths, listing and manipulating files</li>
  <li>The <code>datetime</code> and <code>calendar</code> modules for date and time handling</li>
  <li>The <code>bytearray</code> object as a mutable byte sequence</li>
</ul>

<h3>Study resources</h3>
<table class="table">
  <thead><tr><th>Resource</th><th>What it covers</th></tr></thead>
  <tbody>
    <tr><td><a href="https://edube.org/" target="_blank" rel="noopener">Edube &mdash; PCAP: Programming Essentials in Python</a></td><td>Official free PCAP course from the Python Institute (Modules 1&ndash;5)</td></tr>
    <tr><td><a href="https://docs.python.org/3/tutorial/" target="_blank" rel="noopener">The Python Tutorial (docs.python.org)</a></td><td>Official Python 3 tutorial &mdash; ideal for filling gaps on language semantics</td></tr>
    <tr><td><a href="https://docs.python.org/3/library/" target="_blank" rel="noopener">The Python Standard Library</a></td><td>Reference for <code>math</code>, <code>random</code>, <code>os</code>, <code>datetime</code>, <code>calendar</code>, <code>platform</code>, etc.</td></tr>
    <tr><td><a href="https://pythoninstitute.org/pcap-practice-test" target="_blank" rel="noopener">Official PCAP practice test</a></td><td>Sample questions reflecting the exam's format and difficulty</td></tr>
    <tr><td>This course's Final Exam &mdash; <em>PCAP-31-03 Practice (50 Questions)</em></td><td>Simulates the exam style across all five modules</td></tr>
  </tbody>
</table>

<h3>How this course is structured</h3>
<ol>
  <li><strong>About</strong> (this page) &mdash; exam outline and study plan</li>
  <li><strong>Intro video</strong> &mdash; quick overview of the certification</li>
  <li><strong>First task</strong> &mdash; verify your Python environment</li>
  <li><strong>Lessons 3&ndash;8</strong> &mdash; one lesson per PCAP-31-03 module, each followed by an 8-question quiz</li>
  <li><strong>Final Exam</strong> &mdash; a 50-question, exam-style practice test covering all five modules</li>
</ol>
"""

with app.app_context():
    L = db.session.get(Lesson, 1)
    print('Before:', L.title, 'content_len=', len(L.content or ''))
    L.content = HTML.strip()
    db.session.commit()
    print('After:', L.title, 'content_len=', len(L.content))
