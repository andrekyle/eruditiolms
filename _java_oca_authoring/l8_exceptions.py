LESSON_HTML = """
<h2>Handling Exceptions</h2>

<h3>What Are Exceptions?</h3>
<p>Exceptions are objects that represent exceptional (unusual or error) conditions that occur during program execution. When an exception occurs, normal program flow is disrupted. Java uses the exception mechanism to separate error handling from regular business logic, making code more readable and maintainable.</p>

<h3>The Throwable Hierarchy</h3>
<p>All exceptions and errors in Java inherit from the <strong>Throwable</strong> class. The hierarchy is structured as follows:</p>
<pre><code class="language-java">Throwable
  ├── Error (serious problems, not typically caught)
  └── Exception (problems that should be handled)
      ├── IOException (checked)
      ├── SQLException (checked)
      └── RuntimeException (unchecked)
          ├── NullPointerException
          ├── ArithmeticException
          ├── ArrayIndexOutOfBoundsException
          ├── ClassCastException
          ├── NumberFormatException
          ├── IllegalArgumentException
          └── IllegalStateException</code></pre>

<h3>Checked vs. Unchecked Exceptions</h3>
<p><strong>Checked Exceptions</strong> are exceptions that must be explicitly handled (caught in a try-catch block) or declared in the method's throws clause. The compiler enforces this. Common examples include <code>IOException</code> and <code>SQLException</code>.</p>
<p><strong>Unchecked Exceptions</strong> (also called runtime exceptions) inherit from <code>RuntimeException</code> and are not checked by the compiler. You may handle them, but you don't have to. Examples include <code>NullPointerException</code> and <code>ArithmeticException</code>.</p>
<p><strong>Errors</strong> are serious problems that typically should not be caught (e.g., <code>OutOfMemoryError</code>, <code>StackOverflowError</code>). They indicate something is fundamentally wrong with the JVM or system.</p>

<h3>The try-catch Block</h3>
<p>A <em>try-catch</em> block allows you to handle exceptions that may occur during program execution:</p>
<pre><code class="language-java">try {
    // Code that might throw an exception
    int result = 10 / 0;  // throws ArithmeticException
} catch (ArithmeticException e) {
    // Handle the exception
    System.out.println(&quot;Cannot divide by zero&quot;);
}</code></pre>
<p>The try block contains code that might throw an exception. If an exception is thrown, execution immediately jumps to the matching catch block. The catch block receives an exception object containing information about what went wrong.</p>

<h3>Multiple Catch Blocks</h3>
<p>You can have multiple catch blocks for a single try block. When an exception is thrown, the catch blocks are evaluated <em>in order from top to bottom</em>. The first matching catch block is executed. <strong>Order matters: always place more specific exception types before more general ones.</strong></p>
<pre><code class="language-java">try {
    String[] names = {&quot;Alice&quot;, &quot;Bob&quot;};
    System.out.println(names[5]);
    int x = Integer.parseInt(&quot;abc&quot;);
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println(&quot;Invalid array index&quot;);
} catch (NumberFormatException e) {
    System.out.println(&quot;Invalid number format&quot;);
} catch (Exception e) {
    // Most general catch
    System.out.println(&quot;Some other exception&quot;);
}</code></pre>

<h3>Multi-Catch (Java 7+)</h3>
<p>Java 7 introduced the ability to catch multiple exceptions in a single catch block using the pipe (<code>|</code>) operator:</p>
<pre><code class="language-java">try {
    // Code that might throw IOException or SQLException
} catch (IOException | SQLException e) {
    System.out.println(&quot;Database or file error occurred&quot;);
}</code></pre>
<p>The variable <code>e</code> is implicitly <code>final</code> in a multi-catch block.</p>

<h3>The Finally Block</h3>
<p>A <em>finally</em> block executes regardless of whether an exception was thrown and caught. It is used for cleanup operations such as closing resources:</p>
<pre><code class="language-java">try {
    FileInputStream fis = new FileInputStream(&quot;file.txt&quot;);
    // Use the file
} catch (FileNotFoundException e) {
    System.out.println(&quot;File not found&quot;);
} finally {
    System.out.println(&quot;Cleanup code always runs&quot;);
}</code></pre>
<p>The finally block runs in these scenarios:</p>
<ul>
<li>After a successful try block (no exception).</li>
<li>After a matching catch block executes.</li>
<li>If an exception is thrown but not caught (finally runs before the exception propagates).</li>
</ul>
<p>The finally block does <strong>not</strong> run if the JVM terminates (e.g., via <code>System.exit(0)</code>) or if a fatal error occurs.</p>

<h3>Try-With-Resources (Java 7+)</h3>
<p>The try-with-resources statement automatically closes any resource that implements <code>AutoCloseable</code> (including <code>Closeable</code>):</p>
<pre><code class="language-java">try (FileInputStream fis = new FileInputStream(&quot;file.txt&quot;)) {
    // Use fis here
} catch (IOException e) {
    System.out.println(&quot;Error reading file&quot;);
}</code></pre>
<p>When the try block exits (normally or via exception), the resource is automatically closed by calling its <code>close()</code> method. This eliminates the need for a finally block in most cases.</p>

<h3>Declaring Exceptions with throws</h3>
<p>If a method does not handle a checked exception, it must declare it in the method signature using the <strong>throws</strong> keyword:</p>
<pre><code class="language-java">public void readFile(String filename) throws IOException {
    FileInputStream fis = new FileInputStream(filename);
    // No try-catch; exception propagates to caller
}</code></pre>
<p>The caller of this method must either handle the exception or declare it in its own throws clause.</p>

<h3>Common Exception Classes</h3>
<table border="1" cellpadding="8" cellspacing="0" style="width:100%">
<tr><th>Exception Class</th><th>Type</th><th>Common Cause</th></tr>
<tr><td>NullPointerException</td><td>Unchecked</td><td>Attempting to call a method or access a field on a null reference</td></tr>
<tr><td>ArithmeticException</td><td>Unchecked</td><td>Division by zero or modulo by zero</td></tr>
<tr><td>ArrayIndexOutOfBoundsException</td><td>Unchecked</td><td>Accessing an array with an invalid index</td></tr>
<tr><td>ClassCastException</td><td>Unchecked</td><td>Attempting an illegal cast (e.g., casting a String to an Integer)</td></tr>
<tr><td>NumberFormatException</td><td>Unchecked</td><td>Parsing an invalid string to a number (e.g., Integer.parseInt(&quot;abc&quot;))</td></tr>
<tr><td>IllegalArgumentException</td><td>Unchecked</td><td>Passing an invalid argument to a method</td></tr>
<tr><td>IllegalStateException</td><td>Unchecked</td><td>Invoking a method when the object is in an invalid state</td></tr>
<tr><td>IOException</td><td>Checked</td><td>Input/output operation fails (file not found, read error)</td></tr>
<tr><td>FileNotFoundException</td><td>Checked</td><td>Attempting to open a file that does not exist</td></tr>
<tr><td>SQLException</td><td>Checked</td><td>Database access error</td></tr>
<tr><td>ClassNotFoundException</td><td>Checked</td><td>Requested class cannot be found</td></tr>
</table>

<h3>Exception Flow and Program Execution</h3>
<p>When an exception is thrown:</p>
<ol>
<li>The normal sequence of statements stops.</li>
<li>The exception propagates up the call stack until a matching try-catch block is found.</li>
<li>If a catch block matches, it executes, and program flow continues after the try-catch-finally block.</li>
<li>If no catch block matches, the exception propagates to the caller. If no handler exists, the program terminates and prints a stack trace.</li>
<li>A finally block (if present) always executes before control leaves the try-catch structure.</li>
</ol>
"""

QUESTIONS = [
    (
        "<p>Which of the following is the correct hierarchy of exception classes in Java?</p>",
        [
            ("<code>Throwable</code> → <code>Error</code> → <code>Exception</code> → <code>RuntimeException</code>", False),
            ("<code>Throwable</code> → <code>Exception</code> → <code>RuntimeException</code></code> or <code>Throwable</code> → <code>Error</code>", True),
            ("<code>Exception</code> → <code>Throwable</code> → <code>Error</code> → <code>RuntimeException</code>", False),
            ("<code>Error</code> → <code>Throwable</code> → <code>Exception</code> → <code>RuntimeException</code>", False),
        ],
        "Throwable is the top-level class. Both Error and Exception extend Throwable independently. RuntimeException extends Exception. This structure correctly represents the Java exception hierarchy."
    ),
    (
        "<p>What is the key difference between checked and unchecked exceptions?</p>",
        [
            ("Unchecked exceptions are more severe than checked exceptions.", False),
            ("Checked exceptions must be declared in a throws clause or handled in a try-catch block; unchecked exceptions do not require this.", True),
            ("Checked exceptions can only occur in file I/O operations; unchecked exceptions can occur anywhere.", False),
            ("Unchecked exceptions inherit from Exception; checked exceptions inherit from Error.", False),
        ],
        "The Java compiler enforces handling or declaration of checked exceptions. Unchecked exceptions (RuntimeException subclasses) are not enforced by the compiler, though you may still handle them if desired."
    ),
    (
        "<p>Consider this code snippet. What output is printed?</p><pre><code class=\"language-java\">try {\n    int[] arr = {1, 2, 3};\n    System.out.println(arr[5]);\n} catch (ArrayIndexOutOfBoundsException e) {\n    System.out.println(\"Caught exception\");\n} finally {\n    System.out.println(\"Finally block\");\n}</code></pre>",
        [
            ("No output is printed; the program crashes.", False),
            ("Only \"Caught exception\" is printed.", False),
            ("\"Caught exception\" is printed, then \"Finally block\" is printed.", True),
            ("Only \"Finally block\" is printed.", False),
        ],
        "When the exception is thrown at arr[5], the catch block catches it and prints \"Caught exception\". The finally block always executes after the catch block completes, so \"Finally block\" is also printed."
    ),
    (
        "<p>Which statement about the <code>finally</code> block is <em>incorrect</em>?</p>",
        [
            ("A finally block will execute even if an exception is thrown and caught.", False),
            ("A finally block will always execute after the try or catch blocks complete.", False),
            ("A finally block will execute even if you call <code>System.exit(0)</code> in the try block.", True),
            ("A finally block is typically used for cleanup operations such as closing resources.", False),
        ],
        "If System.exit(0) is called, the JVM terminates immediately, and the finally block does not execute. In all other normal scenarios, finally runs without exception."
    ),
    (
        "<p>What is the output of this code?</p><pre><code class=\"language-java\">try {\n    String s = \"hello\";\n    int x = Integer.parseInt(s);\n} catch (NumberFormatException e) {\n    System.out.println(\"Number format error\");\n} catch (Exception e) {\n    System.out.println(\"General exception\");\n}\nSystem.out.println(\"After try-catch\");</code></pre>",
        [
            ("\"Number format error\" is printed.", False),
            ("\"Number format error\" is printed, then \"After try-catch\" is printed.", True),
            ("\"General exception\" is printed, then \"After try-catch\" is printed.", False),
            ("No output is printed; an exception escapes.", False),
        ],
        "Integer.parseInt(\"hello\") throws NumberFormatException, which is more specific than the general Exception. The first matching catch block (NumberFormatException) executes, printing \"Number format error\". After the try-catch, \"After try-catch\" is printed."
    ),
    (
        "<p>Consider multi-catch syntax (Java 7+). Which statement is correct?</p>",
        [
            ("<code>catch (IOException | SQLException e)</code> allows catching two distinct exceptions in a single catch block, and e is implicitly final.", True),
            ("<code>catch (IOException | SQLException e)</code> is a syntax error because you cannot catch multiple exceptions.", False),
            ("<code>catch (IOException | SQLException e)</code> allows you to modify e inside the catch block.", False),
            ("<code>catch (IOException | SQLException e)</code> will never match RuntimeException objects.", False),
        ],
        "Multi-catch syntax with the pipe operator allows handling multiple specific exception types in one block. The exception variable is implicitly final to ensure type safety."
    ),
    (
        "<p>A method is declared as <code>public void processFile(String path) throws IOException</code>. What does this mean?</p>",
        [
            ("The method will never throw an IOException because it is declared in throws.", False),
            ("The method may throw an IOException, and the caller must either handle it with try-catch or declare it in their own throws clause.", True),
            ("The method is guaranteed to throw an IOException every time it is called.", False),
            ("IOException is automatically caught inside the method.", False),
        ],
        "The throws clause indicates that the method does not handle the checked exception; instead, it propagates to the caller. The caller must handle or re-declare it."
    ),
    (
        "<p>Which code snippet correctly uses try-with-resources (Java 7+)?</p>",
        [
            ("<code>try (FileInputStream fis = new FileInputStream(\"file.txt\")) { /* use fis */ }</code>", True),
            ("<code>try { FileInputStream fis = new FileInputStream(\"file.txt\"); } finally { fis.close(); }</code>", False),
            ("<code>try { FileInputStream fis = new FileInputStream(\"file.txt\"); } catch (Throwable t) { }</code>", False),
            ("<code>try FileInputStream fis = new FileInputStream(\"file.txt\") { /* use fis */ }</code>", False),
        ],
        "Try-with-resources uses the syntax try (ResourceType resource = new Resource()) { }. The resource is automatically closed when the try block exits. The syntax in option A is correct."
    ),
]