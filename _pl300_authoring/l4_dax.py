"""
PL-300 Lesson 4: Create Model Calculations Using DAX
"""

LESSON_HTML = """
<h2>Create Model Calculations Using DAX</h2>

<h3>Measures vs. Calculated Columns</h3>
<p>
  Understanding when to use a measure versus a calculated column is fundamental to DAX authoring.
</p>
<p>
  <strong>Calculated Columns:</strong> Computed for each row at data refresh time. They consume memory because every value is stored.
  Use them when you need row-level logic that applies independently of filters (e.g., profit margin per transaction, age category).
</p>
<pre><code class='language-dax'>
Profit Margin = [Sales] - [Cost]
Age Category = IF([Age] &lt; 18, "Minor", IF([Age] &lt; 65, "Working Age", "Senior"))
</code></pre>
<p>
  <strong>Measures:</strong> Calculated on demand, dynamically responding to filter context. They use CPU at query time, not storage.
  Use them for aggregations or KPIs that need to respect dashboard filters (e.g., total sales, average margin by region).
</p>
<pre><code class='language-dax'>
Total Sales = SUM([Sales])
Avg Transaction = AVERAGE([Profit Margin])
</code></pre>

<h3>Calculated Tables</h3>
<p>
  Calculated tables are stored in memory after creation and behave like imported tables. They use DAX to generate data programmatically.
</p>
<p>
  <strong>Date Tables:</strong> Essential for time-intelligence functions. Use CALENDAR or CALENDARAUTO:
</p>
<pre><code class='language-dax'>
Date Table = CALENDAR(DATE(2020, 1, 1), DATE(2025, 12, 31))

-- Or let Power BI auto-detect:
Dates = CALENDARAUTO()
</code></pre>
<p>
  Enhance the date table with useful columns (Year, Month, Quarter, IsWeekend, etc.) as calculated columns within the table.
</p>

<h3>Row Context vs. Filter Context</h3>
<p>
  <strong>Row Context:</strong> Active when processing row-by-row operations in calculated columns or iterator functions.
  Inside a SUMX, the current row is visible.
</p>
<pre><code class='language-dax'>
-- In a calculated column: row context is active
Profit Per Transaction = [Sales] - [Cost]

-- In an iterator: row context iterates
Total Profit by Product = SUMX(
  ALL(Products),
  [Sales] - [Cost]  -- row context activated for each product
)
</code></pre>
<p>
  <strong>Filter Context:</strong> Applied by slicers, report filters, and the current cell position. Measures respond to filter context automatically.
</p>
<pre><code class='language-dax'>
Total Sales = SUM(Sales[Amount])
-- Automatically sums only rows matching active filters
</code></pre>
<p>
  Row context is <strong>transparent to measures</strong> unless you explicitly use iterators. This is why a measure placed in a calculated column may not behave as expected—the row context does not automatically cascade into the measure.
</p>

<h3>The CALCULATE Function</h3>
<p>
  CALCULATE modifies the filter context of an expression. It is one of the most powerful DAX functions.
</p>
<pre><code class='language-dax'>
-- Syntax:
Sales in Q1 = CALCULATE([Total Sales], MONTH(Dates[Date]) = 1)

-- Example with multiple filters:
Sales USA 2024 = CALCULATE(
  [Total Sales],
  Customers[Country] = "USA",
  YEAR(Dates[Date]) = 2024
)
</code></pre>
<p>
  CALCULATE overwrites existing filters for the columns/tables you specify, or adds new filter conditions.
</p>

<h3>Filter Manipulation Functions</h3>
<p>
  <strong>ALL:</strong> Removes all filters from a table or column, ignoring current slicer selections.
</p>
<pre><code class='language-dax'>
Total Sales All Regions = CALCULATE([Total Sales], ALL(Customers[Region]))
</code></pre>
<p>
  <strong>ALLSELECTED:</strong> Removes filters but preserves explicit selections made by the user (slicers).
</p>
<pre><code class='language-dax'>
Sales % of Selected = [Total Sales] / CALCULATE([Total Sales], ALLSELECTED())
</code></pre>
<p>
  <strong>REMOVEFILTERS:</strong> Removes filters from one or more columns, leaving others intact.
</p>
<pre><code class='language-dax'>
Sales Ignoring Product = CALCULATE([Total Sales], REMOVEFILTERS(Products))
</code></pre>
<p>
  <strong>FILTER:</strong> Creates a dynamic filter table passed to CALCULATE or iterators.
</p>
<pre><code class='language-dax'>
Sales of Top Products = CALCULATE(
  [Total Sales],
  FILTER(Products, [Total Sales] &gt; 50000)
)
</code></pre>

<h3>Iterator Functions</h3>
<p>
  Iterators loop through a table and apply a measure/expression to each row, accumulating results.
</p>
<p>
  <strong>SUMX:</strong> Sums an expression across a table.
</p>
<pre><code class='language-dax'>
Total Profit = SUMX(Sales, [Sales] * [Margin %])
-- Multiplies each row's sales by its margin, then sums
</code></pre>
<p>
  <strong>AVERAGEX:</strong> Averages an expression across a table.
</p>
<pre><code class='language-dax'>
Avg Discount = AVERAGEX(Sales, [Discount Amount])
</code></pre>
<p>
  <strong>RANKX:</strong> Ranks values within a table (useful for finding top 10, etc.).
</p>
<pre><code class='language-dax'>
Product Rank = RANKX(
  ALL(Products),
  [Total Sales],
  ,
  0  -- descending
)
</code></pre>

<h3>Time-Intelligence Functions</h3>
<p>
  Time-intelligence functions simplify year-over-year and period-to-date calculations. They require a marked date table.
</p>
<p>
  <strong>SAMEPERIODLASTYEAR:</strong> Shifts the date filter back one year.
</p>
<pre><code class='language-dax'>
Sales Last Year = CALCULATE(
  [Total Sales],
  SAMEPERIODLASTYEAR(Dates[Date])
)
</code></pre>
<p>
  <strong>TOTALYTD:</strong> Sums from the start of the year to the current date.
</p>
<pre><code class='language-dax'>
YTD Sales = TOTALYTD([Total Sales], Dates[Date])
</code></pre>
<p>
  <strong>DATESYTD:</strong> Returns a table of dates from year-start to current.
</p>
<pre><code class='language-dax'>
YTD Revenue = CALCULATE(
  [Total Sales],
  DATESYTD(Dates[Date])
)
</code></pre>
<p>
  <strong>DATEADD:</strong> Shifts dates forward or backward.
</p>
<pre><code class='language-dax'>
Sales 90 Days Ago = CALCULATE(
  [Total Sales],
  DATEADD(Dates[Date], -90, DAY)
)
</code></pre>

<h3>Variables with VAR/RETURN</h3>
<p>
  Variables improve readability and performance by storing intermediate calculations.
</p>
<pre><code class='language-dax'>
Sales Performance = 
  VAR CurrentSales = [Total Sales]
  VAR LastYearSales = [Sales Last Year]
  VAR Growth = (CurrentSales - LastYearSales) / LastYearSales
  RETURN
    IF(ISBLANK(LastYearSales), 0, Growth)
</code></pre>
<p>
  Variables are scoped to a single measure and are re-evaluated only when their dependencies change.
</p>

<h3>Quick Measures</h3>
<p>
  Power BI's Quick Measures wizard generates common DAX patterns without manual coding:
  Running Total, Year-over-Year Growth, Rank, Percentile, etc.
  While quick measures are not write-once, understanding their generated code helps you master advanced patterns.
</p>

<h3>Best Practices</h3>
<ul>
  <li>Use measures for KPIs and filters; use calculated columns for row-level attributes.</li>
  <li>Always define a date table before using time-intelligence functions.</li>
  <li>Avoid complex row context in measures—use iterators deliberately.</li>
  <li>Use variables to break down complex measures into readable steps.</li>
  <li>Test filter context impact on measures by dragging them into report visuals and adjusting slicers.</li>
</ul>
"""

QUESTIONS = [
    (
        """<strong>Question 1:</strong> When should you create a calculated column instead of a measure?""",
        [
            ("When you need a value to refresh dynamically based on report filters", False),
            ("When you need row-level logic that applies independently of filter context", True),
            ("When you want to reduce memory consumption in the data model", False),
            ("When you need to compute aggregations for KPIs", False),
        ],
        """Correct! Calculated columns compute once at refresh and apply row-by-row logic. Measures compute on demand and respond to filters. Use calculated columns for attributes (age category, profit margin per row). Use measures for KPIs (total sales, average margin by region)."""
    ),
    (
        """<strong>Question 2 (Code):</strong> Given a Sales table with columns [Amount], [Quantity], [Discount], analyze this DAX measure:
<pre><code class='language-dax'>
Net Revenue = SUMX(Sales, ([Amount] - [Discount]) * [Quantity])
</code></pre>
What happens when you place this measure in a report filtered by Region?""",
        [
            ("The measure ignores the Region filter and sums all sales globally", False),
            ("The measure sums only rows from the selected Region, computing net revenue for each row first", True),
            ("The measure returns an error because [Discount] and [Quantity] are not aggregated", False),
            ("The SUMX function fails in filter context", False),
        ],
        """Correct! SUMX iterates the Sales table, applying the expression to each row within the current filter context. The Region filter narrows the iteration to matching rows only. The expression (Amount - Discount) × Quantity is computed per row, then summed."""
    ),
    (
        """<strong>Question 3:</strong> What is the key difference between filter context and row context?""",
        [
            ("Row context is faster than filter context", False),
            ("Filter context is applied by slicers and column placement; row context iterates through table rows", True),
            ("Row context only applies to calculated columns", False),
            ("Filter context and row context are the same thing", False),
        ],
        """Correct! Filter context is set by slicer selections and report placement (e.g., Region slicer). Row context is active when processing row-by-row operations, like in calculated columns or inside iterator functions (SUMX, AVERAGEX). Measures respond to filter context automatically."""
    ),
    (
        """<strong>Question 4 (Code):</strong> You have a Dates table marked as a date table. What does this measure return?
<pre><code class='language-dax'>
YoY Growth = 
  VAR CurrentYearSales = [Total Sales]
  VAR PriorYearSales = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Dates[Date]))
  RETURN
    (CurrentYearSales - PriorYearSales) / PriorYearSales
</code></pre>
What is the purpose of SAMEPERIODLASTYEAR?""",
        [
            ("It adds one year to all dates in the filter context", False),
            ("It shifts the date filter back by one year, comparing the same calendar period", True),
            ("It returns only dates from the prior year", False),
            ("It calculates the difference between two dates", False),
        ],
        """Correct! SAMEPERIODLASTYEAR shifts the active date filter back by 12 months. If the report shows January 2024, SAMEPERIODLASTYEAR selects January 2023. This allows year-over-year comparisons with matching periods."""
    ),
    (
        """<strong>Question 5 (Code):</strong> Consider this DAX expression applied to a Product dimension:
<pre><code class='language-dax'>
Sales Excluding Selected = CALCULATE(
  [Total Sales],
  ALL(Products)
)
</code></pre>
If the report has a Product slicer with "Widget" selected, what does this measure return?""",
        [
            ("Sales for only the Widget product", False),
            ("Sales for all products, ignoring the Widget selection", True),
            ("Sales for all products except Widget", False),
            ("The measure returns an error", False),
        ],
        """Correct! ALL(Products) removes all filters from the Products table. Even though "Widget" is selected in the slicer, CALCULATE ignores that filter and sums [Total Sales] across all products. This is useful for calculating percentages of totals."""
    ),
    (
        """<strong>Question 6:</strong> Why should you create a calculated table for dates instead of using the date column from a transaction table?""",
        [
            ("Calculated date tables have better performance", False),
            ("A standalone date table ensures continuous dates (no gaps) and supports time-intelligence functions", True),
            ("Calculated tables use less memory than imported tables", False),
            ("Transaction date columns cannot be used in DAX formulas", False),
        ],
        """Correct! A dedicated date table (created with CALENDAR or CALENDARAUTO) has no gaps, even for dates with no transactions. Time-intelligence functions (TOTALYTD, SAMEPERIODLASTYEAR) require a complete, marked date table."""
    ),
    (
        """<strong>Question 7 (Code):</strong> Study this DAX formula applied at the product level:
<pre><code class='language-dax'>
Product Rank = RANKX(
  ALL(Products),
  [Total Sales],
  ,
  0
)
</code></pre>
What does the 0 parameter mean, and what happens if you change it to 1?""",
        [
            ("0 = ascending order, 1 = descending order", False),
            ("0 = descending order (highest sales = rank 1), 1 = ascending order (lowest sales = rank 1)", True),
            ("0 and 1 both produce the same result", False),
            ("0 = exclude blanks, 1 = include blanks", False),
        ],
        """Correct! The fourth parameter of RANKX controls sort order: 0 = descending (rank 1 for highest sales), 1 = ascending (rank 1 for lowest sales). In business, you typically use 0 to rank best-performing products first."""
    ),
    (
        """<strong>Question 8:</strong> Which of the following is a best practice when authoring DAX measures?""",
        [
            ("Always nest multiple CALCULATE functions to avoid filter conflicts", False),
            ("Use variables to store intermediate calculations, improving readability and allowing reuse", True),
            ("Avoid using time-intelligence functions; build date filtering manually with CALCULATE", False),
            ("Create calculated columns instead of measures to minimize CPU usage at query time", False),
        ],
        """Correct! Variables (VAR/RETURN) make measures easier to read and debug. Each variable is computed only once and can be referenced multiple times. This is far cleaner than deeply nested functions. Time-intelligence functions and measures are designed to work together efficiently."""
    ),
]