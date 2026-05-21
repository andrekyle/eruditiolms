QUESTIONS = [
    # Prepare the Data (7 questions)
    (
        """You are connecting to a SQL Server database that contains millions of historical records. You need to import only the data from the last 2 years to optimize model performance. Which approach should you use?""",
        [
            ("""Import all data into Power BI and use DAX to filter to the last 2 years""", False),
            ("""Apply a filter in Power Query to exclude older records before loading into Power BI""", True),
            ("""Load all data and manually delete records in the Power Query editor""", False),
            ("""Use a Python script to pre-filter the data before connecting to Power BI""", False),
        ],
        """Power Query is the appropriate place to filter data at the source. This reduces the amount of data loaded into the model and improves refresh times. Filtering in Power BI or external tools is less efficient than filtering during the ETL process.""",
    ),
    (
        """You need to connect to multiple Excel files stored in a SharePoint folder. The number of files changes weekly. What is the best data source connector to use?""",
        [
            ("""Connect to each file individually using the Excel connector""", False),
            ("""Use the Folder connector to dynamically reference all Excel files in the SharePoint location""", True),
            ("""Download all files locally and combine them manually""", False),
            ("""Use the Web connector to scrape data from the SharePoint page""", False),
        ],
        """The Folder connector automatically detects and combines all files in a specified location, making it ideal for dynamic scenarios where file lists change. This eliminates manual maintenance.""",
    ),
    (
        """<pre><code class='language-m'>let
    Source = Csv.Document(file),
    Header = Table.PromoteHeaders(Source),
    Transform = Table.TransformColumnTypes(Header, {{"Sales"", type number}, {""Date"", type date}})
in
    Transform</code></pre>
    What will this M query do when executed?""",
        [
            ("""It will fail because the syntax is incorrect""", False),
            ("""It will load a CSV file, set the first row as headers, and convert Sales and Date columns to appropriate data types""", True),
            ("""It will load the file but skip the header row""", False),
            ("""It will create a new CSV file with the transformed data""", False),
        ],
        """This M query demonstrates the fundamental ETL pattern in Power Query: load, promote headers, and transform column types. The TransformColumnTypes function ensures data integrity at the source.""",
    ),
    (
        """You have a large dataset of daily sales transactions. Should you use Import mode or DirectQuery mode for your model?""",
        [
            ("""DirectQuery, to ensure real-time data but sacrifice query performance""", False),
            ("""Import mode, to allow analysis with fast queries and DAX calculations""", True),
            ("""DirectQuery for better compression""", False),
            ("""Dual mode to store some data and query others directly""", False),
        ],
        """Import mode is suitable for historical transaction data. It compresses data efficiently, enables all DAX features, and provides fast query response. DirectQuery is better for large, frequently-updated data that must stay current.""",
    ),
    (
        """Your Power BI dataset refreshes daily, but sometimes the refresh fails silently without notification. You want to monitor these failures. What should you configure?""",
        [
            ("""Enable Power Query tracing in Power BI Desktop""", False),
            ("""Set up a refresh schedule and configure email notifications in the Power BI Service""", True),
            ("""Use a gateway with automatic retry""", False),
            ("""Switch to a different data source""", False),
        ],
        """Power BI Service refresh settings allow you to schedule refreshes and configure email notifications for failures. This ensures you're immediately aware of any data loading issues and can troubleshoot them.""",
    ),
    (
        """In Power Query, you have a column of ZIP codes stored as numbers. When you load to Power BI, they display incorrectly (missing leading zeros). How should you have prevented this?""",
        [
            ("""Set the column data type to Text in Power Query before loading""", True),
            ("""Format the column as text in Power BI Desktop""", False),
            ("""Use a DAX formula to add leading zeros""", False),
            ("""Export the data and re-import with correct formatting""", False),
        ],
        """Setting the data type to Text in Power Query ensures the leading zeros are preserved during import. Formatting in Power BI only changes display, not the underlying values. Data type transformation must happen in Power Query.""",
    ),
    (
        """You need to create a dependency where Query B pulls data from Query C, which depends on Query A. In Power Query, does the order of query definitions matter?""",
        [
            ("""Yes, you must define A first, then C, then B in that exact order""", False),
            ("""No, Power Query automatically resolves dependencies regardless of definition order""", True),
            ("""Yes, you must define all queries in alphabetical order""", False),
            ("""The order depends on your data source type""", False),
        ],
        """Power Query automatically resolves query dependencies based on the references between queries, not their definition order. You can define queries in any sequence, and Power Query will execute them in the correct order.""",
    ),

    # Model the Data (7 questions)
    (
        """You are designing a star schema for a retail company with Sales facts, Products, Stores, and Dates dimensions. Which dimension should have a many-to-one relationship to the Sales table?""",
        [
            ("""All dimensions should have a many-to-one relationship to Sales (each product/store/date can have many sales)""", True),
            ("""Sales should have a many-to-one relationship to each dimension""", False),
            ("""Dimensions should have a one-to-one relationship with Sales""", False),
            ("""No relationships are needed in a star schema""", False),
        ],
        """In a star schema, dimensions have a many-to-one relationship with the fact table. Many fact records (sales transactions) relate to a single dimension record (product, store, or date). This is the standard design for dimensional models.""",
    ),
    (
        """You have created a one-to-many relationship between Department and Employee tables. However, you notice that sales figures are inflated when you create visuals using both tables. What could be the cause?""",
        [
            ("""The relationship direction is wrong; it should be many-to-one""", False),
            ("""The relationship is creating a Cartesian product due to missing filter propagation""", False),
            ("""The relationship has a one-to-many direction when it should be many-to-many""", True),
            ("""The data source has duplicate records""", False),
        ],
        """The relationship direction (from the "one" side to the "many" side) is critical. An incorrectly configured many-to-many relationship or missing filter propagation can cause duplicate rows and inflated aggregates. Verify the relationship cardinality and cross-filter direction.""",
    ),
    (
        """<pre><code class='language-dax'>TotalSales = SUMX(
    ALL(DimDate),
    [Sales Amount]
)</code></pre>
    What issue does this DAX formula have?""",
        [
            ("""It will calculate the sum correctly with no issues""", False),
            ("""It uses ALL(DimDate) which removes all filters on the Date dimension, making it sum all sales regardless of the selected date""", True),
            ("""It is missing the FILTER function""", False),
            ("""The SUMX function requires three arguments""", False),
        ],
        """The ALL() function removes filters, so this measure sums all sales across all dates regardless of slicing context. This is likely a logic error. If you want to filter to a specific date range, use FILTER() instead of ALL().""",
    ),
    (
        """<pre><code class='language-dax'>YoYGrowth = 
DIVIDE(
    [CurrentYearSales] - [PriorYearSales],
    [PriorYearSales],
    0
)</code></pre>
    This measure compares sales year-over-year. If you place this in a visual filtered to Q3 2024, what will it calculate?""",
        [
            ("""Sales growth from Q3 2023 to Q3 2024""", False),
            ("""Sales growth from 2023 to 2024 for the entire year, not respecting the Q3 filter""", False),
            ("""It depends on how CurrentYearSales and PriorYearSales are defined; if they use context-aware date logic, it will show Q3 2024 vs Q3 2023 growth""", True),
            ("""It will return an error because the measure is ambiguous""", False),
        ],
        """The result depends on how the component measures (CurrentYearSales, PriorYearSales) are defined. If they use time intelligence functions like CALCULATE with DATEADD, they will respect the Q3 filter and compare Q3-to-Q3 growth correctly.""",
    ),
    (
        """In a Power BI model, you have a Date table and a Sales table with a relationship on Sales[OrderDate] &lt;-&gt; Date[DateKey]. What is the minimum cardinality requirement?""",
        [
            ("""Many-to-one (many sales can share the same date)""", True),
            ("""One-to-one (each sale must have a unique date)""", False),
            ("""Many-to-many (each sale can relate to multiple dates)""", False),
            ("""No cardinality requirement in Power BI""", False),
        ],
        """Sales transactions occur on the same dates, so many orders will share a single date. The relationship must be many-to-one: many sales facts reference one date dimension record. This is the fundamental pattern for fact-to-dimension relationships.""",
    ),
    (
        """You need to show revenue by product category with a sub-row showing the top 3 products within each category. Should you use a Calculated Column, Calculated Table, or a Measure?""",
        [
            ("""Calculated Column to pre-compute the rank of each product""", False),
            ("""A Measure with RANKX to calculate the top 3 during visual rendering""", False),
            ("""You must handle this through visual grouping and sorting, not through DAX""", True),
            ("""A Calculated Table to pre-filter the data to top 3 products""", False),
        ],
        """Matrix visuals natively support hierarchical display and sorting. Configure the visual to show categories and products, then sort products by revenue descending. For dynamic top-N filtering by category, use a Measure with conditional logic rather than a Calculated Column.""",
    ),
    (
        """<pre><code class='language-dax'>Calculation = CALCULATE(
    SUM(Sales[Amount]),
    FILTER(ALL(Sales), Sales[Status] = ""Completed"")
)</code></pre>
    What will this formula calculate?""",
        [
            ("""The sum of all sales regardless of their status""", False),
            ("""The sum of sales where Status equals 'Completed', ignoring all other filters on the Sales table""", True),
            ("""The sum of sales with Completed status, while respecting other existing filters""", False),
            ("""It will produce an error because CALCULATE requires FILTER syntax""", False),
        ],
        """CALCULATE with ALL removes all filters on a table, then FILTER reapplies only the specified condition. This measure sums only Completed sales, ignoring any other filters on the Sales table (date, region, etc.).""",
    ),

    # Visualize and Analyze (7 questions)
    (
        """You need to visualize product sales trends over time with monthly granularity. Sales data varies from 10,000 to 500,000 units. Which chart type is most appropriate?""",
        [
            ("""Pie chart to show proportion of sales each month""", False),
            ("""Line chart with months on the X-axis to show trends clearly""", True),
            ("""Scatter plot to show the relationship between sales and month""", False),
            ("""KPI card to show the total sales""", False),
        ],
        """Line charts excel at showing trends over time. The X-axis naturally represents time periods, and the line clearly shows upward or downward movement. Pie charts show composition, not trends. Scatter plots show relationships between two continuous variables.""",
    ),
    (
        """You have a monthly sales table and want to highlight months where sales exceeded the annual average. What Power BI feature should you use?""",
        [
            ("""Conditional formatting with a rule that colors cells exceeding the average""", True),
            ("""A measure to calculate the exception and filter the data""", False),
            ("""Add a reference line manually at the average value""", False),
            ("""Create a separate table of above-average months""", False),
        ],
        """Conditional formatting in Power BI tables/matrices allows you to set rules (e.g., 'values greater than X') and apply colors or data bars automatically. This visually highlights outliers without creating additional queries.""",
    ),
    (
        """You want to allow users to compare sales between selected months by clicking on report visuals. The click selections should update all other visuals on the page. What Power BI feature enables this?""",
        [
            ("""Bookmarks to save different views of the data""", False),
            ("""Drillthrough to navigate to a detailed page""", False),
            ("""Slicers to filter multiple visuals simultaneously""", True),
            ("""Page-level filters that persist across the entire report""", False),
        ],
        """Slicers are the standard tool for cross-filtering. When a user selects a slicer value (or multiple values), all connected visuals update to show data for those selections. This creates interactive exploration without manual page navigation.""",
    ),
    (
        """You have a report with sensitive financial data. You want some users to see only data for their own region while other users see all regions. What approach should you use?""",
        [
            ("""Create separate reports for each region""", False),
            ("""Use Power BI Row-Level Security (RLS) with a role that filters data based on the logged-in user's region""", True),
            ("""Add a slicer that users manually set to their region""", False),
            ("""Use bookmarks to save region-specific views""", False),
        ],
        """Row-Level Security (RLS) in the Power BI Service enforces data filtering at the row level based on the authenticated user's identity. This is the secure, scalable way to provide role-based access control without manual slicer management.""",
    ),
    (
        """You use the AI Insights feature (Key Influencers visual) on your Sales amount data. What type of insight does this feature typically provide?""",
        [
            ("""It forecasts future sales values using time-series analysis""", False),
            ("""It identifies which attributes (e.g., product category, region) have the strongest influence on changes in sales""", True),
            ("""It clusters customers into similar groups for segmentation""", False),
            ("""It compares actual sales against a statistical benchmark""", False),
        ],
        """The Key Influencers visual uses AI to determine which categorical or numerical factors most strongly correlate with or drive the selected measure. It answers 'What influences this metric?' rather than 'What will happen next?'""",
    ),
    (
        """You create a visual showing revenue by product and region. You want users to click on a product to drill to a detailed page showing that product's transactions. How should you configure this?""",
        [
            ("""Set up a bookmark to navigate to the transaction page""", False),
            ("""Enable drillthrough on the Product column to pass the Product filter to the target page""", True),
            ("""Add a slicer for products that links to the transaction page""", False),
            ("""Export the data and manually create a hyperlink""", False),
        ],
        """Drillthrough allows users to right-click on a visual element and navigate to a target page while passing filter context (e.g., Product ID). Configure the target page to receive the drillthrough filter from the source visual.""",
    ),
    (
        """You format a column in a table visual with a gradient color scale (white = low values, green = high values). When you publish to the Power BI Service, the formatting appears incorrect on a mobile device. Why might this happen?""",
        [
            ("""Mobile doesn't support color scales in table visuals; use a different visual type""", False),
            ("""The gradient rendering may vary based on device screen capabilities, but the formatting should persist""", True),
            ("""You must separately configure mobile formatting in the Service""", False),
            ("""Conditional formatting is not supported on mobile devices at all""", False),
        ],
        """Conditional formatting, including color scales, should render on mobile devices, though visual appearance may vary due to screen resolution, brightness, and color depth differences. This is typically a display variation, not a missing feature.""",
    ),

    # Deploy and Maintain (4 questions)
    (
        """Your organization has data that must comply with GDPR regulations. Some users should only see data for their country. Where should you implement this access control in Power BI?""",
        [
            ("""In Power BI Desktop with filters on each visual""", False),
            ("""In the Power BI Service using Row-Level Security (RLS) roles assigned to users""", True),
            ("""In the data source by pre-filtering data before import""", False),
            ("""On the published app by restricting app user permissions""", False),
        ],
        """Row-Level Security in the Power BI Service is the authorized enforcement point for data access control. It ensures that regardless of how a user accesses the report (web, mobile, embedded), they only see data their role permits. Data-source filtering is inflexible; Desktop filters are not secure.""",
    ),
    (
        """You publish a Power BI report to a workspace and want to share it with 50 stakeholders. You want to control who can see it and who can edit it. What should you do?""",
        [
            ("""Create an app from the workspace and assign users with appropriate permissions (Viewer, Editor, etc.)""", True),
            ("""Share the workspace directly with all 50 users""", False),
            ("""Email the .pbix file to each user""", False),
            ("""Embed the report on an external website""", False),
        ],
        """Power BI apps provide the standard way to distribute reports with granular permission controls (Viewer, Editor, Contributor). Apps also provide a curated interface separate from the workspace. Direct workspace sharing is less managed; file sharing outside Power BI lacks governance.""",
    ),
    (
        """Your Power BI dataset uses data from an on-premises SQL Server. The scheduled refresh in the Power BI Service keeps failing. What is the most likely requirement?""",
        [
            ("""Upgrade your SQL Server to the latest version""", False),
            ("""Install and configure an On-premises Data Gateway, then configure the gateway connection in the dataset settings""", True),
            ("""Move the SQL Server data to the cloud""", False),
            ("""Use DirectQuery mode instead of Import mode""", False),
        ],
        """The On-premises Data Gateway acts as a secure bridge between the Power BI Service (cloud) and on-premises data sources. It must be installed and configured for cloud refreshes to access local data. DirectQuery is an alternative but still requires the gateway for security.""",
    ),
    (
        """You have a high-traffic Power BI app with 500 concurrent users. Refresh performance has degraded. Which strategies should you consider to improve performance? (Select the most impactful)""",
        [
            ("""Reduce the number of columns in the dataset to decrease file size and refresh time""", False),
            ("""Implement aggregations or use DirectQuery for large fact tables to reduce data movement during refresh""", True),
            ("""Increase the refresh frequency to ensure data freshness""", False),
            ("""Ask users to clear their browser cache before opening reports""", False),
        ],
        """Aggregations (summary tables for fast queries) and DirectQuery (query on-demand instead of storing all data) reduce the refresh burden on large models. These architectural changes improve both refresh performance and query responsiveness. Increasing refresh frequency worsens performance. Cache clearing is unrelated to server-side performance.""",
    ),
]