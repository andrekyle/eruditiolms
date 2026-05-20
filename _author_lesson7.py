"""Author Lesson 7 (Working with Inheritance) + its quiz for the Java OCA course."""
from app import app, db, Course, Lesson, Quiz, Question, QuestionOption

COURSE_TITLE_LIKE = '%1Z0-808%'
LESSON_TITLE = 'Lesson 7: Working with Inheritance'
QUIZ_TITLE = 'Lesson 7 Quiz — Inheritance'
EXAM_LESSON_TITLE = 'Lesson 7 Quiz — Inheritance'

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

<p class="lsn-p"><strong>Inheritance</strong> lets a class build on another class &mdash; reusing its fields and methods, refining behaviour with overrides, and standing in for it through polymorphism. It is the mechanism behind the IS&minus;A relationship and the foundation for almost every Java framework you will meet.</p>

<div class="lsn-callout"><strong>Learning objectives.</strong> By the end of this lesson you should be able to: describe inheritance and its benefits; develop code that demonstrates the use of polymorphism (including overriding versus overloading); differentiate between the type of a reference and the type of an object; determine when casting is necessary; use <code>super</code> and <code>this</code> to access objects and constructors; and use abstract classes and interfaces at the level required by OCA 1Z0-808.</p>

<h2 class="lsn-h2">1. The <code>extends</code> keyword</h2>
<pre><code>class Animal {
    String name;
    void speak() { System.out.println(name + " makes a sound"); }
}

class Dog extends Animal {          // Dog IS-A Animal
    void speak() { System.out.println(name + " barks"); }
    void fetch() { System.out.println(name + " fetches"); }
}
</code></pre>
<ul class="lsn-ul">
  <li>Java supports <strong>single class inheritance only</strong>: a class has exactly one direct superclass.</li>
  <li>Every class implicitly extends <code>java.lang.Object</code> if no <code>extends</code> clause is given.</li>
  <li>A subclass inherits all <em>non-private</em> members of its superclass. Private members exist in memory but are not directly accessible.</li>
  <li>Constructors are <strong>not inherited</strong>.</li>
</ul>

<figure class="lsn-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 260" role="img" aria-label="Class hierarchy: Object at the top, Animal below, Dog and Cat as siblings">
    <defs>
      <marker id="arrInh" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="10" markerHeight="10" orient="auto-start-reverse">
        <path d="M0,0 L12,6 L0,12 z" fill="none" stroke="#6B6B6B" stroke-width="1.5"/>
      </marker>
    </defs>
    <g fill="rgba(127,127,127,.10)" stroke="#6B6B6B" stroke-width="1.5">
      <rect x="180" y="10"  width="120" height="44" rx="6"/>
      <rect x="180" y="100" width="120" height="44" rx="6"/>
      <rect x="60"  y="200" width="120" height="44" rx="6"/>
      <rect x="300" y="200" width="120" height="44" rx="6"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="14" text-anchor="middle">
      <text x="240" y="37">Object</text>
      <text x="240" y="127">Animal</text>
      <text x="120" y="227">Dog</text>
      <text x="360" y="227">Cat</text>
    </g>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <line x1="240" y1="100" x2="240" y2="56"  marker-end="url(#arrInh)"/>
      <line x1="155" y1="200" x2="210" y2="146" marker-end="url(#arrInh)"/>
      <line x1="325" y1="200" x2="270" y2="146" marker-end="url(#arrInh)"/>
    </g>
  </svg>
  <div class="lsn-cap">Figure 1. Each arrow points from a subclass <em>up</em> to its direct superclass. Inheritance is single &mdash; a class has exactly one parent &mdash; but the tree fans out.</div>
</figure>

<h2 class="lsn-h2">2. Constructors and <code>super(&hellip;)</code></h2>
<p class="lsn-p">The very first line of every constructor is a call to another constructor &mdash; either <code>this(&hellip;)</code> (same class) or <code>super(&hellip;)</code> (parent class). If you write neither, the compiler inserts an implicit <code>super();</code>:</p>
<pre><code>class Animal {
    Animal(String name) { /* &hellip; */ }     // no no-arg constructor
}

class Dog extends Animal {
    Dog() {
        // super();                       // ERROR &mdash; Animal has no no-arg constructor
        super("dog");                     // OK
    }
}
</code></pre>
<div class="lsn-warn"><strong>Pitfall.</strong> If the parent has only constructors that take arguments, every subclass constructor <em>must</em> call <code>super(&hellip;)</code> explicitly with matching arguments.</div>

<h2 class="lsn-h2">3. Overriding vs overloading</h2>
<table class="lsn-table">
  <thead><tr><th>&nbsp;</th><th>Overriding</th><th>Overloading</th></tr></thead>
  <tbody>
    <tr><td>Where</td><td>Subclass replaces a parent method.</td><td>Same class, several methods share a name.</td></tr>
    <tr><td>Signature</td><td>Same name <em>and</em> same parameter list.</td><td>Same name, <strong>different</strong> parameter list.</td></tr>
    <tr><td>Return type</td><td>Same or a <em>covariant</em> subtype.</td><td>May differ freely.</td></tr>
    <tr><td>Access</td><td>Must be the same or <em>wider</em> than the parent's.</td><td>Independent.</td></tr>
    <tr><td>Exceptions</td><td>May not throw new or broader checked exceptions.</td><td>Independent.</td></tr>
    <tr><td>Dispatch</td><td>Resolved at <strong>runtime</strong> (dynamic).</td><td>Resolved at <strong>compile time</strong> (static).</td></tr>
  </tbody>
</table>

<div class="lsn-callout"><strong>Rules for a legal override.</strong> Same name + same parameter list + return type that is the same or a subtype + access &ge; parent's + no broader checked exceptions + parent method is not <code>final</code>, <code>static</code> or <code>private</code>.</div>

<h2 class="lsn-h2">4. Polymorphism &mdash; reference type vs object type</h2>
<p class="lsn-p">The compiler decides which methods you may <em>call</em> based on the <strong>reference</strong> type. The JVM decides which version actually <em>runs</em> based on the <strong>object</strong> type:</p>
<pre><code>Animal a = new Dog();      // reference: Animal, object: Dog
a.speak();                 // prints "&hellip; barks"   (dynamic dispatch)
// a.fetch();              // ERROR &mdash; Animal has no fetch()
((Dog) a).fetch();         // OK after a cast
</code></pre>

<figure class="lsn-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 220" role="img" aria-label="Dynamic dispatch: reference of type Animal calls speak() on a Dog object">
    <defs>
      <marker id="arrDsp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="#6B6B6B"/>
      </marker>
    </defs>
    <g fill="rgba(127,127,127,.10)" stroke="#6B6B6B" stroke-width="1.5">
      <rect x="20"  y="80"  width="140" height="60" rx="6"/>
      <rect x="300" y="40"  width="160" height="60" rx="6"/>
      <rect x="300" y="120" width="160" height="60" rx="6"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="13" text-anchor="middle">
      <text x="90"  y="105">Animal a</text>
      <text x="90"  y="125" font-size="11" fill="#6B6B6B">reference type</text>
      <text x="380" y="65">Animal.speak()</text>
      <text x="380" y="83" font-size="11" fill="#6B6B6B">compile-time check</text>
      <text x="380" y="145">Dog.speak()</text>
      <text x="380" y="163" font-size="11" fill="#6B6B6B">runtime dispatch &#x2714;</text>
    </g>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <line x1="160" y1="100" x2="298" y2="70"  marker-end="url(#arrDsp)"/>
      <line x1="160" y1="120" x2="298" y2="150" stroke-dasharray="5,4" marker-end="url(#arrDsp)"/>
    </g>
  </svg>
  <div class="lsn-cap">Figure 2. The compiler verifies the call against <code>Animal.speak()</code>; at runtime the JVM jumps to <code>Dog.speak()</code> because the object is really a <code>Dog</code>.</div>
</figure>

<div class="lsn-warn"><strong>Fields are not polymorphic.</strong> If both classes declare a field with the same name, the <em>reference</em> type chooses which one you see. Use methods (getters) to get polymorphic behaviour.</div>

<h2 class="lsn-h2">5. Casting and <code>instanceof</code></h2>
<pre><code>Animal a = new Dog();

if (a instanceof Dog) {           // safe runtime check
    Dog d = (Dog) a;              // downcast
    d.fetch();
}

Animal other = new Cat();
Dog bad = (Dog) other;            // compiles, ClassCastException at runtime
</code></pre>
<ul class="lsn-ul">
  <li><strong>Upcasts</strong> (subtype &rarr; supertype) are implicit and always safe.</li>
  <li><strong>Downcasts</strong> (supertype &rarr; subtype) need an explicit cast and may throw <code>ClassCastException</code>.</li>
  <li><code>null instanceof X</code> is always <code>false</code> for any reference type <code>X</code>.</li>
</ul>

<h2 class="lsn-h2">6. <code>this</code> and <code>super</code></h2>
<ul class="lsn-ul">
  <li><code>this.x</code> &mdash; the field <code>x</code> on the current object.</li>
  <li><code>super.x</code> &mdash; the field <code>x</code> as defined by the parent class (useful when the subclass hides it).</li>
  <li><code>this.m()</code> &mdash; polymorphic call on the current object.</li>
  <li><code>super.m()</code> &mdash; explicitly invoke the parent's version of <code>m()</code>, bypassing dynamic dispatch.</li>
  <li><code>this(&hellip;)</code> / <code>super(&hellip;)</code> &mdash; constructor calls; must be the first statement.</li>
</ul>

<h2 class="lsn-h2">7. Abstract classes</h2>
<pre><code>abstract class Shape {
    abstract double area();          // no body &mdash; subclasses must implement
    void describe() { System.out.println("area = " + area()); }
}

class Circle extends Shape {
    double r;
    Circle(double r) { this.r = r; }
    double area() { return Math.PI * r * r; }
}
</code></pre>
<ul class="lsn-ul">
  <li>An <code>abstract</code> class cannot be instantiated with <code>new</code>, but it may have constructors, fields and concrete methods.</li>
  <li>An <code>abstract</code> method has no body and forces non-abstract subclasses to override it.</li>
  <li>A class with any <code>abstract</code> method &mdash; declared or inherited and not overridden &mdash; <strong>must itself</strong> be declared <code>abstract</code>.</li>
  <li><code>abstract</code> cannot combine with <code>final</code>, <code>private</code> or <code>static</code>.</li>
</ul>

<h2 class="lsn-h2">8. Interfaces (introduction)</h2>
<pre><code>interface Drawable {
    void draw();                                    // implicitly public abstract
    int MAX_LAYERS = 8;                             // implicitly public static final
}

class Circle extends Shape implements Drawable {
    public void draw() { /* &hellip; */ }              // must be public
}
</code></pre>
<ul class="lsn-ul">
  <li>A class may extend <strong>one</strong> class but <strong>implement many</strong> interfaces.</li>
  <li>Interface methods are implicitly <code>public abstract</code>; fields are implicitly <code>public static final</code>.</li>
  <li>An implementing class must mark its overrides <code>public</code> &mdash; otherwise it would be narrowing access.</li>
</ul>

<h2 class="lsn-h2">9. Summary</h2>
<ul class="lsn-ul">
  <li>Java has single class inheritance via <code>extends</code>; every class ultimately extends <code>Object</code>.</li>
  <li>A subclass constructor's first line is <code>this(&hellip;)</code> or <code>super(&hellip;)</code>; otherwise the compiler inserts <code>super();</code>.</li>
  <li><strong>Override</strong>: same signature, same/covariant return, same/wider access, no broader checked exceptions. <strong>Overload</strong>: different parameter list.</li>
  <li>Method calls are dispatched on the <em>object</em> type; field access and overload resolution use the <em>reference</em> type.</li>
  <li>Use <code>instanceof</code> before downcasting to avoid <code>ClassCastException</code>.</li>
  <li><code>abstract</code> classes may have state and concrete methods; interfaces declare a public contract and allow multi-implementation.</li>
</ul>
"""

QUESTIONS = [
    (
        'multiple_choice',
        'Which statement about Java inheritance is <strong>true</strong>?',
        [
            ('A class may extend at most one direct superclass.', True),
            ('A class may extend any number of superclasses.', False),
            ('Constructors are inherited by subclasses.', False),
            ('A class without an <code>extends</code> clause has no superclass.', False),
        ],
        'Java has single class inheritance. Constructors are not inherited, and a class with no <code>extends</code> clause silently extends <code>java.lang.Object</code>.'
    ),
    (
        'multiple_choice',
        'Which of the following is a <strong>legal override</strong> of <code>public Number get() throws IOException</code> declared in the parent class?',
        [
            ('<code>public Integer get() throws FileNotFoundException</code>', True),
            ('<code>protected Number get() throws IOException</code>', False),
            ('<code>public Number get() throws Exception</code>', False),
            ('<code>public Number get(int n) throws IOException</code>', False),
        ],
        'A valid override may return a <em>covariant</em> subtype, must not narrow access (<code>protected</code> &lt; <code>public</code>), and may not throw broader checked exceptions. The last option changes the parameter list, so it is an overload, not an override.'
    ),
    (
        'multiple_choice',
        'Given <code>Animal a = new Dog();</code>, where <code>Dog extends Animal</code> and both define <code>speak()</code>, what does <code>a.speak()</code> invoke?',
        [
            ('<code>Dog.speak()</code> &mdash; dispatched at runtime on the object\'s actual type.', True),
            ('<code>Animal.speak()</code> &mdash; dispatched at compile time on the reference type.', False),
            ('Whichever was declared first in the source file.', False),
            ('It does not compile; a cast is required.', False),
        ],
        'Method calls are polymorphic: the compiler verifies them against the reference type, but the JVM dispatches to the implementation on the actual object.'
    ),
    (
        'true_false',
        'A subclass constructor may have <strong>both</strong> <code>this(&hellip;)</code> and <code>super(&hellip;)</code> as its first two statements.',
        [
            ('False', True),
            ('True', False),
        ],
        'Each constructor may contain at most one of them, and it must be the very first statement. The compiler inserts an implicit <code>super();</code> only when neither is written.'
    ),
    (
        'multiple_choice',
        'Which line will <strong>not</strong> compile?<br><pre><code>Animal a = new Dog();    // 1\nDog d   = new Animal();  // 2\nAnimal b = (Animal) new Dog();  // 3\nDog e   = (Dog) a;       // 4</code></pre>',
        [
            ('Line 2', True),
            ('Line 1', False),
            ('Line 3', False),
            ('Line 4', False),
        ],
        'A <code>Dog</code> reference cannot directly hold a plain <code>Animal</code> object &mdash; a downcast is required (and would still fail at runtime here). Line 4 compiles because the compiler trusts the cast; if <code>a</code> is really a <code>Dog</code> it also succeeds at runtime.'
    ),
    (
        'multiple_choice',
        'Which statement about <code>abstract</code> classes is <strong>true</strong>?',
        [
            ('They may declare constructors, fields and concrete methods, but cannot be instantiated with <code>new</code>.', True),
            ('Every method in an abstract class must be abstract.', False),
            ('An abstract class may also be declared <code>final</code>.', False),
            ('A non-abstract subclass need not implement inherited abstract methods.', False),
        ],
        '<code>abstract</code> classes are partial implementations: state and concrete behaviour are allowed, but you cannot say <code>new</code> on them. <code>abstract final</code> is a contradiction the compiler rejects.'
    ),
    (
        'multiple_choice',
        'What is printed?<br><pre><code>class A { String name = "A"; String who() { return name; } }\nclass B extends A { String name = "B"; String who() { return name; } }\n\nA x = new B();\nSystem.out.println(x.name + " " + x.who());</code></pre>',
        [
            ('<code>A B</code>', True),
            ('<code>B B</code>', False),
            ('<code>A A</code>', False),
            ('<code>B A</code>', False),
        ],
        'Fields are resolved by the <em>reference</em> type (<code>A</code> &rarr; <code>"A"</code>), but methods are dispatched by the <em>object</em> type (<code>B</code>\'s override returns its own <code>"B"</code>).'
    ),
    (
        'multiple_choice',
        'Which statement about interfaces (Java&nbsp;8 / OCA level) is <strong>true</strong>?',
        [
            ('A class may implement many interfaces but extend only one class.', True),
            ('An interface may extend at most one other interface.', False),
            ('Interface methods are implicitly <code>protected abstract</code>.', False),
            ('Fields declared in an interface are instance fields of the implementing class.', False),
        ],
        'Java supports multiple <em>interface</em> inheritance &mdash; a class may implement many interfaces (and an interface may extend several others). Interface methods are implicitly <code>public abstract</code>; fields are implicitly <code>public static final</code>.'
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
                order=14,
                points=1.0,
            )
            db.session.add(lesson)
            db.session.flush()
            print(f'inserted lesson {lesson.id}')

        quiz = Quiz.query.filter_by(course_id=course.id, title=QUIZ_TITLE).first()
        if not quiz:
            quiz = Quiz(course_id=course.id, title=QUIZ_TITLE,
                        description='Check your understanding of inheritance, overriding, polymorphism, casting, abstract classes and interfaces.')
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
            exam.order = 15
            print(f'updated exam lesson {exam.id}')
        else:
            exam = Lesson(
                title=EXAM_LESSON_TITLE,
                content='',
                course_id=course.id,
                content_type='exam',
                quiz_id=quiz.id,
                order=15,
                points=1.0,
            )
            db.session.add(exam)
            db.session.flush()
            print(f'inserted exam lesson {exam.id}')

        db.session.commit()
        print('done.')


if __name__ == '__main__':
    upsert()
