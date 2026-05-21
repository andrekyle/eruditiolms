LESSON_HTML = """
<h2>Lesson 5: Optimize Model Performance</h2>

<h3>Understanding Performance Bottlenecks</h3>
<p>Model performance directly impacts user experience and adoption. Slow reports frustrate users, consume unnecessary resources, and undermine confidence in analytics. Performance issues can originate from several sources: poorly designed data models with unnecessary columns or rows, inefficient DAX formulas that repeat expensive calculations, relationships configured incorrectly or creating ambiguity, visuals querying excessive data, or storage and refresh strategies misaligned with business needs. The key to optimization is identifying the true bottleneck before investing effort in solutions.</p>

<h3>Using Performance Analyzer</h3>
<p><strong>Performance Analyzer</strong> is your first diagnostic tool. Located in the Home tab of Power BI Desktop, it records the execution time of every visual on the current page, breaking down time into three components: DAX query time (how long the formula took to execute), rendering time (how long Power BI took to display the visual), and other time (supporting operations). When you enable Performance Analyzer and interact with your report, it captures a timeline showing exactly which visuals slow down your report and where the delay originates.</p>

<p>To use Performance Analyzer effectively:</p>
<ul>
<li><strong>Click Start recording</strong> in the Performance Analyzer pane to begin capturing metrics.</li>
<li><strong>Interact with your report</strong>—click slicers, apply filters, click visuals to trigger DAX queries.</li>
<li><strong>Review the timeline</strong> to identify which visuals consume the most time. Visuals taking longer than 1-2 seconds warrant investigation.</li>
<li><strong>Expand each visual entry</strong> to see the breakdown: if DAX query time dominates, the issue is formula-based; if rendering time is high, consider simplifying the visual or reducing data points.</li>
<li><strong>Copy the diagnostic info</strong> to export detailed metrics for further analysis or sharing with colleagues.</li>
</ul>

<p>Performance Analyzer focuses on user-facing delays in reports. However, understanding what happens behind the scenes requires deeper analysis of your data model itself.</p>

<h3>Identifying and Removing Unnecessary Data</h3>
<p>Every column and row in your model consumes memory and slows down queries. Before importing data, decide what is truly needed for analysis. When connecting to a data source:</p>

<ul>
<li><strong>Exclude unused columns early</strong> in Power Query. If you don't need a column for analysis, filtering, or relationships, remove it before import. This reduces dataset size and improves compression within Power BI's Vertipaq engine.</li>
<li><strong>Remove rows that won't be analyzed</strong>. For example, if you have transaction data spanning 10 years but analysis focuses on the last 2 years, filter out historical data or use incremental refresh (discussed later). Similarly, remove test records, archived items, or rows with null keys that cannot join to dimensions.</li>
<li><strong>Aggregate if appropriate</strong>. Sales transactions can be slow to analyze if you have 500 million rows. Consider pre-aggregating to daily or weekly summaries in the source, then refreshing at that level. You can always maintain a detailed table in DirectQuery for drill-through needs.</li>
<li><strong>Normalize lookups</strong>. If a column has only 50 unique values repeated millions of times, consider extracting it to a separate dimension table and linking via relationship. This reduces memory footprint significantly.</li>
</ul>

<h3>Column Data Types and Cardinality Optimization</h3>
<p>Choosing the correct data type for each column affects both model size and query performance. Power BI's Vertipaq compression engine compresses data more efficiently for certain types:</p>

<ul>
<li><strong>Use whole numbers instead of decimals when possible</strong>. Store prices as integers (cents) rather than floats. The Whole Number type compresses better than Decimal and is often sufficient. Reserve Decimal for truly needed precision.</li>
<li><strong>Use categorical data types (text) sparingly in fact tables</strong>. Fact tables should contain primarily numbers and keys. If you're storing text descriptions in a fact table, move them to a dimension instead. Text does not compress as efficiently.</li>
<li><strong>Use Date data type, not datetime or text</strong>. Dates are internally stored as integers and compress extremely well. If you imported a date column as text, change its type to Date.</li>
<li><strong>Be aware of cardinality</strong>. A column's cardinality is the count of unique values. High-cardinality columns (e.g., transaction IDs with millions of unique values) do not compress well and should be avoided unless necessary for relationships. Avoid storing GUIDs, timestamps at millisecond precision, or sequential IDs as attributes in fact tables.</li>
<li><strong>Hide columns you don't need in the user interface</strong>. Hidden columns still consume memory, but they keep the model interface clean and prevent accidental misuse in formulas.</li>
</ul>

<h3>Disabling Auto Date/Time</h3>
<p>By default, Power BI automatically creates hidden date hierarchies for any column typed as Date. This feature creates hidden tables and relationships behind the scenes. While convenient for quick analysis, these hidden artifacts consume memory and can cause unexpected filter behavior, especially in complex models with multiple date tables.</p>

<p><strong>Best practice:</strong> Disable the auto date/time feature globally or per-model and create explicit date dimensions instead. To disable auto date/time:</p>

<ul>
<li>In Power BI Desktop, go to <strong>File → Options and settings → Options → Current File → Data Load</strong>.</li>
<li>Uncheck <strong>Auto date/time</strong>.</li>
<li>Create your own Date table with explicit year, quarter, month, and week hierarchies. This gives you full control and prevents hidden complexity.</li>
</ul>

<p>A simple Date table structure:</p>
<pre><code class='language-dax'>Date = 
ADDCOLUMNS(
    CALENDAR(DATE(2020,1,1), DATE(2025,12,31)),
    &quot;Year&quot;, YEAR([Date]),
    &quot;Quarter&quot;, &quot;Q&quot; &amp; ROUNDUP(MONTH([Date])/3, 0),
    &quot;Month&quot;, FORMAT([Date], &quot;mmmm&quot;),
    &quot;Week&quot;, WEEKNUM([Date])
)
</code></pre>

<h3>Using Vertipaq Analyzer and DAX Studio</h3>
<p><strong>Vertipaq Analyzer</strong> is an external tool that connects to your Power BI model and displays detailed statistics about column compression, cardinality, and memory usage. It shows exactly how much memory each column consumes and reveals opportunities for optimization. For example, if a column is consuming 500 MB despite having only 1000 unique values, that's a sign of poor data type choice or unnecessary cardinality.</p>

<p><strong>DAX Studio</strong> is a free community tool that provides a query editor for testing DAX formulas and profiling their execution. Unlike Performance Analyzer, which measures end-to-end visual rendering time, DAX Studio isolates just the formula execution time and shows you the internal query plan. This reveals whether a measure is using efficient functions like CALCULATE and FILTER or whether it's accidentally scanning huge data volumes.</p>

<p>Using DAX Studio:</p>
<ul>
<li>Connect DAX Studio to your Power BI Desktop instance or published dataset.</li>
<li>Write or paste a DAX formula into the query editor.</li>
<li>Click <strong>Run</strong> to execute and view execution time.</li>
<li>View the <strong>Server Timings</strong> trace to see the internal query plan and identify expensive operations.</li>
<li>Test variations of the formula to find the most efficient version.</li>
</ul>

<h3>Optimizing DAX with Variables</h3>
<p>DAX variables store intermediate results, avoiding repeated calculation and improving both readability and performance. Without variables, a formula might recalculate the same filter or aggregate multiple times.</p>

<p><strong>Without variables (inefficient):</strong></p>
<pre><code class='language-dax'>Total Revenue = 
SUMX(
    FILTER(Sales, Sales[Year] = 2024),
    Sales[Amount]
) + 
SUMX(
    FILTER(Sales, Sales[Year] = 2024),
    Sales[Discount]
)
</code></pre>

<p>Here, the FILTER runs twice, evaluating the same condition twice.</p>

<p><strong>With variables (optimized):</strong></p>
<pre><code class='language-dax'>Total Revenue = 
VAR FilteredSales = FILTER(Sales, Sales[Year] = 2024)
RETURN
    SUMX(FilteredSales, Sales[Amount]) + SUMX(FilteredSales, Sales[Discount])
</code></pre>

<p>The filter is evaluated once, stored in FilteredSales, and reused. This pattern is especially powerful with complex filters or expensive functions.</p>

<h3>Aggregations and Composite Models</h3>
<p>As datasets grow, even optimized Import models can slow down. <strong>Aggregations</strong> provide a solution by creating summary tables that Power BI queries first, only drilling down to detailed data when necessary. This is the foundation of <strong>composite models</strong>, which combine Import, DirectQuery, and Dual storage modes in a single model.</p>

<p>Example: Your Sales fact table has 100 million rows of daily transactions. Users rarely need to analyze individual transactions—they typically view data by month or region. Create an aggregated table summarizing sales by Month and Region (reducing 100M rows to 5K rows). Configure a relationship such that when a user filters by Month or Region, Power BI queries the aggregation; if they drill down to individual transactions, Power BI switches to the detailed table via DirectQuery.</p>

<p>Setting up aggregations in Power BI Desktop:</p>
<ul>
<li><strong>Create an aggregated table</strong> in your data source or Power Query, summarizing facts by common dimensions.</li>
<li><strong>Import the aggregated table</strong> into Power BI with Dual storage mode.</li>
<li><strong>Set up relationships</strong> between aggregation and details on shared keys (e.g., Month, Region).</li>
<li><strong>In the aggregated table properties</strong>, specify summarization mappings (e.g., this column summarizes the revenue column from the detail table).</li>
<li><strong>Power BI automatically routes queries</strong> to the aggregation when possible, improving responsiveness dramatically.</li>
</ul>

<h3>Incremental Refresh</h3>
<p>For large tables that grow continuously, refreshing the entire dataset each time is wasteful. <strong>Incremental refresh</strong> loads only new or changed rows since the last refresh, dramatically reducing refresh time and data transfer.</p>

<p>To implement incremental refresh:</p>
<ul>
<li><strong>Create query parameters</strong> for RangeStart and RangeEnd dates in Power Query.</li>
<li><strong>Filter your table</strong> to include only rows where the date column falls within the range: <code>between RangeStart and RangeEnd</code>.</li>
<li><strong>Configure the refresh policy</strong> in Power BI Service: go to dataset settings and enable incremental refresh, specifying how many days of historical data to retain and how frequently to refresh.</li>
<li><strong>Power BI automatically manages parameters</strong>: on first refresh, it loads historical data; on subsequent refreshes, it appends only new rows.</li>
</ul>

<p>Power Query example for incremental refresh:</p>
<pre><code class='language-m'>let
    Source = Sql.Database(&quot;server&quot;, &quot;database&quot;),
    Sales = Source{[Schema=&quot;dbo&quot;, Item=&quot;Sales&quot;]}[Data],
    FilteredByDate = Table.SelectRows(Sales, 
        each [TransactionDate] &gt;= RangeStart 
        and [TransactionDate] &lt; RangeEnd)
in
    FilteredByDate
</code></pre>

<p>Incremental refresh turns a 30-minute daily refresh into a 2-minute refresh, freeing up resources and enabling more frequent updates.</p>

<h3>Putting It All Together: An Optimization Checklist</h3>
<ul>
<li><strong>Profile first:</strong> Run Performance Analyzer to identify slow visuals. Use DAX Studio to profile slow measures.</li>
<li><strong>Verify Vertipaq compression:</strong> Use Vertipaq Analyzer to ensure no column is unexpectedly large.</li>
<li><strong>Trim data:</strong> Remove unused columns and rows in Power Query.</li>
<li><strong>Review data types:</strong> Ensure numeric columns are the right type (whole number vs. decimal) and dates are typed as dates.</li>
<li><strong>Disable auto date/time:</strong> Create explicit date dimensions instead.</li>
<li><strong>Optimize DAX:</strong> Use variables to avoid repeated calculations. Test with DAX Studio.</li>
<li><strong>Consider aggregations:</strong> If you have millions of rows and slow queries, evaluate composite models with aggregations.</li>
<li><strong>Plan refresh strategy:</strong> Use incremental refresh for large growing tables instead of full refreshes.</li>
<li><strong>Retest and monitor:</strong> After optimizations, re-run Performance Analyzer to confirm improvement. Monitor refresh times and model size regularly.</li>
</ul>

<p>Performance optimization is iterative. Start with profiling to identify the real bottleneck, apply targeted fixes, and measure improvement. Often, removing unnecessary columns or optimizing a single DAX formula yields dramatic gains without architectural changes.</p>
"""

QUESTIONS = [
    (
        """Which diagnostic tool would you use to determine whether a slow visual is due to DAX query time or rendering time?""",
        [
            ("""Vertipaq Analyzer""", False),
            ("""Performance Analyzer in Power BI Desktop""", True),
            ("""Power Query Editor column profiling""", False),
            ("""DAX Studio alone without Power BI Desktop""", False)
        ],
        """Performance Analyzer breaks down visual execution time into DAX query time, rendering time, and other time. This breakdown shows where the delay originates. Vertipaq Analyzer shows model compression; DAX Studio profiles formula execution but requires separate setup."""
    ),
    (
        """You have a Sales table with 200 million transaction rows. Users typically analyze data at the month and region level, but occasionally drill down to individual transactions. Your refresh time has become unacceptable. Which optimization strategy best addresses this scenario?""",
        [
            ("""Convert the entire table to DirectQuery mode""", False),
            ("""Create a composite model with an aggregated table summarized by month and region, configured to route queries to the aggregation first, with drill-down to detailed transactions via DirectQuery""", True),
            ("""Remove all detail rows and keep only monthly summaries""", False),
            ("""Disable auto date/time to reduce model size""", False)
        ],
        """Composite models with aggregations allow Power BI to query summarized data for typical analysis and drill down to detail only when needed. This balances performance and flexibility. DirectQuery for the entire 200M row table would be slow. Removing detail rows loses analytical capability. Auto date/time alone won't solve the refresh problem."""
    ),
    (
        """A numeric column containing product prices is stored as Text. What is the immediate consequence for model performance?""",
        [
            ("""The column will not compress efficiently in Vertipaq, consuming significantly more memory than if it were a Decimal or Whole Number type""", True),
            ("""Relationships cannot be created from this column""", False),
            ("""DAX measures cannot reference this column""", False),
            ("""Performance Analyzer will show errors for this column""", False)
        ],
        """Text data compresses poorly in Power BI's Vertipaq engine compared to numeric types. Storing numbers as text wastes memory. While relationships and measures can technically work with text, the primary issue is compression efficiency and model size."""
    ),
    (
        """You want to optimize a slow DAX measure that filters sales by year, then calculates both revenue and discount totals, repeating the filter for each calculation. Which technique best improves this measure?""",
        [
            ("""Use SUMPRODUCT instead of SUMX""", False),
            ("""Replace the measure with a calculated column""", False),
            ("""Store the filter result in a variable and reference it multiple times in subsequent calculations""", True),
            ("""Convert the measure to DirectQuery storage mode""", False)
        ],
        """DAX variables evaluate their expression once and store the result, reusing it throughout the formula. This avoids recalculating the same filter. SUMPRODUCT and calculated columns don't address the issue. DirectQuery storage mode doesn't optimize the formula itself."""
    ),
    (
        """Your model has a Date table with several date hierarchies, but when you view the model diagram, you notice hidden tables have been created automatically. What setting likely caused this, and how should you correct it?""",
        [
            ("""Auto date/time is enabled; disable it in Options and create explicit hierarchies in your Date table instead""", True),
            ("""Query folding is creating hidden tables; disable it in Power Query settings""", False),
            ("""Relationships have bidirectional cross-filter enabled; set them all to single direction""", False),
            ("""Incremental refresh is creating hidden staging tables; this cannot be disabled""", False)
        ],
        """Power BI's auto date/time feature automatically creates hidden date hierarchies. While convenient, this consumes memory and can cause unexpected filter behavior. The solution is to disable auto date/time in File → Options → Current File → Data Load, then build explicit hierarchies in your own Date table."""
    ),
    (
        """A column containing customer IDs is stored as Whole Number type and has a cardinality of 5 million unique values. Why is this problematic, and what should you do?""",
        [
            ("""High-cardinality columns compress poorly; consider removing this column from the fact table if it's not needed for filtering or relationships. If required, ensure it's only used as a join key, not as an attribute for analysis""", True),
            ("""Whole Number type is too large; change it to Text""", False),
            ("""5 million unique values mean this column must be hidden from users""", False),
            ("""High cardinality requires incremental refresh to function""", False)
        ],
        """Columns with one unique value per row or very high cardinality don't compress well in Vertipaq. If customer IDs exist only as join keys, consider removing them from Import tables and using them only in DirectQuery tables or dimensional lookups. Text would compress even worse than Whole Number."""
    ),
    (
        """You are setting up incremental refresh for a 500 million row transaction table that grows by 10 million rows monthly. You configure RangeStart and RangeEnd parameters and filter the query to include only transactions within this range. What is the result of this configuration?""",
        [
            ("""The first refresh will load only the previous month of data, then each subsequent refresh appends only new rows since the last refresh""", False),
            ("""The first refresh loads all historical data up to a configured retention period, then subsequent refreshes append only new rows, dramatically reducing refresh time after the first load""", True),
            ("""All previous data will be deleted and replaced with only the data between RangeStart and RangeEnd""", False),
            ("""Incremental refresh will fail because the table is too large""", False)
        ],
        """Incremental refresh's first load captures historical data (often years of it) based on your retention policy, then subsequent refreshes append only new rows. The result is a fast steady-state refresh after the initial load. Data is not deleted; it accumulates within the retention window. Size doesn't prevent incremental refresh—it makes it essential."""
    ),
    (
        """You are using DAX Studio to test two versions of a complex measure. Version A runs in 800ms, and Version B runs in 150ms. What should you do next?""",
        [
            ("""Accept Version B as faster without further analysis""", False),
            ("""Check the Server Timings trace for both versions to understand which operations are expensive in Version A and confirm Version B's efficiency before deploying""", True),
            ("""Run Performance Analyzer to confirm the improvement in the actual report""", False),
            ("""Use Vertipaq Analyzer to verify the model's compression is optimal""", False)
        ],
        """Performance improvement in DAX Studio is promising, but the Server Timings trace reveals the underlying query plan and why one version is faster. Confirm efficiency at the formula level before deploying. Performance Analyzer will validate the end-to-end impact on reports, which is a good follow-up, but understanding the root cause first is essential."""
    )
]