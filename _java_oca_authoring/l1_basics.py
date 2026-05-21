LESSON_HTML = """<h2>Java Basics</h2>

<h3>Understanding a Java Class and the main Method</h3>
<p>A Java program is organized into <strong>classes</strong>. Each source file typically contains one public class, and the filename must match the public class name with a <code>.java</code> extension. When you compile the source file using <code>javac</code>, the Java compiler generates a <code>.class</code> file (bytecode) that the JVM (Java Virtual Machine) executes.</p>
<p>The <code>main</code> method is the entry point for any standalone Java application:</p>
<pre><code class="language-java">public static void main(String[] args) {
    // Program execution starts here
}</code></pre>
<p>The method signature must be exactly as shown: <code>public</code> (required), <code>static</code> (so the JVM can invoke it without instantiation), <code>void</code> (returns nothing), and <code>String[] args</code> (accepts command-line arguments).</p>

<h3>Variable Scope</h3>
<p>Variable scope determines where a variable can be accessed within a program:</p>
<ul>
<li><strong>Class (static) variables</strong> are declared with <code>static</code> and are shared by all instances of the class.</li>
<li><strong>Instance variables</strong> are declared within a class but outside any method; each object has its own copy.</li>
<li><strong>Local variables</strong> are declared inside methods or code blocks and exist only within that scope.</li>
<li><strong>Method parameters</strong> are treated like local variables; their scope is the method body.</li>
</ul>
<p>Local variables must be initialized before use, whereas instance and class variables are automatically initialized to default values.</p>

<h3>Packages and Imports</h3>
<p>Java organizes classes into <strong>packages</strong> to avoid naming conflicts. A package statement must be the first statement (if present) in a source file:</p>
<pre><code class="language-java">package com.example.myapp;</code></pre>
<p>To use classes from other packages, use the <code>import</code> statement:</p>
<pre><code class="language-java">import java.util.Scanner;
import java.io.*;</code></pre>
<p>Wildcard imports (<code>import java.io.*;</code>) import all public classes from a package. The package <code>java.lang</code> is implicitly imported in all Java files, so you do not need to explicitly import classes like <code>String</code>, <code>Object</code>, or <code>System</code>.</p>

<h3>Classpath</h3>
<p>The <strong>classpath</strong> tells the JVM where to find compiled <code>.class</code> files and resources. When you run a program with the <code>java</code> command, specify the classpath using the <code>-cp</code> (or <code>-classpath</code>) flag:</p>
<pre><code class="language-java">java -cp /path/to/classes MyProgram</code></pre>
<p>By default, the current working directory (<code>.</code>) is part of the classpath. Classpath entries can be individual directories or JAR (Java Archive) files.</p>

<h3>Comments and Identifiers</h3>
<p>Java supports three types of comments:</p>
<ul>
<li><strong>Single-line comment:</strong> <code>// This is a comment</code></li>
<li><strong>Multi-line comment:</strong> <code>/* This is a comment */</code></li>
<li><strong>JavaDoc comment:</strong> <code>/** This generates API documentation */</code></li>
</ul>
<p>An <strong>identifier</strong> is a name for a variable, method, class, or package. Identifiers must start with a letter, underscore, or dollar sign, and can contain letters, digits, underscores, or dollar signs. Java is case-sensitive: <code>myVar</code> and <code>MyVar</code> are different identifiers.</p>

<h3>Reserved Keywords</h3>
<p>Reserved keywords cannot be used as identifiers. Examples include: <code>public</code>, <code>class</code>, <code>static</code>, <code>void</code>, <code>if</code>, <code>else</code>, <code>for</code>, <code>while</code>, <code>return</code>, <code>new</code>, <code>abstract</code>, <code>interface</code>, <code>extends</code>, <code>implements</code>, and <code>package</code>.</p>

<h3>Compilation and Execution</h3>
<p>The compilation process converts human-readable Java source code (<code>.java</code>) into bytecode (<code>.class</code>):</p>
<pre><code class="language-java">javac MyProgram.java</code></pre>
<p>This command creates <code>MyProgram.class</code>. To execute the program, invoke the JVM with the class name (without the <code>.class</code> extension):</p>
<pre><code class="language-java">java MyProgram</code></pre>
<p><strong>JVM (Java Virtual Machine)</strong> executes bytecode. <strong>JRE (Java Runtime Environment)</strong> includes the JVM plus standard libraries needed to run Java applications. <strong>JDK (Java Development Kit)</strong> includes the JRE plus development tools like <code>javac</code> (compiler) and <code>jdb</code> (debugger).</p>

<h3>Source File Rules</h3>
<ul>
<li>A source file can contain at most <strong>one public class</strong>.</li>
<li>The public class name must match the source filename (excluding the <code>.java</code> extension).</li>
<li>A source file can contain multiple non-public classes.</li>
<li>If a file contains a package statement, it must be the first statement (before any imports or class declarations).</li>
</ul>
"""

QUESTIONS = [
    (
        "<p>Which of the following is the correct signature for the <code>main</code> method in Java?</p>",
        [
            ("<code>public void main(String[] args)</code>", False),
            ("<code>public static void main(String[] args)</code>", True),
            ("<code>static void main(String args[])</code>", False),
            ("<code>public static int main(String[] args)</code>", False),
        ],
        "The main method must be <code>public static void main(String[] args)</code> so the JVM can invoke it without an instance. The return type must be <code>void</code>, the parameter must be <code>String[]</code>, and <code>static</code> is required."
    ),
    (
        "<p>What is the scope of the variable <code>x</code> in the following code?</p><pre><code class=\"language-java\">public class Example {\n    static int x = 5;\n    public static void main(String[] args) {\n        System.out.println(x);\n    }\n}</code></pre>",
        [
            ("Local scope to the main method", False),
            ("Instance scope (unique to each object)", False),
            ("Class scope (shared by the entire class)", True),
            ("No scope; it will cause a compile error", False),
        ],
        "The keyword <code>static</code> declares <code>x</code> as a class variable, which is shared by all instances and accessible throughout the class."
    ),
    (
        "<p>Which import statement allows you to use all classes from the <code>java.util</code> package?</p>",
        [
            ("<code>import java.util;</code>", False),
            ("<code>import java.util.*;</code>", True),
            ("<code>import java.util.all;</code>", False),
            ("<code>use java.util.*;</code>", False),
        ],
        "Wildcard imports use the <code>*</code> symbol to import all public classes from a package. The single package name without <code>*</code> does not import its contents."
    ),
    (
        "<p>What is automatically imported in every Java source file without an explicit import statement?</p>",
        [
            ("All packages under <code>java</code>", False),
            ("The <code>java.lang</code> package", True),
            ("The <code>java.io</code> package", False),
            ("No packages; all imports must be explicit", False),
        ],
        "The <code>java.lang</code> package (which contains <code>String</code>, <code>Object</code>, <code>System</code>, and others) is implicitly imported in all Java files."
    ),
    (
        "<p>A Java source file contains the following line as the first statement:</p><pre><code class=\"language-java\">package com.mycompany;\nimport java.util.Scanner;\npublic class MyClass { }</code></pre><p>What will happen when this file is compiled and executed?</p>",
        [
            ("It will compile and run successfully", True),
            ("Compile error: package statement is not valid", False),
            ("Compile error: Scanner is not in the classpath", False),
            ("Runtime error: package cannot be specified before imports", False),
        ],
        "This is valid Java syntax. The package statement must come first, followed by import statements, then class declarations."
    ),
    (
        "<p>When you compile a Java source file with <code>javac MyProgram.java</code>, what is created?</p>",
        [
            ("A <code>.java</code> file is modified", False),
            ("A <code>.class</code> file containing bytecode", True),
            ("An executable <code>.exe</code> file", False),
            ("A JAR archive", False),
        ],
        "The <code>javac</code> compiler converts the source code (<code>.java</code>) into bytecode (<code>.class</code>), which the JVM can execute."
    ),
    (
        "<p>Which statement about Java identifiers is incorrect?</p>",
        [
            ("An identifier can start with a letter, underscore, or dollar sign", False),
            ("An identifier cannot contain spaces", False),
            ("An identifier can start with a digit", True),
            ("Java identifiers are case-sensitive", False),
        ],
        "Identifiers cannot start with a digit; they must begin with a letter, underscore, or dollar sign. The other statements are all correct."
    ),
    (
        "<p>What is the primary difference between the JDK and the JRE?</p>",
        [
            ("JRE runs Java programs; JDK includes development tools like the compiler", True),
            ("JDK is for Windows only; JRE is cross-platform", False),
            ("JRE includes a compiler; JDK does not", False),
            ("JDK and JRE are the same thing", False),
        ],
        "JRE (Java Runtime Environment) includes the JVM and libraries for running Java applications. JDK (Java Development Kit) includes the JRE plus development tools such as <code>javac</code> and <code>jdb</code>."
    ),
]