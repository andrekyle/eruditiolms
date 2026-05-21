LESSON_HTML = """
<h2>Working with Inheritance</h2>
<p>Inheritance is a fundamental mechanism in object-oriented programming that allows a class to inherit attributes and methods from another class. In Java, inheritance promotes code reuse, enables polymorphism, and creates hierarchical relationships between classes.</p>

<h3>What is Inheritance?</h3>
<p>Inheritance allows you to create a new class based on an existing class. The <strong>subclass</strong> (or child class) inherits all the members of the <strong>superclass</strong> (or parent class). This mechanism reduces code duplication and establishes an <em>is-a</em> relationship.</p>
<p><strong>Benefits of inheritance:</strong></p>
<ul>
<li>Code reuse — common functionality is written once in the superclass</li>
<li>Polymorphism — subclasses can override methods to provide specialized behavior</li>
<li>Maintainability — changes to common code happen in one place</li>
<li>Extensibility — new classes can extend existing ones without modification</li>
</ul>

<h3>The Implicit Superclass: java.lang.Object</h3>
<p>In Java, every class automatically inherits from <code>java.lang.Object</code>, whether explicitly declared or not. If a class does not use the <code>extends</code> keyword, the compiler inserts <code>extends Object</code> implicitly.</p>
<p>Key methods inherited from <code>Object</code>:</p>
<ul>
<li><code>toString()</code> — returns a string representation of the object</li>
<li><code>equals(Object)</code> — compares objects for equality</li>
<li><code>hashCode()</code> — returns a hash code for the object</li>
<li><code>getClass()</code> — returns the runtime class of the object</li>
<li><code>clone()</code> — creates a shallow copy of the object</li>
</ul>

<h3>The extends Keyword</h3>
<p>Use the <code>extends</code> keyword to declare that a class inherits from another class:</p>
<pre><code class="language-java">public class Animal {
    public void eat() {
        System.out.println(&quot;Animal is eating&quot;);
    }
}

public class Dog extends Animal {
    public void bark() {
        System.out.println(&quot;Dog barks&quot;);
    }
}</code></pre>
<p><strong>Important:</strong> Java supports <em>only single inheritance</em> — a class can extend only one other class. This prevents the &quot;diamond problem&quot; found in multiple inheritance.</p>

<h3>Polymorphism and Method Overriding</h3>
<p>Polymorphism allows objects of different subclasses to be treated through a common superclass reference. The actual method called is determined at runtime based on the <strong>object type</strong>, not the <strong>reference type</strong>.</p>
<pre><code class="language-java">public class Animal {
    public void makeSound() {
        System.out.println(&quot;Generic animal sound&quot;);
    }
}

public class Cat extends Animal {
    @Override
    public void makeSound() {
        System.out.println(&quot;Meow&quot;);
    }
}

Animal a = new Cat();
a.makeSound();  // Prints &quot;Meow&quot;</code></pre>
<p>The reference is of type <code>Animal</code>, but the actual object is a <code>Cat</code>. The correct <code>makeSound()</code> method is invoked based on the <strong>actual object type</strong>.</p>

<h3>Method Overriding Rules</h3>
<p>When a subclass provides a new implementation of a superclass method, these rules must be followed:</p>
<table border="1" cellpadding="8">
<tr><th>Rule</th><th>Requirement</th></tr>
<tr><td>Signature</td><td>Must match exactly (same name, parameters)</td></tr>
<tr><td>Access Level</td><td>Cannot be more restrictive</td></tr>
<tr><td>Return Type</td><td>Can be a covariant subtype (Java 5+)</td></tr>
<tr><td>Exceptions</td><td>Can throw same, fewer, or more specific exceptions</td></tr>
<tr><td>Annotation</td><td><code>@Override</code> optional but recommended</td></tr>
</table>
<pre><code class="language-java">public class Vehicle {
    public Object getInfo() {
        return &quot;Vehicle&quot;;
    }
}

public class Car extends Vehicle {
    @Override
    public String getInfo() {  // Valid: String is subtype of Object
        return &quot;Car&quot;;
    }
}</code></pre>

<h3>Method Overriding vs Overloading</h3>
<table border="1" cellpadding="8">
<tr><th>Aspect</th><th>Overriding</th><th>Overloading</th></tr>
<tr><td>Definition</td><td>Subclass new implementation of superclass method</td><td>Multiple methods same name, different parameters</td></tr>
<tr><td>Inheritance</td><td>Requires inheritance relationship</td><td>Same or inherited class</td></tr>
<tr><td>Signature</td><td>Must be identical</td><td>Must differ</td></tr>
<tr><td>Binding</td><td>Dynamic (runtime)</td><td>Static (compile-time)</td></tr>
</table>

<h3>Constructor Chaining with super()</h3>
<p>Constructors are NOT inherited. A subclass constructor can call the superclass constructor using <code>super()</code>. If not explicitly called, Java inserts a call to the no-argument superclass constructor.</p>
<pre><code class="language-java">public class Animal {
    private String name;
    public Animal(String name) {
        this.name = name;
    }
}

public class Dog extends Animal {
    private String breed;
    public Dog(String name, String breed) {
        super(name);  // MUST be first statement
        this.breed = breed;
    }
}</code></pre>
<p><strong>Key rules:</strong></p>
<ul>
<li><code>super()</code> must be the <strong>first statement</strong> in a constructor</li>
<li>If superclass has no no-argument constructor, subclass must explicitly call <code>super(...)</code></li>
<li>If <code>super()</code> not called explicitly, compiler inserts <code>super()</code></li>
</ul>

<h3>Abstract Classes and Interfaces</h3>
<p><strong>Abstract Classes:</strong> Cannot be instantiated directly. Define common behavior and force subclasses to implement abstract methods.</p>
<pre><code class="language-java">public abstract class Shape {
    abstract double getArea();
    public void describe() {
        System.out.println(&quot;Area: &quot; + getArea());
    }
}

public class Circle extends Shape {
    private double radius;
    @Override
    double getArea() {
        return Math.PI * radius * radius;
    }
}</code></pre>
<p><strong>Interfaces (Java 8):</strong> A contract specifying methods a class must implement. Since Java 8, interfaces support <code>default</code> and <code>static</code> methods with implementation.</p>
<pre><code class="language-java">public interface Drawable {
    void draw();
    default void erase() { System.out.println(&quot;Erasing&quot;); }
    static void info() { System.out.println(&quot;Drawable&quot;); }
}</code></pre>

<h3>Casting Between Types</h3>
<p><strong>Upcasting:</strong> Converting subclass reference to superclass reference. Implicit and always safe.</p>
<pre><code class="language-java">Dog dog = new Dog();
Animal animal = dog;  // Implicit upcasting</code></pre>
<p><strong>Downcasting:</strong> Converting superclass reference to subclass reference. Explicit and may throw <code>ClassCastException</code>.</p>
<pre><code class="language-java">Animal animal = new Dog();
Dog dog = (Dog) animal;  // Safe — animal is actually a Dog

Animal animal2 = new Cat();
Dog dog2 = (Dog) animal2;  // ClassCastException!</code></pre>
<p>Use <code>instanceof</code> to test type before downcasting:</p>
<pre><code class="language-java">if (animal instanceof Dog) {
    Dog dog = (Dog) animal;
}</code></pre>

<h3>Final Classes, Methods, and Variables</h3>
<p>The <code>final</code> keyword prevents modification:</p>
<ul>
<li><code>final class</code> — cannot be subclassed</li>
<li><code>final method</code> — cannot be overridden</li>
<li><code>final variable</code> — cannot be reassigned</li>
</ul>
<pre><code class="language-java">public final class ImmutableClass { }
public class Parent {
    public final void criticalMethod() { }
    private final int value = 42;
}</code></pre>
"""

QUESTIONS = [
    (
        "<strong>Question 1:</strong> Which statement is true regarding the relationship between any user-defined class and the Object class?",
        [
            ("Every class implicitly inherits from Object, even if extends is not used.", True),
            ("Only classes that explicitly extend Object inherit its methods.", False),
            ("Object is a subclass of all other classes.", False),
            ("A class must implement the Object interface to use inheritance.", False),
        ],
        "Java automatically makes Object the superclass of every class. The compiler inserts <code>extends Object</code> if no other superclass is specified."
    ),
    (
        "<strong>Question 2:</strong> What is printed by the following code?<br><pre><code class=\"language-java\">class Shape { public void draw() { System.out.println(&quot;Shape&quot;); } }\nclass Circle extends Shape { public void draw() { System.out.println(&quot;Circle&quot;); } }\npublic class Test {\n    public static void main(String[] args) {\n        Shape s = new Circle();\n        s.draw();\n    }\n}</code></pre>",
        [
            ("Circle", True),
            ("Shape", False),
            ("Shape Circle", False),
            ("Compilation error", False),
        ],
        "This demonstrates polymorphism. Although the reference type is Shape, the actual object is a Circle. The method invoked is determined by the <strong>actual object type</strong> at runtime, so Circle's draw() method executes."
    ),
    (
        "<strong>Question 3:</strong> Which declaration is a valid override of <code>public Object getValue()</code> from the superclass?",
        [
            ("public String getValue() { }", True),
            ("protected Object getValue() { }", False),
            ("public Object getValue(int x) { }", False),
            ("public void getValue() { }", False),
        ],
        "A method can override a superclass method using a <strong>covariant return type</strong> — a return type that is a subclass of the original. String is a subclass of Object, so this override is valid."
    ),
    (
        "<strong>Question 4:</strong> What is the difference between method overriding and method overloading?",
        [
            ("Overriding: same method signature in subclass; Overloading: same method name, different parameters", True),
            ("Overriding: different class; Overloading: same class", False),
            ("Overriding happens at compile-time; Overloading happens at runtime", False),
            ("Overriding requires extends; Overloading requires implements", False),
        ],
        "Method overriding occurs when a subclass provides a new implementation of an inherited method with the same signature. Overloading occurs when multiple methods have the same name but different parameters."
    ),
    (
        "<strong>Question 5:</strong> Consider this code. What is the output?<br><pre><code class=\"language-java\">public class Parent { public static void msg() { System.out.println(&quot;Parent&quot;); } }\npublic class Child extends Parent { public static void msg() { System.out.println(&quot;Child&quot;); } }\npublic class Test {\n    public static void main(String[] args) {\n        Parent p = new Child();\n        p.msg();\n    }\n}</code></pre>",
        [
            ("Parent", True),
            ("Child", False),
            ("Parent Child", False),
            ("Compilation error", False),
        ],
        "Static methods are <strong>hidden</strong>, not overridden. The method executed is determined by the <strong>reference type</strong> at compile-time, not the object type. Since p is of type Parent, Parent.msg() is called."
    ),
    (
        "<strong>Question 6:</strong> Which statement about constructor inheritance is correct?",
        [
            ("Constructors are not inherited, but a subclass constructor can call super() to invoke the superclass constructor.", True),
            ("Constructors are automatically inherited by all subclasses.", False),
            ("The super() call must be the second statement in a constructor.", False),
            ("Subclass constructors do not need to call super().", False),
        ],
        "Constructors are not inherited. However, subclasses can explicitly call the superclass constructor using <code>super()</code>, which must be the <strong>first statement</strong> if present."
    ),
    (
        "<strong>Question 6:</strong> What will happen when executing this code?<br><pre><code class=\"language-java\">class Animal { }\nclass Dog extends Animal { }\npublic class Test {\n    public static void main(String[] args) {\n        Animal a = new Dog();\n        Cat c = (Cat) a;  // Cat is another class extending Animal\n    }\n}</code></pre>",
        [
            ("ClassCastException is thrown at runtime.", True),
            ("The code compiles and runs successfully.", False),
            ("Compilation error occurs.", False),
            ("The code prints a warning message.", False),
        ],
        "Downcasting from Animal to Cat will compile because both are in the inheritance hierarchy. However, at runtime, the actual object is a Dog, not a Cat, so a ClassCastException is thrown."
    ),
    (
        "<strong>Question 8:</strong> Which statement is true about abstract classes and interfaces in Java 8?",
        [
            ("Abstract classes define behavior with abstract methods; interfaces can now contain default and static methods with implementation.", True),
            ("Interfaces cannot have any methods with implementation.", False),
            ("Abstract classes can implement multiple other classes.", False),
            ("Both abstract classes and interfaces can be instantiated if they have concrete methods.", False),
        ],
        "In Java 8, interfaces gained the ability to include <code>default</code> and <code>static</code> methods with implementation, making them more flexible. Abstract classes remain uninstantiable but define behavior that subclasses must implement."
    ),
]