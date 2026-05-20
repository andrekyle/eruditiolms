LESSON_HTML = """<h2>What you will learn</h2>
<ul>
<li>Define and call functions using <strong>def</strong></li>
<li>Distinguish parameters, arguments, and argument types (positional, keyword, default)</li>
<li>Use <strong>*args</strong> and <strong>**kwargs</strong> for flexible parameters</li>
<li>Return values and understand function scope</li>
<li>Apply the LEGB rule, <strong>global</strong> and <strong>nonlocal</strong> keywords</li>
<li>Write docstrings and recursion patterns</li>
<li>Create and use lambda expressions and higher-order functions</li>
</ul>

<h3>Defining Functions</h3>
<p>A function is a reusable block of code that performs a specific task. You define functions with the <strong>def</strong> keyword, followed by a name, parentheses, and a colon. The function body is indented.</p>
<pre><code class="language-python">def greet(name):
    \"\"\"This function greets a person by name.\"\"\"
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
</code></pre>

<h3>Parameters vs Arguments</h3>
<p><strong>Parameters</strong> are the variables listed in the function definition. <strong>Arguments</strong> are the values you pass when calling the function. In the example above, <code>name</code> is a parameter; <code>"Alice"</code> is an argument.</p>

<h3>Argument Types</h3>
<p><em>Positional arguments</em> must be provided in the same order as parameters. <em>Keyword arguments</em> are passed as <code>name=value</code>. <em>Default arguments</em> have preset values if not provided.</p>
<pre><code class="language-python">def introduce(first, last, title="Friend"):
    return f"{title} {first} {last}"

print(introduce("John", "Doe"))                            # Friend John Doe
print(introduce(last="Smith", first="Jane", title="Dr."))  # Dr. Jane Smith
print(introduce("Bob", last="Jones"))                      # Friend Bob Jones
</code></pre>

<h3>*args and **kwargs</h3>
<p>When you don't know how many arguments will be passed, use <code>*args</code> (any number of positional arguments) or <code>**kwargs</code> (keyword arguments). <code>args</code> becomes a tuple; <code>kwargs</code> becomes a dictionary.</p>
<pre><code class="language-python">def summarize(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

summarize(1, 2, 3, name="Alice", age=30)
# Positional args: (1, 2, 3)
# Keyword args: {'name': 'Alice', 'age': 30}
</code></pre>

<h3>Return Values</h3>
<p>Functions return values using the <code>return</code> keyword. Without an explicit return, functions return <code>None</code>. A function can return any data type or multiple values as a tuple.</p>
<pre><code class="language-python">def calculate(a, b):
    \"\"\"Return sum and product of two numbers.\"\"\"
    return a + b, a * b

sum_result, product_result = calculate(4, 5)
print(sum_result, product_result)  # 9 20
</code></pre>

<h3>Scope and the LEGB Rule</h3>
<p>Variable scope determines where a variable is accessible. Python follows the <strong>LEGB rule</strong>: <strong>Local</strong> (inside function), <strong>Enclosing</strong> (in outer functions), <strong>Global</strong> (module level), <strong>Built-in</strong> (Python built-ins). Python searches in this order.</p>
<p>Use <code>global</code> to modify a global variable inside a function. Use <code>nonlocal</code> to modify a variable in an enclosing function.</p>
<pre><code class="language-python">count = 0  # Global

def increment():
    global count
    count += 1
    return count

print(increment())  # 1
print(increment())  # 2

def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    return x

print(outer())  # 20
</code></pre>

<h3>Docstrings</h3>
<p>A docstring is a string literal that documents what a function does. Place it immediately after the <code>def</code> line, using triple quotes. Access docstrings with <code>help()</code> or the <code>__doc__</code> attribute. Good docstrings describe the purpose, parameters, return value, and optional examples.</p>

<h3>Recursion</h3>
<p>A recursive function calls itself. It must have a <strong>base case</strong> (to stop recursion) and a <strong>recursive case</strong> (that gets closer to the base case).</p>
<pre><code class="language-python">def factorial(n):
    \"\"\"Return n factorial.\"\"\"
    if n == 0 or n == 1:        # Base case
        return 1
    return n * factorial(n - 1) # Recursive case

print(factorial(5))  # 120
</code></pre>

<h3>Lambda Expressions</h3>
<p>A <code>lambda</code> is a small anonymous function. Use it for simple one-line operations, especially with <code>map()</code>, <code>filter()</code> or <code>sorted()</code>. Syntax: <code>lambda arguments: expression</code>.</p>
<pre><code class="language-python">add = lambda x, y: x + y
print(add(3, 5))  # 8

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens   = list(filter(lambda x: x % 2 == 0, numbers))
print(squared)  # [1, 4, 9, 16, 25]
print(evens)    # [2, 4]
</code></pre>

<h3>Passing Functions as Arguments</h3>
<p>Functions are first-class objects in Python, meaning you can pass them to other functions. A function that accepts another function is called a <em>higher-order function</em>.</p>
<pre><code class="language-python">def apply_operation(x, y, operation):
    return operation(x, y)

print(apply_operation(10, 5, lambda a, b: a + b))  # 15
print(apply_operation(10, 5, lambda a, b: a * b))  # 50
</code></pre>

<h3>Wrap-up</h3>
<p>Functions are essential to writing clean, reusable Python code. Master the basics&mdash;defining functions, managing parameters and arguments, and understanding scope&mdash;and you'll unlock powerful patterns like recursion, lambdas, and higher-order functions. Remember to write clear docstrings and choose meaningful names so others can understand your code at a glance.</p>
"""

QUESTIONS = [
    ('multiple_choice', '<p>Which of the following is the correct syntax for defining a function in Python?</p>', [
        ('<code>function add(a, b):<br>&nbsp;&nbsp;&nbsp;&nbsp;return a + b</code>', False),
        ('<code>def add(a, b)<br>&nbsp;&nbsp;&nbsp;&nbsp;return a + b</code>', False),
        ('<code>def add(a, b):<br>&nbsp;&nbsp;&nbsp;&nbsp;return a + b</code>', True),
        ('<code>define add(a, b):<br>&nbsp;&nbsp;&nbsp;&nbsp;return a + b</code>', False),
    ], '<p>Python uses the <code>def</code> keyword to define functions, followed by parameters in parentheses and a colon. The body must be indented.</p>'),
    ('multiple_choice', '<p>What value does a function return if it has no <code>return</code> statement?</p>', [
        ('<code>None</code>', True),
        ('<code>0</code>', False),
        ('An empty string <code>""</code>', False),
        ('<code>False</code>', False),
    ], '<p>Functions without an explicit <code>return</code> implicitly return <code>None</code>.</p>'),
    ('multiple_choice', '<p>What does the second call return?</p><pre><code class="language-python">def append_to(element, to=[]):\n    to.append(element)\n    return to\nappend_to(1)\nappend_to(2)</code></pre>', [
        ('<code>[2]</code>', False),
        ('<code>[]</code>', False),
        ('<code>[1]</code>', False),
        ('<code>[1, 2]</code>', True),
    ], '<p>Mutable default arguments are evaluated <em>once</em> when the function is defined, not on each call. The list persists between calls &mdash; this is the famous mutable default trap.</p>'),
    ('multiple_choice', '<p>Which function signature accepts any number of positional <em>and</em> keyword arguments?</p>', [
        ('<code>def func(*args, *kwargs):</code>', False),
        ('<code>def func(*args, **kwargs):</code>', True),
        ('<code>def func(**args, **kwargs):</code>', False),
        ('<code>def func(args, kwargs):</code>', False),
    ], '<p><code>*args</code> captures extra positional arguments as a tuple; <code>**kwargs</code> captures extra keyword arguments as a dict. The double asterisk is required for the keyword form.</p>'),
    ('multiple_choice', '<p>Which call is <strong>invalid</strong> for <code>def greet(name, age): ...</code>?</p>', [
        ('<code>greet("Alice", 25)</code>', False),
        ('<code>greet(age=25, "Alice")</code>', True),
        ('<code>greet(age=25, name="Alice")</code>', False),
        ('<code>greet("Alice", age=25)</code>', False),
    ], '<p>Positional arguments must come before keyword arguments. Once a keyword argument is used, every following argument must also be a keyword argument.</p>'),
    ('multiple_choice', '<p>What is printed?</p><pre><code class="language-python">x = "global"\ndef func():\n    x = "local"\n    print(x)\nfunc()</code></pre>', [
        ('<code>local</code>', True),
        ('<code>global</code>', False),
        ('<code>globallocal</code>', False),
        ('<code>NameError</code>', False),
    ], '<p>Assignment inside a function creates a new local name that shadows the global. The local value is printed; the global is unchanged.</p>'),
    ('multiple_choice', '<p>Which statement correctly describes lambda functions?</p>', [
        ('They can contain multiple statements', False),
        ('They must be assigned to a variable to be used', False),
        ('They cannot accept parameters', False),
        ('They are anonymous, single-expression functions', True),
    ], '<p>A <code>lambda</code> defines an anonymous function consisting of a single expression whose value is returned automatically.</p>'),
    ('multiple_choice', '<p>What is the most important property of a base case in recursion?</p>', [
        ('It must decrement a counter', False),
        ('It must return a list', False),
        ('It stops the recursion from continuing indefinitely', True),
        ('It must call the function recursively', False),
    ], '<p>The base case terminates recursion. Without one, the function recurses forever and raises <code>RecursionError</code>.</p>'),
]
