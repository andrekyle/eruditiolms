"""SAQA 118792 AI Software Developer (NQF 5) - Lesson 06.

Covers:
    PM-04  Use SQL to Communicate with a Database (NQF5, 4 credits)
    PM-06  Use Python Data Scraping to Populate Database Table in SQL
           (NQF5, 4 credits)

Exports:
    LESSON_HTML     -- theory HTML (>= 2200 chars)
    QUESTIONS       -- exactly 8 tuples (qtype, qhtml, opts, fb)
    PRACTICAL_HTML  -- practical lab HTML (>= 1800 chars)
"""

LESSON_HTML = (
    "<h2>SQL, Python and Data Scraping</h2>"
    "<p>This lesson combines two closely related skills that appear in "
    "almost every real AI software project: talking to a relational "
    "database with <strong>SQL</strong>, and pulling new data into that "
    "database using <strong>Python web scraping</strong>. By the end you "
    "should be able to design a small schema, query it confidently, and "
    "write a Python pipeline that scrapes a public web page and stores "
    "the results safely.</p>"

    "<h3>1. The relational model in one minute</h3>"
    "<p>A relational database stores facts in <em>tables</em> (also "
    "called relations). Each row is a record, each column has a fixed "
    "data type. Tables are connected by keys:</p>"
    "<ul>"
    "<li><strong>Primary key</strong> &mdash; a column (or set of columns) "
    "that uniquely identifies a row.</li>"
    "<li><strong>Foreign key</strong> &mdash; a column that references the "
    "primary key of another table, enforcing referential integrity.</li>"
    "<li><strong>Constraints</strong> such as <code>NOT NULL</code>, "
    "<code>UNIQUE</code> and <code>CHECK</code> keep data clean at the "
    "database layer rather than relying only on application code.</li>"
    "</ul>"

    "<h3>2. SQL DDL &mdash; defining structure</h3>"
    "<p>Data Definition Language statements create and change the shape "
    "of the database. The most common are <code>CREATE TABLE</code>, "
    "<code>ALTER TABLE</code> and <code>DROP TABLE</code>.</p>"
    "<pre><code>CREATE TABLE company (\n"
    "    id        INTEGER PRIMARY KEY,\n"
    "    name      TEXT    NOT NULL UNIQUE,\n"
    "    country   TEXT    NOT NULL\n"
    ");\n\n"
    "CREATE TABLE job (\n"
    "    id          INTEGER PRIMARY KEY,\n"
    "    title       TEXT    NOT NULL,\n"
    "    company_id  INTEGER NOT NULL,\n"
    "    posted_at   TEXT    NOT NULL,\n"
    "    FOREIGN KEY (company_id) REFERENCES company(id)\n"
    ");\n\n"
    "ALTER TABLE job ADD COLUMN location TEXT;\n"
    "DROP TABLE IF EXISTS old_jobs;</code></pre>"

    "<h3>3. SQL DML &mdash; manipulating data</h3>"
    "<p>Data Manipulation Language covers the four verbs you will use "
    "every day:</p>"
    "<table>"
    "<thead><tr><th>Statement</th><th>Purpose</th></tr></thead>"
    "<tbody>"
    "<tr><td><code>INSERT</code></td><td>Add new rows.</td></tr>"
    "<tr><td><code>UPDATE</code></td><td>Change existing rows.</td></tr>"
    "<tr><td><code>DELETE</code></td><td>Remove rows.</td></tr>"
    "<tr><td><code>SELECT</code></td><td>Read rows (the workhorse).</td></tr>"
    "</tbody></table>"
    "<p><code>SELECT</code> is extended with <code>WHERE</code> to filter, "
    "<code>ORDER BY</code> to sort, and <code>LIMIT</code> to cap the "
    "number of rows returned. For example:</p>"
    "<pre><code>SELECT title, posted_at\n"
    "FROM   job\n"
    "WHERE  location = 'Cape Town'\n"
    "ORDER  BY posted_at DESC\n"
    "LIMIT  5;</code></pre>"

    "<h3>4. Aggregation and grouping</h3>"
    "<p>Aggregate functions collapse many rows into one summary value: "
    "<code>COUNT</code>, <code>SUM</code>, <code>AVG</code>, "
    "<code>MIN</code> and <code>MAX</code>. They are usually combined "
    "with <code>GROUP BY</code> to summarise per category, and "
    "<code>HAVING</code> to filter on the aggregate result (whereas "
    "<code>WHERE</code> filters the raw rows before aggregation).</p>"
    "<pre><code>SELECT   company_id, COUNT(*) AS n_jobs\n"
    "FROM     job\n"
    "GROUP BY company_id\n"
    "HAVING   COUNT(*) &gt;= 3\n"
    "ORDER BY n_jobs DESC;</code></pre>"

    "<h3>5. Joins</h3>"
    "<p>Joins combine rows from two or more tables on a matching key.</p>"
    "<ul>"
    "<li><strong>INNER JOIN</strong> &mdash; only rows where the key "
    "matches in both tables.</li>"
    "<li><strong>LEFT JOIN</strong> &mdash; all rows from the left table, "
    "with <code>NULL</code> for unmatched right-side columns.</li>"
    "<li><strong>RIGHT JOIN</strong> &mdash; mirror image of LEFT JOIN "
    "(not supported in SQLite, but standard elsewhere).</li>"
    "<li><strong>FULL OUTER JOIN</strong> &mdash; every row from both "
    "sides, matched where possible.</li>"
    "</ul>"
    "<pre><code>SELECT   c.name, j.title\n"
    "FROM     company c\n"
    "INNER JOIN job j ON j.company_id = c.id\n"
    "ORDER BY c.name;</code></pre>"

    "<h3>6. Subqueries and CTEs</h3>"
    "<p>A <strong>subquery</strong> is a query nested inside another. A "
    "<strong>Common Table Expression</strong> (CTE) using <code>WITH</code> "
    "names a temporary result so the outer query stays readable. CTEs are "
    "usually preferred for anything beyond a one-liner because they are "
    "easier to read, test and reuse within the same statement.</p>"

    "<h3>7. Views and indexes</h3>"
    "<p>A <strong>view</strong> is a saved <code>SELECT</code> that "
    "behaves like a virtual table &mdash; useful for hiding complexity "
    "and enforcing a stable interface. An <strong>index</strong> is a "
    "lookup structure (typically a B-tree) that speeds up "
    "<code>WHERE</code> and <code>JOIN</code> conditions at the cost of "
    "slightly slower writes and extra storage.</p>"

    "<h3>8. Transactions and ACID</h3>"
    "<p>A <strong>transaction</strong> groups one or more statements so "
    "they succeed or fail as a unit. Relational databases guarantee the "
    "<strong>ACID</strong> properties:</p>"
    "<ul>"
    "<li><strong>Atomicity</strong> &mdash; all or nothing.</li>"
    "<li><strong>Consistency</strong> &mdash; constraints are never "
    "violated.</li>"
    "<li><strong>Isolation</strong> &mdash; concurrent transactions do not "
    "see each other's partial work.</li>"
    "<li><strong>Durability</strong> &mdash; once committed, changes "
    "survive a crash.</li>"
    "</ul>"

    "<h3>9. SQL injection &mdash; the single most important security topic</h3>"
    "<p>SQL injection happens when untrusted input is concatenated into a "
    "SQL string, allowing an attacker to change the meaning of the "
    "statement. <strong>Never</strong> build SQL with string formatting. "
    "Always use <em>parameterised queries</em>, which send the SQL and "
    "the values separately so values can never be interpreted as code.</p>"
    "<pre><code># DANGEROUS - do NOT do this\n"
    "cur.execute(\"SELECT * FROM users WHERE name = '\" + name + \"'\")\n\n"
    "# SAFE - parameterised\n"
    "cur.execute(\"SELECT * FROM users WHERE name = ?\", (name,))</code></pre>"

    "<h3>10. Python data access</h3>"
    "<p>The Python standard library ships with <code>sqlite3</code>, a "
    "zero-install database that is perfect for learning and for small "
    "production workloads. For server databases such as PostgreSQL you "
    "use <code>psycopg2</code> directly, or an Object Relational Mapper "
    "such as <strong>SQLAlchemy</strong> that lets you describe tables "
    "as Python classes and write queries in a database-agnostic way.</p>"
    "<pre><code>import sqlite3\n\n"
    "conn = sqlite3.connect('jobs.db')\n"
    "cur  = conn.cursor()\n"
    "cur.execute(\n"
    "    'INSERT INTO job (title, company_id, posted_at) '\n"
    "    'VALUES (?, ?, ?)',\n"
    "    ('Junior Developer', 1, '2026-05-22'),\n"
    ")\n"
    "conn.commit()\n"
    "conn.close()</code></pre>"

    "<h3>11. Web scraping with Python</h3>"
    "<p>Scraping is the process of programmatically downloading web "
    "pages and extracting structured data from their HTML. The two "
    "workhorse libraries are <code>requests</code> for the HTTP call "
    "and <code>BeautifulSoup</code> (from <code>bs4</code>) for parsing "
    "the returned HTML into a navigable tree.</p>"
    "<pre><code>import requests\n"
    "from bs4 import BeautifulSoup\n\n"
    "resp = requests.get('https://example.com/jobs', timeout=10)\n"
    "resp.raise_for_status()\n"
    "soup = BeautifulSoup(resp.text, 'html.parser')\n"
    "for card in soup.select('div.job-card'):\n"
    "    title   = card.select_one('h3').get_text(strip=True)\n"
    "    company = card.select_one('.company').get_text(strip=True)\n"
    "    print(title, '-', company)</code></pre>"

    "<h3>12. Ethics, law and good manners</h3>"
    "<p>Just because data is visible in a browser does not mean you may "
    "harvest it. Before you scrape, check:</p>"
    "<ul>"
    "<li><strong>robots.txt</strong> &mdash; the file at "
    "<code>/robots.txt</code> tells crawlers which paths are off limits. "
    "Respect it.</li>"
    "<li><strong>Terms of service</strong> &mdash; many sites forbid "
    "automated access in their T&amp;Cs; breaching them can be a civil "
    "matter.</li>"
    "<li><strong>Computer-misuse legislation</strong> &mdash; in South "
    "Africa the Cybercrimes Act, and elsewhere laws like the UK Computer "
    "Misuse Act, criminalise unauthorised access to a computer system. "
    "Bypassing login walls or rate limits can fall under these acts.</li>"
    "<li><strong>POPIA / GDPR</strong> &mdash; if the data identifies a "
    "living person you become a responsible party with legal duties "
    "around lawful basis, minimisation and retention.</li>"
    "<li><strong>Rate limiting</strong> &mdash; sleep between requests "
    "(<code>time.sleep</code>), set a descriptive <code>User-Agent</code>, "
    "and back off on HTTP 429.</li>"
    "<li><strong>Pagination</strong> &mdash; most listings span many "
    "pages; follow <code>?page=N</code> or &quot;next&quot; links until "
    "they run out, but cap the total to avoid runaway crawls.</li>"
    "</ul>"
    "<blockquote>Rule of thumb: scrape only what you would be comfortable "
    "explaining in writing to the site owner.</blockquote>"

    "<h3>13. End-to-end worked example</h3>"
    "<p>The pieces come together as a small pipeline: <em>fetch</em> a "
    "listing page, <em>parse</em> the HTML into records, then "
    "<em>insert</em> each record into SQLite using parameterised SQL "
    "inside a single transaction.</p>"
    "<pre><code>import sqlite3, requests, time\n"
    "from bs4 import BeautifulSoup\n\n"
    "conn = sqlite3.connect('jobs.db')\n"
    "conn.execute('''CREATE TABLE IF NOT EXISTS job (\n"
    "    id INTEGER PRIMARY KEY,\n"
    "    title TEXT, company TEXT,\n"
    "    location TEXT, posted_at TEXT)''')\n\n"
    "for page in range(1, 4):\n"
    "    url  = 'https://example.com/jobs?page=' + str(page)\n"
    "    html = requests.get(url, timeout=10,\n"
    "        headers={'User-Agent': 'eruditio-learner/1.0'}).text\n"
    "    soup = BeautifulSoup(html, 'html.parser')\n"
    "    rows = []\n"
    "    for c in soup.select('div.job-card'):\n"
    "        rows.append((\n"
    "            c.select_one('h3').get_text(strip=True),\n"
    "            c.select_one('.company').get_text(strip=True),\n"
    "            c.select_one('.location').get_text(strip=True),\n"
    "            c.select_one('time')['datetime'],\n"
    "        ))\n"
    "    conn.executemany(\n"
    "        'INSERT INTO job (title, company, location, posted_at) '\n"
    "        'VALUES (?, ?, ?, ?)', rows)\n"
    "    conn.commit()\n"
    "    time.sleep(1)   # be polite\n"
    "conn.close()</code></pre>"
    "<p>Notice three things: every value goes through a "
    "<code>?</code> placeholder (no injection risk), inserts are batched "
    "with <code>executemany</code> inside one transaction (fast and "
    "atomic), and the script sleeps between pages (polite).</p>"
)


PRACTICAL_HTML = (
    "<h2>Practical Lab \u2014 Scrape Public Data into a SQLite Database</h2>"
    "<p>In this lab you build a complete miniature pipeline: create a "
    "database, parse an HTML snippet, insert the results with safe "
    "parameterised SQL, query the database, and export to CSV. The HTML "
    "is provided inline as a Python string so the lab works offline and "
    "does not depend on any external website.</p>"

    "<h3>Step 1 &mdash; Create the SQLite database and <code>jobs</code> table</h3>"
    "<p>Open a new file <code>lab_scrape.py</code> and start with:</p>"
    "<pre><code>import sqlite3\n\n"
    "conn = sqlite3.connect('jobs.db')\n"
    "cur  = conn.cursor()\n"
    "cur.execute('''\n"
    "    CREATE TABLE IF NOT EXISTS jobs (\n"
    "        id        INTEGER PRIMARY KEY AUTOINCREMENT,\n"
    "        title     TEXT NOT NULL,\n"
    "        company   TEXT NOT NULL,\n"
    "        location  TEXT NOT NULL,\n"
    "        posted_at TEXT NOT NULL\n"
    "    )\n"
    "''')\n"
    "conn.commit()</code></pre>"

    "<h3>Step 2 &mdash; Provide a sample HTML page and parse it</h3>"
    "<p>To keep the lab self-contained we hard-code a small HTML "
    "document. In a real project this string would come from "
    "<code>requests.get(url).text</code>.</p>"
    "<pre><code>from bs4 import BeautifulSoup\n\n"
    "SAMPLE_HTML = '''\n"
    "&lt;html&gt;&lt;body&gt;\n"
    "  &lt;div class=&quot;job-card&quot;&gt;\n"
    "    &lt;h3&gt;Junior Python Developer&lt;/h3&gt;\n"
    "    &lt;span class=&quot;company&quot;&gt;Acme Data&lt;/span&gt;\n"
    "    &lt;span class=&quot;location&quot;&gt;Cape Town&lt;/span&gt;\n"
    "    &lt;time datetime=&quot;2026-05-20&quot;&gt;20 May&lt;/time&gt;\n"
    "  &lt;/div&gt;\n"
    "  &lt;div class=&quot;job-card&quot;&gt;\n"
    "    &lt;h3&gt;Data Engineer&lt;/h3&gt;\n"
    "    &lt;span class=&quot;company&quot;&gt;Beta Insights&lt;/span&gt;\n"
    "    &lt;span class=&quot;location&quot;&gt;Johannesburg&lt;/span&gt;\n"
    "    &lt;time datetime=&quot;2026-05-22&quot;&gt;22 May&lt;/time&gt;\n"
    "  &lt;/div&gt;\n"
    "  &lt;div class=&quot;job-card&quot;&gt;\n"
    "    &lt;h3&gt;ML Intern&lt;/h3&gt;\n"
    "    &lt;span class=&quot;company&quot;&gt;Acme Data&lt;/span&gt;\n"
    "    &lt;span class=&quot;location&quot;&gt;Remote&lt;/span&gt;\n"
    "    &lt;time datetime=&quot;2026-05-21&quot;&gt;21 May&lt;/time&gt;\n"
    "  &lt;/div&gt;\n"
    "&lt;/body&gt;&lt;/html&gt;\n"
    "'''\n\n"
    "soup = BeautifulSoup(SAMPLE_HTML, 'html.parser')</code></pre>"

    "<h3>Step 3 &mdash; Extract listings into Python tuples</h3>"
    "<pre><code>records = []\n"
    "for card in soup.select('div.job-card'):\n"
    "    title     = card.select_one('h3').get_text(strip=True)\n"
    "    company   = card.select_one('.company').get_text(strip=True)\n"
    "    location  = card.select_one('.location').get_text(strip=True)\n"
    "    posted_at = card.select_one('time')['datetime']\n"
    "    records.append((title, company, location, posted_at))\n\n"
    "print('Extracted', len(records), 'jobs')</code></pre>"

    "<h3>Step 4 &mdash; Insert with parameterised statements</h3>"
    "<p>Use <code>executemany</code> with <code>?</code> placeholders. "
    "Never use Python string concatenation or f-strings here, or you "
    "open the door to SQL injection.</p>"
    "<pre><code>cur.executemany(\n"
    "    'INSERT INTO jobs (title, company, location, posted_at) '\n"
    "    'VALUES (?, ?, ?, ?)',\n"
    "    records,\n"
    ")\n"
    "conn.commit()</code></pre>"

    "<h3>Step 5 &mdash; Query the top 5 most-recent jobs</h3>"
    "<pre><code>cur.execute('''\n"
    "    SELECT title, company, location, posted_at\n"
    "    FROM   jobs\n"
    "    ORDER  BY posted_at DESC\n"
    "    LIMIT  5\n"
    "''')\n"
    "top = cur.fetchall()\n"
    "for row in top:\n"
    "    print(row)</code></pre>"

    "<h3>Step 6 &mdash; Export results to CSV</h3>"
    "<pre><code>import csv\n\n"
    "with open('top_jobs.csv', 'w', newline='', encoding='utf-8') as f:\n"
    "    writer = csv.writer(f)\n"
    "    writer.writerow(['title', 'company', 'location', 'posted_at'])\n"
    "    writer.writerows(top)\n\n"
    "conn.close()\n"
    "print('Wrote top_jobs.csv')</code></pre>"

    "<h3>Expected console output</h3>"
    "<pre><code>Extracted 3 jobs\n"
    "('Data Engineer', 'Beta Insights', 'Johannesburg', '2026-05-22')\n"
    "('ML Intern', 'Acme Data', 'Remote', '2026-05-21')\n"
    "('Junior Python Developer', 'Acme Data', 'Cape Town', '2026-05-20')\n"
    "Wrote top_jobs.csv</code></pre>"

    "<h3>Reflection questions</h3>"
    "<ol>"
    "<li>Why is <code>executemany</code> with placeholders both safer "
    "and faster than running one <code>INSERT</code> per row built with "
    "string concatenation?</li>"
    "<li>If the source site listed thousands of jobs across many pages, "
    "what changes would you make to keep the scraper polite (think "
    "<code>robots.txt</code>, rate limits, retries and a sensible "
    "<code>User-Agent</code>)?</li>"
    "<li><strong>Ethics:</strong> the sample page is fictional. Imagine "
    "you point this scraper at a real job board whose terms of service "
    "prohibit automated access, and whose listings include the names "
    "and contact details of recruiters. Which laws and ethical "
    "principles (POPIA, the Cybercrimes Act, the site's T&amp;Cs, "
    "consent and data minimisation) would you have to consider before "
    "running the script even once?</li>"
    "<li>How would you extend the schema so that the same company "
    "appearing in many listings is stored only once, and what kind of "
    "<code>JOIN</code> would you then use to list jobs together with "
    "their company details?</li>"
    "</ol>"
)


QUESTIONS = [
    (
        "mc",
        "<p>Which SQL clause filters rows <strong>after</strong> a "
        "<code>GROUP BY</code> has been applied?</p>",
        [
            ("<code>WHERE</code>", False),
            ("<code>HAVING</code>", True),
            ("<code>ORDER BY</code>", False),
            ("<code>LIMIT</code>", False),
        ],
        "<p><code>WHERE</code> filters individual rows before "
        "aggregation; <code>HAVING</code> filters the grouped results "
        "produced by <code>GROUP BY</code>.</p>",
    ),
    (
        "mc",
        "<p>You need every row from the <code>company</code> table even "
        "when it has no matching rows in <code>job</code>. Which join "
        "should you use?</p>",
        [
            ("<code>INNER JOIN</code>", False),
            ("<code>LEFT JOIN</code>", True),
            ("<code>CROSS JOIN</code>", False),
            ("<code>SELF JOIN</code>", False),
        ],
        "<p>A <code>LEFT JOIN</code> keeps every row from the left "
        "table and fills unmatched right-side columns with "
        "<code>NULL</code>.</p>",
    ),
    (
        "mc",
        "<p>Which of the following correctly protects against SQL "
        "injection when inserting a user-supplied <code>title</code> "
        "into SQLite from Python?</p>",
        [
            ("<code>cur.execute('INSERT INTO job(title) VALUES("
             "\\'' + title + '\\')')</code>", False),
            ("<code>cur.execute(f\"INSERT INTO job(title) VALUES("
             "'{title}')\")</code>", False),
            ("<code>cur.execute('INSERT INTO job(title) VALUES(?)', "
             "(title,))</code>", True),
            ("<code>cur.execute('INSERT INTO job(title) VALUES("
             "%s)' %% title)</code>", False),
        ],
        "<p>Only the parameterised form sends the value separately "
        "from the SQL, so it can never be interpreted as code.</p>",
    ),
    (
        "mc",
        "<p>What does the <strong>A</strong> in <strong>ACID</strong> "
        "stand for, and what does it guarantee?</p>",
        [
            ("Availability &mdash; the database is always online.",
             False),
            ("Atomicity &mdash; a transaction either fully succeeds "
             "or has no effect at all.", True),
            ("Authentication &mdash; only logged-in users may write.",
             False),
            ("Auditing &mdash; every change is written to a log.",
             False),
        ],
        "<p>Atomicity means the statements inside a transaction "
        "behave as a single indivisible unit.</p>",
    ),
    (
        "mc",
        "<p>Which Python library pair is the most common choice for "
        "<em>fetching</em> a web page and <em>parsing</em> its HTML?</p>",
        [
            ("<code>socket</code> + <code>re</code>", False),
            ("<code>urllib3</code> + <code>lxml.etree</code> only",
             False),
            ("<code>requests</code> + <code>BeautifulSoup</code>",
             True),
            ("<code>flask</code> + <code>jinja2</code>", False),
        ],
        "<p><code>requests</code> performs the HTTP call and "
        "<code>BeautifulSoup</code> turns the returned HTML into a "
        "navigable tree.</p>",
    ),
    (
        "mc",
        "<p>Before scraping a public website, which file should you "
        "check first to see which paths the site owner asks crawlers "
        "to avoid?</p>",
        [
            ("<code>sitemap.xml</code>", False),
            ("<code>robots.txt</code>", True),
            ("<code>.htaccess</code>", False),
            ("<code>humans.txt</code>", False),
        ],
        "<p><code>robots.txt</code> at the site root expresses the "
        "owner's wishes about automated access. Respecting it is the "
        "minimum standard of good behaviour.</p>",
    ),
    (
        "tf",
        "<p>True or false: building SQL by concatenating user input "
        "with <code>+</code> in Python is safe as long as you call "
        "<code>str.strip()</code> on the input first.</p>",
        [
            ("True", False),
            ("False", True),
        ],
        "<p>False. Stripping whitespace does nothing to stop SQL "
        "injection. Always use parameterised queries.</p>",
    ),
    (
        "tf",
        "<p>True or false: under POPIA, scraping a public web page "
        "that contains the names and email addresses of identifiable "
        "individuals makes you a responsible party with legal "
        "obligations around how that personal information is used and "
        "retained.</p>",
        [
            ("True", True),
            ("False", False),
        ],
        "<p>True. POPIA applies whenever you process personal "
        "information of identifiable living people, regardless of "
        "whether the data was technically visible to the public.</p>",
    ),
]
