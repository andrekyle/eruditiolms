"""SAQA 118792 AI Software Developer (NQF 5) - Lesson 04.

Covers KM-04 Data, Databases and Data Visualisation (NQF4, 8 cr)
and PM-03 Access, Analyse and Visualise Structured Data Using
Spreadsheets (NQF4, 4 cr).
"""

LESSON_HTML = (
    "<h2>Data, Databases and Visualisation</h2>"
    "<p>Modern software developers spend as much time moving, shaping and "
    "presenting <strong>data</strong> as they spend writing application "
    "logic. This lesson combines two SAQA unit-standard outcomes: the "
    "<em>knowledge module</em> on data, databases and visualisation, and "
    "the <em>practical module</em> on analysing structured data with a "
    "spreadsheet. By the end you should be able to classify data, design "
    "a small relational schema, choose between SQL and NoSQL storage, "
    "build a basic ETL pipeline in your head, and select the right chart "
    "for a question.</p>"

    "<h3>1. Types of data</h3>"
    "<p>Before you can store or visualise data, you must know what kind "
    "of value you are dealing with. Statisticians group measurements into "
    "four <strong>levels of measurement</strong>:</p>"
    "<ul>"
    "<li><strong>Nominal</strong> &mdash; named categories with no order "
    "(province, payment method, blood type).</li>"
    "<li><strong>Ordinal</strong> &mdash; ordered categories where gaps "
    "are not equal (matric symbol A&ndash;F, customer satisfaction "
    "score).</li>"
    "<li><strong>Interval</strong> &mdash; numeric with equal gaps but no "
    "true zero (temperature in &deg;C, calendar year).</li>"
    "<li><strong>Ratio</strong> &mdash; numeric with equal gaps and a "
    "true zero, so ratios are meaningful (rand amount, kilograms, "
    "kilometres, response time).</li>"
    "</ul>"
    "<p>The level of measurement constrains the statistics and charts "
    "you may use: a mean is meaningful for ratio data but nonsense for "
    "nominal data, and a line chart implies an ordered x-axis.</p>"

    "<h3>2. Structured, semi-structured and unstructured data</h3>"
    "<table>"
    "<thead><tr><th>Form</th><th>Examples</th><th>Typical store</th></tr>"
    "</thead>"
    "<tbody>"
    "<tr><td><strong>Structured</strong></td><td>Rows and columns with a "
    "fixed schema: sales, payroll, stock levels.</td><td>Relational "
    "database, spreadsheet, CSV.</td></tr>"
    "<tr><td><strong>Semi-structured</strong></td><td>Self-describing "
    "records with flexible fields: JSON from a web API, XML, "
    "log lines.</td><td>Document database, data lake.</td></tr>"
    "<tr><td><strong>Unstructured</strong></td><td>Free text, images, "
    "audio, video.</td><td>Object storage (S3, Azure Blob), search "
    "index.</td></tr>"
    "</tbody></table>"

    "<h3>3. Data quality dimensions</h3>"
    "<p>Poor data quality silently breaks every model and dashboard built "
    "on top of it. Six widely cited <strong>dimensions</strong> help you "
    "audit a data set:</p>"
    "<ul>"
    "<li><strong>Accuracy</strong> &mdash; do the recorded values match "
    "reality?</li>"
    "<li><strong>Completeness</strong> &mdash; are required fields "
    "populated for every record?</li>"
    "<li><strong>Consistency</strong> &mdash; do the same facts agree "
    "across systems (e.g. one customer, one spelling)?</li>"
    "<li><strong>Timeliness</strong> &mdash; is the data fresh enough "
    "for the decision you are making?</li>"
    "<li><strong>Uniqueness</strong> &mdash; is each real-world entity "
    "represented exactly once (no duplicates)?</li>"
    "<li><strong>Validity</strong> &mdash; do values conform to the "
    "expected type, range and format (e.g. ID number checksum, valid "
    "email)?</li>"
    "</ul>"

    "<h3>4. Relational databases</h3>"
    "<p>A <strong>relational database</strong> stores data as a set of "
    "<em>tables</em> (relations). Each table has named columns with a "
    "data type, and each row is uniquely identified by a "
    "<strong>primary key</strong>. Relationships between tables are "
    "expressed with <strong>foreign keys</strong> that point back at "
    "another table's primary key.</p>"
    "<p>Good schemas are <strong>normalised</strong> to remove "
    "redundancy:</p>"
    "<ol>"
    "<li><strong>1NF</strong> &mdash; atomic values, no repeating groups "
    "in a cell.</li>"
    "<li><strong>2NF</strong> &mdash; 1NF, and every non-key column "
    "depends on the <em>whole</em> primary key (no partial "
    "dependencies).</li>"
    "<li><strong>3NF</strong> &mdash; 2NF, and non-key columns depend "
    "only on the key, not on other non-key columns (no transitive "
    "dependencies).</li>"
    "</ol>"
    "<p>Transactions in a relational database obey the "
    "<strong>ACID</strong> properties: <em>Atomicity</em> (all-or-"
    "nothing), <em>Consistency</em> (constraints always hold), "
    "<em>Isolation</em> (concurrent transactions do not see each "
    "other's partial work) and <em>Durability</em> (committed data "
    "survives a crash).</p>"
    "<pre><code>CREATE TABLE province (\n"
    "  province_id INT PRIMARY KEY,\n"
    "  name VARCHAR(40) NOT NULL UNIQUE\n"
    ");\n\n"
    "CREATE TABLE sale (\n"
    "  sale_id BIGINT PRIMARY KEY,\n"
    "  sale_date DATE NOT NULL,\n"
    "  province_id INT NOT NULL REFERENCES province(province_id),\n"
    "  amount_rand NUMERIC(12,2) NOT NULL CHECK (amount_rand &gt;= 0)\n"
    ");</code></pre>"

    "<h3>5. NoSQL families</h3>"
    "<p>Some workloads do not fit neatly into rows and columns, or need "
    "to scale horizontally across many servers. <strong>NoSQL</strong> "
    "databases trade some ACID guarantees for flexibility and scale:</p>"
    "<ul>"
    "<li><strong>Document</strong> (MongoDB, Couchbase) &mdash; stores "
    "JSON-like documents. Good for content, product catalogues, user "
    "profiles with varying fields.</li>"
    "<li><strong>Key-value</strong> (Redis, DynamoDB) &mdash; a giant "
    "dictionary; ideal for caches, session stores, shopping carts.</li>"
    "<li><strong>Column-family</strong> (Cassandra, HBase) &mdash; "
    "wide-row tables optimised for time-series and write-heavy "
    "workloads such as IoT telemetry.</li>"
    "<li><strong>Graph</strong> (Neo4j, JanusGraph) &mdash; nodes and "
    "edges; perfect for social networks, fraud rings, recommendation "
    "and knowledge graphs.</li>"
    "</ul>"

    "<h3>6. ETL and ELT pipelines</h3>"
    "<p>Operational systems rarely answer analytical questions directly. "
    "A pipeline moves data from sources into an analytics store:</p>"
    "<ul>"
    "<li><strong>ETL</strong> &mdash; Extract from sources, "
    "<em>Transform</em> in a staging area, then Load into the "
    "warehouse. Classic when the warehouse is small or expensive.</li>"
    "<li><strong>ELT</strong> &mdash; Extract, Load raw data into a "
    "cheap, scalable store, then Transform inside it with SQL. Common "
    "with modern cloud warehouses and data lakes.</li>"
    "</ul>"

    "<h3>7. Data warehouses vs data lakes</h3>"
    "<table>"
    "<thead><tr><th>Aspect</th><th>Data warehouse</th><th>Data lake"
    "</th></tr></thead>"
    "<tbody>"
    "<tr><td>Schema</td><td>Schema-on-write (defined up front)</td>"
    "<td>Schema-on-read (defined when queried)</td></tr>"
    "<tr><td>Data</td><td>Cleaned, structured</td><td>Raw, any "
    "format</td></tr>"
    "<tr><td>Users</td><td>Business analysts, BI tools</td>"
    "<td>Data scientists, ML engineers</td></tr>"
    "<tr><td>Cost per TB</td><td>Higher</td><td>Lower</td></tr>"
    "</tbody></table>"

    "<h3>8. Visualisation principles</h3>"
    "<p>Edward <strong>Tufte</strong> argues that good graphics maximise "
    "the <em>data-ink ratio</em>: every drop of ink should carry "
    "information. Avoid 3-D effects, heavy gridlines and decorative "
    "chart-junk; label directly; start bar-chart axes at zero; and never "
    "use a pie chart with more than a few slices.</p>"
    "<p>Pick the chart from the <em>question</em>, not the data:</p>"
    "<ul>"
    "<li><strong>Bar chart</strong> &mdash; compare a numeric value "
    "across categories (sales per province).</li>"
    "<li><strong>Line chart</strong> &mdash; show a trend over an "
    "ordered axis, usually time.</li>"
    "<li><strong>Scatter plot</strong> &mdash; explore the relationship "
    "between two numeric variables.</li>"
    "<li><strong>Histogram</strong> &mdash; show the distribution of a "
    "single numeric variable.</li>"
    "<li><strong>Heatmap</strong> &mdash; show a matrix of values, e.g. "
    "correlation or sales by province &times; month.</li>"
    "</ul>"

    "<h3>9. Spreadsheet workflows</h3>"
    "<p>Excel, LibreOffice Calc and Google Sheets remain the most widely "
    "used data tools in South African businesses. Key skills:</p>"
    "<ul>"
    "<li><strong>VLOOKUP / XLOOKUP</strong> &mdash; look up a value in "
    "another table by key. <code>XLOOKUP</code> is the modern "
    "replacement; it handles missing values and searches in any "
    "direction.</li>"
    "<li><strong>Pivot tables</strong> &mdash; drag-and-drop aggregation "
    "by rows, columns and values; the spreadsheet equivalent of "
    "<code>GROUP BY</code>.</li>"
    "<li><strong>Named ranges</strong> &mdash; give a block of cells a "
    "human-readable name so formulas read like English.</li>"
    "<li><strong>Data validation</strong> &mdash; restrict what users "
    "can type into a cell (list, range, pattern) to protect data "
    "quality.</li>"
    "<li><strong>Charts and dashboards</strong> &mdash; combine pivot "
    "tables, slicers and charts on a single sheet to give "
    "decision-makers a one-page view.</li>"
    "</ul>"

    "<h3>10. Dashboards</h3>"
    "<p>A <strong>dashboard</strong> is a single screen that answers a "
    "small number of recurring questions for a specific audience. Good "
    "dashboards: state the audience and decision at the top, put the "
    "headline metric in the upper-left, group related charts, use "
    "consistent colours, and refresh on a known cadence. Resist the "
    "temptation to cram in every available chart &mdash; a dashboard is "
    "not a report.</p>"

    "<blockquote>&ldquo;Above all else show the data.&rdquo; "
    "&mdash; Edward Tufte</blockquote>"
)


QUESTIONS = [
    (
        "mc",
        "<p>A column stores customer satisfaction as "
        "<em>Poor, Fair, Good, Excellent</em>. Which level of "
        "measurement is this?</p>",
        [
            ("<p>Nominal</p>", False),
            ("<p>Ordinal</p>", True),
            ("<p>Interval</p>", False),
            ("<p>Ratio</p>", False),
        ],
        "<p>The categories have a clear order but the gaps between them "
        "are not numerically equal, which is the definition of "
        "<strong>ordinal</strong> data.</p>",
    ),
    (
        "mc",
        "<p>Which option best describes <strong>semi-structured</strong> "
        "data?</p>",
        [
            ("<p>Rows and columns in a fixed relational schema.</p>",
             False),
            ("<p>Free-form audio and video files.</p>", False),
            ("<p>Self-describing records such as JSON returned by a web "
             "API, where fields can vary between records.</p>", True),
            ("<p>Data that has been deleted but not yet purged.</p>",
             False),
        ],
        "<p>Semi-structured data carries its own field names (tags, "
        "keys) so the schema can vary per record; JSON and XML are the "
        "canonical examples.</p>",
    ),
    (
        "mc",
        "<p>A customer table has the columns "
        "<code>customer_id, name, postcode, city</code>. Because "
        "<em>city</em> is determined by <em>postcode</em> rather than by "
        "<em>customer_id</em>, the table violates which normal form?</p>",
        [
            ("<p>First normal form (1NF)</p>", False),
            ("<p>Second normal form (2NF)</p>", False),
            ("<p>Third normal form (3NF)</p>", True),
            ("<p>It does not violate any normal form.</p>", False),
        ],
        "<p>This is a <strong>transitive dependency</strong>: a non-key "
        "column (city) depends on another non-key column (postcode). "
        "Removing it requires 3NF, typically by extracting a "
        "<code>postcode</code> table.</p>",
    ),
    (
        "mc",
        "<p>Which NoSQL family is the most natural fit for storing a "
        "social network of users who <em>follow</em> each other and for "
        "querying friend-of-friend relationships?</p>",
        [
            ("<p>Key-value store</p>", False),
            ("<p>Document store</p>", False),
            ("<p>Column-family store</p>", False),
            ("<p>Graph database</p>", True),
        ],
        "<p>Graph databases model nodes (users) and edges (follows) "
        "directly, and traverse multi-hop relationships such as "
        "friend-of-friend far more efficiently than the other "
        "families.</p>",
    ),
    (
        "mc",
        "<p>You want to show how a single numeric variable "
        "(transaction amount, in rand) is <strong>distributed</strong> "
        "across thousands of sales. Which chart type is most "
        "appropriate?</p>",
        [
            ("<p>Pie chart</p>", False),
            ("<p>Line chart</p>", False),
            ("<p>Histogram</p>", True),
            ("<p>Stacked bar chart</p>", False),
        ],
        "<p>A <strong>histogram</strong> buckets a numeric variable "
        "into bins and shows how many observations fall in each, which "
        "is exactly a distribution.</p>",
    ),
    (
        "mc",
        "<p>Which spreadsheet feature is the equivalent of SQL's "
        "<code>GROUP BY</code> with aggregate functions?</p>",
        [
            ("<p>Data validation</p>", False),
            ("<p>Pivot table</p>", True),
            ("<p>Conditional formatting</p>", False),
            ("<p>Named range</p>", False),
        ],
        "<p>A <strong>pivot table</strong> groups rows by one or more "
        "fields and applies an aggregate (sum, average, count) to a "
        "value field, mirroring <code>GROUP BY</code>.</p>",
    ),
    (
        "tf",
        "<p><strong>True or False:</strong> In an <em>ELT</em> pipeline "
        "the raw data is loaded into the target store first and "
        "transformations are run there afterwards.</p>",
        [
            ("<p>True</p>", True),
            ("<p>False</p>", False),
        ],
        "<p>That is precisely what distinguishes <strong>ELT</strong> "
        "from ETL: Extract, Load, then Transform inside a powerful "
        "warehouse or lake.</p>",
    ),
    (
        "tf",
        "<p><strong>True or False:</strong> The <em>Durability</em> "
        "property in ACID means that two concurrent transactions cannot "
        "see each other's uncommitted changes.</p>",
        [
            ("<p>True</p>", False),
            ("<p>False</p>", True),
        ],
        "<p>That description is <strong>Isolation</strong>. "
        "<em>Durability</em> means that once a transaction commits, its "
        "changes survive crashes and power loss.</p>",
    ),
]


PRACTICAL_HTML = (
    "<h2>Practical Lab \u2014 Analyse Sales Data with a Spreadsheet</h2>"
    "<p>In this lab you will play the role of a junior analyst at a "
    "national retailer. Head office has sent you a small CSV of sales "
    "by province and month and asked for a one-page dashboard with three "
    "insights by the end of the day. You may use Microsoft Excel, "
    "LibreOffice Calc or Google Sheets &mdash; the steps are almost "
    "identical.</p>"

    "<h3>Sample data set</h3>"
    "<p>Create a file called <code>sa_sales.csv</code> with the "
    "following content (the leading and trailing spaces in some rows "
    "are intentional &mdash; you will clean them later):</p>"
    "<pre><code>province,month,amount_rand\n"
    "Gauteng,Jan,182340\n"
    " Gauteng ,Feb,201500\n"
    "Western Cape,Jan,154200\n"
    "Western Cape,Feb,167800\n"
    "KwaZulu-Natal,Jan,121050\n"
    "KwaZulu-Natal,Feb,133900\n"
    "Eastern Cape,Jan,78400\n"
    "Eastern Cape,Feb,81200\n"
    "Gauteng,Jan,182340\n"
    "Free State,Feb,45600\n"
    "Limpopo,Jan,52800\n"
    "Limpopo,Feb,58100\n"
    "Mpumalanga,Jan,61400\n"
    "Mpumalanga,Feb,64900\n"
    "North West,Jan,49200\n"
    "Northern Cape,Feb,28700</code></pre>"

    "<h3>Step 1 &mdash; Import the CSV</h3>"
    "<ol>"
    "<li>Open the spreadsheet application and choose "
    "<strong>File &rarr; Open</strong> (or <strong>File &rarr; Import"
    "</strong> in Google Sheets).</li>"
    "<li>Select <code>sa_sales.csv</code>. In the import dialog confirm "
    "that the separator is a comma and that the first row is treated as "
    "headers.</li>"
    "<li><em>Screenshot in words:</em> you should see three columns "
    "&mdash; <strong>province</strong>, <strong>month</strong>, "
    "<strong>amount_rand</strong> &mdash; with 16 data rows below the "
    "header.</li>"
    "</ol>"

    "<h3>Step 2 &mdash; Clean the data</h3>"
    "<ol>"
    "<li>Insert a new column <code>province_clean</code> and enter "
    "<code>=TRIM(A2)</code>, copying the formula down. This removes "
    "the leading/trailing spaces that broke the second Gauteng row.</li>"
    "<li>Select the three data columns and use "
    "<strong>Data &rarr; Remove Duplicates</strong>. You should see one "
    "duplicate Gauteng/Jan row removed.</li>"
    "<li>Right-click the <code>amount_rand</code> column header and "
    "choose <strong>Format Cells &rarr; Number &rarr; Currency (ZAR, "
    "no decimals)</strong>.</li>"
    "<li>Add <strong>Data Validation</strong> on the month column: "
    "allow only the list <code>Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,"
    "Nov,Dec</code>. Any future typo will now be rejected at entry.</li>"
    "<li><em>Expected output:</em> 15 clean, currency-formatted rows "
    "with no duplicates and a green tick of trust over the data.</li>"
    "</ol>"

    "<h3>Step 3 &mdash; Build a pivot table</h3>"
    "<ol>"
    "<li>Click anywhere in the cleaned table and choose "
    "<strong>Insert &rarr; PivotTable</strong>. Place it on a new "
    "sheet called <em>Pivot</em>.</li>"
    "<li>Drag <strong>province_clean</strong> into <em>Rows</em>, "
    "<strong>month</strong> into <em>Columns</em>, and "
    "<strong>amount_rand</strong> into <em>Values</em> (Sum).</li>"
    "<li>Turn on <strong>Grand Totals</strong> for both rows and "
    "columns.</li>"
    "<li><em>Screenshot in words:</em> a 9-row by 3-column matrix "
    "(provinces &times; Jan/Feb) with a Grand Total column on the "
    "right and a Grand Total row at the bottom.</li>"
    "</ol>"

    "<h3>Step 4 &mdash; Clustered bar chart</h3>"
    "<ol>"
    "<li>Select the pivot table excluding grand totals.</li>"
    "<li>Choose <strong>Insert &rarr; Chart &rarr; Clustered Bar</strong>"
    " (or Clustered Column).</li>"
    "<li>Title it <em>Monthly sales by province (ZAR)</em>. Remove "
    "gridlines, label axes, and use a single restrained colour per "
    "month.</li>"
    "<li><em>Expected output:</em> each province has two bars side by "
    "side, making it easy to compare Jan vs Feb within and across "
    "provinces.</li>"
    "</ol>"

    "<h3>Step 5 &mdash; Line chart of trend</h3>"
    "<ol>"
    "<li>On the pivot table, switch the layout so months are on "
    "<em>Rows</em> and provinces on <em>Columns</em>.</li>"
    "<li>Insert a <strong>Line</strong> chart. Each province becomes a "
    "line tracking Jan &rarr; Feb.</li>"
    "<li>Title it <em>Sales trend Jan&ndash;Feb by province</em>.</li>"
    "<li><em>Note:</em> with only two time points the line is a single "
    "segment &mdash; this is intentional; in a real project you would "
    "extend the data to 12 months.</li>"
    "</ol>"

    "<h3>Step 6 &mdash; Assemble the dashboard</h3>"
    "<ol>"
    "<li>Create a new sheet called <strong>Dashboard</strong>.</li>"
    "<li>In the top-left, place a large KPI cell that reads "
    "<em>Total sales:</em> with the formula "
    "<code>=SUM(Pivot!B2:C10)</code>.</li>"
    "<li>Copy the bar chart to the upper-right and the line chart "
    "directly below it.</li>"
    "<li>Add a small text box at the bottom listing your three "
    "insights from Step 7.</li>"
    "<li>Set the page layout to <strong>A4 Landscape, fit to one "
    "page</strong> and print-preview to make sure nothing is cut "
    "off.</li>"
    "</ol>"

    "<h3>Step 7 &mdash; Draw three insights</h3>"
    "<p>Look at your charts and write three short, decision-ready "
    "statements. Examples a learner might produce from this data set:</p>"
    "<ol>"
    "<li><strong>Gauteng dominates:</strong> Gauteng alone accounts for "
    "roughly a quarter of national sales in both months &mdash; any "
    "supply-chain disruption there is a national risk.</li>"
    "<li><strong>February is up everywhere:</strong> every province "
    "with two months of data grew from January to February, suggesting "
    "a seasonal or campaign effect worth investigating.</li>"
    "<li><strong>Northern Cape and Free State under-trade:</strong> "
    "both contribute under R50&nbsp;000 per month; head office should "
    "decide whether to invest in marketing there or accept the gap.</li>"
    "</ol>"

    "<h3>Reflection questions</h3>"
    "<ul>"
    "<li>Which of the six data-quality dimensions did Step 2 improve, "
    "and how would you measure that improvement?</li>"
    "<li>Why is a clustered bar chart a better choice than a pie chart "
    "for comparing provinces across two months?</li>"
    "<li>If next month's file arrives with a new province spelled "
    "<em>&ldquo;Kwazulu Natal&rdquo;</em>, what controls in your "
    "workbook would catch the inconsistency before it reaches the "
    "dashboard?</li>"
    "<li>How would you redesign this dashboard for a store manager who "
    "only cares about their own province?</li>"
    "</ul>"
)
