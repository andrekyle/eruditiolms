"""Author Lesson 8 (Handling Exceptions) + its quiz for the Java OCA course."""
from app import app, db, Course, Lesson, Quiz, Question, QuestionOption

COURSE_TITLE_LIKE = '%1Z0-808%'
LESSON_TITLE = 'Lesson 8: Handling Exceptions'
QUIZ_TITLE = 'Lesson 8 Quiz — Handling Exceptions'
EXAM_LESSON_TITLE = 'Lesson 8 Quiz — Handling Exceptions'

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
  .lsn-fig{margin:22px auto;max-width:620px;text-align:center;}
  .lsn-fig svg{max-width:100%;height:auto;display:block;margin:0 auto;}
  .lsn-cap{font-size:.9rem;color:#6B6B6B;margin-top:6px;}
</style>

<p class="lsn-p">An <strong>exception</strong> is an object that represents an abnormal condition. Throwing one interrupts the normal flow of the program and starts looking, frame by frame up the call stack, for code prepared to handle it. Java's exception model decides at compile time which exceptions you must acknowledge and gives you a single language construct &mdash; <code>try/catch/finally</code> &mdash; to recover safely.</p>

<div class="lsn-callout"><strong>Learning objectives.</strong> By the end of this lesson you should be able to: differentiate between checked and unchecked exceptions and errors; describe the advantages of exception handling; create <code>try/catch</code> blocks and determine how exceptions alter normal program flow; recognise common Java exception classes; and invoke a method that throws an exception.</div>

<h2 class="lsn-h2">1. The exception hierarchy</h2>
<figure class="lsn-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 360" role="img" aria-label="Exception hierarchy: Throwable splits into Error and Exception; Exception further splits into checked exceptions and RuntimeException">
    <defs>
      <marker id="arrEx" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" orient="auto-start-reverse">
        <path d="M0,0 L12,6 L0,12 z" fill="none" stroke="#6B6B6B" stroke-width="1.5"/>
      </marker>
    </defs>

    <!-- Boxes -->
    <g fill="rgba(127,127,127,.10)" stroke="#6B6B6B" stroke-width="1.5">
      <!-- Root -->
      <rect x="300" y="10"  width="120" height="46" rx="6"/>
      <!-- Tier 2 -->
      <rect x="80"  y="130" width="140" height="46" rx="6"/>
      <rect x="500" y="130" width="140" height="46" rx="6"/>
      <!-- Tier 3 leaves -->
      <rect x="40"  y="260" width="220" height="46" rx="6"/>
      <rect x="290" y="260" width="200" height="46" rx="6"/>
      <rect x="520" y="260" width="180" height="46" rx="6"/>
    </g>

    <!-- Class names -->
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="14" text-anchor="middle">
      <text x="360" y="38">Throwable</text>
      <text x="150" y="158">Error</text>
      <text x="570" y="158">Exception</text>
      <text x="150" y="282">OutOfMemoryError</text>
      <text x="390" y="282">RuntimeException</text>
      <text x="610" y="282">IOException</text>
    </g>

    <!-- Checked / unchecked labels -->
    <g fill="#6B6B6B" font-family="system-ui,sans-serif" font-size="11" text-anchor="middle">
      <text x="150" y="326">unchecked</text>
      <text x="390" y="326">unchecked</text>
      <text x="610" y="326">checked</text>
    </g>

    <!-- Inheritance arrows (subclass &rarr; superclass) -->
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <!-- Error / Exception &rarr; Throwable -->
      <line x1="150" y1="130" x2="330" y2="58"  marker-end="url(#arrEx)"/>
      <line x1="570" y1="130" x2="390" y2="58"  marker-end="url(#arrEx)"/>
      <!-- Leaves &rarr; Error / Exception -->
      <line x1="150" y1="260" x2="150" y2="180" marker-end="url(#arrEx)"/>
      <line x1="390" y1="260" x2="540" y2="180" marker-end="url(#arrEx)"/>
      <line x1="610" y1="260" x2="600" y2="180" marker-end="url(#arrEx)"/>
    </g>
  </svg>
  <div class="lsn-cap">Figure 1. <code>Throwable</code> is the root. Everything under <code>Error</code> or <code>RuntimeException</code> is <strong>unchecked</strong>; every other descendant of <code>Exception</code> is <strong>checked</strong>.</div>
</figure>

<table class="lsn-table">
  <thead><tr><th>Category</th><th>Examples</th><th>Must declare / catch?</th><th>Typical cause</th></tr></thead>
  <tbody>
    <tr><td>Checked exception</td><td><code>IOException</code>, <code>SQLException</code>, <code>FileNotFoundException</code></td><td><strong>Yes</strong> &mdash; compiler enforces it</td><td>Recoverable, environmental</td></tr>
    <tr><td>Runtime (unchecked) exception</td><td><code>NullPointerException</code>, <code>ArithmeticException</code>, <code>ArrayIndexOutOfBoundsException</code>, <code>ClassCastException</code>, <code>NumberFormatException</code>, <code>IllegalArgumentException</code></td><td>No</td><td>Programmer mistakes</td></tr>
    <tr><td>Error</td><td><code>OutOfMemoryError</code>, <code>StackOverflowError</code></td><td>No</td><td>JVM problems &mdash; not meant to be caught</td></tr>
  </tbody>
</table>

<h2 class="lsn-h2">2. <code>try</code> / <code>catch</code> / <code>finally</code></h2>
<pre><code>try {
    risky();                 // may throw
} catch (IOException e) {    // handle one specific kind
    log(e);
} catch (RuntimeException e) {
    log(e);
} finally {
    cleanup();               // ALWAYS runs (except System.exit / JVM crash)
}
</code></pre>
<ul class="lsn-ul">
  <li>A <code>try</code> needs at least one <code>catch</code> or one <code>finally</code> &mdash; not both required.</li>
  <li><code>catch</code> blocks are tried <em>in order</em>; the first one whose declared type matches the thrown exception wins.</li>
  <li>You may <strong>not</strong> list a broader exception type before a narrower one &mdash; the narrower <code>catch</code> would be unreachable and the code will not compile.</li>
  <li><code>finally</code> runs even if the <code>try</code> or a <code>catch</code> uses <code>return</code>, <code>break</code> or throws.</li>
</ul>

<div class="lsn-warn"><strong>Pitfall.</strong> A <code>return</code> in <code>finally</code> overrides any return or exception from <code>try</code>/<code>catch</code> &mdash; the original exception is silently swallowed. Avoid it.</div>

<h2 class="lsn-h2">3. How an exception travels</h2>
<figure class="lsn-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 240" role="img" aria-label="Exception propagation up the call stack until a matching catch handles it">
    <defs>
      <marker id="arrFlow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="#6B6B6B"/>
      </marker>
    </defs>
    <g fill="rgba(127,127,127,.10)" stroke="#6B6B6B" stroke-width="1.5">
      <rect x="40"  y="40"  width="140" height="50" rx="6"/>
      <rect x="40"  y="120" width="140" height="50" rx="6"/>
      <rect x="40"  y="180" width="140" height="50" rx="6"/>
      <rect x="320" y="120" width="200" height="50" rx="6" fill="rgba(127,127,127,.18)"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="13" text-anchor="middle">
      <text x="110" y="68">main()</text>
      <text x="110" y="148">load()</text>
      <text x="110" y="208">parse() &mdash; throws</text>
      <text x="420" y="148">catch (IOException e)</text>
      <text x="420" y="180" font-size="11" fill="#6B6B6B">first frame that matches</text>
    </g>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <line x1="110" y1="180" x2="110" y2="172" marker-end="url(#arrFlow)"/>
      <line x1="110" y1="120" x2="110" y2="92"  marker-end="url(#arrFlow)"/>
      <line x1="180" y1="65"  x2="318" y2="140" marker-end="url(#arrFlow)"/>
    </g>
  </svg>
  <div class="lsn-cap">Figure 2. The exception unwinds from <code>parse()</code> up through <code>load()</code> and <code>main()</code> until a <code>catch</code> whose type matches accepts it. If no frame matches, the thread terminates.</div>
</figure>

<h2 class="lsn-h2">4. Multi-catch</h2>
<pre><code>try {
    risky();
} catch (IOException | SQLException e) {     // one block, several types
    log(e);
    // e is implicitly final &mdash; cannot reassign
}
</code></pre>
<ul class="lsn-ul">
  <li>The listed types may <strong>not</strong> be in a parent/child relationship with each other (e.g. <code>IOException | Exception</code> is illegal).</li>
  <li>The variable's compile-time type is the common supertype of the listed exceptions.</li>
</ul>

<h2 class="lsn-h2">5. Declaring vs handling: the <code>throws</code> clause</h2>
<pre><code>void load(String path) throws IOException {
    Files.readAllLines(Paths.get(path));     // declares IOException &mdash; we re-declare
}
</code></pre>
<ul class="lsn-ul">
  <li>If a method may let a <strong>checked</strong> exception escape, it must declare it with <code>throws</code>.</li>
  <li>Callers must then either declare it themselves or wrap the call in <code>try/catch</code>.</li>
  <li>Unchecked exceptions (<code>RuntimeException</code> and subclasses) may be declared but are never required.</li>
  <li>An override may declare <em>fewer</em> or <em>narrower</em> checked exceptions than the parent &mdash; never broader ones.</li>
</ul>

<h2 class="lsn-h2">6. Throwing exceptions of your own</h2>
<pre><code>public Account withdraw(int amount) {
    if (amount &lt; 0)        throw new IllegalArgumentException("negative");
    if (amount &gt; balance)  throw new IllegalStateException("insufficient funds");
    balance -= amount;
    return this;
}
</code></pre>
<ul class="lsn-ul">
  <li><code>throw</code> (verb) actually throws an instance; <code>throws</code> (noun-ish, in the signature) only declares the possibility.</li>
  <li>Throwing <code>null</code> &mdash; e.g. <code>throw (RuntimeException) null;</code> &mdash; itself throws a <code>NullPointerException</code>.</li>
  <li>Prefer specific standard exceptions: <code>IllegalArgumentException</code>, <code>IllegalStateException</code>, <code>NullPointerException</code>, <code>UnsupportedOperationException</code>.</li>
</ul>

<h2 class="lsn-h2">7. Common runtime exceptions &mdash; one&#x2011;line cheat sheet</h2>
<table class="lsn-table">
  <thead><tr><th>Exception</th><th>Typical trigger</th></tr></thead>
  <tbody>
    <tr><td><code>NullPointerException</code></td><td>Dereferencing a <code>null</code> reference (<code>x.field</code>, <code>x.m()</code>).</td></tr>
    <tr><td><code>ArrayIndexOutOfBoundsException</code></td><td>Array index <code>&lt; 0</code> or <code>&gt;= length</code>.</td></tr>
    <tr><td><code>StringIndexOutOfBoundsException</code></td><td>Same idea for <code>String.charAt</code>, <code>substring</code>&hellip;</td></tr>
    <tr><td><code>ClassCastException</code></td><td>Invalid downcast (<code>(Dog) someCatRef</code>).</td></tr>
    <tr><td><code>ArithmeticException</code></td><td>Integer division or remainder by zero.</td></tr>
    <tr><td><code>NumberFormatException</code></td><td><code>Integer.parseInt("abc")</code>.</td></tr>
    <tr><td><code>IllegalArgumentException</code></td><td>Method received an argument it cannot accept.</td></tr>
  </tbody>
</table>

<h2 class="lsn-h2">8. Summary</h2>
<ul class="lsn-ul">
  <li>Checked exceptions must be <em>handled or declared</em>; unchecked exceptions (<code>RuntimeException</code>, <code>Error</code>) need not be.</li>
  <li>A <code>try</code> needs a <code>catch</code> or a <code>finally</code> (or both); list catches narrowest first.</li>
  <li><code>finally</code> always runs &mdash; avoid <code>return</code> inside it.</li>
  <li>Multi-catch (<code>A | B</code>) requires unrelated types; the variable is implicitly final.</li>
  <li>An overriding method may narrow but not broaden the parent's checked-exception list.</li>
  <li><code>throw</code> hurls an instance, <code>throws</code> advertises the possibility.</li>
</ul>
"""

QUESTIONS = [
    (
        'multiple_choice',
        'Which of these is a <strong>checked</strong> exception?',
        [
            ('<code>IOException</code>', True),
            ('<code>NullPointerException</code>', False),
            ('<code>ArithmeticException</code>', False),
            ('<code>ClassCastException</code>', False),
        ],
        'Everything under <code>RuntimeException</code> (and under <code>Error</code>) is unchecked. <code>IOException</code> extends <code>Exception</code> directly, so it is checked and must be handled or declared.'
    ),
    (
        'multiple_choice',
        'Why will this code <strong>fail to compile</strong>?<br><pre><code>try { risky(); }\ncatch (Exception e) { /* ... */ }\ncatch (IOException e) { /* ... */ }</code></pre>',
        [
            ('The second <code>catch</code> is unreachable &mdash; a broader type must come after the narrower one.', True),
            ('Two <code>catch</code> blocks for one <code>try</code> are not allowed.', False),
            ('<code>Exception</code> may not be caught directly.', False),
            ('The <code>try</code> must have a <code>finally</code> block.', False),
        ],
        'The compiler refuses an unreachable <code>catch</code>. <code>IOException</code> is a subtype of <code>Exception</code>, so the first <code>catch</code> already swallows it; swap the order or merge them with multi-catch.'
    ),
    (
        'true_false',
        'A <code>try</code> block must have at least one <code>catch</code> clause.',
        [
            ('False', True),
            ('True', False),
        ],
        'A <code>try</code> only needs at least one of <code>catch</code> or <code>finally</code>. A bare <code>try { } finally { }</code> is perfectly legal.'
    ),
    (
        'multiple_choice',
        'What is printed?<br><pre><code>static int f() {\n    try { return 1; }\n    finally { return 2; }\n}\nSystem.out.println(f());</code></pre>',
        [
            ('<code>2</code>', True),
            ('<code>1</code>', False),
            ('Throws an exception.', False),
            ('Does not compile.', False),
        ],
        'A <code>return</code> in <code>finally</code> replaces the value returned from <code>try</code>. This is exactly why a <code>return</code> in <code>finally</code> is considered a smell.'
    ),
    (
        'multiple_choice',
        'Which multi-catch clause is <strong>illegal</strong>?',
        [
            ('<code>catch (IOException | Exception e)</code>', True),
            ('<code>catch (IOException | SQLException e)</code>', False),
            ('<code>catch (FileNotFoundException | ArithmeticException e)</code>', False),
            ('<code>catch (IllegalArgumentException | NullPointerException e)</code>', False),
        ],
        'The listed types in a multi-catch must not be in a subtype relationship with one another. <code>IOException</code> is already a subtype of <code>Exception</code>, so listing both is redundant and a compile-time error.'
    ),
    (
        'multiple_choice',
        'A parent class declares <code>void m() throws IOException</code>. Which override compiles?',
        [
            ('<code>void m() throws FileNotFoundException</code>', True),
            ('<code>void m() throws Exception</code>', False),
            ('<code>void m() throws IOException, SQLException</code>', False),
            ('<code>void m() throws Throwable</code>', False),
        ],
        'An override may declare <em>fewer</em> or <em>narrower</em> checked exceptions, never broader ones. <code>FileNotFoundException</code> is a subtype of <code>IOException</code>, so it is allowed.'
    ),
    (
        'multiple_choice',
        'What kind of exception does <code>Integer.parseInt("12a")</code> throw?',
        [
            ('<code>NumberFormatException</code> (unchecked)', True),
            ('<code>IOException</code> (checked)', False),
            ('<code>IllegalStateException</code> (unchecked)', False),
            ('It returns <code>0</code> rather than throwing.', False),
        ],
        '<code>Integer.parseInt</code> throws <code>NumberFormatException</code> when the input is not a parseable integer; it is a subclass of <code>IllegalArgumentException</code> and is unchecked.'
    ),
    (
        'multiple_choice',
        'What does this method print when called?<br><pre><code>static void g() {\n    try {\n        System.out.print("A");\n        throw new RuntimeException();\n    } catch (RuntimeException e) {\n        System.out.print("B");\n        return;\n    } finally {\n        System.out.print("C");\n    }\n}</code></pre>',
        [
            ('<code>ABC</code>', True),
            ('<code>AB</code>', False),
            ('<code>ACB</code>', False),
            ('<code>AC</code>', False),
        ],
        'The <code>try</code> prints <code>A</code> and throws; the <code>catch</code> prints <code>B</code>; the <code>return</code> is queued; the <code>finally</code> runs and prints <code>C</code>; then control returns.'
    ),
]


def upsert():
    with app.app_context():
        course = Course.query.filter(Course.title.like(COURSE_TITLE_LIKE)).first()
        if not course:
            print('Java course not found.')
            return

        lesson = Lesson.query.filter_by(course_id=course.id, title=LESSON_TITLE).first()
        if lesson:
            lesson.content = LESSON_HTML
            lesson.content_type = 'lesson'
            print(f'updated lesson {lesson.id}')
        else:
            lesson = Lesson(
                title=LESSON_TITLE,
                content=LESSON_HTML,
                course_id=course.id,
                content_type='lesson',
                order=16,
                points=1.0,
            )
            db.session.add(lesson)
            db.session.flush()
            print(f'inserted lesson {lesson.id}')

        quiz = Quiz.query.filter_by(course_id=course.id, title=QUIZ_TITLE).first()
        if not quiz:
            quiz = Quiz(course_id=course.id, title=QUIZ_TITLE,
                        description='Check your understanding of checked vs unchecked exceptions, try/catch/finally, multi-catch, throws and common runtime exceptions.')
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

        exam = Lesson.query.filter_by(course_id=course.id, title=EXAM_LESSON_TITLE,
                                       content_type='exam').first()
        if exam:
            exam.quiz_id = quiz.id
            exam.order = 17
            print(f'updated exam lesson {exam.id}')
        else:
            exam = Lesson(
                title=EXAM_LESSON_TITLE,
                content='',
                course_id=course.id,
                content_type='exam',
                quiz_id=quiz.id,
                order=17,
                points=1.0,
            )
            db.session.add(exam)
            db.session.flush()
            print(f'inserted exam lesson {exam.id}')

        db.session.commit()
        print('done.')


if __name__ == '__main__':
    upsert()
