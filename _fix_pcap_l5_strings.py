"""Rebuild PCAP L5 Strings (order=8) lesson + quiz with inline content."""
from app import app, db, Lesson, Quiz, Question, QuestionOption, QuestionResponse, QuestionResponseOption

LESSON_HTML = """
<h2>Lesson 5: Strings</h2>
<p>The <strong>Strings</strong> module of the PCAP-31-03 exam carries an 18% weight. You are expected to understand how Python represents textual data, how to manipulate strings as <em>immutable sequences</em>, how to format output, and how to compare and sort strings reliably.</p>

<h3>Character encoding fundamentals</h3>
<p>Internally Python 3 strings are sequences of <strong>Unicode code points</strong>. The original ASCII standard covers code points 0&ndash;127 (basic Latin letters, digits, common punctuation, and control characters). <strong>Unicode</strong> extends the address space to over 1.1 million code points, and <strong>UTF-8</strong> is the most common variable-length byte encoding used to store Unicode on disk and on the network.</p>
<ul>
  <li><code>ord(c)</code> returns the integer code point of a single-character string <code>c</code>.</li>
  <li><code>chr(n)</code> is the inverse: it returns the one-character string whose code point is the integer <code>n</code>.</li>
  <li>Note that <code>'A'</code> is <code>65</code>, <code>'a'</code> is <code>97</code>, <code>'0'</code> is <code>48</code>.</li>
</ul>
<pre><code>print(ord('A'), ord('a'), ord('0'))   # 65 97 48
print(chr(65) + chr(97) + chr(48))    # 'Aa0'</code></pre>

<h3>Strings as immutable sequences</h3>
<p>A Python string supports all sequence operations &mdash; indexing, slicing, concatenation (<code>+</code>), repetition (<code>*</code>), membership (<code>in</code>), iteration, and the built-in <code>len()</code> &mdash; but it cannot be modified in place. Any operation that "changes" a string actually creates a new one.</p>
<pre><code>s = "abcdef"
print(s[0])     # 'a'  (indexing)
print(s[-1])    # 'f'  (negative indexing)
print(s[1:4])   # 'bcd' (slice: start inclusive, stop exclusive)
print(s[::2])   # 'ace' (step)
print(s[::-1])  # 'fedcba' (reverse)
print('c' in s) # True
print(len(s))   # 6
# s[0] = 'X'   # TypeError: 'str' object does not support item assignment</code></pre>

<h3>Comparing strings</h3>
<p>Comparison uses <strong>lexicographic order</strong> based on Unicode code points, character by character. Because uppercase letters have lower code points than lowercase letters, <code>'Z' &lt; 'a'</code> is True.</p>
<pre><code>print('apple' &lt; 'banana')  # True
print('Z' &lt; 'a')             # True  (90 &lt; 97)
print('10' &lt; '9')            # True  (string comparison, NOT numeric)
print(sorted(['banana', 'Apple', 'cherry']))  # ['Apple', 'banana', 'cherry']</code></pre>

<h3>Common string methods</h3>
<table class="table">
  <thead><tr><th>Method</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td><code>upper()</code> / <code>lower()</code></td><td>Return uppercase / lowercase copy</td></tr>
    <tr><td><code>title()</code></td><td>Capitalize the first letter of each word</td></tr>
    <tr><td><code>capitalize()</code></td><td>Uppercase first character; lowercase the rest</td></tr>
    <tr><td><code>swapcase()</code></td><td>Swap case of every letter</td></tr>
    <tr><td><code>strip()</code> / <code>lstrip()</code> / <code>rstrip()</code></td><td>Remove leading/trailing whitespace (or supplied chars)</td></tr>
    <tr><td><code>split(sep)</code></td><td>Split into a list; default separator is any run of whitespace</td></tr>
    <tr><td><code>join(iterable)</code></td><td>Concatenate strings from an iterable using the called-upon string as separator</td></tr>
    <tr><td><code>replace(old, new)</code></td><td>Return copy with all <code>old</code> replaced by <code>new</code></td></tr>
    <tr><td><code>find(sub)</code> / <code>index(sub)</code></td><td>Locate <code>sub</code>; <code>find</code> returns <code>-1</code> if missing, <code>index</code> raises <code>ValueError</code></td></tr>
    <tr><td><code>startswith(p)</code> / <code>endswith(p)</code></td><td>Boolean prefix / suffix test</td></tr>
    <tr><td><code>count(sub)</code></td><td>Number of non-overlapping occurrences</td></tr>
    <tr><td><code>isalpha()</code> / <code>isdigit()</code> / <code>isalnum()</code></td><td>True only if the string is non-empty AND every character matches the predicate</td></tr>
  </tbody>
</table>

<pre><code>print("  Hello, World!  ".strip())       # 'Hello, World!'
print("a,b,,c".split(","))                # ['a', 'b', '', 'c']
print("-".join(["2025", "05", "20"]))    # '2025-05-20'
print("banana".count("a"))                 # 3
print("abc".isalpha(), "abc123".isalnum()) # True True
print("".isalpha())                         # False  (empty string)</code></pre>

<h3>Formatting output</h3>
<p>Python supports three primary ways to produce formatted strings:</p>
<ol>
  <li>Old-style <code>%</code> formatting (C-like): <code>"%d apples, %.2f kg" % (3, 1.5)</code></li>
  <li><code>str.format()</code> with positional / keyword placeholders</li>
  <li><strong>f-strings</strong> (Python 3.6+) with embedded expressions inside <code>{}</code></li>
</ol>
<pre><code>name, score = "Ann", 92.5
print("%-10s %6.2f" % (name, score))         # 'Ann            92.50'
print("{0:&lt;10} {1:&gt;6.2f}".format(name, score)) # 'Ann             92.50'
print(f"{name:&lt;10} {score:&gt;6.2f}")             # 'Ann             92.50'
print(f"{score:.0%}")                            # '9250%' (decimal interpreted as fraction-of-1: 92.5 == 9250%)
print(f"{0.925:.0%}")                            # '92%'</code></pre>

<h3>Sorting strings and lists of strings</h3>
<p>Use <code>sorted(iterable, key=..., reverse=...)</code> to return a new list, or <code>list.sort(...)</code> to sort in place. To sort case-insensitively, pass a <code>key</code> function such as <code>str.lower</code>.</p>
<pre><code>words = ["banana", "Apple", "cherry"]
print(sorted(words))                  # ['Apple', 'banana', 'cherry']   (uppercase comes first)
print(sorted(words, key=str.lower))   # ['Apple', 'banana', 'cherry']   (case-insensitive)
print(sorted(words, reverse=True))    # ['cherry', 'banana', 'Apple']
print(sorted("dcba"))                  # ['a', 'b', 'c', 'd']</code></pre>

<h3>Iteration and the <code>bytes</code> / <code>bytearray</code> companions</h3>
<p>Iterating over a string yields one-character strings. Iterating over a <code>bytes</code> or <code>bytearray</code> object yields <strong>integers</strong> (the byte values), not single-character strings.</p>
<pre><code>for ch in "ab":
    print(ch)        # 'a' then 'b'

for b in b"ab":
    print(b)         # 97 then 98</code></pre>

<h3>What to study next</h3>
<ul>
  <li>Practice slice expressions with start/stop/step (including negatives).</li>
  <li>Memorize which methods return a new string versus a list (e.g. <code>split</code> returns a list; <code>join</code> returns a string).</li>
  <li>Try every format-spec mini-language token: width, precision, alignment (<code>&lt;</code>, <code>&gt;</code>, <code>^</code>), fill, sign, type (<code>d</code>, <code>f</code>, <code>e</code>, <code>x</code>, <code>b</code>, <code>%</code>).</li>
</ul>
""".strip()

QUESTIONS = [
    (
        "<p>What is the output of the following code?</p><pre><code>s = \"abcdef\"\nprint(s[1:4])</code></pre>",
        [
            ("abc", False),
            ("bcd", True),
            ("bcde", False),
            ("cde", False),
        ],
        "A slice s[1:4] starts at index 1 (inclusive) and stops at index 4 (exclusive), so it returns the characters at indices 1, 2, and 3 — 'b', 'c', 'd' — which is 'bcd'.",
    ),
    (
        "<p>Given <code>ord('A') == 65</code>, what is the value of <code>ord('a') - ord('A')</code>?</p>",
        [
            ("26", False),
            ("32", True),
            ("33", False),
            ("65", False),
        ],
        "In ASCII (and Unicode), lowercase letters start at code point 97 ('a') and uppercase letters start at 65 ('A'). 97 - 65 = 32, the constant offset between lowercase and uppercase letters.",
    ),
    (
        "<p>What is the output of the following code?</p><pre><code>print(sorted([\"banana\", \"Apple\", \"cherry\"]))</code></pre>",
        [
            ("['Apple', 'banana', 'cherry']", True),
            ("['apple', 'banana', 'cherry']", False),
            ("['banana', 'Apple', 'cherry']", False),
            ("['cherry', 'banana', 'Apple']", False),
        ],
        "sorted() compares strings lexicographically by Unicode code point. Uppercase letters (A=65) come before lowercase letters (a=97), so 'Apple' sorts before 'banana' and 'cherry'.",
    ),
    (
        "<p>What is the output of the following code?</p><pre><code>s = \"  hello  world  \"\nprint(s.strip().split())</code></pre>",
        [
            ("['  hello', 'world  ']", False),
            ("['hello', 'world']", True),
            ("['hello  world']", False),
            ("['hello', '', 'world']", False),
        ],
        "strip() removes leading and trailing whitespace, giving 'hello  world'. split() with no argument splits on any run of whitespace (treating consecutive spaces as one separator) and produces ['hello', 'world'] — no empty string between them.",
    ),
    (
        "<p>What is the output of the following code?</p><pre><code>print(\"-\".join([\"2025\", \"05\", \"20\"]))</code></pre>",
        [
            ("'2025 05 20'", False),
            ("'2025-05-20'", True),
            ("'-2025-05-20-'", False),
            ("TypeError", False),
        ],
        "str.join(iterable) returns a single string formed by concatenating the elements of the iterable, with the calling string ('-') inserted between (NOT around) each pair, producing '2025-05-20'.",
    ),
    (
        "<p>What is the output of the following code?</p><pre><code>print(\"banana\".count(\"a\"))</code></pre>",
        [
            ("1", False),
            ("2", False),
            ("3", True),
            ("4", False),
        ],
        "str.count(sub) returns the number of non-overlapping occurrences of sub in the string. 'banana' contains three 'a' characters (positions 1, 3, 5).",
    ),
    (
        "<p>What does the following expression evaluate to?</p><pre><code>\"\".isalpha()</code></pre>",
        [
            ("True", False),
            ("False", True),
            ("None", False),
            ("Raises a ValueError", False),
        ],
        "isalpha() (and the related isdigit / isalnum predicates) require the string to be non-empty AND have every character match the predicate. An empty string fails the non-empty requirement, so it returns False.",
    ),
    (
        "<p>What does the following f-string print?</p><pre><code>value = 0.0875\nprint(f\"{value:.1%}\")</code></pre>",
        [
            ("'0.1%'", False),
            ("'8.8%'", True),
            ("'0.0875%'", False),
            ("'87.5%'", False),
        ],
        "The percent format type ('%') multiplies the value by 100 and appends a percent sign. The precision .1 keeps one digit after the decimal point, so 0.0875 * 100 = 8.75, rounded to '8.8%'.",
    ),
]

with app.app_context():
    lesson = Lesson.query.filter_by(course_id=1, order=8).first()
    exam_lesson = Lesson.query.filter_by(course_id=1, order=9).first()
    quiz = db.session.get(Quiz, exam_lesson.quiz_id)
    lesson.content = LESSON_HTML

    # Wipe responses then questions
    for q in list(quiz.questions):
        resps = QuestionResponse.query.filter_by(question_id=q.id).all()
        for r in resps:
            QuestionResponseOption.query.filter_by(response_id=r.id).delete(synchronize_session=False)
            db.session.delete(r)
    db.session.flush()
    for q in list(quiz.questions):
        db.session.delete(q)
    db.session.flush()

    for qh, opts, fb in QUESTIONS:
        q = Question(quiz_id=quiz.id, question_type='multiple_choice', question_html=qh, points=1.0, feedback=fb)
        db.session.add(q)
        db.session.flush()
        for i, (oh, ic) in enumerate(opts):
            db.session.add(QuestionOption(question_id=q.id, option_html=oh, is_correct=ic, order=i))
    db.session.commit()
    print(f'L8 OK lesson_id={lesson.id} content_len={len(LESSON_HTML)} quiz#{quiz.id} qs={len(QUESTIONS)}')
