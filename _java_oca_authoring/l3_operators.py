# c:\Users\hp\Documents\lms - Amazing 19\_java_oca_authoring\l3_operators.py

LESSON_HTML = """
<h2>Using Operators and Decision Constructs</h2>

<h3>Operator Fundamentals</h3>
<p>Java operators are special symbols that perform operations on one, two, or three operands and return a result. Understanding operator precedence, type promotion, and evaluation order is essential for writing correct programs.</p>

<h3>Operator Precedence and Parentheses</h3>
<p>Java follows a strict operator precedence hierarchy. Operators higher in precedence are evaluated before those lower. Use parentheses to override default precedence:</p>
<table>
  <tr><th>Precedence</th><th>Operators</th></tr>
  <tr><td>1 (Highest)</td><td>Postfix: <code>expr++</code>, <code>expr--</code></td></tr>
  <tr><td>2</td><td>Unary: <code>++expr</code>, <code>--expr</code>, <code>+expr</code>, <code>-expr</code>, <code>~</code>, <code>!</code></td></tr>
  <tr><td>3</td><td>Multiplicative: <code>*</code>, <code>/</code>, <code>%</code></td></tr>
  <tr><td>4</td><td>Additive: <code>+</code>, <code>-</code></td></tr>
  <tr><td>5</td><td>Relational: <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, <code>&gt;=</code></td></tr>
  <tr><td>6</td><td>Equality: <code>==</code>, <code>!=</code></td></tr>
  <tr><td>7</td><td>Logical AND: <code>&amp;&amp;</code></td></tr>
  <tr><td>8</td><td>Logical OR: <code>||</code></td></tr>
  <tr><td>9</td><td>Ternary: <code>? :</code></td></tr>
  <tr><td>10 (Lowest)</td><td>Assignment: <code>=</code>, <code>+=</code>, <code>-=</code>, etc.</td></tr>
</table>
<p><strong>Example:</strong> <code>2 + 3 * 4</code> evaluates to 14 (multiplication first), but <code>(2 + 3) * 4</code> evaluates to 20.</p>

<h3>Arithmetic Operators</h3>
<p>Arithmetic operators perform calculations on numeric types:</p>
<ul>
  <li><code>+</code> Addition</li>
  <li><code>-</code> Subtraction</li>
  <li><code>*</code> Multiplication</li>
  <li><code>/</code> Division (integer division truncates toward zero)</li>
  <li><code>%</code> Remainder (modulo)</li>
</ul>
<blockquote><strong>Note:</strong> Integer division does <em>not</em> round; it truncates. For example, <code>7 / 2</code> equals 3, not 3.5.</blockquote>

<h3>Assignment and Compound Assignment Operators</h3>
<p>The assignment operator <code>=</code> assigns a value to a variable. Compound assignment operators combine an operation with assignment:</p>
<ul>
  <li><code>+=</code> Add and assign: <code>x += 5</code> is equivalent to <code>x = x + 5</code></li>
  <li><code>-=</code> Subtract and assign</li>
  <li><code>*=</code> Multiply and assign</li>
  <li><code>/=</code> Divide and assign</li>
  <li><code>%=</code> Modulo and assign</li>
</ul>
<p><strong>Key Point:</strong> Compound assignments include automatic type casting. For example, <code>byte b = 10; b += 5;</code> is valid, but <code>byte b = 10; b = b + 5;</code> causes a compilation error because <code>b + 5</code> produces an <code>int</code>.</p>

<h3>Relational Operators</h3>
<p>Relational operators compare two operands and return a boolean:</p>
<ul>
  <li><code>&lt;</code> Less than</li>
  <li><code>&gt;</code> Greater than</li>
  <li><code>&lt;=</code> Less than or equal</li>
  <li><code>&gt;=</code> Greater than or equal</li>
  <li><code>==</code> Equal (for primitives) or same reference (for objects)</li>
  <li><code>!=</code> Not equal</li>
</ul>

<h3>Logical Operators</h3>
<p>Logical operators work with boolean values:</p>
<ul>
  <li><code>&amp;&amp;</code> Logical AND (short-circuit): returns true if both operands are true. <strong>Right operand is not evaluated if left is false.</strong></li>
  <li><code>||</code> Logical OR (short-circuit): returns true if at least one operand is true. <strong>Right operand is not evaluated if left is true.</strong></li>
  <li><code>!</code> Logical NOT: inverts the boolean value</li>
  <li><code>&amp;</code> Bitwise AND (non-short-circuit): always evaluates both operands</li>
  <li><code>|</code> Bitwise OR (non-short-circuit): always evaluates both operands</li>
  <li><code>^</code> Logical XOR: returns true if operands differ</li>
</ul>
<blockquote><strong>Short-Circuit Evaluation:</strong> With <code>&amp;&amp;</code> and <code>||</code>, the right side may not execute. This is important when the right operand has side effects (like method calls).</blockquote>

<h3>Numeric Promotion</h3>
<p>When a binary operator combines operands of different types, Java applies numeric promotion rules:</p>
<ul>
  <li>If any operand is <code>double</code>, the result is <code>double</code></li>
  <li>If any operand is <code>float</code>, the result is <code>float</code></li>
  <li>If any operand is <code>long</code>, the result is <code>long</code></li>
  <li>Otherwise, both operands are promoted to <code>int</code></li>
</ul>
<p><strong>Example:</strong> <code>byte b = 5; int i = 10; long result = b + i;</code> The byte is promoted to int, the sum is int, then implicitly converted to long.</p>

<h3>String Equality and the equals() Method</h3>
<p>For Strings, use <code>.equals()</code> for value comparison, not <code>==</code>:</p>
<ul>
  <li><code>==</code> compares object references (whether they point to the same object)</li>
  <li><code>.equals()</code> compares string content (the actual characters)</li>
</ul>
<pre><code class="language-java">String s1 = &quot;hello&quot;;
String s2 = new String(&quot;hello&quot;);
String s3 = &quot;hello&quot;;

s1 == s2  // false (different objects)
s1.equals(s2)  // true (same content)
s1 == s3  // true (same object, string literal pool)</code></pre>

<h3>Conditional Statements: if and if/else</h3>
<p>The <code>if</code> statement executes code if a boolean condition is true:</p>
<pre><code class="language-java">if (age &gt;= 18) {
    System.out.println(&quot;Adult&quot;);
}</code></pre>
<p>The <code>if/else</code> statement provides an alternative path:</p>
<pre><code class="language-java">if (score &gt;= 60) {
    System.out.println(&quot;Pass&quot;);
} else {
    System.out.println(&quot;Fail&quot;);
}</code></pre>
<p><code>if/else if/else</code> chains test multiple conditions in sequence.</p>

<h3>Ternary Conditional Operator</h3>
<p>The ternary operator <code>? :</code> is a compact way to make decisions:</p>
<pre><code class="language-java">int max = (a &gt; b) ? a : b;
String result = (score &gt;= 60) ? &quot;Pass&quot; : &quot;Fail&quot;;</code></pre>
<p>The condition is evaluated; if true, the first expression is returned; if false, the second.</p>

<h3>Switch Statements</h3>
<p>A <code>switch</code> statement selects one of many code blocks to execute based on a single value. Switch expressions must be <code>int</code>, <code>byte</code>, <code>short</code>, <code>char</code>, String, or enum.</p>
<pre><code class="language-java">switch (day) {
    case 1:
        System.out.println(&quot;Monday&quot;);
        break;
    case 2:
        System.out.println(&quot;Tuesday&quot;);
        break;
    default:
        System.out.println(&quot;Other day&quot;);
}</code></pre>
<p><strong>Fall-Through:</strong> If a <code>break</code> is omitted, execution continues to the next case. This is often a bug but can be intentional:</p>
<pre><code class="language-java">switch (grade) {
    case 'A':
    case 'B':
        System.out.println(&quot;Excellent&quot;);
        break;
    case 'C':
        System.out.println(&quot;Good&quot;);
        break;
}</code></pre>
<p>The <code>default</code> case is optional and executes if no case matches.</p>
"""

QUESTIONS = [
    (
        "<p>What is the output of this code?</p><pre><code class=\"language-java\">int x = 5;\nint y = 2;\nint result = x + y * 2;\nSystem.out.println(result);</code></pre>",
        [
            ("<code>9</code>", True),
            ("<code>14</code>", False),
            ("<code>7</code>", False),
            ("<code>Compilation error</code>", False),
        ],
        "Multiplication has higher precedence than addition. So y * 2 is evaluated first (2 * 2 = 4), then x + 4 = 9."
    ),
    (
        "<p>Which expression correctly tests if two String variables <code>s1</code> and <code>s2</code> have the same content?</p>",
        [
            ("<code>s1 == s2</code>", False),
            ("<code>s1.equals(s2)</code>", True),
            ("<code>s1.compareTo(s2)</code>", False),
            ("<code>s1.equalsIgnoreCase(s2)</code>", False),
        ],
        "The <code>equals()</code> method compares the actual content of strings. The <code>==</code> operator compares object references, which would likely be false for separately created strings."
    ),
    (
        "<p>What is the result of this expression?</p><pre><code class=\"language-java\">int a = 10;\nint b = 3;\nint c = a / b;\nSystem.out.println(c);</code></pre>",
        [
            ("<code>3.33</code>", False),
            ("<code>3</code>", True),
            ("<code>4</code>", False),
            ("<code>3.0</code>", False),
        ],
        "Integer division truncates the decimal part. 10 / 3 = 3 (not 3.33). Both operands are ints, so the result is int."
    ),
    (
        "<p>What is the output of this code?</p><pre><code class=\"language-java\">int x = 5;\nx += 3;\nSystem.out.println(x);</code></pre>",
        [
            ("<code>3</code>", False),
            ("<code>8</code>", True),
            ("<code>5</code>", False),
            ("<code>Compilation error</code>", False),
        ],
        "The compound assignment operator <code>+=</code> adds the right operand to the left and assigns the result. x += 3 is equivalent to x = x + 3, so 5 + 3 = 8."
    ),
    (
        "<p>What is the output of this code?</p><pre><code class=\"language-java\">int num = 5;\nString result = (num &gt; 3) ? &quot;High&quot; : &quot;Low&quot;;\nSystem.out.println(result);</code></pre>",
        [
            ("<code>true</code>", False),
            ("<code>High</code>", True),
            ("<code>Low</code>", False),
            ("<code>Compilation error</code>", False),
        ],
        "The ternary operator evaluates the condition num > 3 (true), so it returns the first expression \"High\"."
    ),
    (
        "<p>Consider the following code. Which statement is true?</p><pre><code class=\"language-java\">boolean result = true;\nif (false &amp;&amp; (result = false)) {\n    System.out.println(&quot;In if&quot;);\n}\nSystem.out.println(result);</code></pre>",
        [
            ("<code>result</code> is false and \"In if\" is printed", False),
            ("<code>result</code> is true and \"In if\" is printed", False),
            ("<code>result</code> is true and only the value of result is printed", True),
            ("<code>Compilation error</code>", False),
        ],
        "The <code>&amp;&amp;</code> operator short-circuits. Since the left side is false, the right side <code>(result = false)</code> is never evaluated. result remains true, and \"In if\" is not printed."
    ),
    (
        "<p>What is the output of this switch statement?</p><pre><code class=\"language-java\">int day = 2;\nswitch (day) {\n    case 1:\n        System.out.println(&quot;Monday&quot;);\n    case 2:\n        System.out.println(&quot;Tuesday&quot;);\n        break;\n    case 3:\n        System.out.println(&quot;Wednesday&quot;);\n}\n</code></pre>",
        [
            ("<code>Monday Tuesday</code>", False),
            ("<code>Tuesday</code>", True),
            ("<code>Tuesday Wednesday</code>", False),
            ("<code>Compilation error</code>", False),
        ],
        "When day is 2, the case 2 label is matched. \"Tuesday\" is printed, then break exits the switch. Note: case 1 has no break, but we never reach it because the match is on case 2."
    ),
    (
        "<p>What is the result of this expression?</p><pre><code class=\"language-java\">byte b = 100;\nint i = 50;\nbyte result = b + i;</code></pre>",
        [
            ("<code>150</code>", False),
            ("<code>Compilation error</code>", True),
            ("<code>The code compiles and result is 150</code>", False),
            ("<code>The code compiles and result is -6</code>", False),
        ],
        "Adding byte and int produces an int result (numeric promotion). Assigning an int to a byte variable requires an explicit cast; the code does not compile without it."
    ),
]