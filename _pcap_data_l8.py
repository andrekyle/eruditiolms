LESSON_HTML = """<h2>What you will learn</h2>
<ul>
<li>Import modules using <code>import</code>, <code>from...import</code>, and aliases</li>
<li>Use standard library modules like <code>math</code>, <code>random</code>, and <code>datetime</code></li>
<li>Create and organize your own modules and packages</li>
<li>Work with files using <code>open()</code> and the <code>with</code> statement</li>
<li>Understand file modes for reading and writing</li>
<li>Handle errors gracefully with <code>try/except</code> blocks and raise exceptions</li>
</ul>

<h3>Modules: Reusing Code</h3>
<p>A <strong>module</strong> is a Python file containing functions, variables, or classes that you can reuse. Python ships with a huge <strong>standard library</strong> that solves common problems&mdash;you import what you need instead of writing everything from scratch.</p>

<h3>Importing Modules</h3>
<p>There are three main ways to import code:</p>
<pre><code class="language-python">
# 1. Import the whole module
import math
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793

# 2. Import specific names
from random import randint, choice
number = randint(1, 10)
item = choice(['apple', 'banana', 'cherry'])
print(f"Number: {number}, Item: {item}")

# 3. Alias with 'as'
import datetime as dt
today = dt.date.today()
print(f"Today is {today}")
</code></pre>
<p>Use <code>import math</code> when you want everything math provides. Use <code>from math import sqrt</code> when you only need one function. Aliases shorten long names.</p>

<h3>The Standard Library</h3>
<p>The standard library includes hundreds of modules for math, randomness, dates and times, file operations, and much more. Three essentials:</p>
<pre><code class="language-python">
import math
import random
from datetime import datetime, timedelta

radius = 5
area = math.pi * radius ** 2
print(f"Circle area: {area:.2f}")

dice_roll = random.randint(1, 6)
shuffled = random.sample(range(1, 11), 5)
print(f"Dice: {dice_roll}, Sample: {shuffled}")

now = datetime.now()
tomorrow = now + timedelta(days=1)
print(f"Now: {now.strftime('%Y-%m-%d %H:%M')}")
print(f"Tomorrow: {tomorrow.date()}")
</code></pre>

<h3>Creating Your Own Module</h3>
<p>Any Python file can be a module. Save functions in a file, then import them elsewhere.</p>
<pre><code class="language-python">
# calculator.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

VERSION = "1.0"

# main.py (in the same folder)
import calculator
result = calculator.add(5, 3)
print(f"5 + 3 = {result}")
print(f"Calculator version: {calculator.VERSION}")
</code></pre>

<h3>Packages and Organization</h3>
<p>A <strong>package</strong> is a folder containing Python files and a special <code>__init__.py</code> file. The presence of <code>__init__.py</code> tells Python the folder is a package. Packages let you group related modules together.</p>
<pre><code class="language-python">
# Folder layout:
# myapp/
#   __init__.py
#   math_tools.py
#   string_tools.py

from myapp.math_tools import add
from myapp.string_tools import reverse_string
</code></pre>

<h3>Working with Files</h3>
<p>The <code>open()</code> function opens a file and returns a file object. Always use the <code>with</code> statement&mdash;it automatically closes the file when you're done, even if an exception is raised.</p>
<pre><code class="language-python">
# Write
with open('notes.txt', 'w') as f:
    f.write('Line 1: Hello\\n')
    f.write('Line 2: Python\\n')
    f.write('Line 3: World\\n')

# Read everything at once
with open('notes.txt', 'r') as f:
    content = f.read()
    print(content)

# Read line by line (memory-friendly for large files)
with open('notes.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Append (does not overwrite)
with open('notes.txt', 'a') as f:
    f.write('Line 4: New entry\\n')
</code></pre>

<h3>File Modes</h3>
<ul>
<li><code>'r'</code> &mdash; Read (default; file must exist)</li>
<li><code>'w'</code> &mdash; Write (creates or <strong>overwrites</strong>)</li>
<li><code>'a'</code> &mdash; Append (creates if absent, otherwise adds to end)</li>
<li><code>'rb'</code>, <code>'wb'</code> &mdash; Binary read/write (images, executables)</li>
</ul>

<h3>Exception Handling</h3>
<p>Errors happen&mdash;users enter bad data, files don't exist, code divides by zero. <strong>Exceptions</strong> are Python's way of handling errors without crashing. Use <code>try/except</code> to catch them:</p>
<pre><code class="language-python">
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Your age is {age}")
except ValueError as e:
    print(f"Error: {e}")
except Exception:
    print("An unexpected error occurred")

try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print(f"Successfully read {len(data)} characters")
finally:
    print("This line always runs, regardless of errors")
</code></pre>
<p><code>else</code> runs only when no exception was raised. <code>finally</code> always runs&mdash;ideal for cleanup like closing resources.</p>

<h3>Common Built-In Exceptions</h3>
<table>
<tr><th>Exception</th><th>Cause</th></tr>
<tr><td><code>ValueError</code></td><td>Wrong value type, e.g. <code>int("hello")</code></td></tr>
<tr><td><code>TypeError</code></td><td>Wrong operation on a type, e.g. <code>"5" + 3</code></td></tr>
<tr><td><code>ZeroDivisionError</code></td><td>Division by zero: <code>10 / 0</code></td></tr>
<tr><td><code>FileNotFoundError</code></td><td>Opening a file that doesn't exist</td></tr>
<tr><td><code>KeyError</code></td><td>Dict key missing: <code>my_dict['missing']</code></td></tr>
<tr><td><code>IndexError</code></td><td>List index out of range</td></tr>
</table>

<h3>Raising Your Own Exceptions</h3>
<p>Use <code>raise</code> to deliberately trigger an exception when something is wrong.</p>
<pre><code class="language-python">
def check_password(pwd):
    if len(pwd) < 8:
        raise ValueError("Password must be at least 8 characters")
    if not any(c.isupper() for c in pwd):
        raise ValueError("Password must contain an uppercase letter")
    return True

try:
    check_password("hello")
except ValueError as e:
    print(f"Invalid password: {e}")
</code></pre>

<h3>Wrap-up</h3>
<p>Modules, files, and exceptions are the building blocks of professional Python programs. Modules let you reuse and organize code; files let you save data persistently; exceptions let your code handle problems gracefully. Practice importing standard library modules, creating your own modules, reading and writing files with <code>with</code> statements, and catching exceptions.</p>
"""

QUESTIONS = [
    ('multiple_choice', '<p>What is the key difference between <code>import module</code> and <code>from module import function</code>?</p>', [
        ('<code>import</code> loads the entire namespace only', False),
        ('<code>from-import</code> brings specific names directly into the current namespace', True),
        ('<code>import</code> only works with packages', False),
        ('<code>from-import</code> requires the module to be installed first', False),
    ], '<p><code>from-import</code> binds individual names into the current namespace, avoiding the <code>module.</code> prefix.</p>'),
    ('multiple_choice', '<p>What happens when you open a file with mode <code>"w"</code>?</p>', [
        ('If the file exists, it is completely overwritten with new content', True),
        ('If the file exists, new content is appended to it', False),
        ('A new file is created while preserving existing content', False),
        ('The file is opened read-only to prevent accidental changes', False),
    ], '<p>Mode <code>"w"</code> truncates the file, removing all previous content before writing.</p>'),
    ('multiple_choice', '<p>What is the primary advantage of using a <code>with</code> statement for file operations?</p>', [
        ('It allows multiple files to be opened simultaneously', False),
        ('It improves disk I/O performance by optimizing buffering', False),
        ('It automatically closes the file when the block exits, even if an exception occurs', True),
        ('It prevents other programs from accessing the file during the operation', False),
    ], '<p>The <code>with</code> statement guarantees the file is closed when the block ends &mdash; no leaks even on exceptions.</p>'),
    ('multiple_choice', '<p>When reading a file in text mode, what does <code>file.read()</code> return?</p>', [
        ('A <code>bytes</code> object containing the raw file data', False),
        ('A <code>list</code> of strings, one per line', False),
        ('An <code>int</code> representing the number of bytes read', False),
        ('A <code>str</code> containing the entire file content as text', True),
    ], '<p>Text mode decodes bytes to <code>str</code>. Binary mode (<code>"rb"</code>) would return <code>bytes</code>.</p>'),
    ('multiple_choice', '<p>When you have multiple <code>except</code> blocks, which one executes?</p>', [
        ('The first <code>except</code> block in source order', False),
        ('The <code>except</code> block whose exception class matches the raised exception', True),
        ('All <code>except</code> blocks that could match', False),
        ('Only the most generic handler', False),
    ], '<p>Python checks each <code>except</code> in order and runs the first whose class matches (including subclasses) the raised exception.</p>'),
    ('multiple_choice', '<p>When does the <code>finally</code> block run?</p>', [
        ('Always, regardless of whether an exception occurred or was handled', True),
        ('Only if an exception was raised and caught', False),
        ('Only if no exception occurs during the <code>try</code> block', False),
        ('Only if the <code>except</code> block completes without a <code>return</code>', False),
    ], '<p><code>finally</code> is guaranteed to run, making it ideal for cleanup such as closing files.</p>'),
    ('multiple_choice', '<p>How do you raise a custom <code>ValueError</code> with a message?</p>', [
        ('<code>raise("ValueError: message")</code>', False),
        ('<code>ValueError("message")</code>', False),
        ('<code>raise ValueError("message")</code>', True),
        ('<code>throw ValueError("message")</code>', False),
    ], '<p>The <code>raise</code> keyword triggers an exception. Python has no <code>throw</code>; you raise an instance of the exception class.</p>'),
    ('multiple_choice', '<p>Which exception is raised by <code>int("abc")</code>?</p>', [
        ('<code>TypeError</code>', False),
        ('<code>AttributeError</code>', False),
        ('<code>KeyError</code>', False),
        ('<code>ValueError</code>', True),
    ], '<p><code>int()</code> raises <code>ValueError</code> when given a string it cannot convert to an integer.</p>'),
]
