LESSON_HTML = """
<h2>Working with Java Data Types</h2>

<h3>Overview</h3>
<p>Java data types define what kind of values variables can hold. Java has two main categories: <strong>primitive types</strong> (built-in, store raw values) and <strong>reference types</strong> (store addresses to objects in memory).</p>

<h3>The Eight Primitive Types</h3>
<p>Java defines exactly eight primitive data types. Each has a fixed size and range of valid values:</p>
<table border="1" cellpadding="8" cellspacing="0">
<tr><th>Type</th><th>Size</th><th>Range</th><th>Default</th></tr>
<tr><td><code>byte</code></td><td>8 bits</td><td>-128 to 127</td><td>0</td></tr>
<tr><td><code>short</code></td><td>16 bits</td><td>-32,768 to 32,767</td><td>0</td></tr>
<tr><td><code>int</code></td><td>32 bits</td><td>-2,147,483,648 to 2,147,483,647</td><td>0</td></tr>
<tr><td><code>long</code></td><td>64 bits</td><td>-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807</td><td>0L</td></tr>
<tr><td><code>float</code></td><td>32 bits</td><td>IEEE 754 single-precision floating-point</td><td>0.0f</td></tr>
<tr><td><code>double</code></td><td>64 bits</td><td>IEEE 754 double-precision floating-point</td><td>0.0d</td></tr>
<tr><td><code>char</code></td><td>16 bits</td><td>0 to 65,535 (Unicode characters)</td><td><code>'\\u0000'</code></td></tr>
<tr><td><code>boolean</code></td><td>JVM-dependent</td><td><code>true</code> or <code>false</code></td><td>false</td></tr>
</table>

<h3>Declaring and Initializing Variables</h3>
<p>Variables must be declared with a type before use. Local variables <strong>must be explicitly initialized</strong> before reading their value, while instance variables in classes receive default values automatically.</p>
<pre><code class="language-java">int age = 25;           // declaration and initialization
double salary;
salary = 45000.50;      // initialization after declaration
boolean isActive = true;</code></pre>

<h3>Integer Literals</h3>
<p>Integer values can be written in decimal (base 10), hexadecimal (base 16, prefix <code>0x</code>), octal (base 8, prefix <code>0</code>), or binary (base 2, prefix <code>0b</code>). Use suffix <code>L</code> for <code>long</code> values; suffix is required for large values exceeding <code>int</code> range:</p>
<pre><code class="language-java">int decimal = 100;
int hexadecimal = 0xFF;     // 255 in decimal
int octal = 0755;           // 493 in decimal
int binary = 0b1010;        // 10 in decimal
long largeNum = 1234567890L;
long underscores = 1_000_000L;  // underscores improve readability</code></pre>

<h3>Floating-Point and Character Literals</h3>
<p>Floating-point literals default to <code>double</code>; use suffix <code>f</code> or <code>F</code> for <code>float</code>. Character literals use single quotes and represent a single Unicode character:</p>
<pre><code class="language-java">float price = 19.99f;       // f suffix required
double rate = 3.14;         // default double
char letter = 'A';
char escape = '\\n';        // escape sequence for newline
char unicode = '\\u0041';    // Unicode 'A'</code></pre>

<h3>Primitive vs. Reference Types</h3>
<p>Primitive variables store the actual value directly in memory. Reference variables store an <em>address</em> to an object located elsewhere in memory (the heap). Assigning a primitive copies the value; assigning a reference copies the address, making both variables point to the same object.</p>
<pre><code class="language-java">int x = 10;
int y = x;          // y contains 10 (separate value)
x = 20;             // does not affect y

String str1 = new String(&quot;Hello&quot;);
String str2 = str1; // str2 points to the same object
str1 = new String(&quot;World&quot;);  // str1 now points to a different object</code></pre>

<h3>Object Lifecycle and Garbage Collection</h3>
<p>Objects are created with the <code>new</code> keyword and exist on the heap. When a reference variable is reassigned or goes out of scope, the object may become <em>unreachable</em> (no references point to it). The garbage collector automatically reclaims memory from unreachable objects; you cannot force garbage collection in Java.</p>
<pre><code class="language-java">Person p = new Person(&quot;Alice&quot;);   // object created
p = null;                          // dereference by assigning null
// object is now unreachable and eligible for garbage collection</code></pre>

<h3>Default Values and Local Variable Initialization</h3>
<p>Instance fields and static variables receive default values based on type: numeric primitives default to 0, booleans to <code>false</code>, and references to <code>null</code>. <strong>Local variables do not receive default values</strong> and must be explicitly initialized before use, or a compile error occurs.</p>
<pre><code class="language-java">class Example {
    int count;           // instance variable: default 0
    boolean flag;        // instance variable: default false
    String name;         // instance variable: default null
    
    void method() {
        int local;       // local variable: NO default
        System.out.println(local);  // COMPILE ERROR
    }
}</code></pre>

<h3>Wrapper Classes and Autoboxing</h3>
<p>Java provides wrapper classes to treat primitives as objects: <code>Integer</code>, <code>Long</code>, <code>Float</code>, <code>Double</code>, <code>Short</code>, <code>Byte</code>, <code>Character</code>, and <code>Boolean</code>. <strong>Autoboxing</strong> automatically converts a primitive to its wrapper (e.g., <code>int</code> to <code>Integer</code>); <strong>unboxing</strong> reverses this. Wrapper classes provide utility methods and allow primitives to work with collections.</p>
<pre><code class="language-java">int primitiveInt = 42;
Integer wrappedInt = primitiveInt;   // autoboxing
int unwrapped = wrappedInt;          // unboxing

Integer count = 100;      // autoboxing
if (count &lt; 50) { }       // unboxing to compare</code></pre>

<h3>String Literal Pool</h3>
<p>String literals in Java are stored in a special memory region called the <em>string literal pool</em>. When you create a string using a literal (e.g., <code>"Hello"</code>), Java checks if an identical string already exists in the pool and reuses it. Creating a string with <code>new String("Hello")</code> creates a new object in heap memory, distinct from the pool entry.</p>
<pre><code class="language-java">String s1 = "Hello";        // pool
String s2 = "Hello";        // same object as s1
String s3 = new String("Hello");  // different object
System.out.println(s1 == s2);  // true (same reference)
System.out.println(s1 == s3);  // false (different objects)</code></pre>

<h3>Reading and Writing Object Fields</h3>
<p>Use the dot operator (<code>.</code>) to access fields and methods on an object. Fields can be read (retrieved) and written (assigned) if accessible according to their access modifiers.</p>
<pre><code class="language-java">class Employee {
    public String name;
    public double salary;
}

Employee emp = new Employee();
emp.name = "John";          // write to field
emp.salary = 50000.0;       // write to field
System.out.println(emp.name);  // read from field</code></pre>
"""

QUESTIONS = [
    (
        "<p>What is the size and default value of a <code>byte</code> variable?</p>",
        [
            ("<code>byte</code> is 8 bits with default value 0", True),
            ("<code>byte</code> is 16 bits with default value 0", False),
            ("<code>byte</code> is 8 bits with default value null", False),
            ("<code>byte</code> is 32 bits with default value 0", False),
        ],
        "A <code>byte</code> is always 8 bits in Java and holds values from -128 to 127. When declared as an instance variable, its default value is 0. Bytes do not have a null default; null applies only to reference types."
    ),
    (
        "<p>Which of the following is a <strong>valid</strong> integer literal in Java?</p>",
        [
            ("<code>int x = 0b1111_0000;</code>", True),
            ("<code>int x = 0888;</code>", False),
            ("<code>int x = 1.5e2;</code>", False),
            ("<code>int x = 0xGG;</code>", False),
        ],
        "Binary literals use the <code>0b</code> prefix and can include underscores for readability. Octal literals cannot contain the digit 8, hexadecimal cannot use letters beyond F, and floating-point literals (like <code>1.5e2</code>) are not valid for <code>int</code> types."
    ),
    (
        "<p>Consider this code snippet:<br><code>String a = \"Test\";<br>String b = \"Test\";<br>String c = new String(\"Test\");<br>System.out.println(a == b);</code><br>What is printed?</p>",
        [
            ("<code>true</code>", True),
            ("<code>false</code>", False),
            ("A compile error occurs", False),
            ("A runtime exception occurs", False),
        ],
        "Both <code>a</code> and <code>b</code> are assigned string literals, so Java reuses the same object from the string literal pool. The <code>==</code> operator compares references, and since both point to the same pool object, it prints <code>true</code>."
    ),
    (
        "<p>A local variable in a method is declared but not initialized. What happens when you try to use it?</p>",
        [
            ("The variable receives a default value and can be used safely", False),
            ("A compile error occurs: variable must be initialized before use", True),
            ("The variable holds a random value from memory", False),
            ("A runtime NullPointerException is thrown", False),
        ],
        "Local variables do not receive automatic default values. Java's compiler enforces that every local variable must be assigned before it is read. Attempting to read an uninitialized local variable causes a compile-time error, not a runtime error."
    ),
    (
        "<p>Which statement correctly demonstrates autoboxing?</p>",
        [
            ("<code>int x = new Integer(5);</code> // unboxing", False),
            ("<code>Integer obj = 42;</code> // autoboxing", True),
            ("<code>int y = 3.14;</code>", False),
            ("<code>boolean flag = 1;</code>", False),
        ],
        "Autoboxing automatically converts a primitive value to its wrapper class. When you assign <code>42</code> (an <code>int</code>) to an <code>Integer</code> variable, Java automatically wraps it. Unboxing is the reverse: converting a wrapper to a primitive."
    ),
    (
        "<p>Consider this code:<br><code>long amount = 1234567890L;<br>float price = 29.99f;<br>char symbol = '$';</code><br>Why are the suffixes <code>L</code> and <code>f</code> used?</p>",
        [
            ("The suffixes are optional and make no difference", False),
            ("The <code>L</code> suffix indicates a <code>long</code> literal; the <code>f</code> suffix indicates a <code>float</code> literal, overriding their default types", True),
            ("The suffixes are required for all numeric literals in Java", False),
            ("The suffixes convert the values to strings", False),
        ],
        "By default, large integer literals are <code>int</code> (which overflow for large values) and floating-point literals are <code>double</code>. The <code>L</code> suffix explicitly marks a literal as <code>long</code>, and the <code>f</code> suffix marks it as <code>float</code>. Without the <code>L</code> suffix, the value would attempt to fit in an <code>int</code> and fail."
    ),
    (
        "<p>An object is created and referenced by variable <code>obj</code>. The statement <code>obj = null;</code> is executed. What happens next?</p>",
        [
            ("The object is immediately deleted from memory", False),
            ("The object becomes unreachable and is eligible for garbage collection when the garbage collector runs", True),
            ("The program throws an exception", False),
            ("The variable <code>obj</code> no longer exists", False),
        ],
        "Setting a reference to <code>null</code> dereferences the object, making it unreachable. However, Java does not immediately delete the object; instead, it becomes eligible for garbage collection. The garbage collector runs at an unpredictable time and reclaims the memory."
    ),
    (
        "<p>Which of the following correctly initializes a variable and demonstrates understanding of primitive vs. reference types?</p>",
        [
            ("<code>int num = new int(5);</code>", False),
            ("<code>double value = 3.0;</code>", True),
            ("<code>String message = 'Hello';</code>", False),
            ("<code>boolean flag = 'true';</code>", False),
        ],
        "<code>double value = 3.0;</code> correctly declares a primitive variable of type <code>double</code> and initializes it with a floating-point literal. Primitives are initialized directly without <code>new</code>. String literals use double quotes, not single quotes, and booleans are keywords, not strings."
    ),
]