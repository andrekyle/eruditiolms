"""Author Lesson 6 (Working with Methods and Encapsulation) + its quiz for the Java OCA course."""
from app import app, db, Course, Lesson, Quiz, Question, QuestionOption

COURSE_TITLE_LIKE = '%1Z0-808%'
LESSON_TITLE = 'Lesson 6: Working with Methods and Encapsulation'
QUIZ_TITLE = 'Lesson 6 Quiz — Methods and Encapsulation'
EXAM_LESSON_TITLE = 'Lesson 6 Quiz — Methods and Encapsulation'

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
  .lsn-fig{margin:22px auto;max-width:560px;text-align:center;}
  .lsn-fig svg{max-width:100%;height:auto;display:block;margin:0 auto;}
  .lsn-cap{font-size:.9rem;color:#6B6B6B;margin-top:6px;}
</style>

<p class="lsn-p">Methods are the units of work in a Java program; <strong>encapsulation</strong> is the discipline of hiding internal state behind those methods. Together they decide who can read or modify the data inside an object &mdash; and how safely your code can evolve.</p>

<div class="lsn-callout"><strong>Learning objectives.</strong> By the end of this lesson you should be able to: create methods with arguments and return values (including overloaded methods); apply the <code>static</code> keyword to methods and fields; create and overload constructors and explain default vs user-defined constructors; apply access modifiers; apply encapsulation principles to a class; and reason about pass-by-value for primitives and references.</div>

<h2 class="lsn-h2">1. Anatomy of a method</h2>
<pre><code>// modifiers  return-type  name  ( parameter-list )  throws-clause? { body }
public static int max(int a, int b) {
    return (a &gt;= b) ? a : b;
}
</code></pre>
<ul class="lsn-ul">
  <li>The <strong>return type</strong> may be <code>void</code> or any value type; <code>return</code> in a <code>void</code> method is optional but legal as a way to exit early.</li>
  <li>Parameters are local variables initialized from the caller's arguments.</li>
  <li>A method that declares a checked exception in a <code>throws</code> clause forces callers to handle or re-declare it.</li>
</ul>

<h2 class="lsn-h2">2. Overloading methods</h2>
<p class="lsn-p">Two methods <em>overload</em> when they share a name but differ in their <em>parameter list</em> (number, types, or order). The return type alone is <strong>not</strong> enough:</p>
<pre><code>void log(String s)               { /* ... */ }
void log(int i)                  { /* ... */ }       // OK &mdash; different type
void log(String s, int level)    { /* ... */ }       // OK &mdash; different count
// int log(String s) { ... }                          // ERROR &mdash; same parameter list
</code></pre>

<div class="lsn-callout">When more than one overload matches, the compiler prefers an <strong>exact match</strong> over a widening conversion, widening over autoboxing, and autoboxing over varargs. It will refuse to choose if two overloads are equally specific.</div>

<h2 class="lsn-h2">3. <code>static</code> methods and fields</h2>
<p class="lsn-p"><code>static</code> members belong to the <em>class</em>, not to any instance. They are shared by all objects of the class, so they have no <code>this</code>:</p>
<pre><code>class Counter {
    static int count = 0;        // one variable for the whole class
    int id;                      // one variable per instance

    Counter() {
        id = ++count;            // legal: instance code may read static state
    }

    static void reset() {
        count = 0;
        // this.id = 0;          // ERROR &mdash; no instance available
    }
}
</code></pre>

<div class="lsn-warn"><strong>Common trap.</strong> A static method cannot reference an instance field or call an instance method without an explicit object: <code>instanceMethod();</code> fails inside a <code>static</code> method, but <code>new Counter().id</code> is fine.</div>

<h2 class="lsn-h2">4. Constructors</h2>
<p class="lsn-p">A constructor initializes a new object. It has <em>no return type</em> (not even <code>void</code>) and shares the class's name:</p>
<pre><code>class Point {
    int x, y;

    Point()              { this(0, 0); }     // delegates to the 2-arg version
    Point(int x, int y)  { this.x = x; this.y = y; }
}
</code></pre>

<ul class="lsn-ul">
  <li>If you write <strong>no</strong> constructor, the compiler adds a public no-argument <em>default</em> constructor that does nothing.</li>
  <li>As soon as you declare any constructor, the default disappears.</li>
  <li><code>this(...)</code> calls another constructor of the same class; it must be the <strong>first</strong> statement of the constructor.</li>
  <li><code>super(...)</code> calls a parent constructor; it must also be the first statement (so <code>this(...)</code> and <code>super(...)</code> cannot both appear).</li>
</ul>

<h2 class="lsn-h2">5. Access modifiers</h2>
<table class="lsn-table">
  <thead><tr><th>Modifier</th><th>Same class</th><th>Same package</th><th>Subclass (other pkg)</th><th>Everywhere</th></tr></thead>
  <tbody>
    <tr><td><code>public</code></td><td>&#x2713;</td><td>&#x2713;</td><td>&#x2713;</td><td>&#x2713;</td></tr>
    <tr><td><code>protected</code></td><td>&#x2713;</td><td>&#x2713;</td><td>&#x2713;</td><td>&#x2717;</td></tr>
    <tr><td><em>(package-private &mdash; no keyword)</em></td><td>&#x2713;</td><td>&#x2713;</td><td>&#x2717;</td><td>&#x2717;</td></tr>
    <tr><td><code>private</code></td><td>&#x2713;</td><td>&#x2717;</td><td>&#x2717;</td><td>&#x2717;</td></tr>
  </tbody>
</table>
<p class="lsn-p">Top-level classes may only be <code>public</code> or package-private. Nested classes may use any of the four.</p>

<h2 class="lsn-h2">6. Encapsulation</h2>
<p class="lsn-p">The encapsulation recipe for a normal &ldquo;data&rdquo; class is:</p>
<ul class="lsn-ul">
  <li>Make every field <code>private</code>.</li>
  <li>Expose state through <code>public</code> getters and (if mutation is allowed) setters.</li>
  <li>Validate inside the setter so the object can never enter an illegal state.</li>
</ul>
<pre><code>public class Person {
    private String name;
    private int age;

    public String getName()           { return name; }
    public void   setName(String n)   { this.name = (n == null ? "" : n.trim()); }

    public int    getAge()            { return age; }
    public void   setAge(int a) {
        if (a &lt; 0) throw new IllegalArgumentException("age &lt; 0");
        this.age = a;
    }
}
</code></pre>

<figure class="lsn-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" role="img" aria-label="Encapsulation diagram: private fields surrounded by public methods">
    <defs>
      <marker id="arrEnc" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="#6B6B6B"/>
      </marker>
    </defs>
    <g fill="rgba(127,127,127,.10)" stroke="#6B6B6B" stroke-width="1.5">
      <rect x="100" y="30" width="260" height="160" rx="10"/>
      <rect x="170" y="80" width="120" height="60" rx="6" fill="rgba(127,127,127,.18)"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="13" text-anchor="middle">
      <text x="230" y="50">public class Person</text>
      <text x="230" y="105" font-size="12">private String name;</text>
      <text x="230" y="125" font-size="12">private int age;</text>
    </g>
    <g fill="#6B6B6B" font-family="system-ui,sans-serif" font-size="12" text-anchor="middle">
      <text x="135" y="180">getName()</text>
      <text x="230" y="180">setName(&hellip;)</text>
      <text x="325" y="180">setAge(&hellip;)</text>
    </g>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <line x1="20"  y1="180" x2="86"  y2="180" marker-end="url(#arrEnc)"/>
      <line x1="440" y1="180" x2="374" y2="180" marker-end="url(#arrEnc)"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="12" text-anchor="middle">
      <text x="20"  y="170">caller</text>
      <text x="440" y="170">caller</text>
    </g>
  </svg>
  <div class="lsn-cap">Figure 1. Callers reach the private fields (inner box) only through the public methods on the outer boundary.</div>
</figure>

<h2 class="lsn-h2">7. Pass-by-value &mdash; primitives vs references</h2>
<p class="lsn-p">Java always passes arguments <strong>by value</strong>. For primitives the caller gives a <em>copy of the value</em>; for objects the caller gives a <em>copy of the reference</em>. The method can mutate the object the reference points to, but reassigning the parameter does not affect the caller's variable:</p>
<pre><code>void grow(int[] a)         { a[0] = 99;   a = new int[]{1,2,3}; }
void bump(int n)           { n = n + 1; }

int[] arr = {0, 0, 0};
int   x   = 10;

grow(arr);                 // arr[0] becomes 99; arr itself is unchanged
bump(x);                   // x is still 10
</code></pre>

<figure class="lsn-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" role="img" aria-label="Pass-by-value: caller and parameter both reference the same array object">
    <defs>
      <marker id="arrPV" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="#6B6B6B"/>
      </marker>
    </defs>
    <g fill="rgba(127,127,127,.10)" stroke="#6B6B6B" stroke-width="1.5">
      <rect x="20"  y="40"  width="120" height="50" rx="4"/>
      <rect x="20"  y="120" width="120" height="50" rx="4"/>
      <rect x="300" y="80"  width="140" height="50" rx="4"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="12" text-anchor="middle">
      <text x="80"  y="65">caller: arr</text>
      <text x="80"  y="80" font-size="11" fill="#6B6B6B">reference</text>
      <text x="80"  y="145">method: a</text>
      <text x="80"  y="160" font-size="11" fill="#6B6B6B">copy of reference</text>
      <text x="370" y="100">int[]{ 99, 0, 0 }</text>
      <text x="370" y="118" font-size="11" fill="#6B6B6B">heap object</text>
    </g>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <line x1="140" y1="65"  x2="298" y2="98"  marker-end="url(#arrPV)"/>
      <line x1="140" y1="145" x2="298" y2="112" marker-end="url(#arrPV)"/>
    </g>
  </svg>
  <div class="lsn-cap">Figure 2. Both <code>arr</code> and the parameter <code>a</code> point at the same heap object, so mutations through <code>a</code> are visible to the caller &mdash; but reassigning <code>a</code> rebinds only the local copy.</div>
</figure>

<h2 class="lsn-h2">8. Summary</h2>
<ul class="lsn-ul">
  <li>Methods differ from constructors: methods have a return type, constructors share the class's name and have none.</li>
  <li>Overloads vary by <em>parameter list</em>; the compiler picks the most specific match (exact &gt; widening &gt; autoboxing &gt; varargs).</li>
  <li><code>static</code> members belong to the class. They cannot use <code>this</code> or directly access instance state.</li>
  <li>The default no-arg constructor only appears when you declare <strong>no</strong> constructors of your own.</li>
  <li>Access modifiers (from most to least restrictive): <code>private</code> &lt; package &lt; <code>protected</code> &lt; <code>public</code>.</li>
  <li>Encapsulate by making fields <code>private</code> and validating through setters.</li>
  <li>Java is pass-by-value &mdash; references are copied, not the objects they point to.</li>
</ul>
"""

QUESTIONS = [
    (
        'multiple_choice',
        'Which of the following pairs are <strong>valid overloads</strong> of each other?',
        [
            ('<code>void f(int x)</code> and <code>void f(long x)</code>', True),
            ('<code>void f(int x)</code> and <code>void f(int x, int y)</code>', True),
            ('<code>void f(int x)</code> and <code>int f(int x)</code>', False),
            ('<code>void f(int a, int b)</code> and <code>void f(int x, int y)</code>', False),
        ],
        'Overloads must differ in the <em>parameter list</em> (number, types, or order). Return type alone &mdash; or just parameter <em>names</em> &mdash; is not enough.'
    ),
    (
        'multiple_choice',
        'What does the compiler do for a class that declares <strong>no</strong> constructors?',
        [
            ('It inserts a <code>public</code> no-argument constructor with an empty body.', True),
            ('Nothing &mdash; the class cannot be instantiated.', False),
            ('It inserts a <code>private</code> no-argument constructor.', False),
            ('It inserts one constructor for every field.', False),
        ],
        'When you declare no constructors, the compiler synthesises a public default constructor that simply calls <code>super()</code>.'
    ),
    (
        'multiple_choice',
        'Which statement about the <code>static</code> keyword is <strong>true</strong>?',
        [
            ('A <code>static</code> method may not reference <code>this</code>.', True),
            ('A <code>static</code> method may not read a <code>static</code> field.', False),
            ('An instance method may not read a <code>static</code> field.', False),
            ('A <code>static</code> field has one copy per instance.', False),
        ],
        'Static members belong to the class, not an instance, so there is no <code>this</code>. They may still access other static members.'
    ),
    (
        'true_false',
        'Inside a constructor, the call <code>this(other)</code> may appear anywhere &mdash; before or after other statements.',
        [
            ('False', True),
            ('True', False),
        ],
        'Both <code>this(&hellip;)</code> and <code>super(&hellip;)</code> must be the <strong>first</strong> statement of the constructor &mdash; which means they cannot both appear in the same constructor.'
    ),
    (
        'multiple_choice',
        'A <code>protected</code> member is accessible from&hellip;',
        [
            ('&hellip;the same class, the same package, and subclasses (even in another package).', True),
            ('&hellip;only the same class.', False),
            ('&hellip;only the same package.', False),
            ('&hellip;anywhere &mdash; it is equivalent to <code>public</code>.', False),
        ],
        '<code>protected</code> widens package-private access by also allowing subclasses in other packages.'
    ),
    (
        'multiple_choice',
        'After this code runs, what is the value of <code>arr[0]</code>?<br><pre><code>void grow(int[] a) {\n    a[0] = 99;\n    a = new int[]{1, 2, 3};\n}\n\nint[] arr = {0, 0, 0};\ngrow(arr);</code></pre>',
        [
            ('<code>99</code>', True),
            ('<code>0</code>', False),
            ('<code>1</code>', False),
            ('It throws <code>NullPointerException</code>', False),
        ],
        'Java passes a copy of the reference. Mutating the array through <code>a</code> is visible; reassigning <code>a</code> only rebinds the local copy.'
    ),
    (
        'multiple_choice',
        'Which class follows good <strong>encapsulation</strong> practice?',
        [
            ('<pre><code>public class P { private int age; public int getAge(){return age;} public void setAge(int a){ if(a&lt;0) throw new IllegalArgumentException(); this.age=a;} }</code></pre>', True),
            ('<pre><code>public class P { public int age; }</code></pre>', False),
            ('<pre><code>public class P { protected int age; }</code></pre>', False),
            ('<pre><code>public class P { int age; public int getAge(){return age;} }</code></pre>', False),
        ],
        'Make fields <code>private</code> and expose access through methods that can validate input. The other options leave the field reachable without checks.'
    ),
    (
        'multiple_choice',
        'Which line will fail to compile?<br><pre><code>class C {\n    int x;\n    static int y;\n    static void s() {\n        x = 1;       // 1\n        y = 1;       // 2\n        this.y = 1;  // 3\n        C.y = 1;     // 4\n    }\n}</code></pre>',
        [
            ('Lines 1 and 3', True),
            ('Only line 1', False),
            ('Only line 3', False),
            ('Lines 2 and 4', False),
        ],
        'Inside a <code>static</code> method there is no <code>this</code> and no implicit instance, so the instance field <code>x</code> and the <code>this</code> keyword are both unavailable.'
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
                order=12,
                points=1.0,
            )
            db.session.add(lesson)
            db.session.flush()
            print(f'inserted lesson {lesson.id}')

        quiz = Quiz.query.filter_by(course_id=course.id, title=QUIZ_TITLE).first()
        if not quiz:
            quiz = Quiz(course_id=course.id, title=QUIZ_TITLE,
                        description='Check your understanding of methods, constructors, static members, access modifiers and encapsulation.')
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
            exam.order = 13
            print(f'updated exam lesson {exam.id}')
        else:
            exam = Lesson(
                title=EXAM_LESSON_TITLE,
                content='',
                course_id=course.id,
                content_type='exam',
                quiz_id=quiz.id,
                order=13,
                points=1.0,
            )
            db.session.add(exam)
            db.session.flush()
            print(f'inserted exam lesson {exam.id}')

        db.session.commit()
        print('done.')


if __name__ == '__main__':
    upsert()
