LESSON_HTML = """<h2>Clean, Transform, and Load Data with Power Query</h2>
<p>Power Query is a powerful data transformation tool integrated into Power BI that allows you to connect to various data sources, clean inconsistencies, reshape data structures, and prepare data for analysis. This lesson covers essential techniques for preparing your data through Power Query.</p>

<h3>Data Quality and Profiling</h3>
<p>Before transforming data, you must assess its quality. Power Query provides built-in profiling tools to identify issues:</p>
<ul>
<li><strong>Column Quality:</strong> Shows percentage of valid, error, and empty values in each column</li>
<li><strong>Column Distribution:</strong> Displays the frequency of each value in a column</li>
<li><strong>Column Profile:</strong> Provides detailed statistics including count, distinct values, and data types</li>
</ul>
<p>These tools help you identify missing values, unexpected data types, outliers, and inconsistencies that require cleaning before loading into Power BI.</p>

<h3>Resolving Data Quality Issues</h3>
<p>Common data quality problems and resolution strategies:</p>
<ul>
<li><strong>Null or Missing Values:</strong> Remove rows with critical missing data, fill with defaults, or use interpolation</li>
<li><strong>Inconsistent Formatting:</strong> Standardize text case, trim whitespace, and ensure consistent delimiters</li>
<li><strong>Type Mismatches:</strong> Convert text to numbers, dates, or other appropriate types</li>
<li><strong>Duplicate Records:</strong> Identify and remove duplicates based on key columns</li>
<li><strong>Outliers:</strong> Filter extreme values that may indicate data entry errors</li>
</ul>

<h3>Column Data Types and Transformations</h3>
<p>Power Query requires you to explicitly set column data types. This prevents errors during calculations and ensures proper filtering and sorting:</p>
<pre><code class='language-m'>= Table.TransformColumnTypes(Source,{{"OrderDate", type date}, {"Amount", type number}, {"ProductName", type text}})</code></pre>
<p>Use the <strong>Data Type</strong> feature in Power Query to change types for single or multiple columns. Text-to-number conversions often require removing currency symbols or separators first.</p>

<h3>Creating Keys for Relationships</h3>
<p>Relationships between tables require key columns. Power Query supports multiple key strategies:</p>
<ul>
<li><strong>Natural Keys:</strong> Existing columns that uniquely identify records (e.g., CustomerID, OrderID)</li>
<li><strong>Composite Keys:</strong> Multiple columns combined to create unique identifiers. Merge them using a custom column: <code>&lt;col1&gt; &amp; "-" &amp; &lt;col2&gt;</code></li>
<li><strong>Surrogate Keys:</strong> Artificial unique identifiers created via the <strong>Index Column</strong> feature, useful when natural keys don't exist</li>
</ul>
<p>Use <strong>Add Column &gt; Index Column</strong> to generate surrogate keys starting from 0 or 1.</p>

<h3>Data Shape Transformations</h3>
<p><strong>Pivot Columns:</strong> Convert column values into new columns with aggregated data:</p>
<pre><code class='language-m'>= Table.Pivot(Source, List.Distinct(Source[MonthName]), "MonthName", "Revenue", List.Sum)</code></pre>
<p>Pivot is useful for converting transactional data into a cross-tabular format for analysis.</p>

<p><strong>Unpivot Columns:</strong> Convert wide tables (many columns) into narrow tables (fewer columns with more rows):</p>
<pre><code class='language-m'>= Table.Unpivot(Source, {"2023", "2024", "2025"}, "Year", "Value")</code></pre>
<p>Unpivot is essential for normalizing data structures. Use this when your source data has time periods, categories, or attributes spread across multiple columns.</p>

<p><strong>Transpose:</strong> Swap rows and columns using <strong>Transform &gt; Transpose</strong>. This completely reverses table orientation.</p>

<h3>Combining Data: Merge vs Append</h3>
<p><strong>Append Queries:</strong> Stack rows vertically from multiple tables with the same structure. Use when you have data from different periods or sources:</p>
<ul>
<li>Tables must have matching column names</li>
<li>Creates a union of all records</li>
<li>Example: Combine January, February, March sales into one annual table</li>
</ul>

<p><strong>Merge Queries:</strong> Join columns horizontally from two tables based on matching key columns. Choose the appropriate join type:</p>
<ul>
<li><strong>Inner Join:</strong> Only matching records from both tables</li>
<li><strong>Left Outer Join:</strong> All records from left table, matching records from right table</li>
<li><strong>Right Outer Join:</strong> All records from right table, matching records from left table</li>
<li><strong>Full Outer Join:</strong> All records from both tables</li>
<li><strong>Left Anti Join:</strong> Records from left table NOT in right table</li>
<li><strong>Right Anti Join:</strong> Records from right table NOT in left table</li>
</ul>
<p>Merge creates a new column containing the joined data; expand it to expose joined columns.</p>

<h3>Naming Conventions</h3>
<p>Apply user-friendly naming to improve report usability and reduce confusion:</p>
<ul>
<li><strong>Query Names:</strong> Use descriptive names like "Sales_Transactions" instead of "Query1"</li>
<li><strong>Column Names:</strong> Use proper case (Sales Amount, Order Date) rather than database names (SalesAmt_2024)</li>
<li><strong>Avoid Special Characters:</strong> Use underscores or spaces, not symbols</li>
<li><strong>Consistency:</strong> Apply naming standards across all queries and columns</li>
</ul>

<h3>AI Insights and Advanced Transformations</h3>
<p>Power Query integrates AI capabilities:</p>
<ul>
<li><strong>Text Analytics:</strong> Use AI to extract key phrases, sentiment, or language from text fields</li>
<li><strong>Vision:</strong> Detect objects, read text, or classify images (requires Azure Cognitive Services)</li>
<li><strong>Clustering:</strong> Group similar text values automatically</li>
</ul>
<p>Access these through <strong>Add Column &gt; Insights</strong>. AI Insights enhance data enrichment without manual effort.</p>

<h3>Configuring Data Load and Refresh</h3>
<p>Control which queries and columns load into your Power BI model:</p>
<ul>
<li><strong>Enable Load:</strong> Toggle whether a query's results appear in the data model (right-click query &gt; Enable Load)</li>
<li><strong>Reference Queries:</strong> Create intermediate queries for reuse without loading them separately</li>
<li><strong>Refresh Behavior:</strong> Configure incremental refresh for large datasets to load only new data</li>
</ul>
<p>Disabling load on intermediate queries reduces model size and improves refresh performance.</p>

<h3>Resolving Data Import Errors</h3>
<p>Power Query provides error handling capabilities:</p>
<ul>
<li><strong>Error Rows:</strong> Review the Errors query (auto-generated for failed rows) to diagnose import issues</li>
<li><strong>Row-Level Errors:</strong> Use <strong>Transform &gt; Keep Errors</strong> or <strong>Remove Errors</strong> to manage problematic rows</li>
<li><strong>Error Details:</strong> Click error cells to view specific error messages (e.g., type conversion failures)</li>
<li><strong>Recovery:</strong> Adjust transformations, change data types, or filter problematic data to resolve errors</li>
</ul>
<blockquote>Always review the error log before loading data; unresolved errors indicate data quality or transformation logic issues.</blockquote>"""

QUESTIONS = [
    (
        """<h3>Question 1: Merge vs Append</h3><p>Your company has sales data from three monthly CSV files. All files have identical columns (OrderID, Date, Amount, Product). You want to combine them into one dataset. Which operation should you use?</p>""",
        [
            ("Merge the files to create relationships between them", False),
            ("Append the files to stack rows vertically", True),
            ("Pivot all three files into columns", False),
            ("Transpose each file separately", False),
        ],
        """<p>Correct! Append is used to stack rows from multiple tables with identical structures. Merge would be inappropriate here since you are combining like-structured data, not joining on keys. Pivot and transpose address different transformation needs.</p>""",
    ),
    (
        """<h3>Question 2: Pivot vs Unpivot</h3><p>Your dataset has one column per month (Jan_Sales, Feb_Sales, Mar_Sales, etc.), with products in rows. You need to prepare this for standard analysis. What transformation is required?</p>""",
        [
            ("Unpivot the month columns into a single Month column with values", True),
            ("Pivot the product names into separate columns", False),
            ("Merge with a calendar table", False),
            ("Append this table to historical data", False),
        ],
        """<p>Correct! Unpivot converts wide tables (many columns) into normalized, narrow tables (fewer columns, more rows), which is ideal for analysis. This transforms the month columns into rows for easier filtering and aggregation.</p>""",
    ),
    (
        """<h3>Question 3: Data Quality Assessment</h3><p>Before loading customer data, you enable Column Quality. You notice that the Email column shows 92% valid, 5% empty, 3% error. What should you do?</p>""",
        [
            ("Immediately load the data; Power BI will handle errors automatically", False),
            ("Investigate the 3% errors and 5% empty values to determine if they should be removed or filled", True),
            ("Delete the Email column entirely because it has errors", False),
            ("Pivot the Email column to remove errors", False),
        ],
        """<p>Correct! Data quality profiling is diagnostic. You should investigate errors and nulls to understand their cause. Some may be legitimate (e.g., contacts without email), while others indicate data entry issues. Decide to remove, fill, or flag these records based on your business logic.</p>""",
    ),
    (
        """<h3>Question 4: Creating Surrogate Keys</h3><p>Your transaction table has no natural unique identifier. You need to create a key for relationships. What is the most appropriate method in Power Query?</p>""",
        [
            ("Manually assign numbers to each row in a custom column", False),
            ("Use Add Column > Index Column to generate sequential unique identifiers", True),
            ("Combine three random columns into a composite key", False),
            ("Use the customer ID as the primary key", False),
        ],
        """<p>Correct! Index Column is the standard method for creating surrogate keys in Power Query. It generates sequential, unique identifiers (starting from 0 or 1) for every row, perfect for establishing relationships when natural keys do not exist.</p>""",
    ),
    (
        """<h3>Question 5: When to Use Merge</h3><p>You have an Orders table (OrderID, CustomerID, Amount) and a Customers table (CustomerID, CustomerName, City). You want to add customer names to orders. What operation is needed?</p>""",
        [
            ("Append the Customers table to Orders", False),
            ("Merge Orders with Customers on CustomerID using a Left Outer Join", True),
            ("Unpivot the customer attributes", False),
            ("Pivot the Orders table by CustomerID", False),
        ],
        """<p>Correct! Merge joins the tables horizontally based on a common key (CustomerID). A Left Outer Join preserves all orders and adds matching customer details. This is fundamentally different from append, which stacks tables vertically.</p>""",
    ),
    (
        """<h3>Question 6: Column Data Type Configuration</h3><p>Your Invoice table imports with Amount as text (e.g., "1,234.56"). You need it as a number for calculations. What steps are required?</p>""",
        [
            ("Change the data type directly to number without cleaning", False),
            ("Remove the comma separator, then change data type to decimal number", True),
            ("Unpivot the Amount column first", False),
            ("Create an Index Column to represent amounts", False),
        ],
        """<p>Correct! Text-to-number conversions often fail if the text contains formatting characters. Remove delimiters (commas, currency symbols) first using the Replace function, then change the data type. Power Query processes these steps sequentially.</p>""",
    ),
    (
        """<h3>Question 7: Error Resolution</h3><p>Your Power Query fails to load 47 rows due to type conversion errors. The error message indicates these rows have text in a column you defined as integer. How should you handle this?</p>""",
        [
            ("Delete all 47 rows immediately to resolve errors", False),
            ("Review the errors, correct the source data or transformation, and retry the load", True),
            ("Ignore errors and load the remaining data without investigating", False),
            ("Change the column type to text to avoid errors", False),
        ],
        """<p>Correct! Always investigate errors before accepting data loss. Review the error details, determine the root cause, and fix either the source data or your transformation logic. This ensures data integrity and prevents silent failures in your analysis.</p>""",
    ),
    (
        """<h3>Question 8: Query Load Configuration</h3><p>You create three intermediate queries to prepare different data sources before combining them. These intermediate queries are essential transformations that stakeholders need to reference. What configuration is best?</p>""",
        [
            ("Leave Enable Load on for all three queries so they appear in the data model", True),
            ("Disable Enable Load on all intermediate queries to reduce clutter", False),
            ("Pivot all three queries to save space", False),
            ("Delete intermediate queries after combining them", False),
        ],
        """<p>Correct! If intermediate queries are essential transformations that stakeholders need to reference or audit, keep Enable Load on. Use descriptive query names and organize them logically. This supports transparency and maintainability. Conversely, disable load only on true helper queries to avoid cluttering the model.</p>""",
    ),
]