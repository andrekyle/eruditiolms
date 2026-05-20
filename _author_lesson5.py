"""Author Lesson 5 (Using Loop Constructs) + its quiz for the Java OCA course."""
from app import app, db, Course, Lesson, Quiz, Question, QuestionOption

COURSE_TITLE_LIKE = '%1Z0-808%'
LESSON_TITLE = 'Lesson 5: Using Loop Constructs'
QUIZ_TITLE = 'Lesson 5 Quiz — Loops'
EXAM_LESSON_TITLE = 'Lesson 5 Quiz — Loops'

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
</style>

<p class="lsn-p">Loops let you execute the same block of code many times. Java offers four loop forms &mdash; <code>while</code>, <code>do/while</code>, the classic <code>for</code> and the enhanced <code>for</code> (&ldquo;for-each&rdquo;) &mdash; together with the <code>break</code> and <code>continue</code> control-flow keywords. Choosing the right loop is mostly about <em>when</em> the condition is tested and <em>what</em> you need to iterate over.</p>

<div class="lsn-callout"><strong>Learning objectives.</strong> By the end of this lesson you should be able to: create and use <code>while</code>, <code>do/while</code>, classic <code>for</code> and enhanced <code>for</code> loops; compare the four loop constructs; and use <code>break</code> and <code>continue</code> (including labelled forms) to alter loop flow.</div>

<h2 class="lsn-h2">1. The <code>while</code> loop</h2>
<p class="lsn-p">A <code>while</code> loop tests its <code>boolean</code> condition <em>before</em> each iteration, so the body may execute zero times:</p>
<pre><code>int i = 0;
while (i &lt; 3) {
    System.out.println(i);
    i++;
}
// prints 0, 1, 2
</code></pre>

<h2 class="lsn-h2">2. The <code>do/while</code> loop</h2>
<p class="lsn-p">A <code>do/while</code> loop tests its condition <em>after</em> each iteration, so the body always executes at least once. Note the mandatory trailing semicolon:</p>
<pre><code>int n = 10;
do {
    System.out.println(n);
    n++;
} while (n &lt; 3);
// prints 10 (once), then stops
</code></pre>

<h2 class="lsn-h2">3. The classic <code>for</code> loop</h2>
<p class="lsn-p">The classic <code>for</code> packs initialization, condition and update onto one line. All three sections are optional &mdash; an empty condition is treated as <code>true</code>, producing an infinite loop:</p>
<pre><code>for (int i = 0; i &lt; 5; i++) {
    System.out.print(i + " ");
}
// 0 1 2 3 4

for (;;) {                 // infinite loop &mdash; legal
    if (Math.random() &gt; 0.99) break;
}
</code></pre>

<div class="lsn-callout">You may declare <strong>multiple variables of the same type</strong> in the initializer, and use a comma list for the update; you cannot mix types or use commas in the condition.</div>
<pre><code>for (int a = 0, b = 10; a &lt; b; a++, b--) {
    System.out.println(a + " " + b);
}
</code></pre>

<h2 class="lsn-h2">4. The enhanced <code>for</code> (&ldquo;for-each&rdquo;)</h2>
<p class="lsn-p">The enhanced <code>for</code> reads each element of an array or anything that implements <code>Iterable</code>. You give up the index in exchange for cleaner code:</p>
<pre><code>String[] names = {"Ada", "Linus", "Grace"};
for (String name : names) {
    System.out.println(name);
}
</code></pre>

<div class="lsn-warn"><strong>Common trap.</strong> Reassigning the loop variable inside an enhanced <code>for</code> does <em>not</em> change the underlying element. For primitives you hold a copy of the value; for objects you hold a copy of the reference.</div>

<h2 class="lsn-h2">5. Comparing the four loop constructs</h2>
<table class="lsn-table">
  <thead><tr><th>Loop</th><th>When the condition is tested</th><th>Best for</th></tr></thead>
  <tbody>
    <tr><td><code>while</code></td><td>Before each iteration</td><td>Repeat while some external condition holds; body may run zero times.</td></tr>
    <tr><td><code>do/while</code></td><td>After each iteration</td><td>Always run the body at least once (menu prompts, input validation).</td></tr>
    <tr><td>Classic <code>for</code></td><td>Before each iteration</td><td>Counted iteration where you need the index.</td></tr>
    <tr><td>Enhanced <code>for</code></td><td>Before each iteration</td><td>Walking every element of an array or <code>Iterable</code> when you do not need the index.</td></tr>
  </tbody>
</table>

<h2 class="lsn-h2">6. <code>break</code> and <code>continue</code></h2>
<p class="lsn-p"><code>break</code> exits the nearest enclosing loop (or <code>switch</code>). <code>continue</code> skips the rest of the current iteration and jumps to the next test (and to the update section, for a classic <code>for</code>):</p>
<pre><code>for (int i = 0; i &lt; 10; i++) {
    if (i == 3) continue;       // skip 3
    if (i == 7) break;          // stop at 7
    System.out.print(i + " ");
}
// prints: 0 1 2 4 5 6
</code></pre>

<h2 class="lsn-h2">7. Labelled <code>break</code> and <code>continue</code></h2>
<p class="lsn-p">With nested loops, an unlabelled <code>break</code>/<code>continue</code> only affects the innermost loop. A label lets you target an outer loop:</p>
<pre><code>outer:
for (int r = 0; r &lt; 3; r++) {
    for (int c = 0; c &lt; 3; c++) {
        if (r == 1 &amp;&amp; c == 1) break outer;   // exits BOTH loops
        System.out.println(r + "," + c);
    }
}
</code></pre>

<h2 class="lsn-h2">8. Common pitfalls</h2>
<ul class="lsn-ul">
  <li>Forgetting the semicolon after <code>do { ... } while (cond);</code> &mdash; compile error.</li>
  <li>Off-by-one errors: <code>i &lt;= a.length</code> is one step too far; use <code>i &lt; a.length</code>.</li>
  <li>Modifying the array size inside an enhanced <code>for</code> over a <code>Collection</code> throws <code>ConcurrentModificationException</code>.</li>
  <li>An empty <code>for(;;)</code> is an infinite loop &mdash; you must <code>break</code> out.</li>
  <li>A condition that is a compile-time constant <code>false</code> (e.g. <code>while(false)</code>) is a compile-time error; the body would be unreachable.</li>
</ul>

<h2 class="lsn-h2">9. Summary</h2>
<ul class="lsn-ul">
  <li><code>while</code> and the two <code>for</code> forms test <strong>before</strong> the body; <code>do/while</code> tests <strong>after</strong>.</li>
  <li>The classic <code>for</code> can declare multiple variables of one type and run multiple update expressions.</li>
  <li>The enhanced <code>for</code> hides the index; reassigning the loop variable has no effect on the source.</li>
  <li><code>break</code> exits a loop; <code>continue</code> skips to the next iteration. Labels let either keyword target an outer loop.</li>
</ul>
"""

QUESTIONS = [
    (
        'multiple_choice',
        'Which loop is guaranteed to execute its body <strong>at least once</strong>?',
        [
            ('<code>do/while</code>', True),
            ('<code>while</code>', False),
            ('Classic <code>for</code>', False),
            ('Enhanced <code>for</code>', False),
        ],
        'Only <code>do/while</code> tests the condition after the first iteration, so the body always runs at least once.'
    ),
    (
        'multiple_choice',
        'How many times does this loop print?<br><pre><code>int n = 10;\ndo {\n    System.out.println(n);\n    n++;\n} while (n &lt; 3);</code></pre>',
        [
            ('Once', True),
            ('Zero times', False),
            ('Three times', False),
            ('It does not compile', False),
        ],
        'The body runs first, prints 10, then the condition <code>11 &lt; 3</code> is false and the loop ends.'
    ),
    (
        'multiple_choice',
        'Which of the following <code>for</code> headers <strong>compile</strong>?',
        [
            ('<code>for (int i = 0, j = 10; i &lt; j; i++, j--)</code>', True),
            ('<code>for ( ; ; )</code>', True),
            ('<code>for (int i = 0, double d = 0.0; i &lt; 5; i++)</code>', False),
            ('<code>for (int i = 0; i &lt; 5, i &gt; -1; i++)</code>', False),
        ],
        'The init section may declare multiple variables of the <em>same</em> type; the condition must be a single <code>boolean</code> expression. Empty sections are legal.'
    ),
    (
        'multiple_choice',
        'What does this loop print?<br><pre><code>for (int i = 0; i &lt; 6; i++) {\n    if (i == 2) continue;\n    if (i == 4) break;\n    System.out.print(i + " ");\n}</code></pre>',
        [
            ('<code>0 1 3</code>', True),
            ('<code>0 1 2 3</code>', False),
            ('<code>0 1 3 5</code>', False),
            ('<code>0 1 3 4</code>', False),
        ],
        '<code>continue</code> skips printing when i is 2; <code>break</code> exits before printing when i is 4. So 0, 1, 3 are printed.'
    ),
    (
        'true_false',
        'In an enhanced <code>for</code> loop over an <code>int[]</code>, reassigning the loop variable updates the corresponding element of the array.',
        [
            ('False', True),
            ('True', False),
        ],
        'The loop variable holds a copy of the primitive value (or a copy of the reference). Reassigning it does not change the source.'
    ),
    (
        'multiple_choice',
        'Which statement about <code>break</code> and <code>continue</code> is <strong>correct</strong>?',
        [
            ('A labelled <code>break</code> can exit an outer enclosing loop in one step.', True),
            ('<code>continue</code> exits the loop entirely.', False),
            ('<code>break</code> is only legal inside a <code>switch</code>.', False),
            ('Labels are required on every loop.', False),
        ],
        'A label placed before a loop lets <code>break label;</code> or <code>continue label;</code> target that specific (outer) loop.'
    ),
    (
        'multiple_choice',
        'Why does this line fail to compile?<br><pre><code>while (false) { System.out.println("x"); }</code></pre>',
        [
            ('The condition is a compile-time constant <code>false</code>, so the body is unreachable.', True),
            ('You must use <code>do/while</code> when the condition is <code>false</code>.', False),
            ('A <code>while</code> condition cannot be a literal.', False),
            ('It compiles; the body simply never runs.', False),
        ],
        'Java forbids unreachable statements. A constant-<code>false</code> <code>while</code> makes its body unreachable, which is a compile-time error. (Note: <code>if (false)</code> is allowed.)'
    ),
    (
        'multiple_choice',
        'What is printed?<br><pre><code>outer:\nfor (int r = 0; r &lt; 3; r++) {\n    for (int c = 0; c &lt; 3; c++) {\n        if (c == 1) continue outer;\n        System.out.print(r + "" + c + " ");\n    }\n}</code></pre>',
        [
            ('<code>00 10 20</code>', True),
            ('<code>00 01 10 11 20 21</code>', False),
            ('<code>00 10 20 01 11 21</code>', False),
            ('Nothing &mdash; it does not compile', False),
        ],
        'For each row, column 0 prints and then <code>continue outer</code> skips straight to the next row, so only 00, 10, 20 appear.'
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
                order=10,
                points=1.0,
            )
            db.session.add(lesson)
            db.session.flush()
            print(f'inserted lesson {lesson.id}')

        quiz = Quiz.query.filter_by(course_id=course.id, title=QUIZ_TITLE).first()
        if not quiz:
            quiz = Quiz(course_id=course.id, title=QUIZ_TITLE,
                        description='Check your understanding of Java loops and flow-control keywords.')
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
            exam.order = 11
            print(f'updated exam lesson {exam.id}')
        else:
            exam = Lesson(
                title=EXAM_LESSON_TITLE,
                content='',
                course_id=course.id,
                content_type='exam',
                quiz_id=quiz.id,
                order=11,
                points=1.0,
            )
            db.session.add(exam)
            db.session.flush()
            print(f'inserted exam lesson {exam.id}')

        db.session.commit()
        print('done.')


if __name__ == '__main__':
    upsert()
