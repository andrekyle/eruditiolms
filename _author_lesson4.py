"""Author Lesson 4 (Creating and Using Arrays) + its quiz for the Java OCA course."""
from app import app, db, Course, Lesson, Quiz, Question, QuestionOption

COURSE_TITLE_LIKE = '%1Z0-808%'
LESSON_TITLE = 'Lesson 4: Creating and Using Arrays'
QUIZ_TITLE = 'Lesson 4 Quiz — Arrays'
EXAM_LESSON_TITLE = 'Lesson 4 Quiz — Arrays'

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

<p class="lsn-p">Arrays are Java's most basic <strong>fixed-size container</strong>. They store a sequence of values of the same type, are <em>indexed from zero</em>, and &mdash; once created &mdash; they cannot grow or shrink. Understanding the difference between <em>declaring</em>, <em>instantiating</em> and <em>initializing</em> an array is essential for the OCA exam.</p>

<div class="lsn-callout"><strong>Learning objectives.</strong> By the end of this lesson you should be able to: declare, instantiate, initialize and use a one-dimensional array; declare, instantiate, initialize and use multi-dimensional arrays; explain default element values; iterate with both classic <code>for</code> and the enhanced <code>for</code>; and recognize <code>ArrayIndexOutOfBoundsException</code>.</div>

<h2 class="lsn-h2">1. Declaring an array variable</h2>
<p class="lsn-p">A declaration only creates a <em>reference</em>. No memory for elements is allocated yet. Both bracket positions are legal, but the brackets-after-type form is the convention:</p>
<pre><code>int[] numbers;     // preferred
int numbers2 [];   // also legal, discouraged
String[] names;
</code></pre>

<h2 class="lsn-h2">2. Instantiating with <code>new</code></h2>
<p class="lsn-p">The <code>new</code> keyword allocates the actual storage. The length is fixed at this moment and stored in the read-only <code>length</code> field:</p>
<pre><code>int[] numbers = new int[5];      // length 5, all elements default to 0
String[] names = new String[3];  // length 3, all elements default to null
System.out.println(numbers.length); // 5
</code></pre>

<table class="lsn-table">
  <thead><tr><th>Element type</th><th>Default value</th></tr></thead>
  <tbody>
    <tr><td><code>byte, short, int, long</code></td><td><code>0</code></td></tr>
    <tr><td><code>float, double</code></td><td><code>0.0</code></td></tr>
    <tr><td><code>char</code></td><td><code>'\\u0000'</code> (the null character)</td></tr>
    <tr><td><code>boolean</code></td><td><code>false</code></td></tr>
    <tr><td>Any reference type</td><td><code>null</code></td></tr>
  </tbody>
</table>

<h2 class="lsn-h2">3. Array initializers</h2>
<p class="lsn-p">Java offers two shorthand forms that allocate and populate the array in one expression:</p>
<pre><code>// Anonymous array initializer &mdash; only valid in a declaration:
int[] primes = {2, 3, 5, 7, 11};

// "new" array initializer &mdash; valid anywhere an expression is:
int[] primes2 = new int[]{2, 3, 5, 7, 11};
printAll(new int[]{1, 2, 3});       // legal
// printAll({1, 2, 3});             // does NOT compile
</code></pre>

<div class="lsn-warn"><strong>Common trap.</strong> You cannot specify both a size <em>and</em> an initializer: <code>int[] a = new int[3]{1,2,3};</code> fails to compile.</div>

<h2 class="lsn-h2">4. Reading and writing elements</h2>
<p class="lsn-p">Elements are accessed with <code>array[index]</code>. Valid indices run from <code>0</code> to <code>array.length - 1</code>. Anything outside that range throws <code>ArrayIndexOutOfBoundsException</code> <em>at runtime</em> &mdash; not at compile time:</p>
<pre><code>int[] a = {10, 20, 30};
a[0] = 99;                       // write
int first = a[0];                // read &rarr; 99
int bad   = a[3];                // ArrayIndexOutOfBoundsException
</code></pre>

<h2 class="lsn-h2">5. Iterating an array</h2>
<p class="lsn-p">Use a classic <code>for</code> loop when you need the index, and the enhanced <code>for</code> (&ldquo;for-each&rdquo;) when you only need the values:</p>
<pre><code>int[] a = {10, 20, 30};

for (int i = 0; i &lt; a.length; i++) {
    System.out.println(i + ": " + a[i]);
}

for (int n : a) {                // enhanced for
    System.out.println(n);
}
</code></pre>

<div class="lsn-callout">The enhanced <code>for</code> gives you a <em>copy</em> of each element value (for primitives) or a copy of the reference (for objects). Reassigning the loop variable does <strong>not</strong> change the array.</div>

<h2 class="lsn-h2">6. Multi-dimensional arrays</h2>
<p class="lsn-p">A &ldquo;multi-dimensional&rdquo; array in Java is really an <em>array of arrays</em>. Each inner array is a separate object, so the inner lengths do not have to match (&ldquo;jagged&rdquo; arrays):</p>
<pre><code>int[][] grid = new int[3][4];        // 3 rows, each 4 columns &mdash; all zeros
grid[1][2] = 7;

int[][] jagged = new int[3][];       // only the outer length is fixed
jagged[0] = new int[]{1};
jagged[1] = new int[]{1, 2, 3};
jagged[2] = new int[]{1, 2, 3, 4, 5};

int[][] table = { {1, 2}, {3, 4, 5}, {} };  // initializer form
</code></pre>

<p class="lsn-p">A nested loop walks every cell:</p>
<pre><code>for (int r = 0; r &lt; jagged.length; r++) {
    for (int c = 0; c &lt; jagged[r].length; c++) {
        System.out.print(jagged[r][c] + " ");
    }
    System.out.println();
}
</code></pre>

<h2 class="lsn-h2">7. Useful array facts</h2>
<ul class="lsn-ul">
  <li><code>array.length</code> is a <strong>field</strong>, not a method &mdash; no parentheses.</li>
  <li>An array's runtime type includes its element type: <code>new int[3]</code> is an <code>int[]</code>, not an <code>Object[]</code>.</li>
  <li><code>java.util.Arrays</code> provides helpers: <code>Arrays.toString(a)</code>, <code>Arrays.sort(a)</code>, <code>Arrays.equals(a,b)</code>, <code>Arrays.copyOf(a,n)</code>.</li>
  <li>Arrays <em>are</em> objects: <code>a.getClass().getName()</code> returns names like <code>[I</code> for <code>int[]</code> and <code>[[Ljava.lang.String;</code> for <code>String[][]</code>.</li>
</ul>

<h2 class="lsn-h2">8. Summary</h2>
<ul class="lsn-ul">
  <li><strong>Declare</strong> creates a reference; <strong>instantiate</strong> with <code>new</code> allocates storage and fixes the length; <strong>initialize</strong> assigns values.</li>
  <li>Elements have type-specific defaults (<code>0</code>, <code>0.0</code>, <code>'\\u0000'</code>, <code>false</code>, <code>null</code>).</li>
  <li>The anonymous initializer <code>{1,2,3}</code> is only legal in a declaration; use <code>new int[]{1,2,3}</code> elsewhere.</li>
  <li>Multi-dimensional arrays are arrays of arrays and may be jagged.</li>
  <li>Bad indices throw <code>ArrayIndexOutOfBoundsException</code> at runtime.</li>
</ul>
"""

# Each question: (type, html, options_list, feedback)
# Options list: list of (option_html, is_correct)
QUESTIONS = [
    (
        'multiple_choice',
        'Which of the following declarations of a one-dimensional <code>int</code> array are <strong>legal</strong> in Java?',
        [
            ('<code>int[] a;</code>', True),
            ('<code>int a[];</code>', True),
            ('<code>int[5] a;</code>', False),
            ('<code>int a[5];</code>', False),
        ],
        'Brackets may appear before or after the variable name, but a size belongs in the <code>new</code> expression, not in the declaration.'
    ),
    (
        'multiple_choice',
        'What is the value of <code>numbers[2]</code> after this code runs?<br><pre><code>int[] numbers = new int[5];</code></pre>',
        [
            ('<code>0</code>', True),
            ('<code>null</code>', False),
            ('Undefined &mdash; the element has no value', False),
            ('A compile-time error occurs', False),
        ],
        '<code>new int[5]</code> default-initializes every element. The default for an <code>int</code> is <code>0</code>.'
    ),
    (
        'multiple_choice',
        'Which line will cause a compile-time error?<br><pre><code>int[] a = {1, 2, 3};               // 1\nint[] b = new int[]{1, 2, 3};      // 2\nint[] c = new int[3]{1, 2, 3};     // 3\nint[] d;\nd = new int[]{1, 2, 3};            // 4</code></pre>',
        [
            ('Line 3', True),
            ('Line 1', False),
            ('Line 2', False),
            ('Line 4', False),
        ],
        'You may specify a size <em>or</em> an initializer, never both. <code>new int[3]{1,2,3}</code> does not compile.'
    ),
    (
        'true_false',
        '<code>array.length</code> is a method call and must be written with parentheses: <code>array.length()</code>.',
        [
            ('False', True),
            ('True', False),
        ],
        '<code>length</code> is a <strong>field</strong> on arrays (only <code>String.length()</code> is a method). No parentheses.'
    ),
    (
        'multiple_choice',
        'What happens at runtime?<br><pre><code>int[] a = {10, 20, 30};\nSystem.out.println(a[3]);</code></pre>',
        [
            ('An <code>ArrayIndexOutOfBoundsException</code> is thrown', True),
            ('It prints <code>0</code>', False),
            ('It prints <code>null</code>', False),
            ('It fails to compile', False),
        ],
        'Valid indices are <code>0</code> through <code>length-1</code>. Index <code>3</code> on a length-3 array throws <code>ArrayIndexOutOfBoundsException</code>.'
    ),
    (
        'multiple_choice',
        'Which statement about the following array is <strong>true</strong>?<br><pre><code>int[][] jagged = new int[3][];</code></pre>',
        [
            ('The outer length is 3; each inner array is currently <code>null</code> and may later be assigned arrays of different lengths.', True),
            ('It is a 3&times;3 array of zeros.', False),
            ('It fails to compile because the second dimension is missing.', False),
            ('Each inner array is automatically an <code>int[0]</code>.', False),
        ],
        'Only the outer length is fixed. The inner references are <code>null</code> until you assign them, and they may have different lengths.'
    ),
    (
        'multiple_choice',
        'What is the output?<br><pre><code>String[] names = new String[2];\nSystem.out.println(names[0]);\nSystem.out.println(names.length);</code></pre>',
        [
            ('<code>null</code><br><code>2</code>', True),
            ('<code>""</code><br><code>2</code>', False),
            ('A <code>NullPointerException</code> is thrown', False),
            ('It fails to compile', False),
        ],
        'Reference-type elements default to <code>null</code>, and <code>length</code> reports the allocated size (<code>2</code>).'
    ),
    (
        'multiple_choice',
        'Inside an enhanced <code>for</code> loop over an <code>int[]</code>, reassigning the loop variable&hellip;',
        [
            ('&hellip;does <strong>not</strong> change the underlying array element.', True),
            ('&hellip;updates the corresponding array element.', False),
            ('&hellip;throws an exception at runtime.', False),
            ('&hellip;is a compile-time error.', False),
        ],
        'The loop variable holds a copy of the primitive value (or a copy of the reference). Assigning to it has no effect on the array.'
    ),
]


def upsert():
    with app.app_context():
        course = Course.query.filter(Course.title.like(COURSE_TITLE_LIKE)).first()
        if not course:
            print('Java course not found.')
            return

        # 1. Lesson body
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
                order=8,
                points=1.0,
            )
            db.session.add(lesson)
            db.session.flush()
            print(f'inserted lesson {lesson.id}')

        # 2. Quiz
        quiz = Quiz.query.filter_by(course_id=course.id, title=QUIZ_TITLE).first()
        if not quiz:
            quiz = Quiz(course_id=course.id, title=QUIZ_TITLE,
                        description='Check your understanding of one- and multi-dimensional arrays.')
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

        # 3. Exam lesson linking to the quiz
        exam = Lesson.query.filter_by(course_id=course.id, title=EXAM_LESSON_TITLE,
                                       content_type='exam').first()
        if exam:
            exam.quiz_id = quiz.id
            exam.order = 9
            print(f'updated exam lesson {exam.id}')
        else:
            exam = Lesson(
                title=EXAM_LESSON_TITLE,
                content='',
                course_id=course.id,
                content_type='exam',
                quiz_id=quiz.id,
                order=9,
                points=1.0,
            )
            db.session.add(exam)
            db.session.flush()
            print(f'inserted exam lesson {exam.id}')

        db.session.commit()
        print('done.')


if __name__ == '__main__':
    upsert()
