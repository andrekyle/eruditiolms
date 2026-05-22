"""SAQA 118792 AI Software Developer (NQF 5).

Lesson 05 - KM-05 Computing Theory (NQF4, 8 cr).

Exports:
    LESSON_HTML      -- main lesson content (>=2000 chars)
    QUESTIONS        -- exactly 8 assessment tuples (>=6 MC, <=2 TF)
    PRACTICAL_HTML   -- practical lab (>=1400 chars)
"""

LESSON_HTML = (
    "<h2>Computing Theory for AI Developers</h2>"
    "<p>Modern AI systems do not run on magic. They run on the same digital "
    "circuits, memory hierarchies, operating systems and networks that power "
    "every other piece of software. This lesson gives you the computing-theory "
    "vocabulary that an AI developer needs in order to reason about "
    "<strong>performance</strong>, <strong>scalability</strong> and "
    "<strong>cost</strong> when training or serving models.</p>"

    "<h3>1. Number systems, bits and bytes</h3>"
    "<p>Computers store everything as binary digits (bits). Eight bits form a "
    "byte. Common bases are <em>binary</em> (base&nbsp;2), <em>decimal</em> "
    "(base&nbsp;10) and <em>hexadecimal</em> (base&nbsp;16). Hex is popular "
    "because one hex digit represents exactly four bits, so a byte is two hex "
    "digits.</p>"
    "<table><thead><tr><th>Decimal</th><th>Binary</th><th>Hex</th></tr></thead>"
    "<tbody>"
    "<tr><td>0</td><td>0000</td><td>0</td></tr>"
    "<tr><td>10</td><td>1010</td><td>A</td></tr>"
    "<tr><td>15</td><td>1111</td><td>F</td></tr>"
    "<tr><td>255</td><td>11111111</td><td>FF</td></tr>"
    "</tbody></table>"
    "<p>Signed integers use <strong>two's complement</strong>: to negate a "
    "value you invert every bit and add one. This keeps addition circuitry "
    "identical for signed and unsigned numbers and gives one unique zero.</p>"

    "<h3>2. Boolean logic</h3>"
    "<p>Boolean algebra (AND, OR, NOT, XOR, NAND) is the foundation of every "
    "digital circuit and of every <code>if</code> statement you write. AI "
    "models such as decision trees and binary classifiers also reduce to "
    "Boolean predicates at inference time.</p>"

    "<h3>3. Von Neumann architecture</h3>"
    "<p>Almost every general-purpose computer follows the <em>von Neumann</em> "
    "model: a single memory holds both data and instructions, and a CPU "
    "fetches, decodes and executes them in a cycle.</p>"
    "<ul>"
    "<li><strong>CPU</strong> contains the <strong>ALU</strong> (arithmetic "
    "and logic unit), control unit and a small set of fast <strong>registers"
    "</strong>.</li>"
    "<li><strong>Cache hierarchy</strong>: <strong>L1</strong> (smallest, "
    "fastest, ~1&nbsp;ns), <strong>L2</strong> (larger, ~3-10&nbsp;ns), "
    "<strong>L3</strong> (shared, ~20-40&nbsp;ns) sit between registers and "
    "<strong>RAM</strong> (~100&nbsp;ns).</li>"
    "<li><strong>Secondary storage</strong> (SSD, HDD, object storage) is "
    "orders of magnitude slower but persistent.</li>"
    "<li><strong>GPU</strong> contains thousands of small cores that perform "
    "the same operation on many data items in parallel "
    "(<em>SIMD/SIMT</em>). This is why deep-learning training, which is "
    "dominated by dense matrix multiplications, runs 10-100x faster on a GPU "
    "than on a CPU. TPUs and other accelerators push this further.</li>"
    "</ul>"

    "<h3>4. Operating system concepts</h3>"
    "<ul>"
    "<li>A <strong>process</strong> is an isolated program with its own "
    "memory; a <strong>thread</strong> is a lighter unit of execution that "
    "shares memory with sibling threads in the same process.</li>"
    "<li>The OS <strong>scheduler</strong> decides which thread runs on which "
    "core. Common policies include round-robin and priority-based scheduling."
    "</li>"
    "<li><strong>Virtual memory</strong> gives every process the illusion of "
    "a private address space; pages are mapped to physical RAM or swapped to "
    "disk on demand.</li>"
    "<li><strong>File systems</strong> (NTFS, ext4, APFS) organise persistent "
    "data into files and directories with permissions and metadata.</li>"
    "</ul>"

    "<h3>5. Algorithms and Big-O</h3>"
    "<p><strong>Big-O</strong> notation describes how the run-time or memory "
    "of an algorithm grows as input size <em>n</em> grows.</p>"
    "<table><thead><tr><th>Class</th><th>Example</th></tr></thead><tbody>"
    "<tr><td>O(1)</td><td>Hash-table lookup, array index</td></tr>"
    "<tr><td>O(log n)</td><td>Binary search on a sorted array</td></tr>"
    "<tr><td>O(n)</td><td>Sequential / linear search</td></tr>"
    "<tr><td>O(n log n)</td><td>Merge sort, quick sort (average)</td></tr>"
    "<tr><td>O(n&sup2;)</td><td>Bubble sort, naive nested loops</td></tr>"
    "<tr><td>O(2&#8319;)</td><td>Brute-force subset enumeration</td></tr>"
    "</tbody></table>"
    "<p>A small Python sketch comparing growth:</p>"
    "<pre><code>import time\n"
    "\n"
    "def linear_search(xs, target):\n"
    "    for i, x in enumerate(xs):\n"
    "        if x == target:\n"
    "            return i\n"
    "    return -1\n"
    "\n"
    "def binary_search(xs, target):\n"
    "    lo, hi = 0, len(xs) - 1\n"
    "    while lo &lt;= hi:\n"
    "        mid = (lo + hi) // 2\n"
    "        if xs[mid] == target:\n"
    "            return mid\n"
    "        if xs[mid] &lt; target:\n"
    "            lo = mid + 1\n"
    "        else:\n"
    "            hi = mid - 1\n"
    "    return -1\n"
    "\n"
    "n = 10_000_000\n"
    "data = list(range(n))\n"
    "target = n - 1\n"
    "\n"
    "t0 = time.perf_counter(); linear_search(data, target); t1 = time.perf_counter()\n"
    "t2 = time.perf_counter(); binary_search(data, target); t3 = time.perf_counter()\n"
    "print('linear', t1 - t0)\n"
    "print('binary', t3 - t2)\n"
    "</code></pre>"

    "<h3>6. Data structures</h3>"
    "<ul>"
    "<li><strong>Array</strong> - contiguous memory, O(1) index, O(n) insert "
    "in the middle. Used for tensors and feature vectors.</li>"
    "<li><strong>Linked list</strong> - O(1) insert at a known node, O(n) "
    "search. Good for queues of streaming events.</li>"
    "<li><strong>Stack</strong> (LIFO) - call stacks, undo history, depth-"
    "first search.</li>"
    "<li><strong>Queue</strong> (FIFO) - task queues, message brokers, "
    "breadth-first search.</li>"
    "<li><strong>Hash table</strong> - O(1) average lookup. Used everywhere: "
    "tokeniser vocabularies, feature stores, caches.</li>"
    "<li><strong>Tree</strong> - hierarchical data, decision trees, gradient-"
    "boosted trees, file systems.</li>"
    "<li><strong>Graph</strong> - social networks, knowledge graphs, the "
    "computation graphs that frameworks like PyTorch and TensorFlow build for "
    "back-propagation.</li>"
    "</ul>"

    "<h3>7. Networking basics</h3>"
    "<p>AI services almost always communicate over networks.</p>"
    "<table><thead><tr><th>OSI layer</th><th>TCP/IP layer</th><th>Examples"
    "</th></tr></thead><tbody>"
    "<tr><td>7 Application</td><td>Application</td><td>HTTP, HTTPS, DNS, "
    "gRPC</td></tr>"
    "<tr><td>4 Transport</td><td>Transport</td><td>TCP, UDP</td></tr>"
    "<tr><td>3 Network</td><td>Internet</td><td>IP (v4/v6), ICMP</td></tr>"
    "<tr><td>1-2 Physical / Data link</td><td>Network access</td><td>"
    "Ethernet, Wi-Fi</td></tr>"
    "</tbody></table>"
    "<p><strong>IP addressing</strong> identifies machines (e.g. 192.0.2.10 "
    "or 2001:db8::1). <strong>DNS</strong> maps human names like "
    "<code>api.openai.com</code> to IPs. <strong>HTTPS</strong> wraps HTTP in "
    "TLS for confidentiality and integrity. Most AI inference APIs follow a "
    "<em>client-server</em> model, while distributed training and "
    "federated-learning topologies are closer to <em>peer-to-peer</em>.</p>"

    "<h3>8. Cloud computing and virtualisation</h3>"
    "<ul>"
    "<li><strong>IaaS</strong> - raw VMs, networks and disks (Azure VM, AWS "
    "EC2).</li>"
    "<li><strong>PaaS</strong> - managed runtimes (Azure App Service, Google "
    "App Engine, Azure ML).</li>"
    "<li><strong>SaaS</strong> - finished applications you simply consume "
    "(Microsoft 365, ChatGPT).</li>"
    "</ul>"
    "<p><strong>Virtualisation</strong> lets one physical host run many "
    "isolated VMs. <strong>Containers</strong> (Docker, containerd) share "
    "the host kernel but isolate user space, so they start in milliseconds "
    "and package an AI model plus its Python dependencies into one "
    "reproducible artefact. AI workloads typically run in the cloud because "
    "they need bursty access to <em>GPUs</em>, <em>large datasets</em> in "
    "object storage and <em>elastic scaling</em> for inference traffic - all "
    "billed per second rather than per server.</p>"

    "<h3>9. Concurrency basics</h3>"
    "<p><strong>Concurrency</strong> is dealing with many things at once; "
    "<strong>parallelism</strong> is doing many things at once. Threads, "
    "<code>asyncio</code> tasks and multiprocessing all enable concurrency, "
    "but only multiprocessing and GPU kernels give true parallelism in "
    "CPython (because of the Global Interpreter Lock). Race conditions, "
    "deadlocks and starvation are the classic hazards; locks, queues and "
    "immutable messages are the classic mitigations. AI inference servers "
    "rely heavily on async I/O so that a single process can hold thousands "
    "of open HTTP connections while the GPU does the heavy lifting.</p>"

    "<blockquote><strong>Key takeaway:</strong> performance bottlenecks in "
    "AI systems almost always come down to one of three things - "
    "<em>algorithmic complexity</em>, the <em>memory hierarchy</em>, or the "
    "<em>network</em>. A good AI developer can diagnose which one is the "
    "culprit before reaching for more hardware.</blockquote>"
)


QUESTIONS = [
    (
        "mc",
        "<p>Which Big-O class best describes binary search on a sorted "
        "array of length <em>n</em>?</p>",
        [
            ("<p>O(1)</p>", False),
            ("<p>O(log n)</p>", True),
            ("<p>O(n)</p>", False),
            ("<p>O(n log n)</p>", False),
        ],
        "<p>Each comparison halves the remaining search range, giving "
        "logarithmic growth.</p>",
    ),
    (
        "mc",
        "<p>What is the hexadecimal representation of the decimal value "
        "<code>255</code>?</p>",
        [
            ("<p><code>0xEF</code></p>", False),
            ("<p><code>0xFE</code></p>", False),
            ("<p><code>0xFF</code></p>", True),
            ("<p><code>0x100</code></p>", False),
        ],
        "<p>255 = 11111111<sub>2</sub> = FF<sub>16</sub>, the largest value "
        "that fits in a single byte.</p>",
    ),
    (
        "mc",
        "<p>Which component of the memory hierarchy is typically the "
        "<strong>fastest</strong> but <strong>smallest</strong>?</p>",
        [
            ("<p>L3 cache</p>", False),
            ("<p>Main RAM</p>", False),
            ("<p>CPU registers</p>", True),
            ("<p>SSD storage</p>", False),
        ],
        "<p>Registers sit inside the CPU and are accessed in a single clock "
        "cycle, but there are only a handful of them.</p>",
    ),
    (
        "mc",
        "<p>Which statement best distinguishes a <strong>process</strong> "
        "from a <strong>thread</strong>?</p>",
        [
            ("<p>Processes share memory; threads do not.</p>", False),
            (
                "<p>Threads share the address space of their parent process; "
                "processes are isolated from each other.</p>",
                True,
            ),
            ("<p>Threads can only run on GPUs.</p>", False),
            ("<p>Processes are always faster to create than threads.</p>",
             False),
        ],
        "<p>Threads are lightweight units inside a process and share its "
        "memory; processes have separate address spaces.</p>",
    ),
    (
        "mc",
        "<p>Why are GPUs preferred over CPUs for training deep neural "
        "networks?</p>",
        [
            (
                "<p>They have thousands of cores that execute the same "
                "operation on many data items in parallel, which suits dense "
                "matrix multiplications.</p>",
                True,
            ),
            ("<p>They have larger L1 caches than any CPU.</p>", False),
            ("<p>They run Python bytecode natively.</p>", False),
            ("<p>They eliminate the need for RAM.</p>", False),
        ],
        "<p>GPU SIMT execution is a near-perfect match for the matrix "
        "algebra at the heart of neural-network training.</p>",
    ),
    (
        "mc",
        "<p>Which cloud service model gives the consumer the <em>least</em> "
        "responsibility for the underlying operating system?</p>",
        [
            ("<p>IaaS</p>", False),
            ("<p>PaaS</p>", False),
            ("<p>SaaS</p>", True),
            ("<p>On-premises</p>", False),
        ],
        "<p>With SaaS the provider manages everything; the consumer only "
        "uses the finished application.</p>",
    ),
    (
        "tf",
        "<p>True or false: a <strong>hash table</strong> typically offers "
        "average-case O(1) lookup for a key.</p>",
        [
            ("<p>True</p>", True),
            ("<p>False</p>", False),
        ],
        "<p>With a good hash function and load factor, lookups are constant "
        "time on average; worst case is O(n) when many keys collide.</p>",
    ),
    (
        "tf",
        "<p>True or false: <strong>DNS</strong> is responsible for "
        "encrypting traffic between a browser and a web server.</p>",
        [
            ("<p>True</p>", False),
            ("<p>False</p>", True),
        ],
        "<p>DNS translates names to IP addresses. Encryption between browser "
        "and server is provided by <strong>TLS</strong> (the 'S' in HTTPS).</p>",
    ),
]


PRACTICAL_HTML = (
    "<h2>Practical Lab \u2014 Measure and Compare Algorithm Complexity</h2>"
    "<p>In this lab you will <strong>empirically</strong> measure how the "
    "running time of three lookup strategies grows with input size, and "
    "compare the measurements to the theoretical Big-O classes you met in "
    "the lesson.</p>"

    "<h3>Goals</h3>"
    "<ul>"
    "<li>Implement and time <em>linear search</em>, <em>binary search</em> "
    "and <em>hash-set membership</em>.</li>"
    "<li>Run them on inputs of size 10<sup>3</sup>, 10<sup>4</sup>, "
    "10<sup>5</sup> and 10<sup>6</sup>.</li>"
    "<li>Plot the results and reason about why the curves look the way "
    "they do.</li>"
    "</ul>"

    "<h3>Step 1 - Set up the environment</h3>"
    "<pre><code>python -m venv .venv\n"
    ".venv\\Scripts\\activate   # Windows\n"
    "pip install matplotlib\n"
    "</code></pre>"

    "<h3>Step 2 - Write the benchmark script</h3>"
    "<p>Create a file <code>bench.py</code> with the following content:</p>"
    "<pre><code>import time\n"
    "import random\n"
    "import matplotlib.pyplot as plt\n"
    "\n"
    "def linear_search(xs, target):\n"
    "    for i, x in enumerate(xs):\n"
    "        if x == target:\n"
    "            return i\n"
    "    return -1\n"
    "\n"
    "def binary_search(xs, target):\n"
    "    lo, hi = 0, len(xs) - 1\n"
    "    while lo &lt;= hi:\n"
    "        mid = (lo + hi) // 2\n"
    "        if xs[mid] == target:\n"
    "            return mid\n"
    "        if xs[mid] &lt; target:\n"
    "            lo = mid + 1\n"
    "        else:\n"
    "            hi = mid - 1\n"
    "    return -1\n"
    "\n"
    "def timed(fn, *args, repeats=5):\n"
    "    best = float('inf')\n"
    "    for _ in range(repeats):\n"
    "        t0 = time.perf_counter()\n"
    "        fn(*args)\n"
    "        best = min(best, time.perf_counter() - t0)\n"
    "    return best\n"
    "\n"
    "sizes = [10**3, 10**4, 10**5, 10**6]\n"
    "linear_times, binary_times, hash_times = [], [], []\n"
    "\n"
    "for n in sizes:\n"
    "    data = list(range(n))\n"
    "    data_set = set(data)\n"
    "    target = n - 1   # worst case for linear search\n"
    "\n"
    "    linear_times.append(timed(linear_search, data, target))\n"
    "    binary_times.append(timed(binary_search, data, target))\n"
    "    hash_times.append(timed(lambda: target in data_set))\n"
    "\n"
    "for n, lt, bt, ht in zip(sizes, linear_times, binary_times, hash_times):\n"
    "    print(n, 'linear', lt, 'binary', bt, 'hash', ht)\n"
    "\n"
    "plt.figure()\n"
    "plt.plot(sizes, linear_times, marker='o', label='linear  O(n)')\n"
    "plt.plot(sizes, binary_times, marker='o', label='binary  O(log n)')\n"
    "plt.plot(sizes, hash_times,   marker='o', label='hash    O(1)')\n"
    "plt.xscale('log')\n"
    "plt.yscale('log')\n"
    "plt.xlabel('input size n')\n"
    "plt.ylabel('best-of-5 seconds')\n"
    "plt.title('Empirical complexity of search algorithms')\n"
    "plt.legend()\n"
    "plt.grid(True, which='both', linestyle='--', alpha=0.4)\n"
    "plt.savefig('complexity.png', dpi=150)\n"
    "</code></pre>"

    "<h3>Step 3 - Run and observe</h3>"
    "<pre><code>python bench.py\n"
    "</code></pre>"
    "<p>Expected trends on a typical laptop:</p>"
    "<table><thead><tr><th>n</th><th>linear (s)</th><th>binary (s)</th>"
    "<th>hash (s)</th></tr></thead><tbody>"
    "<tr><td>10<sup>3</sup></td><td>~0.00005</td><td>~0.000002</td>"
    "<td>~0.0000002</td></tr>"
    "<tr><td>10<sup>4</sup></td><td>~0.0005</td><td>~0.000003</td>"
    "<td>~0.0000002</td></tr>"
    "<tr><td>10<sup>5</sup></td><td>~0.005</td><td>~0.000004</td>"
    "<td>~0.0000002</td></tr>"
    "<tr><td>10<sup>6</sup></td><td>~0.05</td><td>~0.000005</td>"
    "<td>~0.0000002</td></tr>"
    "</tbody></table>"
    "<p>Linear search scales <em>roughly proportionally</em> with n; binary "
    "search barely moves (the time only doubles when n grows by a factor of "
    "10<sup>6</sup>, which is consistent with log<sub>2</sub>); the hash-set "
    "test is essentially flat.</p>"

    "<h3>Step 4 - Estimate empirical Big-O</h3>"
    "<p>For two sizes n<sub>1</sub> and n<sub>2</sub> with times "
    "t<sub>1</sub>, t<sub>2</sub>, estimate the exponent <em>k</em> in "
    "t = c &middot; n<sup>k</sup>:</p>"
    "<pre><code>import math\n"
    "k = math.log(t2 / t1) / math.log(n2 / n1)\n"
    "print('estimated exponent k =', k)\n"
    "</code></pre>"
    "<p>You should see <em>k</em> close to 1.0 for linear search and close "
    "to 0 for binary search and hash lookup.</p>"

    "<h3>Reflection questions</h3>"
    "<ol>"
    "<li>Why does binary search require the input list to be <em>sorted</em>, "
    "and how would sorting cost change the picture if you only searched "
    "once?</li>"
    "<li>Why is the hash-set lookup essentially flat, and under what "
    "conditions would it degrade to O(n)?</li>"
    "<li>How would the curves change if you measured <em>average</em> case "
    "instead of <em>worst</em> case for linear search?</li>"
    "<li>Relate these findings to a real AI scenario: looking up a token in "
    "a vocabulary of 50 000 entries during tokenisation. Which structure "
    "should you choose and why?</li>"
    "</ol>"

    "<h3>Submission</h3>"
    "<p>Submit <code>bench.py</code>, the generated <code>complexity.png</code> "
    "plot, and a short paragraph (150-250 words) answering the reflection "
    "questions in your own words.</p>"
)
