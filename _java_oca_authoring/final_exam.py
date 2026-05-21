QUESTIONS = [('<p>Which of the following is a valid signature for the main method in a Java application?</p>',
  [('<code>public void main(String[] args)</code>', False),
   ('<code>public static void main(String[] args)</code>', True),
   ('<code>protected static void main(String args)</code>', False),
   ('<code>public final void main(String... args)</code>', False)],
  'The JVM looks for a <code>public static void main(String[] args)</code> signature to start execution. A non-static '
  "main method will compile but won't be recognized as an entry point; protected won't work as the JVM is outside the "
  'package.'),
 ('<p>A Java source file named <code>Example.java</code> contains two public classes. What happens during '
  'compilation?</p>',
  [('The compilation succeeds and creates one .class file.', False),
   ('The compilation fails with an error.', True),
   ('The compilation creates two .class files in the same directory.', False),
   ('The compiler creates one .class file for each public class.', False)],
  'Only one public class is allowed per source file. If <code>Example.java</code> has two public classes, the compiler '
  'will fail immediately. You can have multiple non-public (package-private) classes in one file.'),
 ("<p>What is the output of the following code?</p><pre><code class='language-java'>byte b = 100;\n"
  'int i = 200;\n'
  'long result = b + i;\n'
  'System.out.println(result);</code></pre>',
  [('<code>100</code>', False),
   ('<code>300</code>', True),
   ('Compilation error: incompatible types', False),
   ('<code>200</code>', False)],
  'When adding a byte and int, both are promoted to int (300). Assigning an int to long succeeds automatically via '
  'widening conversion. The output is <code>300</code>.'),
 ('<p>Which statement about wrapper classes is correct?</p>',
  [('Wrapper classes like Integer can be used in arithmetic operations without unboxing.', False),
   ('<code>new Integer(10) == new Integer(10)</code> returns true.', False),
   ('Autoboxing automatically converts primitives to their wrapper class equivalents.', True),
   ('Wrapper classes inherit from Number but are considered primitive types.', False)],
  'Autoboxing (since Java 5) automatically wraps primitives into their wrapper objects. Two separately instantiated '
  'Integer objects are not equal with <code>==</code> (reference comparison); you must use <code>.equals()</code>. '
  'Wrapper objects cannot participate in arithmetic directly.'),
 ("<p>What is the type of variable <code>x</code> after this declaration?</p><pre><code class='language-java'>var x = "
  '42;</code></pre>',
  [('<code>Object</code>', False),
   ('<code>int</code>', True),
   ('<code>Integer</code>', False),
   ('The type cannot be determined until runtime.', False)],
  'Local variable type inference (var keyword, Java 10+) infers the type from the right-hand side. Since '
  '<code>42</code> is an int literal, <code>x</code> is inferred as <code>int</code>. The type is determined at '
  'compile time, not runtime.'),
 ("<p>What is the output?</p><pre><code class='language-java'>int a = 5, b = 10;\n"
  'boolean result = (a &gt; 10) || (b++ &gt; 5);\n'
  'System.out.println(a + &quot; &quot; + b + &quot; &quot; + result);</code></pre>',
  [('<code>5 10 true</code>', False),
   ('<code>5 11 true</code>', True),
   ('<code>5 10 false</code>', False),
   ('<code>5 11 false</code>', False)],
  'Since <code>(a &gt; 10)</code> is false, the OR operator does NOT short-circuit; it evaluates <code>(b++ &gt; '
  '5)</code> which is true and increments <code>b</code> to 11. Result is true. Post-increment happens after the '
  'comparison.'),
 ("<p>What does this code print?</p><pre><code class='language-java'>int score = 75;\n"
  'String grade = (score &gt;= 90) ? "A" : (score &gt;= 80) ? "B" : (score &gt;= 70) ? "C" : "F";\n'
  'System.out.println(grade);</code></pre>',
  [('<code>A</code>', False), ('<code>B</code>', False), ('<code>C</code>', True), ('<code>F</code>', False)],
  'The nested ternary operator evaluates left-to-right. Score 75 fails the first two conditions (90 and 80) but meets '
  "(70), so grade is 'C'."),
 ("<p>What is the output?</p><pre><code class='language-java'>int day = 3;\n"
  'switch(day) {\n'
  '  case 1: System.out.print("Mon");\n'
  '  case 2: System.out.print("Tue");\n'
  '  case 3: System.out.print("Wed");\n'
  '  default: System.out.print("Other");\n'
  '}</code></pre>',
  [('<code>Wed</code>', False),
   ('<code>WedOther</code>', True),
   ('<code>Mon Tue Wed Other</code>', False),
   ('Compilation error', False)],
  "Case 3 matches, but there's no <code>break</code> statement, so execution falls through to the default block. "
  'Output is <code>WedOther</code>. This is a common gotcha in OCA exams.'),
 ("<p>What is the output?</p><pre><code class='language-java'>int[] nums = {10, 20, 30};\n"
  'int[] copy = nums;\n'
  'copy[0] = 99;\n'
  'System.out.println(nums[0]);</code></pre>',
  [('<code>10</code>', False), ('<code>99</code>', True), ('<code>null</code>', False), ('Compilation error', False)],
  'Arrays are objects; <code>copy = nums</code> creates a reference to the same array, not a copy. Modifying '
  '<code>copy[0]</code> also modifies <code>nums[0]</code>. Output is <code>99</code>.'),
 ('<p>Which declaration is valid?</p>',
  [('<code>int[5] array;</code>', False),
   ('<code>int array[5];</code>', False),
   ('<code>int[][] matrix = new int[3][3];</code>', True),
   ('<code>String[] names = new String[10]{"Alice", "Bob"};</code>', False)],
  'Array size is specified at instantiation, not declaration. <code>int[] array</code> is the correct form, and '
  'multi-dimensional arrays use <code>new int[rows][cols]</code>. Anonymous array initialization cannot have a size '
  'specifier.'),
 ("<p>What is the output?</p><pre><code class='language-java'>int[][] grid = {{1, 2, 3}, {4, 5, 6}};\n"
  'System.out.println(grid[1][2]);</code></pre>',
  [('<code>2</code>', False), ('<code>3</code>', False), ('<code>5</code>', False), ('<code>6</code>', True)],
  '<code>grid[1][2]</code> accesses row index 1 (second row: {4, 5, 6}), column index 2 (third element: 6). Arrays are '
  '0-indexed.'),
 ("<p>What is the output?</p><pre><code class='language-java'>int[] nums = {1, 2, 3, 4, 5};\n"
  'for(int num : nums) {\n'
  '  if(num == 3) continue;\n'
  '  if(num == 4) break;\n'
  '  System.out.print(num + " ");\n'
  '}</code></pre>',
  [('<code>1 2 3 4 5</code>', False),
   ('<code>1 2</code>', True),
   ('<code>1 2 3 4</code>', False),
   ('<code>1 2 5</code>', False)],
  '<code>continue</code> skips 3, printing 1 and 2. When num equals 4, <code>break</code> exits the loop entirely. '
  'Output is <code>1 2</code>.'),
 ("<p>What is the output?</p><pre><code class='language-java'>int i = 0;\n"
  'do {\n'
  '  System.out.print(i++ + " ");\n'
  '} while(i &lt; 3);</code></pre>',
  [('<code>0 1 2</code>', True), ('<code>0 1 2 3</code>', False), ('<code>1 2 3</code>', False), ('No output', False)],
  'A do-while loop executes at least once. <code>i++</code> prints 0, 1, 2 (post-increment), and then the while '
  'condition <code>i &lt; 3</code> becomes false when i reaches 3. Output is <code>0 1 2</code>.'),
 ('<p>Which method would overload <code>public void process(int x)</code>?</p>',
  [('<code>private void process(int x)</code>', False),
   ('<code>public void process(int y)</code>', False),
   ('<code>public void process(double x)</code>', True),
   ('<code>public int process(int x)</code>', False)],
  'Method overloading requires different parameter types or number of parameters. Changing the return type alone or '
  "parameter names doesn't create an overload. <code>public void process(double x)</code> differs by parameter type."),
 ("<p>What is the output?</p><pre><code class='language-java'>class Dog {\n"
  '  public static void bark() { System.out.print("Woof "); }\n'
  '}\n'
  'public class Main {\n'
  '  public static void main(String[] args) {\n'
  '    Dog dog = null;\n'
  '    dog.bark();\n'
  '  }\n'
  '}</code></pre>',
  [('<code>Woof</code>', True), ('NullPointerException', False), ('Compilation error', False), ('No output', False)],
  'Static methods belong to the class, not the instance. Even though <code>dog</code> is null, <code>dog.bark()</code> '
  'is resolved at compile time to <code>Dog.bark()</code>, so output is <code>Woof</code>. This is considered bad '
  'practice but is valid Java.'),
 ("<p>What is the output?</p><pre><code class='language-java'>class Animal {\n"
  '  public Animal() { System.out.print("A "); }\n'
  '}\n'
  'class Dog extends Animal {\n'
  '  public Dog() { super(); System.out.print("D "); }\n'
  '}\n'
  'new Dog();</code></pre>',
  [('<code>A</code>', False), ('<code>D</code>', False), ('<code>A D</code>', True), ('<code>D A</code>', False)],
  'The Dog constructor calls <code>super()</code> explicitly, which invokes the Animal constructor first, printing '
  "'A'. Then Dog's constructor completes, printing 'D'. Output is <code>A D</code>."),
 ("<p>What is the output?</p><pre><code class='language-java'>class Animal {\n"
  '  public void speak() { System.out.print("Sound"); }\n'
  '}\n'
  'class Cat extends Animal {\n'
  '  public void speak() { System.out.print("Meow"); }\n'
  '}\n'
  'Animal animal = new Cat();\n'
  'animal.speak();</code></pre>',
  [('<code>Sound</code>', False),
   ('<code>Meow</code>', True),
   ('Compilation error', False),
   ('<code>SoundMeow</code>', False)],
  'This demonstrates polymorphism. Although the reference is of type Animal, the actual object is Cat. The overridden '
  '<code>speak()</code> method in Cat is called at runtime, printing <code>Meow</code>.'),
 ('<p>Which access modifier is the standard choice for members that subclasses should access from their '
  'superclass?</p>',
  [('<code>private</code>', False),
   ('package-private (default)', False),
   ('<code>protected</code>', True),
   ('<code>public</code>', False)],
  'The <code>protected</code> modifier is designed for inheritance; it restricts access to the package and subclasses, '
  'allowing controlled access in inheritance hierarchies. <code>public</code> provides unrestricted access, which is '
  'less appropriate for base class members.'),
 ("<p>What is the output?</p><pre><code class='language-java'>class Shape {\n"
  '  public double getArea() { return 0; }\n'
  '}\n'
  'class Circle extends Shape {\n'
  '  private double radius = 5;\n'
  '  public double getArea() { return Math.PI * radius * radius; }\n'
  '}\n'
  'Shape shape = new Circle();\n'
  'System.out.println((int)shape.getArea());</code></pre>',
  [('<code>0</code>', False), ('<code>78</code>', True), ('<code>25</code>', False), ('Compilation error', False)],
  "Method overriding: Circle's <code>getArea()</code> calculates π &times; 5² ≈ 78.54, which casts to (int) 78. The "
  'runtime type is Circle, not Shape, so the overridden version is called (polymorphism).'),
 ("<p>What is the output?</p><pre><code class='language-java'>try {\n"
  '  System.out.print("A");\n'
  '  throw new Exception();\n'
  '  System.out.print("B");\n'
  '} catch(Exception e) {\n'
  '  System.out.print("C");\n'
  '} finally {\n'
  '  System.out.print("D");\n'
  '}</code></pre>',
  [('<code>ABCD</code>', False),
   ('<code>ACD</code>', True),
   ('<code>AD</code>', False),
   ('<code>ACD</code> then Exception is re-thrown', False)],
  "'A' prints, then an exception is thrown, skipping 'B'. The catch block prints 'C', and finally always executes, "
  "printing 'D'. Output is <code>ACD</code>."),
 ('<p>What is true about checked and unchecked exceptions?</p>',
  [('All exceptions are checked at compile time.', False),
   ('Unchecked exceptions include NullPointerException and ArrayIndexOutOfBoundsException.', True),
   ('A method must declare all exceptions it might throw.', False),
   ('Unchecked exceptions must be caught or declared in the method signature.', False)],
  'Checked exceptions (IOException, SQLException) must be caught or declared. Unchecked exceptions (RuntimeException '
  'subclasses like NullPointerException) are optional to handle. NullPointerException is unchecked.'),
 ("<p>What is the output?</p><pre><code class='language-java'>try {\n"
  '  System.out.print("1");\n'
  '} catch(IOException e) {\n'
  '  System.out.print("2");\n'
  '} catch(Exception e) {\n'
  '  System.out.print("3");\n'
  '} finally {\n'
  '  System.out.print("4");\n'
  '}</code></pre>',
  [('<code>1234</code>', False), ('<code>14</code>', True), ('<code>124</code>', False), ('Compilation error', False)],
  'No exception is thrown, so catch blocks are skipped entirely. Finally always executes. Output is <code>14</code>.'),
 ('<p>What is the output?</p><pre><code class=\'language-java\'>String str = "Hello";\n'
  "str = str.replace('l', 'x');\n"
  'System.out.println(str);</code></pre>',
  [('<code>Hexlo</code>', False),
   ('<code>Hexxo</code>', True),
   ('<code>Hello</code>', False),
   ('Compilation error', False)],
  "Strings are immutable, so <code>replace('l', 'x')</code> returns a new String with both 'l' characters replaced: "
  "'Hexxo'. The result is assigned back to <code>str</code>."),
 ('<p>What is the output?</p><pre><code class=\'language-java\'>StringBuilder sb = new StringBuilder("Java");\n'
  'sb.insert(2, "x").append("!");\n'
  'System.out.println(sb);</code></pre>',
  [('<code>Java!</code>', False),
   ('<code>Jaxa!</code>', True),
   ('<code>xJava!</code>', False),
   ('<code>Jaxva!</code>', False)],
  '<code>insert(2, "x")</code> inserts \'x\' at index 2 (between \'a\' and \'v\'), producing "Jaxa". '
  '<code>append("!")</code> adds \'!\' at the end. Output is <code>Jaxa!</code>.'),
 ("<p>What is the output?</p><pre><code class='language-java'>ArrayList&lt;Integer&gt; list = new "
  'ArrayList&lt;&gt;();\n'
  'list.add(10);\n'
  'list.add(20);\n'
  'list.add(1, 15);\n'
  'for(int num : list) System.out.print(num + " ");</code></pre>',
  [('<code>10 20</code>', False),
   ('<code>10 15 20</code>', True),
   ('<code>10 20 15</code>', False),
   ('<code>15 10 20</code>', False)],
  '<code>add(1, 15)</code> inserts 15 at index 1 (between 10 and 20), shifting 20 to index 2. The list is [10, 15, '
  '20]. Output is <code>10 15 20</code>.')]