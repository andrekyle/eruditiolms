LESSON_HTML = """
<h2>Working with Methods and Encapsulation</h2>

<h3>Understanding Methods</h3>
<p>A method is a code block that performs a specific task. Methods allow you to organize code into reusable units. Every method must have a return type (including <code>void</code>), a name, and parameters (which may be empty).</p>
<p><strong>Method signature</strong> consists of the method name and parameter list (not including return type). Two methods in the same class may have the same name if their parameter lists differ—this is called <em>method overloading</em>.</p>

<h3>Method Parameters and Return Types</h3>
<p>Methods accept parameters (arguments) and may return a value. Parameters are separated by commas in the method definition.</p>
<pre><code class="language-java">public int add(int a, int b) {
    return a + b;
}

public void printMessage(String msg) {
    System.out.println(msg);  // returns nothing
}

public String getName() {
    return &quot;John&quot;;
}
</code></pre>
<p>When a method is declared with a return type other than <code>void</code>, it <strong>must</strong> return a value of that type (or a compatible type) using the <code>return</code> statement.</p>

<h3>Method Overloading</h3>
<p>Method overloading enables multiple methods with the same name, provided they have different parameter lists. The <strong>method resolution</strong> process selects the most specific method based on argument types at compile time.</p>
<pre><code class="language-java">public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
    
    public double add(double a, double b) {
        return a + b;
    }
    
    public int add(int a, int b, int c) {
        return a + b + c;
    }
}
</code></pre>
<p>Overloading rules: methods must have the same name, but the parameter list must differ in number, type, or order. <strong>Return type alone does not distinguish overloaded methods</strong>.</p>

<h3>The static Keyword</h3>
<p>The <code>static</code> keyword designates a method or field as belonging to the <em>class</em> rather than to individual instances. Static members are shared by all instances of the class and can be accessed without creating an object.</p>
<p><strong>Static methods:</strong> called on the class name, not on objects. They cannot access instance fields or call instance methods directly.</p>
<pre><code class="language-java">public class Utility {
    public static int square(int x) {
        return x * x;
    }
}

// Calling static method
int result = Utility.square(5);  // Does not require an object
</code></pre>
<p><strong>Static fields:</strong> shared by all instances. Changes to a static field affect all instances.</p>
<pre><code class="language-java">public class Counter {
    public static int count = 0;
    
    public Counter() {
        count++;
    }
}

Counter c1 = new Counter();
Counter c2 = new Counter();
System.out.println(Counter.count);  // Output: 2
</code></pre>

<h3>Constructors</h3>
<p>A constructor is a special method that runs when an object is instantiated. Constructors initialize object state. A constructor has the same name as the class and <strong>no return type</strong> (not even <code>void</code>).</p>
<p>If you do not define a constructor, Java provides a <em>default (no-arg) constructor</em> that calls the superclass constructor and initializes fields to default values (0 for numbers, <code>false</code> for booleans, <code>null</code> for references).</p>
<pre><code class="language-java">public class Person {
    private String name;
    private int age;
    
    // User-defined constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
</code></pre>

<h3>Constructor Overloading</h3>
<p>You can define multiple constructors with different parameter lists—just like method overloading. This allows objects to be created in different ways.</p>
<pre><code class="language-java">public class Book {
    private String title;
    private String author;
    
    public Book() {
        this(&quot;Unknown&quot;, &quot;Unknown&quot;);  // calls another constructor
    }
    
    public Book(String title) {
        this(title, &quot;Unknown&quot;);
    }
    
    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }
}
</code></pre>
<p>The <code>this()</code> call must be the <strong>first statement</strong> in a constructor if used.</p>

<h3>Access Modifiers</h3>
<p>Access modifiers control the visibility of classes, methods, and fields. Java provides four levels of access:</p>
<table>
<thead>
<tr>
<th>Modifier</th>
<th>Same Class</th>
<th>Same Package</th>
<th>Subclass</th>
<th>Outside Package</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>public</strong></td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
</tr>
<tr>
<td><strong>protected</strong></td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✗ (only via subclass)</td>
</tr>
<tr>
<td><strong>package-private (default)</strong></td>
<td>✓</td>
<td>✓</td>
<td>✗</td>
<td>✗</td>
</tr>
<tr>
<td><strong>private</strong></td>
<td>✓</td>
<td>✗</td>
<td>✗</td>
<td>✗</td>
</tr>
</tbody>
</table>
<p><em>Package-private</em> (no modifier) is the default access level when no modifier is specified.</p>

<h3>Encapsulation</h3>
<p>Encapsulation is the principle of bundling data (fields) and methods into a single unit and hiding internal details from the outside world. A well-encapsulated class uses <code>private</code> fields and provides <code>public</code> getter and setter methods to control access.</p>
<pre><code class="language-java">public class Student {
    private String name;
    private int gpa;
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        if (name != null &amp;&amp; !name.isEmpty()) {
            this.name = name;
        }
    }
    
    public int getGpa() {
        return gpa;
    }
    
    public void setGpa(int gpa) {
        if (gpa &gt;= 0 &amp;&amp; gpa &lt;= 100) {
            this.gpa = gpa;
        }
    }
}
</code></pre>
<p>Benefits of encapsulation: <strong>data validation</strong>, hiding implementation details, and enabling future changes without affecting external code.</p>

<h3>Pass-by-Value Semantics</h3>
<p>Java passes both primitives and object references by value. When you pass a primitive, a copy of its value is sent. When you pass an object reference, a copy of the reference is sent, not the object itself.</p>
<p><strong>For primitives:</strong> changes inside the method do not affect the original variable.</p>
<pre><code class="language-java">public void increment(int x) {
    x++;
}

int num = 5;
increment(num);
System.out.println(num);  // Output: 5 (unchanged)
</code></pre>
<p><strong>For objects:</strong> the method receives a copy of the reference. Changing the object's state affects the original. Reassigning the reference inside the method does not affect the original reference.</p>
<pre><code class="language-java">public void modifyList(List&lt;String&gt; list) {
    list.add(&quot;new item&quot;);  // Affects the original list
    list = new ArrayList&lt;&gt;();  // Local reassignment only
}

List&lt;String&gt; myList = new ArrayList&lt;&gt;();
modifyList(myList);
System.out.println(myList.size());  // myList still has the added item
</code></pre>

<h3>Variable Scope and Shadowing</h3>
<p>The scope of a variable is the region of code where it is accessible. Java defines four scope levels: <strong>block</strong>, <strong>method</strong>, <strong>instance</strong>, and <strong>class (static)</strong>.</p>
<ul>
<li><strong>Block scope:</strong> Variables declared in a block are accessible only within that block.</li>
<li><strong>Method scope:</strong> Variables declared in a method are accessible throughout the method.</li>
<li><strong>Instance scope:</strong> Non-static fields of a class are accessible throughout the class.</li>
<li><strong>Class scope:</strong> Static fields and methods are accessible throughout the class and via the class name.</li>
</ul>
<p><strong>Shadowing</strong> occurs when a variable declared in an inner scope has the same name as a variable in an outer scope, effectively hiding the outer variable within that scope.</p>
<pre><code class="language-java">public class ShadowExample {
    private String name = &quot;Class Level&quot;;  // instance scope
    
    public void printName() {
        String name = &quot;Method Level&quot;;      // method scope (shadows instance field)
        System.out.println(name);           // Output: Method Level
        System.out.println(this.name);      // Output: Class Level (explicit access)
    }
}
</code></pre>

<h3>Variable Arguments (Varargs)</h3>
<p>Varargs allow a method to accept a variable number of arguments of the same type. The syntax is <code>type... name</code>, where the three dots indicate varargs.</p>
<pre><code class="language-java">public int sum(int... numbers) {
    int total = 0;
    for (int num : numbers) {
        total += num;
    }
    return total;
}

sum(1, 2, 3);       // 3 arguments
sum(10, 20, 30, 40);  // 4 arguments
sum();              // 0 arguments
</code></pre>
<p>Inside the method, varargs are treated as an array. <strong>Varargs must be the last parameter</strong> if other parameters are present.</p>
<pre><code class="language-java">public void process(String prefix, int... values) {
    // prefix is a String, values is an int array
    for (int val : values) {
        System.out.println(prefix + val);
    }
}
</code></pre>
"""

QUESTIONS = [
    (
        "<p>Which of the following correctly demonstrates proper method overloading?</p>",
        [
            (
                "<code>public int getValue() { return 1; }</code> and <code>public double getValue() { return 1.0; }</code>",
                False
            ),
            (
                "<code>public void process(int x) { }</code> and <code>public void process(int x, int y) { }</code>",
                True
            ),
            (
                "<code>public int add(int a, int b) { }</code> and <code>public int add(int a, int b) { }</code>",
                False
            ),
            (
                "<code>private static void test(String s) { }</code> and <code>public static void test(String s) { }</code>",
                False
            ),
        ],
        "Method overloading requires different parameter lists (different number, type, or order of parameters). Return type alone does not distinguish overloaded methods. Only option B has a different parameter count."
    ),
    (
        "<p>What is the output of this code?</p><pre><code class=\"language-java\">public class Test {<br/>&nbsp;&nbsp;public static int count = 0;<br/>&nbsp;&nbsp;public Test() { count++; }<br/>&nbsp;&nbsp;public static void main(String[] args) {<br/>&nbsp;&nbsp;&nbsp;&nbsp;Test t1 = new Test();<br/>&nbsp;&nbsp;&nbsp;&nbsp;Test t2 = new Test();<br/>&nbsp;&nbsp;&nbsp;&nbsp;Test t3 = new Test();<br/>&nbsp;&nbsp;&nbsp;&nbsp;System.out.println(count);<br/>&nbsp;&nbsp;}<br/>}</code></pre>",
        [
            ("1", False),
            ("2", False),
            ("3", True),
            ("0", False),
        ],
        "The static field 'count' is shared by all instances of the Test class. Each constructor call increments 'count' by 1. Three Test objects are created, so 'count' is incremented three times, resulting in output 3."
    ),
    (
        "<p>What is the output of this code?</p><pre><code class=\"language-java\">public void modify(int x, List&lt;String&gt; list) {<br/>&nbsp;&nbsp;x = 99;<br/>&nbsp;&nbsp;list.add(&quot;added&quot;);<br/>&nbsp;&nbsp;list = new ArrayList&lt;&gt;();<br/>}<br/>int num = 5;<br/>List&lt;String&gt; myList = new ArrayList&lt;&gt;();<br/>myList.add(&quot;original&quot;);<br/>modify(num, myList);<br/>System.out.println(num + &quot;,&quot; + myList.size());</code></pre>",
        [
            ("99, 0", False),
            ("5, 1", True),
            ("99, 1", False),
            ("5, 0", False),
        ],
        "Java passes both primitives and object references by value. The primitive 'num' is unchanged (still 5). The method receives a copy of the reference to myList and adds an item, but reassigning 'list' to a new ArrayList does not affect the original reference myList. Thus, myList.size() is 1."
    ),
    (
        "<p>Which access modifier allows access from the same package and from subclasses in different packages?</p>",
        [
            ("private", False),
            ("package-private (default)", False),
            ("protected", True),
            ("public", False),
        ],
        "The 'protected' modifier allows access from within the same package and from subclasses, even if those subclasses are in a different package. This is the distinguishing feature of protected access."
    ),
    (
        "<p>A class has a private field 'balance' and public getter/setter methods. What principle does this demonstrate?</p>",
        [
            ("Inheritance", False),
            ("Polymorphism", False),
            ("Encapsulation", True),
            ("Static binding", False),
        ],
        "Encapsulation involves bundling data (private fields) and methods (public getters/setters) into a single unit, hiding internal implementation details and providing controlled access to the data."
    ),
    (
        "<p>What will be printed by this code?</p><pre><code class=\"language-java\">public class Shadow {<br/>&nbsp;&nbsp;private int value = 10;<br/>&nbsp;&nbsp;public void test() {<br/>&nbsp;&nbsp;&nbsp;&nbsp;int value = 20;<br/>&nbsp;&nbsp;&nbsp;&nbsp;System.out.println(value);<br/>&nbsp;&nbsp;&nbsp;&nbsp;System.out.println(this.value);<br/>&nbsp;&nbsp;}<br/>}<br/>Shadow s = new Shadow();<br/>s.test();</code></pre>",
        [
            ("10, 10", False),
            ("10, 20", False),
            ("20, 10", True),
            ("20, 20", False),
        ],
        "The local variable 'value' (20) shadows the instance field 'value' (10). The first println uses the local variable (20). The second println uses 'this.value' to explicitly access the instance field (10)."
    ),
    (
        "<p>What is the output of calling the sum method with these arguments?</p><pre><code class=\"language-java\">public int sum(int... nums) {<br/>&nbsp;&nbsp;int total = 0;<br/>&nbsp;&nbsp;for (int n : nums) { total += n; }<br/>&nbsp;&nbsp;return total;<br/>}<br/>System.out.println(sum(5, 10, 15) + sum(1) + sum());</code></pre>",
        [
            ("31", True),
            ("36", False),
            ("30", False),
            ("46", False),
        ],
        "Varargs are passed as an array. sum(5, 10, 15) returns 30, sum(1) returns 1, and sum() (called with no arguments) treats nums as an empty array and returns 0. Total: 30 + 1 + 0 = 31."
    ),
    (
        "<p>Given two packages: <code>com.example.shapes</code> (contains class <code>Circle</code>) and <code>com.example.app</code> (contains class <code>Main</code>). If Circle has a protected method, can Main call that method directly?</p>",
        [
            ("Yes, because protected allows public access", False),
            ("No, protected access is limited to the same package or subclasses", True),
            ("Yes, because both are in the com.example package", False),
            ("No, protected methods cannot be called at all", False),
        ],
        "Protected members are accessible only from the same package OR from subclasses (even in different packages). Since Main is neither in the same package nor a subclass of Circle, it cannot call a protected method of Circle."
    ),
]