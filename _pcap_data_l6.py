LESSON_HTML = """<h2>What you will learn</h2>
<ul>
<li>Create and manipulate lists, tuples, dictionaries, and sets</li>
<li>Understand the differences between mutable and immutable collections</li>
<li>Use indexing, slicing, and unpacking to access collection elements</li>
<li>Apply methods and comprehensions to transform data efficiently</li>
<li>Recognize when to use each collection type for different tasks</li>
<li>Understand copy vs. reference semantics and avoid common pitfalls</li>
</ul>

<h3>Lists: Ordered, Mutable Collections</h3>
<p>Lists are Python's most versatile collection type. They are ordered (items have a position), mutable (you can change them after creation), and can hold any type of data mixed together.</p>
<pre><code class="language-python">
fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # apple
print(fruits[-1])     # cherry (last item)
print(fruits[1:3])    # ['banana', 'cherry'] (slice)
print(fruits[::-1])   # ['cherry', 'banana', 'apple'] (reversed)
</code></pre>
<p>Common list methods modify the list in place: <code>append()</code> adds to the end, <code>pop()</code> removes and returns the last item, <code>insert()</code> adds at a position, <code>sort()</code> arranges in order, and <code>reverse()</code> flips the sequence.</p>
<pre><code class="language-python">
numbers = [3, 1, 4, 1, 5]
numbers.append(9)       # [3, 1, 4, 1, 5, 9]
numbers.pop()           # back to [3, 1, 4, 1, 5]
numbers.insert(0, 99)   # [99, 3, 1, 4, 1, 5]
numbers.sort()          # [1, 1, 3, 4, 5, 99]
numbers.reverse()       # [99, 5, 4, 3, 1, 1]
</code></pre>
<p><strong>List comprehensions</strong> provide a concise way to create new lists by transforming or filtering existing ones:</p>
<pre><code class="language-python">
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
</code></pre>

<h3>Tuples: Immutable Collections</h3>
<p>Tuples are like lists, but they're <em>immutable</em>&mdash;once created, you cannot change their content. Immutability makes them safer for protecting data and lets tuples serve as dictionary keys (lists cannot).</p>
<pre><code class="language-python">
coordinates = (10, 20)
person = ("Alice", 30, "Engineer")

print(coordinates[0])  # 10
print(person[1])       # 30

# Tuple unpacking
name, age, job = person
print(f"{name} is {age} and works as a {job}")

# Tuples are immutable - this raises TypeError:
# coordinates[0] = 15
</code></pre>

<h3>Dictionaries: Key-Value Pairs</h3>
<p>Dictionaries store data as key-value pairs and enable fast lookups by key. They're mutable and (in Python 3.7+) maintain insertion order. Keys must be immutable types like strings, numbers, or tuples.</p>
<pre><code class="language-python">
student = {"name": "Bob", "age": 22, "grade": "A"}
print(student["name"])              # Bob

# .get() returns None (or a default) if the key is missing
print(student.get("age"))           # 22
print(student.get("email", "N/A"))  # N/A

for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(4)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9}
</code></pre>

<h3>Sets: Unique Elements and Set Operations</h3>
<p>Sets are unordered collections of unique elements. They're ideal for removing duplicates and performing mathematical operations like union, intersection, and difference.</p>
<pre><code class="language-python">
colors = {"red", "blue", "green"}
numbers_with_duplicates = {1, 2, 2, 3, 3, 3}
print(numbers_with_duplicates)  # {1, 2, 3}

a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)  # Union:        {1, 2, 3, 4}
print(a & b)  # Intersection: {2, 3}
print(a - b)  # Difference:   {1}
print(a ^ b)  # Symmetric:    {1, 4}
</code></pre>

<h3>Mutability, References, and Copying</h3>
<p><em>Mutable</em> objects (lists, dictionaries, sets) can be modified after creation, while <em>immutable</em> objects (tuples, strings, numbers) cannot. When you assign a mutable collection to another variable, you create a <em>reference</em>, not a copy.</p>
<pre><code class="language-python">
original = [1, 2, 3]
reference = original
reference.append(4)
print(original)  # [1, 2, 3, 4] - both changed!

true_copy = list(original)
true_copy.append(5)
print(original)  # [1, 2, 3, 4] - unchanged

import copy
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0].append(99)
print(nested)    # inner list still shared

deep = copy.deepcopy(nested)
deep[0].append(100)
print(nested)    # unchanged
</code></pre>

<h3>Choosing the Right Collection</h3>
<table>
<tr><th>Collection</th><th>Ordered</th><th>Mutable</th><th>Unique</th><th>Best For</th></tr>
<tr><td>List</td><td>Yes</td><td>Yes</td><td>No</td><td>Ordered sequences you'll modify</td></tr>
<tr><td>Tuple</td><td>Yes</td><td>No</td><td>No</td><td>Protecting data; dict keys</td></tr>
<tr><td>Dictionary</td><td>Yes*</td><td>Yes</td><td>Keys</td><td>Fast key-based lookup</td></tr>
<tr><td>Set</td><td>No</td><td>Yes</td><td>Yes</td><td>Uniqueness; set math</td></tr>
</table>

<h3>Wrap-up</h3>
<p>You now understand Python's four fundamental collection types and when to use each one. Lists provide flexibility for sequences you'll modify; tuples protect data with immutability; dictionaries enable efficient key-based lookup; sets guarantee uniqueness and support powerful set logic. Always remember the distinction between mutability and immutability, and be aware of how references work.</p>
"""

QUESTIONS = [
    ('multiple_choice', '<p>What is the result of <code>lst[1:4]</code> when <code>lst = [10, 20, 30, 40, 50]</code>?</p>', [
        ('<code>[20, 30, 40]</code>', True),
        ('<code>[20, 30, 40, 50]</code>', False),
        ('<code>[10, 20, 30, 40]</code>', False),
        ('<code>[30, 40]</code>', False),
    ], '<p>Slicing uses <code>lst[start:end]</code> with the end index <em>exclusive</em>. Indices 1, 2, 3 are included.</p>'),
    ('multiple_choice', '<p>What is the difference between <code>lst.append([4, 5])</code> and <code>lst.extend([4, 5])</code> on <code>lst = [1, 2, 3]</code>?</p>', [
        ('<code>append()</code> adds the list as a single element; <code>extend()</code> adds each element individually', True),
        ('<code>extend()</code> adds the list as one element; <code>append()</code> unpacks it', False),
        ('Both methods add elements individually', False),
        ('<code>append()</code> returns a new list; <code>extend()</code> modifies in place', False),
    ], '<p><code>append()</code> treats its argument as a single object. <code>extend()</code> iterates and adds each element separately.</p>'),
    ('multiple_choice', '<p>What is the key difference between <code>lst.sort()</code> and <code>sorted(lst)</code>?</p>', [
        ('<code>sort()</code> sorts in place and returns <code>None</code>; <code>sorted()</code> returns a new sorted list', True),
        ('<code>sorted()</code> modifies the original list; <code>sort()</code> returns a new list', False),
        ('Both modify the original list and return the sorted result', False),
        ('<code>sort()</code> is a built-in function; <code>sorted()</code> is a list method', False),
    ], '<p><code>sort()</code> is a list method that mutates in place and returns nothing. <code>sorted()</code> is a built-in that returns a new list.</p>'),
    ('multiple_choice', '<p>What happens when you execute <code>tpl[0] = 99</code> on <code>tpl = (1, 2, 3)</code>?</p>', [
        ('A <code>TypeError</code> is raised', True),
        ('<code>tpl</code> becomes <code>(99, 2, 3)</code>', False),
        ('The assignment is silently ignored', False),
        ('A <code>ValueError</code> is raised', False),
    ], '<p>Tuples are immutable. Any attempt to set an element raises <code>TypeError</code>.</p>'),
    ('multiple_choice', '<p>When a key is missing, what is the difference between <code>d["missing"]</code> and <code>d.get("missing")</code>?</p>', [
        ('<code>d["missing"]</code> raises <code>KeyError</code>; <code>get()</code> returns <code>None</code>', True),
        ('Both raise <code>KeyError</code>', False),
        ('Both return <code>None</code>', False),
        ('<code>get()</code> raises an error; bracket notation returns <code>None</code>', False),
    ], '<p>Bracket access raises <code>KeyError</code> on missing keys. <code>get()</code> returns <code>None</code> by default, or a value you supply.</p>'),
    ('multiple_choice', '<p>What does this comprehension create?</p><pre><code class="language-python">d = {x: x**2 for x in range(3)}</code></pre>', [
        ('<code>{0: 0, 1: 1, 2: 4}</code>', True),
        ('<code>[0, 1, 4]</code>', False),
        ('<code>{0, 1, 4}</code>', False),
        ('<code>(0, 1, 2)</code>', False),
    ], '<p>A dict comprehension maps keys to values. Each element from <code>range(3)</code> becomes a key mapped to its square.</p>'),
    ('multiple_choice', '<p>Given <code>s1 = {1, 2, 3, 4}</code> and <code>s2 = {3, 4, 5, 6}</code>, what does <code>s1 &amp; s2</code> return?</p>', [
        ('<code>{3, 4}</code>', True),
        ('<code>{1, 2, 3, 4, 5, 6}</code>', False),
        ('<code>{5, 6}</code>', False),
        ('<code>{1, 2, 5, 6}</code>', False),
    ], '<p>The <code>&amp;</code> operator returns the intersection &mdash; elements present in both sets.</p>'),
    ('multiple_choice', '<p>After <code>copy_list = copy.copy(original)</code> where <code>original = [[1, 2], [3, 4]]</code>, what is true of the nested lists?</p>', [
        ('The nested lists are still shared between <code>original</code> and <code>copy_list</code>', True),
        ('The nested lists are independent copies', False),
        ('A <code>TypeError</code> is raised', False),
        ('The copy has no nested lists', False),
    ], '<p>A shallow copy duplicates only the top-level container. Inner mutable objects are still referenced from the original. Use <code>copy.deepcopy()</code> to clone recursively.</p>'),
]
