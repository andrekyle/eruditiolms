LESSON_HTML = """
<style>
  .lsn-h2{font-size:1.5rem;font-weight:600;margin:32px 0 12px;letter-spacing:-0.005em;}
  .lsn-h3{font-size:1.25rem;font-weight:600;margin:24px 0 10px;}
  .lsn-p{font-size:1.0625rem;line-height:1.7;margin:0 0 14px;}
  .lsn-ul{font-size:1.0625rem;line-height:1.7;margin:0 0 18px 1.25rem;padding:0;}
  .lsn-li{margin-bottom:8px;}
  .lsn-pre{background:rgba(127,127,127,.08);border-left:3px solid rgba(127,127,127,.25);padding:12px 14px;margin:16px 0;border-radius:4px;overflow-x:auto;}
  .lsn-table{width:100%;border-collapse:collapse;margin:14px 0 22px;font-size:1rem;}
  .lsn-table th,.lsn-table td{border:1px solid rgba(127,127,127,.35);padding:10px 12px;text-align:left;vertical-align:top;}
  .lsn-table th{background:rgba(127,127,127,.10);font-weight:600;}
  .lsn-callout{background:rgba(127,127,127,.10);padding:14px 18px;border-radius:6px;margin:18px 0;}
  .lsn-warn{background:rgba(127,127,127,.14);padding:14px 18px;border-radius:6px;margin:18px 0;}
  code{font-family:monospace;background:rgba(127,127,127,.08);padding:2px 5px;border-radius:3px;}
</style>

<p class="lsn-p">Loop constructs are fundamental to writing Java programs that repeat operations. Understanding how to create and control loops—including when and how to use <code>break</code> and <code>continue</code>—is essential for the OCA 1Z0-808 exam. This lesson covers all loop types, their syntax, and the common pitfalls you must avoid.</p>

<div class="lsn-callout"><strong>Learning objectives.</strong> By the end of this lesson you should be able to: create and use <code>while</code>, <code>do-while</code>, and <code>for</code> loops correctly; use the enhanced for loop (for-each) with arrays and collections; understand which loop construct is most appropriate in different scenarios; use <code>break</code> and <code>continue</code> (labeled and unlabeled); avoid infinite loops and off-by-one errors; and work effectively with nested loops.</div>

<h2 class="lsn-h2">1. The while loop</h2>

<p class="lsn-p">A <code>while</code> loop repeats a block of code <strong>as long as</strong> a boolean condition is true. The condition is evaluated <strong>at the top</strong> of each iteration (before the body executes).</p>

<div class="lsn-pre"><pre><code class="language-java">while (condition) {
    // body executes if condition is true
    // when body finishes, control returns to test condition
}</code></pre></div>

<p class="lsn-p"><strong>Example:</strong></p>

<div class="lsn-pre"><pre><code class="language-java">int count = 0;
while (count &lt; 3) {
    System.out.println("count is " + count);
    count++;
}
// Output:
// count is 0
// count is 1
// count is 2</code></pre></div>

<p class="lsn-p">If the condition is false on entry, the body never executes:</p>

<div class="lsn-pre"><pre><code class="language-java">int x = 10;
while (x &lt; 5) {
    System.out.println(x);  // this never runs
}
// Output: (nothing)</code></pre></div>

<h2 class="lsn-h2">2. The do-while loop</h2>

<p class="lsn-p">A <code>do-while</code> loop is like a <code>while</code> loop, but the condition is evaluated <strong>at the bottom</strong> of each iteration. The body <strong>always executes at least once</strong>, even if the condition is false initially.</p>

<div class="lsn-pre"><pre><code class="language-java">do {
    // body executes first
    // after body completes, condition is tested
    // if true, loop repeats; if false, exit
} while (condition);</code></pre></div>

<p class="lsn-p"><strong>Example:</strong></p>

<div class="lsn-pre"><pre><code class="language-java">int x = 10;
do {
    System.out.println(x);
    x++;
} while (x &lt; 5);
// Output:
// 10</code></pre></div>

<p class="lsn-p">Note the semicolon at the end—it is required. Unlike <code>while (condition) { }</code>, the <code>do-while</code> statement terminates with a semicolon.</p>

<h2 class="lsn-h2">3. The classical for loop</h2>

<p class="lsn-p">The <code>for</code> loop combines initialization, condition testing, and update into one line. The full syntax has three parts, separated by semicolons:</p>

<div class="lsn-pre"><pre><code class="language-java">for (init; condition; update) {
    // body
}</code></pre></div>

<p class="lsn-p">Each part is optional:</p>

<ul class="lsn-ul">
  <li class="lsn-li"><strong>init:</strong> Runs once before the loop starts. Declare and initialize variables here (e.g., <code>int i = 0</code>).</li>
  <li class="lsn-li"><strong>condition:</strong> Tested before each iteration. If false, the loop exits.</li>
  <li class="lsn-li"><strong>update:</strong> Runs after each iteration, before the condition is tested again.</li>
</ul>

<p class="lsn-p"><strong>Typical example:</strong></p>

<div class="lsn-pre"><pre><code class="language-java">for (int i = 0; i &lt; 3; i++) {
    System.out.println("i is " + i);
}
// Output:
// i is 0
// i is 1
// i is 2</code></pre></div>

<p class="lsn-p"><strong>All three parts are optional.</strong> An empty for creates an infinite loop:</p>

<div class="lsn-pre"><pre><code class="language-java">for (;;) {
    // this runs forever (or until break)
}</code></pre></div>

<p class="lsn-p">You can omit any part:</p>

<div class="lsn-pre"><pre><code class="language-java">int i = 0;
for (; i &lt; 3; i++) {  // no init
    System.out.println(i);
}

for (int j = 0; j &lt; 3;) {  // no update
    System.out.println(j);
    j++;
}

for (int k = 0; ; k++) {  // no condition (infinite)
    if (k &gt;= 3) break;
}</code></pre></div>

<p class="lsn-p"><strong>Multiple variables in init and update:</strong> You can declare and initialize multiple variables of the <strong>same type</strong> in the init section, separated by commas. Similarly, multiple update expressions are separated by commas:</p>

<div class="lsn-pre"><pre><code class="language-java">for (int i = 0, j = 10; i &lt; j; i++, j--) {
    System.out.println(i + " " + j);
}
// Output:
// 0 10
// 1 9
// 2 8
// 3 7
// 4 6</code></pre></div>

<p class="lsn-p">Variables declared in the init section are local to the loop and cease to exist after it exits:</p>

<div class="lsn-pre"><pre><code class="language-java">for (int i = 0; i &lt; 3; i++) {
    System.out.println(i);
}
System.out.println(i);  // COMPILATION ERROR: i is out of scope</code></pre></div>

<h2 class="lsn-h2">4. The enhanced for loop (for-each)</h2>

<p class="lsn-p">The enhanced for loop (also called the for-each loop) is a simplified syntax for iterating over arrays and collections:</p>

<div class="lsn-pre"><pre><code class="language-java">for (type variable : collection) {
    // body; 'variable' holds the current element
}</code></pre></div>

<p class="lsn-p"><strong>With an array:</strong></p>

<div class="lsn-pre"><pre><code class="language-java">int[] numbers = {10, 20, 30};
for (int num : numbers) {
    System.out.println(num);
}
// Output:
// 10
// 20
// 30</code></pre></div>

<p class="lsn-p"><strong>With an Iterable (e.g., ArrayList):</strong></p>

<div class="lsn-pre"><pre><code class="language-java">List&lt;String&gt; names = Arrays.asList("Alice", "Bob", "Charlie");
for (String name : names) {
    System.out.println(name);
}
// Output:
// Alice
// Bob
// Charlie</code></pre></div>

<p class="lsn-p">The for-each loop has no index variable, making it cleaner when you don't need the index. However, if you need the index or need to remove elements during iteration, use a classical <code>for</code> or <code>while</code> loop instead.</p>

<h2 class="lsn-h2">5. break and continue</h2>

<p class="lsn-p"><code>break</code> exits the loop immediately; <code>continue</code> skips the rest of the current iteration and jumps to the condition test (or the update in a <code>for</code>).</p>

<p class="lsn-p"><strong>Unlabeled break:</strong></p>

<div class="lsn-pre"><pre><code class="language-java">for (int i = 0; i &lt; 5; i++) {
    if (i == 3) break;  // exit the loop when i is 3
    System.out.println(i);
}
// Output:
// 0
// 1
// 2</code></pre></div>

<p class="lsn-p"><strong>Unlabeled continue:</strong></p>

<div class="lsn-pre"><pre><code class="language-java">for (int i = 0; i &lt; 5; i++) {
    if (i == 2) continue;  // skip to the next iteration
    System.out.println(i);
}
// Output:
// 0
// 1
// 3
// 4</code></pre></div>

<p class="lsn-p"><strong>Labeled break and continue:</strong> When loops are nested, you can use labels to break out of or continue an outer loop:</p>

<div class="lsn-pre"><pre><code class="language-java">outer: for (int i = 0; i &lt; 3; i++) {
    for (int j = 0; j &lt; 3; j++) {
        if (i == 1 &amp;&amp; j == 1) break outer;  // exit both loops
        System.out.println("i=" + i + ", j=" + j);
    }
}
// Output:
// i=0, j=0
// i=0, j=1
// i=0, j=2
// i=1, j=0</code></pre></div>

<p class="lsn-p">A label is an identifier followed by a colon, placed before the loop. <code>break label;</code> exits the labeled loop. <code>continue label;</code> jumps to the next iteration of the labeled loop.</p>

<h2 class="lsn-h2">6. Choosing the right loop construct</h2>

<table class="lsn-table">
  <thead>
    <tr><th>Construct</th><th>Condition Check</th><th>When to use</th></tr>
  </thead>
  <tbody>
    <tr><td><code>while</code></td><td>Top (before body)</td><td>Repeat while a condition holds; body may never execute.</td></tr>
    <tr><td><code>do-while</code></td><td>Bottom (after body)</td><td>Body must execute at least once (e.g., input validation).</td></tr>
    <tr><td><code>for</code> (classical)</td><td>Top</td><td>Known iteration count or need an index variable.</td></tr>
    <tr><td>Enhanced <code>for</code></td><td>Top</td><td>Iterate over all elements of an array or collection; no index needed.</td></tr>
  </tbody>
</table>

<h2 class="lsn-h2">7. Common pitfalls</h2>

<h3 class="lsn-h3">Infinite loops</h3>

<p class="lsn-p">If the loop condition never becomes false (or you forget to update the counter), the loop runs forever:</p>

<div class="lsn-pre"><pre><code class="language-java">for (int i = 0; i &lt; 5; ) {
    System.out.println(i);
    // forgot to increment i—infinite loop!
}</code></pre></div>

<h3 class="lsn-h3">Off-by-one errors</h3>

<p class="lsn-p">Using <code>&lt;</code> vs. <code>&lt;=</code> (or <code>&gt;</code> vs. <code>&gt;=</code>) can cause the loop to run one too many or one too few times:</p>

<div class="lsn-pre"><pre><code class="language-java">for (int i = 0; i &lt;= 5; i++) {  // includes 5 (6 iterations: 0..5)
    System.out.println(i);
}

for (int i = 0; i &lt; 5; i++) {   // excludes 5 (5 iterations: 0..4)
    System.out.println(i);
}</code></pre></div>

<h3 class="lsn-h3">Assignment instead of comparison in conditions</h3>

<p class="lsn-p">Using <code>=</code> (assignment) instead of <code>==</code> (comparison) in a loop condition assigns a value and uses that value as the condition. This usually results in unexpected behavior:</p>

<div class="lsn-pre"><pre><code class="language-java">while (x = 5) {  // WRONG! Assigns 5 to x, then checks if 5 is true (it is)
    // infinite loop (5 is truthy)
}

while (x == 5) {  // Correct: compares x to 5
    // ...
}</code></pre></div>

<p class="lsn-p">Note: This actually fails to compile in many modern Java contexts because the compiler is strict about types, but it demonstrates a common logical mistake.</p>

<h2 class="lsn-h2">8. Nested loops and performance</h2>

<p class="lsn-p">Nested loops execute the inner loop fully for each iteration of the outer loop. Be aware of the iteration count:</p>

<div class="lsn-pre"><pre><code class="language-java">for (int i = 0; i &lt; 3; i++) {
    for (int j = 0; j &lt; 4; j++) {
        System.out.print("*");
    }
    System.out.println();
}
// Prints 3 rows of 4 stars each (12 iterations total)</code></pre></div>

<p class="lsn-p">The inner loop runs 3 × 4 = 12 times. For performance-critical code, minimize unnecessary iterations.</p>

<div class="lsn-callout"><strong>Key takeaway:</strong> Choose the loop construct that best fits your intent. Use <code>while</code> and <code>do-while</code> for condition-driven loops, classical <code>for</code> when you need an index, and enhanced <code>for</code> to iterate cleanly over all elements of a collection.</div>
"""

QUESTIONS = [
    (
        "<strong>Question 1:</strong> What is the output of the following code?<br><pre><code class=\"language-java\">int i = 0;&#10;while (i &lt; 2) {&#10;    System.out.println(i);&#10;    i++;&#10;}</code></pre>",
        [
            ("<code>0</code><br><code>1</code>", True),
            ("<code>0</code><br><code>1</code><br><code>2</code>", False),
            ("(no output)", False),
            ("<code>1</code><br><code>2</code>", False),
        ],
        "The while loop tests <code>i &lt; 2</code> at the top. Starting with i = 0, the condition is true, so the loop prints 0 and increments i to 1. On the next iteration, i = 1 (condition still true), prints 1 and increments i to 2. Now i = 2, so <code>2 &lt; 2</code> is false, and the loop exits."
    ),
    (
        "<strong>Question 2:</strong> What is the output of the following code?<br><pre><code class=\"language-java\">int x = 5;&#10;do {&#10;    System.out.println(x);&#10;    x--;&#10;} while (x &gt; 10);</code></pre>",
        [
            ("(no output)", False),
            ("<code>5</code>", True),
            ("<code>5</code><br><code>4</code><br><code>3</code><br><code>2</code><br><code>1</code>", False),
            ("<code>6</code>", False),
        ],
        "The do-while loop executes the body first, regardless of the condition. It prints 5 (x = 5), then decrements x to 4. Now it tests the condition <code>4 &gt; 10</code>, which is false, so the loop exits. The body ran exactly once."
    ),
    (
        "<strong>Question 3:</strong> What is the output of this loop?<br><pre><code class=\"language-java\">for (int i = 0, j = 4; i &lt; j; i++, j--) {&#10;    System.out.println(i + \",\" + j);&#10;}</code></pre>",
        [
            ("<code>0,4</code><br><code>1,3</code><br><code>2,2</code><br><code>3,1</code>", False),
            ("<code>0,4</code><br><code>1,3</code>", True),
            ("<code>0,4</code><br><code>1,3</code><br><code>2,2</code>", False),
            ("<code>4,0</code>", False),
        ],
        "The for loop initializes i = 0 and j = 4. Iteration 1: <code>0 &lt; 4</code> is true, prints \"0,4\", then i becomes 1 and j becomes 3. Iteration 2: <code>1 &lt; 3</code> is true, prints \"1,3\", then i becomes 2 and j becomes 2. Now <code>2 &lt; 2</code> is false, so the loop exits."
    ),
    (
        "<strong>Question 4:</strong> Which statement best describes the difference between a <code>while</code> loop and a <code>do-while</code> loop?",
        [
            ("A <code>while</code> loop tests the condition at the top; a <code>do-while</code> loop tests the condition at the bottom. With <code>do-while</code>, the body always executes at least once.", True),
            ("A <code>while</code> loop is slower than a <code>do-while</code> loop.", False),
            ("<code>do-while</code> loops cannot use a counter variable.", False),
            ("They are identical; the names are just stylistic preferences.", False),
        ],
        "A while loop evaluates the condition before entering the body (top), so the body might never execute. A do-while evaluates the condition after the body (bottom), guaranteeing at least one execution. This makes do-while ideal for scenarios like input validation where you need to process at least one iteration."
    ),
    (
        "<strong>Question 5:</strong> What is the output of the following code?<br><pre><code class=\"language-java\">for (int i = 0; i &lt; 5; i++) {&#10;    if (i == 2) continue;&#10;    if (i == 4) break;&#10;    System.out.println(i);&#10;}</code></pre>",
        [
            ("<code>0</code><br><code>1</code><br><code>3</code>", True),
            ("<code>0</code><br><code>1</code>", False),
            ("<code>0</code><br><code>1</code><br><code>2</code><br><code>3</code><br><code>4</code>", False),
            ("<code>1</code><br><code>3</code>", False),
        ],
        "The loop runs with i = 0 (prints 0), i = 1 (prints 1), i = 2 (continue skips the print), i = 3 (prints 3), i = 4 (break exits before the print). So the output is 0, 1, 3."
    ),
    (
        "<strong>Question 6:</strong> What does the following code produce?<br><pre><code class=\"language-java\">int[] arr = {1, 2, 3};&#10;for (int num : arr) {&#10;    System.out.print(num + \" \");&#10;}</code></pre>",
        [
            ("<code>1 2 3 </code>", True),
            ("<code>0 1 2 </code>", False),
            ("<code>1 2 3</code> (no trailing space)", False),
            ("(compilation error)", False),
        ],
        "The enhanced for loop (for-each) iterates over each element of the array in order. The variable <code>num</code> takes on the value of each element (1, 2, 3) and prints it followed by a space, resulting in \"1 2 3 \" with a trailing space."
    ),
    (
        "<strong>Question 7:</strong> What is the output of this nested loop with a labeled break?<br><pre><code class=\"language-java\">outer: for (int i = 0; i &lt; 2; i++) {&#10;    for (int j = 0; j &lt; 3; j++) {&#10;        if (i == 0 &amp;&amp; j == 1) break outer;&#10;        System.out.print(j);&#10;    }&#10;}&#10;System.out.println(\" done\");</code></pre>",
        [
            ("<code>0 done</code>", True),
            ("<code>0 1 done</code>", False),
            ("<code>0 1 2 0 1 2  done</code>", False),
            ("<code>0 1 2  done</code>", False),
        ],
        "The outer loop starts with i = 0. The inner loop begins with j = 0, prints 0. When j = 1, the condition <code>i == 0 &amp;&amp; j == 1</code> is true, so <code>break outer</code> exits both loops entirely. Control jumps to after both loops, printing \" done\"."
    ),
    (
        "<strong>Question 8:</strong> Identify the error in this code:<br><pre><code class=\"language-java\">for (int i = 0; i &lt; 5; ) {&#10;    System.out.println(i);&#10;}</code></pre>",
        [
            ("The update section is missing, so the loop will be infinite.", True),
            ("The init section is missing; this will not compile.", False),
            ("The condition is invalid syntax.", False),
            ("You cannot omit sections in a for loop.", False),
        ],
        "While the for loop allows optional sections, this code omits the update (third section). Since <code>i</code> is never incremented, it remains 0, the condition <code>0 &lt; 5</code> is always true, and the loop runs forever. To fix it, add <code>i++</code> in the update section or increment i inside the body."
    ),
]