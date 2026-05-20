LESSON_HTML = """<h2>What you will learn</h2>
<ul>
<li>How to make decisions with <code>if</code>, <code>elif</code>, and <code>else</code> statements</li>
<li>Comparison operators and logical operators for building conditions</li>
<li>Understanding truthiness and falsy values in Python</li>
<li>Using conditional (ternary) expressions for one-liners</li>
<li>Building loops with <code>while</code> and <code>for</code> statements</li>
<li>Controlling loops with <code>break</code>, <code>continue</code>, and <code>else</code> clauses</li>
<li>Working with nested loops and common pitfalls</li>
</ul>

<h3>Conditional Statements: if, elif, else</h3>
<p>Conditional statements let your program make decisions. The basic structure is: if a condition is true, execute a block of code. Here's the syntax:</p>
<pre><code class="language-python">
age = 16

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
</code></pre>
<p>Python evaluates <code>if</code> first. If that condition is false, it checks <code>elif</code> (else if) blocks in order. If all are false, it runs the <code>else</code> block. Only one block executes&mdash;Python stops checking once it finds a true condition.</p>

<h3>Comparison and Logical Operators</h3>
<p>Conditions use comparison operators: <code>==</code> (equal), <code>!=</code> (not equal), <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, <code>&gt;=</code>. Combine them with logical operators: <code>and</code>, <code>or</code>, <code>not</code>.</p>
<pre><code class="language-python">
score = 75
passed = score >= 60

if score >= 80 and passed:
    print("Excellent score!")

if score < 50 or score > 95:
    print("Extreme score")

if not passed:
    print("Try again next time")
</code></pre>
<p><code>and</code> requires both conditions true. <code>or</code> requires at least one true. <code>not</code> reverses the truth value. These operators are essential for building complex decisions.</p>

<h3>Truthiness and Falsy Values</h3>
<p>In Python, values have inherent truth values. An object is <em>falsy</em> if it evaluates to <code>False</code> in a boolean context. These are falsy: <code>False</code>, <code>None</code>, <code>0</code>, <code>0.0</code>, empty string <code>""</code>, empty list <code>[]</code>, empty dict <code>{}</code>. Everything else is truthy.</p>
<pre><code class="language-python">
name = "Alice"
if name:
    print("Name exists")

items = []
if not items:
    print("No items in list")

count = 0
if count:
    print("This won't print - 0 is falsy")
else:
    print("Count is zero or falsy")
</code></pre>

<h3>The Conditional (Ternary) Expression</h3>
<p>For simple if-else logic, use a conditional expression: <code>value_if_true if condition else value_if_false</code>. It's a one-liner alternative to a full if-else block.</p>
<pre><code class="language-python">
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

score = 45
result = "Pass" if score >= 50 else "Fail"
print(result)

temperature = 25
weather = "Hot" if temperature > 30 else "Cool" if temperature > 15 else "Cold"
</code></pre>

<h3>While Loops</h3>
<p>A <code>while</code> loop repeats a block as long as a condition is true. Be careful&mdash;if the condition never becomes false, you'll have an infinite loop.</p>
<pre><code class="language-python">
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
</code></pre>
<p>Use <code>break</code> to exit a loop immediately and <code>continue</code> to skip to the next iteration:</p>
<pre><code class="language-python">
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")

count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
</code></pre>
<p>A <code>while-else</code> clause runs after the loop ends normally (without <code>break</code>). This is useful when you search for something and want to know if you found it.</p>

<h3>For Loops and Ranges</h3>
<p>A <code>for</code> loop iterates over a sequence. The <code>range()</code> function generates numbers. <code>range(n)</code> produces 0 through n-1.</p>
<pre><code class="language-python">
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)

colors = ["red", "green", "blue"]
for color in colors:
    print(color)
</code></pre>
<p><code>range(start, stop, step)</code> lets you control the sequence. You can loop over strings, lists, tuples, dictionaries, and other iterables.</p>

<h3>Nested Loops and Loop Control</h3>
<p>Loops can contain other loops. Each iteration of the outer loop runs the inner loop completely. Use this for multi-dimensional structures or combinations.</p>
<pre><code class="language-python">
for row in range(3):
    for col in range(3):
        print(f"({row}, {col})", end=" ")
    print()

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()
</code></pre>
<p>The <code>pass</code> statement does nothing&mdash;use it when Python requires a code block but you don't have code yet.</p>

<h3>Common Pitfalls</h3>
<p><strong>Off-by-one errors:</strong> <code>range(5)</code> gives 0, 1, 2, 3, 4&mdash;not including 5. If you want 1 through 5, use <code>range(1, 6)</code>.</p>
<p><strong>Infinite loops:</strong> A <code>while</code> loop with a condition that never becomes false runs forever. Always ensure your condition will eventually be false or you have a <code>break</code>.</p>
<p><strong>Mutating during iteration:</strong> Avoid adding or removing items from a list while iterating over it&mdash;this skips elements or causes errors. Iterate over a copy or build a new list instead.</p>

<h3>Wrap-up</h3>
<p>Control flow structures&mdash;conditionals and loops&mdash;are foundational to programming. <code>if</code> statements let you branch based on conditions and make decisions. <code>while</code> and <code>for</code> loops let you repeat code efficiently. Master <code>break</code>, <code>continue</code>, and loop boundaries. Pay attention to off-by-one errors and infinite loops. With these tools, you can write responsive programs that handle complex logic and process data systematically.</p>
"""

QUESTIONS = [
    ('multiple_choice', '<p>What will this code print?</p><pre><code class="language-python">if 5 &gt; 3:\n    print("A")\nelif 5 &gt; 1:\n    print("B")\nelse:\n    print("C")</code></pre>', [
        ('<code>A</code>', True),
        ('<code>B</code>', False),
        ('<code>C</code>', False),
        ('<code>A</code> and <code>B</code>', False),
    ], '<p>Once an <code>if</code> block executes successfully, the <code>elif</code> and <code>else</code> blocks are skipped entirely, regardless of whether their conditions are true.</p>'),
    ('multiple_choice', '<p>Which value is <strong>falsy</strong> in Python?</p>', [
        ('<code>1</code>', False),
        ('<code>"hello"</code>', False),
        ('<code>[]</code>', True),
        ('<code>True</code>', False),
    ], '<p>An empty list <code>[]</code> is falsy. Non-zero numbers, non-empty strings, and <code>True</code> are all truthy.</p>'),
    ('multiple_choice', '<p>What is the output?</p><pre><code class="language-python">x = 10\nprint(x != 10 and x &gt; 5)</code></pre>', [
        ('<code>True</code>', False),
        ('<code>False</code>', True),
        ('<code>None</code>', False),
        ('<code>10</code>', False),
    ], '<p><code>x != 10</code> evaluates to <code>False</code>. Since the first operand of <code>and</code> is <code>False</code>, the entire expression short-circuits to <code>False</code>.</p>'),
    ('multiple_choice', '<p>What will <code>result</code> be?</p><pre><code class="language-python">age = 25\nresult = "Adult" if age &gt;= 18 else "Minor"</code></pre>', [
        ('<code>"Minor"</code>', False),
        ('<code>"Adult"</code>', True),
        ('<code>True</code>', False),
        ('<code>25</code>', False),
    ], '<p>A ternary expression evaluates the condition (<code>age &gt;= 18</code>); since 25 satisfies it, the first value <code>"Adult"</code> is returned.</p>'),
    ('multiple_choice', '<p>What does this code print?</p><pre><code class="language-python">count = 0\nwhile count &lt; 2:\n    print(count)\n    count += 1\nelse:\n    print("Done")</code></pre>', [
        ('<code>0</code><br><code>1</code>', False),
        ('<code>0</code><br><code>1</code><br><code>Done</code>', True),
        ('<code>Done</code>', False),
        ('<code>0</code><br><code>1</code><br><code>2</code><br><code>Done</code>', False),
    ], '<p>The <code>while</code> loop prints 0 and 1, then exits normally. The <code>else</code> block runs because the loop completed without a <code>break</code>.</p>'),
    ('multiple_choice', '<p>How many times does the loop body execute?</p><pre><code class="language-python">for i in range(2, 6):\n    print(i)</code></pre>', [
        ('<code>6</code> times', False),
        ('<code>4</code> times', True),
        ('<code>5</code> times', False),
        ('<code>3</code> times', False),
    ], '<p><code>range(2, 6)</code> produces 2, 3, 4, 5 &mdash; exactly 4 values. The end value (6) is excluded.</p>'),
    ('multiple_choice', '<p>What is printed?</p><pre><code class="language-python">for i in range(5):\n    if i == 2:\n        break\n    print(i)</code></pre>', [
        ('<code>0</code><br><code>1</code><br><code>2</code>', False),
        ('<code>0</code><br><code>1</code>', True),
        ('<code>2</code><br><code>3</code><br><code>4</code>', False),
        ('<code>0</code><br><code>1</code><br><code>3</code><br><code>4</code>', False),
    ], '<p><code>break</code> exits the loop immediately. When <code>i == 2</code> the break fires before printing, so only 0 and 1 appear.</p>'),
    ('multiple_choice', '<p>What is the bug in this code?</p><pre><code class="language-python">numbers = [1, 2, 3, 4, 5]\nfor num in numbers:\n    if num == 3:\n        numbers.remove(num)\nprint(numbers)</code></pre>', [
        ('<code>Syntax error</code>', False),
        ('<code>NameError: num is undefined</code>', False),
        ('The element <code>4</code> is skipped because the list is modified during iteration', True),
        ('The loop never terminates', False),
    ], '<p>Modifying a list while iterating over it causes the iterator to skip elements. After removing 3, the iterator jumps past 4 to 5.</p>'),
]
