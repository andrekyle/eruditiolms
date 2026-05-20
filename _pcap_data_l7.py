LESSON_HTML = """<h2>What you will learn</h2>
<ul>
<li>Create and work with string literals using single, double, and triple quotes</li>
<li>Use escape sequences to include special characters in strings</li>
<li>Understand why strings are immutable and what that means</li>
<li>Access individual characters and extract substrings using indexing and slicing</li>
<li>Apply common string methods to modify and analyze text</li>
<li>Format strings using f-strings and the <code>format()</code> method</li>
<li>Convert between strings and numbers safely</li>
<li>Choose between concatenation and <code>join()</code> for performance</li>
</ul>

<h3>String Literals and Escape Sequences</h3>
<p>In Python, strings can be created using single quotes, double quotes, or triple quotes. All three styles work identically&mdash;choose the one that makes your code most readable. Triple-quoted strings allow text across multiple lines without explicit newlines.</p>
<pre><code class="language-python">single = 'Hello'
double = "World"
triple = '''This is
a multiline
string'''

print(single)
print(double)
print(triple)
</code></pre>
<p>Escape sequences let you include special characters. The most common are <code>\\n</code> (newline), <code>\\t</code> (tab), <code>\\\\</code> (literal backslash), and <code>\\"</code> (quote inside a string).</p>
<pre><code class="language-python">path = "C:\\\\Users\\\\Name\\\\Documents"
quote = "She said, \\"Hello!\\""
formatted = "Name\\tAge\\nAlice\\t30\\nBob\\t25"

print(path)
print(quote)
print(formatted)
</code></pre>

<h3>String Immutability</h3>
<p>Strings in Python are <strong>immutable</strong>: once created, they cannot be changed. Any operation that appears to modify a string actually creates a new one. This guarantees the original stays the same and is essential for predictability.</p>
<pre><code class="language-python">name = "Alice"
print(id(name))     # memory address

name = name + " Smith"
print(id(name))     # different - new string created

# Raises TypeError:
# name[0] = 'B'
</code></pre>

<h3>Indexing and Slicing</h3>
<p>Access individual characters with square brackets. Python uses zero-based indexing; negative indices count backward from the end. Slicing extracts a range using <code>start:end:step</code> where <code>end</code> is exclusive.</p>
<pre><code class="language-python">word = "Python"
print(word[0])      # 'P'
print(word[-1])     # 'n'
print(word[1:4])    # 'yth'
print(word[::-1])   # 'nohtyP' (reverse)
print(word[::2])    # 'Pto'
</code></pre>

<h3>Essential String Methods</h3>
<p><code>lower()</code> and <code>upper()</code> change case; <code>strip()</code> removes whitespace from the edges; <code>replace()</code> swaps substrings; <code>split()</code> breaks a string into a list; <code>join()</code> combines a list into a string; <code>startswith()</code>/<code>endswith()</code> check boundaries; <code>find()</code> locates substrings; <code>count()</code> counts occurrences.</p>
<pre><code class="language-python">text = "  Hello World  "
print(text.strip())          # "Hello World"
print(text.lower())          # "  hello world  "

sentence = "python is awesome"
print(sentence.replace("awesome", "fun"))  # "python is fun"
print(sentence.startswith("python"))        # True

words = "apple,banana,cherry"
print(words.split(","))      # ['apple', 'banana', 'cherry']

fruits = ["apple", "banana", "cherry"]
print(" and ".join(fruits))  # "apple and banana and cherry"
</code></pre>

<h3>Formatting Strings</h3>
<p><strong>F-strings</strong> (formatted string literals) are the modern, readable way to embed values. Prefix the string with <code>f</code> and place expressions inside curly braces. The <code>format()</code> method is the older alternative.</p>
<pre><code class="language-python">name = "Alice"
age = 30
price = 19.99

print(f"{name} is {age} years old")
print(f"Price: ${price:.2f}")

print("My name is {} and I am {} years old".format(name, age))

# Slower, less readable
result = "Name: " + name + ", Age: " + str(age)
print(result)
</code></pre>

<h3>String Conversions</h3>
<p>Convert between strings and numbers using <code>int()</code>, <code>float()</code>, and <code>str()</code>. Wrap conversions in try-except when input is untrusted.</p>
<pre><code class="language-python">num_str = "42"
num_int = int(num_str)
print(num_int + 8)  # 50

price_float = float("19.99")
print(price_float * 2)  # 39.98

print(str(100) + " dollars")  # "100 dollars"

# Raw strings ignore escape sequences
path = r"C:\\Users\\Name\\file.txt"
print(path)
</code></pre>

<h3>Performance: Join vs Concatenation</h3>
<p>When combining many strings, <code>join()</code> is significantly faster than repeated <code>+</code>. Because strings are immutable, each <code>+</code> creates a new string and copies all previous characters.</p>
<table>
<tr><th>Method</th><th>Code</th><th>Speed</th></tr>
<tr><td>Concatenation</td><td><code>result = result + item</code></td><td>Slow</td></tr>
<tr><td>Join</td><td><code>result = "".join(items)</code></td><td>Fast</td></tr>
</table>

<h3>Wrap-up</h3>
<p>Strings are one of Python's fundamental data types. You now understand their immutable nature, how to access parts using indexing and slicing, and how to transform them with methods like <code>lower()</code>, <code>split()</code>, and <code>replace()</code>. You can format output clearly with f-strings and safely convert between strings and numbers. Remember: use <code>join()</code> when combining many strings, and escape special characters when needed.</p>
"""

QUESTIONS = [
    ('multiple_choice', '<p>What does this code print?</p><pre><code class="language-python">s = "hello"\ns = s.upper()</code></pre>', [
        ('<code>"hello"</code>', False),
        ('<code>"HELLO"</code>', True),
        ('<code>None</code>', False),
        ('Error', False),
    ], '<p>Strings are immutable; <code>.upper()</code> returns a new uppercase string. The variable <code>s</code> is reassigned to that new string.</p>'),
    ('multiple_choice', '<p>What is the result of <code>s[1:4]</code> when <code>s = "Python"</code>?</p>', [
        ('<code>"Pyt"</code>', False),
        ('<code>"ytho"</code>', False),
        ('<code>"yth"</code>', True),
        ('<code>"Pyth"</code>', False),
    ], '<p>Slicing returns characters at indices 1, 2 and 3 (the end is exclusive): <code>"yth"</code>.</p>'),
    ('multiple_choice', '<p>What does <code>print("Line1\\nLine2")</code> output?</p>', [
        ('<code>Line1\\nLine2</code>', False),
        ('<code>Line1 Line2</code>', False),
        ('<code>Line1</code> on one line, <code>Line2</code> on the next', True),
        ('Error', False),
    ], '<p>The escape sequence <code>\\n</code> is a newline. The two parts print on separate lines.</p>'),
    ('multiple_choice', '<p>What does <code>"one,two,three".split(",")</code> return?</p>', [
        ('<code>"one" "two" "three"</code>', False),
        ('<code>["one", "two", "three"]</code>', True),
        ('<code>"onetwothree"</code>', False),
        ('<code>None</code>', False),
    ], '<p><code>.split()</code> returns a list of substrings divided by the separator. The inverse is <code>.join()</code>.</p>'),
    ('multiple_choice', '<p>What is the primary difference between <code>.strip()</code> and <code>.replace()</code>?</p>', [
        ('<code>.strip()</code> removes leading/trailing whitespace; <code>.replace()</code> swaps occurrences of a substring anywhere in the string', True),
        ('<code>.replace()</code> only works at string edges; <code>.strip()</code> works anywhere', False),
        ('<code>.strip()</code> returns <code>None</code>; <code>.replace()</code> returns a string', False),
        ('<code>.strip()</code> modifies the original; <code>.replace()</code> creates a new string', False),
    ], '<p><code>.strip()</code> targets whitespace at the edges. <code>.replace()</code> searches throughout the string.</p>'),
    ('multiple_choice', '<p>What is the output?</p><pre><code class="language-python">name = "Bob"\nprint(f"Hello, {name.upper()}!")</code></pre>', [
        ('<code>Hello, {name.upper()}!</code>', False),
        ('<code>Hello, Bob!</code>', False),
        ('<code>Hello, BOB!</code>', True),
        ('Error: invalid syntax', False),
    ], '<p>F-strings evaluate expressions inside braces. <code>"Bob".upper()</code> becomes <code>"BOB"</code>.</p>'),
    ('multiple_choice', '<p>What does <code>"hello".find("l")</code> return?</p>', [
        ('<code>-1</code>', False),
        ('<code>0</code>', False),
        ('<code>2</code>', True),
        ('<code>None</code>', False),
    ], '<p><code>.find()</code> returns the lowest index where the substring appears. The first <code>l</code> in <code>"hello"</code> is at index 2. (<code>.find()</code> returns <code>-1</code> only when the substring is absent.)</p>'),
    ('multiple_choice', '<p>Which statement about Python string methods is <strong>correct</strong>?</p>', [
        ('<code>.replace()</code> modifies the string in place', False),
        ('Only <code>.upper()</code> and <code>.lower()</code> return new strings', False),
        ('<code>.split()</code> returns a modified version of the original string', False),
        ('All string methods return a new string; none modify strings in place', True),
    ], '<p>Strings are immutable, so no method can mutate the original. Every method that &ldquo;changes&rdquo; a string returns a new one &mdash; you must reassign the result to keep it.</p>'),
]
