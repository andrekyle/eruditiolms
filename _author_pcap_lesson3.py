"""Author PCAP Lesson 3 (Variables, Data Types and Operators) + its quiz, and
bump the existing 'Lesson 3: Exam' to 'Lesson 4: Final Exam'. Idempotent."""
from app import app, db, Course, Lesson, Quiz, Question, QuestionOption

COURSE_TITLE_LIKE = 'PCAP%'
LESSON_TITLE = 'Lesson 3: Variables, Data Types and Operators'
QUIZ_TITLE = 'Lesson 3 Quiz \u2014 Variables, Data Types and Operators'
EXAM_LESSON_TITLE = 'Lesson 3 Quiz \u2014 Variables, Data Types and Operators'
OLD_FINAL_TITLE = 'Lesson 3: Exam'
NEW_FINAL_TITLE = 'Lesson 4: Final Exam'

LESSON_HTML = """
<style>
  .lsn-h2{font-size:1.5rem;font-weight:600;margin:32px 0 12px;letter-spacing:-0.005em;}
  .lsn-p{font-size:1.0625rem;line-height:1.7;margin:0 0 14px;}
  .lsn-ul{font-size:1.0625rem;line-height:1.7;margin:0 0 18px 1.25rem;padding:0;}
  .lsn-callout{background:rgba(127,127,127,.10);padding:14px 18px;border-radius:6px;margin:18px 0;}
  .lsn-warn{background:rgba(127,127,127,.14);padding:14px 18px;border-radius:6px;margin:18px 0;}
  .lsn-table{width:100%;border-collapse:collapse;margin:14px 0 22px;font-size:1rem;}
  .lsn-table th,.lsn-table td{border:1px solid rgba(127,127,127,.35);padding:10px 12px;text-align:left;vertical-align:top;}
  .lsn-table th{background:rgba(127,127,127,.10);font-weight:600;}
  .lsn-fig{margin:22px auto;max-width:600px;text-align:center;}
  .lsn-fig svg{max-width:100%;height:auto;display:block;margin:0 auto;}
  .lsn-cap{font-size:.9rem;color:#6B6B6B;margin-top:6px;}
</style>

<p class="lsn-p">In Python everything is an <strong>object</strong>, and a <strong>variable</strong> is just a name bound to one of those objects. This lesson covers the rules that govern how names are created, the built-in data types you will meet on day one, and how Python's operators behave (including the rules the PCAP exam loves to test).</p>

<div class="lsn-callout"><strong>Learning objectives.</strong> By the end of this lesson you should be able to: name and create variables that obey Python's identifier rules; recognise Python's core built-in types and their literals; predict the result of mixed-type arithmetic; use the comparison, logical and bitwise operators correctly; and apply operator precedence and associativity without surprises.</div>

<h2 class="lsn-h2">1. Variables are references, not boxes</h2>
<p class="lsn-p">Assignment in Python binds a <em>name</em> to a value &mdash; it does <strong>not</strong> copy data into a slot.</p>
<pre><code>x = 10           # the name x now refers to the int object 10
y = x            # y refers to the SAME int object
y = y + 1        # y now refers to a NEW int object 11; x is still 10
</code></pre>

<figure class="lsn-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 200" role="img" aria-label="Two names x and y referring to integer objects">
    <defs>
      <marker id="arrRef" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="#6B6B6B"/>
      </marker>
    </defs>
    <g fill="rgba(127,127,127,.10)" stroke="#6B6B6B" stroke-width="1.5">
      <rect x="40"  y="40"  width="100" height="44" rx="6"/>
      <rect x="40"  y="120" width="100" height="44" rx="6"/>
      <rect x="320" y="30"  width="140" height="44" rx="6"/>
      <rect x="320" y="120" width="140" height="44" rx="6"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="14" text-anchor="middle">
      <text x="90"  y="66">x</text>
      <text x="90"  y="146">y</text>
      <text x="390" y="56">int  10</text>
      <text x="390" y="146">int  11</text>
    </g>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <line x1="140" y1="62"  x2="318" y2="50"  marker-end="url(#arrRef)"/>
      <line x1="140" y1="142" x2="318" y2="142" marker-end="url(#arrRef)"/>
    </g>
  </svg>
  <div class="lsn-cap">Figure 1. After <code>y = y + 1</code>, the name <code>y</code> is rebound to a fresh integer object; the original <code>10</code> is unchanged.</div>
</figure>

<h3 class="lsn-h2" style="font-size:1.15rem;">Identifier rules</h3>
<ul class="lsn-ul">
  <li>Must start with a letter or underscore; the remaining characters may be letters, digits or underscores.</li>
  <li>Are <strong>case sensitive</strong>: <code>data</code>, <code>Data</code> and <code>DATA</code> are three different names.</li>
  <li>May not be a Python <strong>keyword</strong> (<code>if</code>, <code>for</code>, <code>None</code>, <code>True</code>, <code>class</code>, &hellip;). Get the full list with <code>import keyword; keyword.kwlist</code>.</li>
  <li>By convention: <code>snake_case</code> for variables and functions, <code>UPPER_CASE</code> for constants, <code>_leading</code> for &ldquo;internal use&rdquo;.</li>
</ul>

<h2 class="lsn-h2">2. The core built-in types</h2>
<table class="lsn-table">
  <thead><tr><th>Type</th><th>Literal examples</th><th>Mutable?</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td><code>int</code></td><td><code>0</code>, <code>-12</code>, <code>0x1F</code>, <code>0b1010</code>, <code>1_000_000</code></td><td>no</td><td>Unlimited precision.</td></tr>
    <tr><td><code>float</code></td><td><code>3.14</code>, <code>2e10</code>, <code>1.0</code></td><td>no</td><td>IEEE&nbsp;754 double precision.</td></tr>
    <tr><td><code>bool</code></td><td><code>True</code>, <code>False</code></td><td>no</td><td>Subclass of <code>int</code> &mdash; <code>True == 1</code>, <code>False == 0</code>.</td></tr>
    <tr><td><code>complex</code></td><td><code>2 + 3j</code></td><td>no</td><td>Real plus imaginary part.</td></tr>
    <tr><td><code>str</code></td><td><code>"hi"</code>, <code>'a'</code>, <code>&quot;&quot;&quot;...&quot;&quot;&quot;</code></td><td>no</td><td>Sequence of Unicode code points.</td></tr>
    <tr><td><code>NoneType</code></td><td><code>None</code></td><td>n/a</td><td>The single &ldquo;no value&rdquo; sentinel.</td></tr>
  </tbody>
</table>

<div class="lsn-callout">Use <code>type(x)</code> to ask what something is and <code>isinstance(x, T)</code> to ask whether <code>x</code> is a <code>T</code> (or a subclass of it). Prefer <code>isinstance</code>.</div>

<h2 class="lsn-h2">3. Arithmetic operators</h2>
<pre><code>7 / 2     # 3.5   &mdash; true division, ALWAYS a float
7 // 2    # 3     &mdash; floor division: rounds toward minus infinity
-7 // 2   # -4    &mdash; not -3!
7 %  2    # 1     &mdash; remainder, same sign as the divisor
2 ** 10   # 1024  &mdash; exponentiation; right-associative
</code></pre>
<ul class="lsn-ul">
  <li><code>/</code> always returns a <code>float</code>, even when the result is a whole number (<code>4 / 2</code> &rarr; <code>2.0</code>).</li>
  <li><code>//</code> rounds <strong>down</strong>, not toward zero. <code>-7 // 2</code> is <code>-4</code>.</li>
  <li>Mixing <code>int</code> and <code>float</code> upgrades to <code>float</code>.</li>
  <li><code>**</code> binds tighter than unary minus on the right: <code>-2 ** 2</code> is <code>-4</code>, not <code>4</code>.</li>
</ul>

<h2 class="lsn-h2">4. Comparison and logical operators</h2>
<pre><code>1 &lt; 2 &lt; 3            # True &mdash; chained comparisons are allowed
0 == False           # True &mdash; bool is a subclass of int
"" or "fallback"     # "fallback"   &mdash; returns one of the operands, not True
"x" and 0 and 1/0    # 0            &mdash; short-circuits, never raises
not 0                # True
</code></pre>
<ul class="lsn-ul">
  <li><code>and</code> / <code>or</code> return one of their <strong>operands</strong>, not a bool. <code>x or y</code> is <code>x</code> if <code>x</code> is truthy, otherwise <code>y</code>.</li>
  <li>Both short-circuit; the right-hand side may never run.</li>
  <li><code>==</code> compares values; <code>is</code> compares identity (the same object in memory). Use <code>is</code> only with sentinels like <code>None</code>, <code>True</code>, <code>False</code>.</li>
</ul>

<h2 class="lsn-h2">5. Truthiness</h2>
<p class="lsn-p">When Python expects a boolean &mdash; an <code>if</code>, a <code>while</code>, an <code>and</code>/<code>or</code> &mdash; it asks the object for its truth value. The following values are <strong>false</strong>; everything else is <strong>true</strong>:</p>
<ul class="lsn-ul">
  <li><code>None</code> and <code>False</code></li>
  <li>Any numeric zero: <code>0</code>, <code>0.0</code>, <code>0j</code>, <code>Decimal(0)</code>, <code>Fraction(0)</code></li>
  <li>Any empty collection: <code>""</code>, <code>[]</code>, <code>()</code>, <code>{}</code>, <code>set()</code>, <code>range(0)</code></li>
</ul>

<h2 class="lsn-h2">6. Bitwise operators</h2>
<pre><code>0b1100 &amp; 0b1010   # 0b1000   (8)   &mdash; AND
0b1100 | 0b1010   # 0b1110   (14)  &mdash; OR
0b1100 ^ 0b1010   # 0b0110   (6)   &mdash; XOR
~5                # -6             &mdash; ~x == -(x + 1)
1 &lt;&lt; 4            # 16             &mdash; left shift, multiply by 2**4
20 &gt;&gt; 2           # 5              &mdash; right shift, integer divide by 2**2
</code></pre>

<h2 class="lsn-h2">7. Operator precedence (high &rarr; low)</h2>
<table class="lsn-table">
  <thead><tr><th>Tier</th><th>Operators</th><th>Associativity</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><code>**</code></td><td>right</td></tr>
    <tr><td>2</td><td>unary <code>+</code>&nbsp;<code>-</code>&nbsp;<code>~</code></td><td>right</td></tr>
    <tr><td>3</td><td><code>*</code>&nbsp;<code>/</code>&nbsp;<code>//</code>&nbsp;<code>%</code>&nbsp;<code>@</code></td><td>left</td></tr>
    <tr><td>4</td><td><code>+</code>&nbsp;<code>-</code></td><td>left</td></tr>
    <tr><td>5</td><td><code>&lt;&lt;</code>&nbsp;<code>&gt;&gt;</code></td><td>left</td></tr>
    <tr><td>6</td><td><code>&amp;</code></td><td>left</td></tr>
    <tr><td>7</td><td><code>^</code></td><td>left</td></tr>
    <tr><td>8</td><td><code>|</code></td><td>left</td></tr>
    <tr><td>9</td><td>comparisons (<code>&lt;</code>&nbsp;<code>&lt;=</code>&nbsp;<code>==</code>&nbsp;<code>!=</code>&nbsp;<code>is</code>&nbsp;<code>in</code> &hellip;)</td><td>left, chained</td></tr>
    <tr><td>10</td><td><code>not</code></td><td>right</td></tr>
    <tr><td>11</td><td><code>and</code></td><td>left</td></tr>
    <tr><td>12</td><td><code>or</code></td><td>left</td></tr>
  </tbody>
</table>

<div class="lsn-warn"><strong>Easy to forget.</strong> Comparisons sit <em>below</em> bitwise operators in precedence. <code>x &amp; 1 == 0</code> parses as <code>x &amp; (1 == 0)</code>, which is <code>x &amp; False</code>. Use parentheses: <code>(x &amp; 1) == 0</code>.</div>

<h2 class="lsn-h2">8. Conversions between types</h2>
<pre><code>int("42")        # 42
int("0b101", 2)  # 5      &mdash; second arg is the base
float("3.14")    # 3.14
str(3.14)        # "3.14"
bool(0), bool("")   # (False, False)
bool("0")            # True   &mdash; non-empty string!
</code></pre>
<p class="lsn-p"><code>int</code> and <code>float</code> raise <code>ValueError</code> on garbage input; <code>bool</code> never does.</p>

<h2 class="lsn-h2">9. Summary</h2>
<ul class="lsn-ul">
  <li>Names are references &mdash; assignment rebinds, it does not copy.</li>
  <li>Core types: <code>int</code>, <code>float</code>, <code>bool</code> (a subclass of <code>int</code>), <code>complex</code>, <code>str</code>, <code>None</code>.</li>
  <li><code>/</code> always returns a <code>float</code>; <code>//</code> floors; <code>**</code> is right-associative and binds tighter than unary minus on its right.</li>
  <li><code>and</code> / <code>or</code> short-circuit and return one of their operands; <code>==</code> tests value, <code>is</code> tests identity.</li>
  <li>Falsy values: <code>None</code>, <code>False</code>, numeric zero, empty containers; everything else is truthy.</li>
  <li>Bitwise operators sit between arithmetic and comparison in the precedence table &mdash; parenthesise when in doubt.</li>
</ul>
"""

QUESTIONS = [
    (
        'multiple_choice',
        'Which of these is <strong>not</strong> a legal Python identifier?',
        [
            ('<code>2nd_place</code>', True),
            ('<code>_private</code>', False),
            ('<code>data2</code>', False),
            ('<code>\u00e9clair</code>', False),
        ],
        'Identifiers may not <em>begin</em> with a digit. Underscores and Unicode letters are both fine, but <code>2nd_place</code> starts with <code>2</code> and so is rejected by the lexer.'
    ),
    (
        'multiple_choice',
        'What does <code>7 / 2</code> evaluate to in Python 3?',
        [
            ('<code>3.5</code> &mdash; a <code>float</code>', True),
            ('<code>3</code> &mdash; an <code>int</code>', False),
            ('<code>4</code> &mdash; rounded up', False),
            ('A <code>TypeError</code>', False),
        ],
        'In Python 3 the <code>/</code> operator always performs true division and returns a <code>float</code>. Use <code>//</code> when you want integer floor division.'
    ),
    (
        'multiple_choice',
        'What is the value of <code>-7 // 2</code>?',
        [
            ('<code>-4</code>', True),
            ('<code>-3</code>', False),
            ('<code>-3.5</code>', False),
            ('<code>3</code>', False),
        ],
        '<code>//</code> rounds toward <em>minus infinity</em>, not toward zero. <code>-3.5</code> rounds down to <code>-4</code>.'
    ),
    (
        'multiple_choice',
        'What does <code>-2 ** 2</code> evaluate to?',
        [
            ('<code>-4</code>', True),
            ('<code>4</code>', False),
            ('<code>2</code>', False),
            ('It is a syntax error.', False),
        ],
        '<code>**</code> binds tighter than the unary minus on its left, so the expression parses as <code>-(2 ** 2)</code>, which is <code>-4</code>. Use <code>(-2) ** 2</code> if you really want <code>4</code>.'
    ),
    (
        'multiple_choice',
        'What is the value of <code>"" or 0 or "fallback"</code>?',
        [
            ('<code>"fallback"</code>', True),
            ('<code>True</code>', False),
            ('<code>False</code>', False),
            ('<code>""</code>', False),
        ],
        '<code>or</code> returns the first truthy operand &mdash; or the last operand if every value is falsy. Both <code>""</code> and <code>0</code> are falsy, so the result is the third operand.'
    ),
    (
        'multiple_choice',
        'Which value is <strong>truthy</strong>?',
        [
            ('<code>"0"</code>', True),
            ('<code>0.0</code>', False),
            ('<code>[]</code>', False),
            ('<code>None</code>', False),
        ],
        'Truthiness for strings depends on <em>length</em>, not contents. <code>"0"</code> is a length-1 string, so it is truthy. Empty collections, numeric zero and <code>None</code> are all falsy.'
    ),
    (
        'multiple_choice',
        'What does this expression evaluate to?<br><pre><code>5 &amp; 1 == 0</code></pre>',
        [
            ('<code>0</code>', True),
            ('<code>True</code>', False),
            ('<code>False</code>', False),
            ('<code>1</code>', False),
        ],
        'Comparisons have <em>lower</em> precedence than bitwise operators, so this parses as <code>5 &amp; (1 == 0)</code> &rarr; <code>5 &amp; False</code> &rarr; <code>5 &amp; 0</code> &rarr; <code>0</code>. Add parentheses: <code>(5 &amp; 1) == 0</code>.'
    ),
    (
        'true_false',
        'In Python, <code>True == 1</code> evaluates to <code>True</code>.',
        [
            ('True', True),
            ('False', False),
        ],
        '<code>bool</code> is a subclass of <code>int</code>; <code>True</code> equals <code>1</code> and <code>False</code> equals <code>0</code> by both <code>==</code> and arithmetic operators. They are <em>not</em>, however, the same object as the corresponding ints under <code>is</code> &mdash; that is implementation-defined.'
    ),
]


def upsert():
    with app.app_context():
        course = Course.query.filter(Course.title.like(COURSE_TITLE_LIKE)).first()
        if not course:
            print('PCAP course not found.')
            return

        # Bump the existing final exam out of the way so the new lesson + its
        # quiz can claim orders 4 and 5.
        final = Lesson.query.filter_by(course_id=course.id, title=OLD_FINAL_TITLE).first()
        if final:
            final.title = NEW_FINAL_TITLE
            final.order = 6
            print(f'renamed/bumped final exam lesson {final.id}')
        else:
            final = Lesson.query.filter_by(course_id=course.id, title=NEW_FINAL_TITLE).first()
            if final:
                final.order = 6
                print(f'final exam lesson {final.id} already renamed')

        # New content lesson at order 4
        lesson = Lesson.query.filter_by(course_id=course.id, title=LESSON_TITLE).first()
        if lesson:
            lesson.content = LESSON_HTML
            lesson.content_type = 'lesson'
            lesson.order = 4
            print(f'updated lesson {lesson.id}')
        else:
            lesson = Lesson(
                title=LESSON_TITLE,
                content=LESSON_HTML,
                course_id=course.id,
                content_type='lesson',
                order=4,
                points=1.0,
            )
            db.session.add(lesson)
            db.session.flush()
            print(f'inserted lesson {lesson.id}')

        # Quiz
        quiz = Quiz.query.filter_by(course_id=course.id, title=QUIZ_TITLE).first()
        if not quiz:
            quiz = Quiz(course_id=course.id, title=QUIZ_TITLE,
                        description='Check your understanding of Python variables, data types, operators, truthiness and precedence.')
            db.session.add(quiz)
            db.session.flush()
            print(f'inserted quiz {quiz.id}')
        else:
            print(f'quiz {quiz.id} already exists; rebuilding questions')
            for q in list(quiz.questions):
                db.session.delete(q)
            db.session.flush()

        for qtype, qhtml, opts, feedback in QUESTIONS:
            q = Question(quiz_id=quiz.id, question_type=qtype, question_html=qhtml,
                         points=1.0, feedback=feedback)
            db.session.add(q)
            db.session.flush()
            for i, (ohtml, correct) in enumerate(opts):
                db.session.add(QuestionOption(
                    question_id=q.id, option_html=ohtml, is_correct=correct, order=i
                ))

        # Quiz-as-lesson at order 5
        exam = Lesson.query.filter_by(course_id=course.id, title=EXAM_LESSON_TITLE,
                                       content_type='exam').first()
        if exam:
            exam.quiz_id = quiz.id
            exam.order = 5
            print(f'updated exam lesson {exam.id}')
        else:
            exam = Lesson(
                title=EXAM_LESSON_TITLE,
                content='',
                course_id=course.id,
                content_type='exam',
                quiz_id=quiz.id,
                order=5,
                points=1.0,
            )
            db.session.add(exam)
            db.session.flush()
            print(f'inserted exam lesson {exam.id}')

        db.session.commit()
        print('done.')


if __name__ == '__main__':
    upsert()
