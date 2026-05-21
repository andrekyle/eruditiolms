LESSON_HTML = """
<h2>Creating and Using Arrays</h2>

<h3>Array Basics</h3>
<p>An array is an object that holds a fixed-size collection of elements of the same type. Arrays are <strong>ordered</strong> and <strong>index-based</strong>, with indices starting at 0.</p>

<h3>Declaring Arrays</h3>
<p>Arrays can be declared in two equivalent styles:</p>
<ul>
<li><code>int[] numbers;</code> — preferred style</li>
<li><code>int numbers[];</code> — legacy C-style (valid but not preferred)</li>
</ul>
<p>Declaration reserves a variable that will reference an array, but does <strong>not</strong> create the array object itself.</p>

<h3>Instantiating Arrays</h3>
<p>To create an array object, use the <code>new</code> keyword:</p>
<pre><code class="language-java">int[] scores = new int[5];      // Array of 5 integers
String[] names = new String[3]; // Array of 3 String references
double[] prices = new double[10]; // Array of 10 doubles</code></pre>
<p>The number in brackets specifies the <strong>fixed size</strong> of the array. Once created, the size cannot change.</p>

<h3>Initializing Arrays</h3>
<p>When an array is created, its elements receive default values:</p>
<ul>
<li>Numeric types: <code>0</code> (or <code>0.0</code> for floating-point)</li>
<li><code>boolean</code>: <code>false</code></li>
<li>Reference types (String, custom objects): <code>null</code></li>
</ul>
<p>You can initialize elements during declaration using an <strong>array initializer</strong> (anonymous array):</p>
<pre><code class="language-java">int[] values = {1, 2, 3, 4, 5};           // Array literal
String[] colors = {"red", "green", "blue"}; // 3-element array
int[] mixed = new int[]{10, 20, 30};       // Anonymous array</code></pre>

<h3>Accessing Array Elements</h3>
<p>Arrays are accessed by index, using square brackets:</p>
<pre><code class="language-java">int[] arr = {10, 20, 30, 40, 50};
int first = arr[0];     // 10
int third = arr[2];     // 30
arr[1] = 99;            // Modify second element to 99</code></pre>

<h3>Array Length</h3>
<p>The <code>length</code> field gives the fixed size of an array (it is a <strong>field</strong>, not a method):</p>
<pre><code class="language-java">int[] arr = new int[7];
System.out.println(arr.length); // 7

String[] names = {"Alice", "Bob"};
System.out.println(names.length); // 2</code></pre>

<h3>Array Exceptions</h3>
<p><strong>ArrayIndexOutOfBoundsException</strong> occurs when accessing an index that does not exist:</p>
<pre><code class="language-java">int[] arr = new int[5];    // Valid indices: 0, 1, 2, 3, 4
int x = arr[5];            // Throws ArrayIndexOutOfBoundsException
int y = arr[-1];           // Throws ArrayIndexOutOfBoundsException</code></pre>
<p><strong>NullPointerException</strong> occurs when attempting to use a null array reference:</p>
<pre><code class="language-java">int[] arr = null;
int x = arr[0];            // Throws NullPointerException</code></pre>

<h3>Multidimensional Arrays</h3>
<p>Arrays can have multiple dimensions. A 2D array is useful for matrices, grids, and tables:</p>
<pre><code class="language-java">int[][] grid = new int[3][4];  // 3 rows, 4 columns
int[][] matrix = {{1, 2}, {3, 4}, {5, 6}}; // 3x2 matrix
grid[0][0] = 99;               // Access row 0, column 0
grid[2][3] = 50;               // Access row 2, column 3</code></pre>

<h3>Jagged Arrays</h3>
<p>In Java, multidimensional arrays need not be rectangular. A <strong>jagged array</strong> is an array of arrays where each row can have a different length:</p>
<pre><code class="language-java">int[][] jagged = new int[3][];   // 3 rows, unknown column counts
jagged[0] = new int[2];           // Row 0 has 2 elements
jagged[1] = new int[4];           // Row 1 has 4 elements
jagged[2] = new int[1];           // Row 2 has 1 element</code></pre>

<h3>Arrays Are Objects</h3>
<p>Arrays are <strong>reference types</strong>. Assignment copies the reference, not the contents:</p>
<pre><code class="language-java">int[] a = {1, 2, 3};
int[] b = a;           // b points to the same array as a
b[0] = 99;             // Modifies both a and b
System.out.println(a[0]); // 99

// Use equals() for content comparison (default == is reference equality)
int[] x = {1, 2, 3};
int[] y = {1, 2, 3};
System.out.println(x == y);              // false (different objects)
System.out.println(java.util.Arrays.equals(x, y)); // true (same content)</code></pre>

<h3>Iterating Over Arrays</h3>
<p><strong>Classical for loop:</strong></p>
<pre><code class="language-java">int[] scores = {85, 90, 78, 92};
for (int i = 0; i &amp;lt; scores.length; i++) {
    System.out.println(scores[i]);
}</code></pre>
<p><strong>Enhanced for-each loop:</strong></p>
<pre><code class="language-java">int[] scores = {85, 90, 78, 92};
for (int score : scores) {  // Read-only iteration
    System.out.println(score);
}

String[][] grid = {{"A", "B"}, {"C", "D"}};
for (String[] row : grid) {
    for (String cell : row) {
        System.out.println(cell);
    }
}</code></pre>

<h3>Arrays Utility Class</h3>
<p>The <code>java.util.Arrays</code> class provides helpful static methods:</p>
<ul>
<li><code>Arrays.toString(array)</code> — returns a string representation of the array contents</li>
<li><code>Arrays.sort(array)</code> — sorts the array in ascending order</li>
<li><code>Arrays.binarySearch(array, key)</code> — searches for a key in a sorted array</li>
<li><code>Arrays.copyOf(array, length)</code> — creates a copy of the array with a specified length</li>
<li><code>Arrays.equals(array1, array2)</code> — compares array contents for equality</li>
</ul>

<h3>ArrayList</h3>
<p><code>java.util.ArrayList</code> is a resizable array alternative. While arrays have a fixed size, ArrayLists grow and shrink dynamically:</p>
<pre><code class="language-java">java.util.ArrayList&amp;lt;Integer&amp;gt; list = new java.util.ArrayList&amp;lt;&amp;gt;();
list.add(10);      // Add element
list.add(20);
list.add(30);
System.out.println(list.size());  // 3
System.out.println(list.get(1));  // 20 (access by index)
list.set(1, 99);   // Modify element
list.remove(0);    // Remove by index
boolean contains = list.contains(20); // true
boolean empty = list.isEmpty();   // false</code></pre>
"""

QUESTIONS = [
    (
        "Which of the following correctly declares and instantiates an integer array with 5 elements?",
        [
            ("int[] arr = {5};", False),
            ("int[] arr = new int[5];", True),
            ("int arr[] = 5;", False),
            ("int arr = new int[5];", False),
        ],
        "To create an array of fixed size, use the syntax <code>int[] arr = new int[size];</code>. The value in brackets specifies the number of elements, not the initial value. Option with the empty braces <code>{5}</code> creates a single-element array, not a 5-element array."
    ),
    (
        "What are the default values in a newly created integer array?",
        [
            ("1 for each element", False),
            ("null for each element", False),
            ("0 for each element", True),
            ("false for each element", False),
        ],
        "In Java, numeric primitive types default to 0 (or 0.0 for floating-point). The default values 0, 0.0, false, and null apply only to their respective types—null is for reference types like String or objects, not int."
    ),
    (
        "Consider this code:<pre><code class=\"language-java\">int[] arr = {10, 20, 30, 40};\nint value = arr[arr.length - 1];</code></pre>What is the value of <code>value</code>?",
        [
            ("30", False),
            ("40", True),
            ("5", False),
            ("ArrayIndexOutOfBoundsException is thrown", False),
        ],
        "The array has 4 elements (indices 0–3). <code>arr.length</code> is 4, so <code>arr.length - 1</code> is 3, which is the last valid index. <code>arr[3]</code> holds 40."
    ),
    (
        "Which statement correctly accesses the number of elements in an array?",
        [
            ("int size = arr.length();", False),
            ("int size = arr.length;", True),
            ("int size = arr.size();", False),
            ("int size = arr.getLength();", False),
        ],
        "<code>length</code> is a field (not a method) on array objects. Use <code>arr.length</code> without parentheses. The method <code>size()</code> belongs to ArrayList, not arrays."
    ),
    (
        "What exception is thrown by this code?<pre><code class=\"language-java\">int[] arr = new int[3];\nint x = arr[3];</code></pre>",
        [
            ("NullPointerException", False),
            ("ArrayIndexOutOfBoundsException", True),
            ("IndexOutOfRangeException", False),
            ("No exception; x is 0", False),
        ],
        "An array with size 3 has valid indices 0, 1, and 2. Accessing index 3 is out of bounds and throws ArrayIndexOutOfBoundsException. NullPointerException would occur if the array reference itself were null."
    ),
    (
        "What is the output of this code?<pre><code class=\"language-java\">int[][] grid = {{1, 2, 3}, {4, 5, 6}};\nSystem.out.println(grid[1][0]);</code></pre>",
        [
            ("1", False),
            ("4", True),
            ("6", False),
            ("ArrayIndexOutOfBoundsException", False),
        ],
        "The 2D array has 2 rows (indices 0 and 1) and 3 columns (indices 0, 1, and 2). <code>grid[1][0]</code> accesses row 1, column 0, which contains 4."
    ),
    (
        "Which statement correctly compares the contents of two arrays for equality?",
        [
            ("if (arr1 == arr2) { }", False),
            ("if (java.util.Arrays.equals(arr1, arr2)) { }", True),
            ("if (arr1.equals(arr2)) { }", False),
            ("if (arr1.compareTo(arr2) == 0) { }", False),
        ],
        "The <code>==</code> operator on arrays compares object references, not contents. Use <code>java.util.Arrays.equals()</code> to compare the actual elements. Arrays do not override <code>equals()</code>."
    ),
    (
        "What is the primary advantage of using ArrayList over an array?",
        [
            ("ArrayList is faster than arrays", False),
            ("ArrayList can change its size dynamically, while arrays are fixed-size", True),
            ("ArrayList does not require the import statement", False),
            ("ArrayList automatically sorts its elements", False),
        ],
        "Arrays have a fixed size determined at creation. ArrayList is a resizable collection that can grow or shrink as elements are added or removed, providing greater flexibility for unknown collection sizes."
    ),
]