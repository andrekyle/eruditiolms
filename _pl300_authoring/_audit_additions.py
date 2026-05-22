"""Audit-driven additions layered on top of the original PL-300 lesson modules.

Closes gaps identified by the 5-agent audit against the official Microsoft
Study Guide for Exam PL-300 (skills measured as of April 20, 2026).

LESSON_ADDITIONS[module_name]      -> extra HTML appended to LESSON_HTML.
QUESTION_ADDITIONS[module_name]    -> extra (qtype, qhtml, opts, fb) tuples
                                       appended to that module's QUESTIONS.
FINAL_EXAM_ADDITIONS               -> extra questions appended to the final.
"""

# ---------------------------------------------------------------------------
# Lesson 1 — DirectLake gap
# ---------------------------------------------------------------------------
L1_ADDITION = """
<h2>Additional Study Guide Topics</h2>

<h3>DirectLake storage mode (Microsoft Fabric)</h3>
<p><strong>DirectLake</strong> is a third storage option (alongside Import and DirectQuery) introduced with Microsoft Fabric. It queries Delta-Parquet files directly from <em>OneLake</em> without importing data into the semantic model and without falling back to DirectQuery's per-query latency. Use DirectLake when:</p>
<ul>
  <li>Your data already lives in a Fabric lakehouse or warehouse and is stored as Delta tables.</li>
  <li>You need near-real-time freshness without scheduled refresh.</li>
  <li>Datasets are too large to fit comfortably in Import mode (multi-GB or larger).</li>
  <li>You want the in-memory query performance of Import without the data duplication.</li>
</ul>
<p>DirectLake falls back to DirectQuery automatically when a query exceeds the capacity guard-rails (for example, very high column cardinality or unsupported transformations). Prefer DirectLake over DirectQuery when your data is in OneLake; prefer DirectQuery when data lives in an external source such as Snowflake or Azure SQL.</p>
"""

# ---------------------------------------------------------------------------
# Lesson 2 — Group By, semi-structured, fact/dimension, ref vs duplicate
# ---------------------------------------------------------------------------
L2_ADDITION = """
<h2>Additional Study Guide Topics</h2>

<h3>Group and aggregate rows</h3>
<p>The Power Query <strong>Group By</strong> transformation summarises a table by one or more columns and lets you aggregate the remaining columns (Sum, Average, Min, Max, Count Rows, Count Distinct, or All Rows). Use it to roll detail rows up to a coarser grain before loading &mdash; for example, collapsing 10 million daily order lines into one row per product per month for a dashboard. <em>Basic</em> grouping aggregates a single column; <em>Advanced</em> grouping lets you add multiple aggregations in one step.</p>

<h3>Convert semi-structured data to a table</h3>
<p>JSON, XML, and nested record/list columns are very common from REST APIs and document stores. In Power Query:</p>
<ul>
  <li>Right-click the column with the nested <em>Record</em> and choose <strong>Expand</strong> to promote its fields to columns.</li>
  <li>For nested <em>Lists</em>, choose <strong>Expand to New Rows</strong> to fan the list out into multiple rows, then expand the resulting records.</li>
  <li>Use <code>Json.Document</code> or <code>Xml.Tables</code> against a text/binary column when the source returns raw text.</li>
</ul>
<p>The goal is always to land a flat, tabular shape with explicit column data types before loading.</p>

<h3>Create fact tables and dimension tables (star schema)</h3>
<p>For Power BI to perform well, shape your model as a <strong>star schema</strong>: one or more <em>fact</em> tables surrounded by <em>dimension</em> tables.</p>
<ul>
  <li><strong>Fact tables</strong> hold the numeric measures and foreign keys (e.g. <code>FactSales</code> with <code>ProductKey</code>, <code>DateKey</code>, <code>CustomerKey</code>, <code>Quantity</code>, <code>Amount</code>).</li>
  <li><strong>Dimension tables</strong> hold the descriptive attributes you slice by (e.g. <code>DimProduct</code>, <code>DimCustomer</code>, <code>DimDate</code>).</li>
</ul>
<p>Build dimensions by reducing the source detail to distinct attribute rows and assigning a surrogate key. Star schemas compress better than flat tables, evaluate DAX faster, and produce cleaner reports than snowflake or single-table designs.</p>

<h3>Reference vs duplicate queries &mdash; impact</h3>
<p><strong>Duplicate</strong> creates an independent copy of the query and its full step history; future changes to the original do not flow through. <strong>Reference</strong> creates a new query that starts from the output of the original, so changes to the original ripple into every referencing query. Prefer <em>Reference</em> for shared cleansing logic (one source of truth) and disable <em>Enable Load</em> on the upstream reference so it does not bloat the model.</p>
"""

# ---------------------------------------------------------------------------
# Lesson 3 — Calculated columns use cases
# ---------------------------------------------------------------------------
L3_ADDITION = """
<h2>Additional Study Guide Topics</h2>

<h3>Calculated columns vs calculated tables &mdash; when to use which</h3>
<p>A <strong>calculated column</strong> stores a per-row value computed in DAX at refresh time, materialised into the model. Use one when:</p>
<ul>
  <li>You need a row-level attribute to <em>slice or filter by</em> (e.g. an Age Band, a Profit Margin %% bucket, a Fiscal Period label).</li>
  <li>The value depends on row context that a measure cannot reproduce cleanly.</li>
  <li>You need the value evaluated at refresh time rather than re-computed on every visual interaction.</li>
</ul>
<p>Prefer a <strong>measure</strong> when the value is an aggregation that responds to filter context (totals, ratios, time-intelligence). Prefer a <strong>calculated table</strong> (e.g. <code>CALENDAR()</code>, <code>SUMMARIZE()</code>) when you need a new whole table that does not exist in the source &mdash; most commonly a Date dimension.</p>
<p>Example calculated columns:</p>
<pre><code>Profit Margin % = DIVIDE(Sales[Amount] - Sales[Cost], Sales[Amount])
Age Band       = SWITCH(TRUE(),
                        Customer[Age] &lt; 25, "Under 25",
                        Customer[Age] &lt; 45, "25-44",
                        Customer[Age] &lt; 65, "45-64",
                                            "65+")</code></pre>
"""

# ---------------------------------------------------------------------------
# Lesson 4 — Semi-additive, calculation groups, statistical functions
# ---------------------------------------------------------------------------
L4_ADDITION = """
<h2>Additional Study Guide Topics</h2>

<h3>Basic statistical functions</h3>
<p>Beyond <code>SUM</code> and <code>AVERAGE</code>, DAX provides a full set of aggregation primitives for analytical reporting:</p>
<ul>
  <li><code>MIN</code> / <code>MAX</code> &mdash; smallest / largest value in a column.</li>
  <li><code>COUNT</code> / <code>COUNTA</code> / <code>COUNTROWS</code> / <code>DISTINCTCOUNT</code> &mdash; counting variants.</li>
  <li><code>STDEV.S</code> / <code>STDEV.P</code> / <code>VAR.S</code> / <code>VAR.P</code> &mdash; sample and population dispersion.</li>
  <li><code>MEDIAN</code> / <code>PERCENTILE.INC</code> / <code>PERCENTILE.EXC</code> &mdash; distribution-aware measures.</li>
</ul>
<p>Each has an <em>X</em>-suffixed iterator counterpart (<code>MINX</code>, <code>MAXX</code>, <code>COUNTX</code>, etc.) when you need to evaluate an expression per row of a table.</p>

<h3>Semi-additive measures</h3>
<p>Some measures should not be summed across time &mdash; for example account <em>Balances</em>, <em>Inventory On Hand</em>, or daily <em>Headcount</em>. Adding January and February balances together produces a meaningless number. These are called <strong>semi-additive</strong>: additive across non-date dimensions but not across the Date dimension. Common patterns:</p>
<pre><code>Closing Balance =
  CALCULATE(SUM(Finance[Balance]), LASTDATE('Date'[Date]))

Opening Balance =
  CALCULATE(SUM(Finance[Balance]), FIRSTDATE('Date'[Date]))

Avg Daily Inventory =
  AVERAGEX(VALUES('Date'[Date]), [Inventory On Hand])</code></pre>

<h3>Calculation groups</h3>
<p><strong>Calculation groups</strong> (authored in Tabular Editor or in Power BI Desktop's model view) let you define a reusable set of <em>calculation items</em> &mdash; for example <em>Current</em>, <em>YTD</em>, <em>PY</em>, <em>YoY %</em>, <em>YoY $</em> &mdash; that apply to any measure on the model. Instead of writing 50 time-intelligence variants by hand, you write one set of items and pivot them in a slicer or column. This dramatically reduces the number of measures you maintain and keeps formatting consistent across the report. Calculation groups are essential for enterprise-scale semantic models.</p>
"""

# ---------------------------------------------------------------------------
# Lesson 6 — Copilot, paginated reports, visual calculations (DAX)
# ---------------------------------------------------------------------------
L6_ADDITION = """
<h2>Additional Study Guide Topics</h2>

<h3>Copilot in Power BI reports</h3>
<p>Copilot for Power BI accelerates report authoring when your tenant has Fabric or Premium capacity available. Three Copilot capabilities are explicitly in scope for PL-300:</p>
<ul>
  <li><strong>Create a narrative visual with Copilot</strong> &mdash; add a Smart Narrative visual and let Copilot generate the executive summary text from the underlying semantic model. The narrative re-evaluates as filters and slicers change.</li>
  <li><strong>Use Copilot to create a new report page</strong> &mdash; from the Copilot pane, prompt "Create a page that shows sales by region with year-over-year comparison" and Copilot lays out visuals on a new page.</li>
  <li><strong>Use Copilot to suggest content for a new report page</strong> &mdash; Copilot inspects the model, suggests relevant topics, and proposes which visuals to add for the audience you specify.</li>
</ul>
<p>Always review Copilot-generated DAX, narratives, and visuals: it relies on the model metadata, so clear table/column names, descriptions, and synonyms greatly improve output quality.</p>

<h3>When to use a paginated report</h3>
<p><strong>Paginated reports</strong> (.rdl, authored in Power BI Report Builder) are designed for pixel-perfect, print-ready output rather than interactive exploration. Choose a paginated report when you need:</p>
<ul>
  <li>Multi-page documents with consistent headers/footers and page numbering (invoices, statements, regulatory filings).</li>
  <li>Exports to PDF, Word, or Excel that preserve exact layout across thousands of rows.</li>
  <li>Parameter-driven subscriptions that mail one PDF per region or customer.</li>
</ul>
<p>Choose a <em>standard Power BI report</em> for interactive dashboards, drill-through, and exploration.</p>

<h3>Visual calculations using DAX</h3>
<p><strong>Visual calculations</strong> are DAX expressions defined on the visual itself rather than on the semantic model. They operate over the visual's already-aggregated rows and have access to special functions such as <code>RUNNINGSUM</code>, <code>MOVINGAVERAGE</code>, <code>PREVIOUS</code>, and <code>COLLAPSE</code>. Use them for "last-mile" calculations &mdash; running totals, period-over-period deltas, or rank-within-visual &mdash; that you do not want to materialise as model measures. Visual calculations live and die with the visual, simplifying maintenance for one-off analytics.</p>
"""

# ---------------------------------------------------------------------------
# Lesson 7 — Export, personalization, auto page refresh
# ---------------------------------------------------------------------------
L7_ADDITION = """
<h2>Additional Study Guide Topics</h2>

<h3>Configure export settings</h3>
<p>Report authors control what consumers can export. In <strong>File &rarr; Options and settings &rarr; Options &rarr; Report settings</strong> (and the matching tenant-level switches in the Power BI Admin Portal), you can enable or disable:</p>
<ul>
  <li>Export to <strong>PDF</strong>, <strong>PowerPoint</strong>, and <strong>image</strong>.</li>
  <li>Export <strong>summarized data</strong> (post-aggregation) versus <strong>underlying data</strong> (row-level).</li>
  <li>Export to <strong>.xlsx</strong> with <em>live connection</em>, which lets analysts continue exploring in Excel.</li>
</ul>
<p>Disable underlying-data export on sensitive reports, and pair with sensitivity labels to enforce protection on the exported file.</p>

<h3>Enable personalization (including personalized visuals)</h3>
<p>Turn on <strong>Personalize visuals</strong> in <em>Format &rarr; Report settings</em> so consumers can change a visual's type, swap measures, switch fields, and save their preferred view as a <em>personal bookmark</em>. Personalisation lives in the Power BI Service per user and does not modify the published report for other consumers. This empowers business users to self-serve without raising change requests.</p>

<h3>Configure automatic page refresh</h3>
<p>For operational dashboards that must reflect near-real-time data, enable <strong>Automatic page refresh</strong> on the page formatting pane. Two refresh types are available:</p>
<ul>
  <li><strong>Fixed interval</strong> &mdash; refresh every N seconds/minutes; available for any storage mode but tenant admins enforce a minimum interval.</li>
  <li><strong>Change detection</strong> &mdash; only refresh when a designated measure changes; only available for DirectQuery sources and requires Premium capacity.</li>
</ul>
<p>Automatic page refresh is incompatible with Import mode at sub-minute intervals; pair it with DirectQuery, DirectLake, or a Real-Time dataset.</p>
"""

# ---------------------------------------------------------------------------
# Lesson 9 — Item-level permissions, sensitivity labels, dashboards
# ---------------------------------------------------------------------------
L9_ADDITION = """
<h2>Additional Study Guide Topics</h2>

<h3>Configure item-level access</h3>
<p>Workspace roles (Admin, Member, Contributor, Viewer) grant blanket access to <em>everything</em> in a workspace. When you need to share a specific report, dashboard, or semantic model with a narrower audience &mdash; without making the user a workspace member &mdash; use <strong>item-level permissions</strong>. On the item, choose <em>Manage permissions</em> and grant <em>Read</em>, <em>Reshare</em>, or <em>Build</em> to specific users or Microsoft Entra security groups. Build permission lets the consumer create new content from the underlying semantic model.</p>

<h3>Apply sensitivity labels</h3>
<p><strong>Sensitivity labels</strong> from Microsoft Purview (Information Protection) classify Power BI content as <em>Public</em>, <em>General</em>, <em>Confidential</em>, <em>Highly Confidential</em>, or your organisation's custom labels. Labels:</p>
<ul>
  <li>Flow with the content through every export &mdash; PDF, PowerPoint, Excel &mdash; and are honoured by Microsoft 365 apps.</li>
  <li>Can enforce encryption and watermarks via the underlying Purview policy.</li>
  <li>Are applied per item (semantic model, report, dashboard) and surfaced in the Service UI for easy auditing.</li>
</ul>
<p>Enable sensitivity labels in the Power BI Admin Portal first; report authors then apply them from each item's settings.</p>

<h3>Create dashboards</h3>
<p>A <strong>dashboard</strong> in the Power BI Service is a single-page canvas of <em>tiles</em> pinned from one or more reports in the same workspace. Dashboards differ from reports in three important ways:</p>
<ul>
  <li>They are <em>single-page</em>, read-only, and optimised for at-a-glance monitoring.</li>
  <li>Tiles can come from <em>different</em> reports and even different semantic models, so a dashboard is a great consolidated landing page.</li>
  <li>Dashboards uniquely support <strong>data alerts</strong> on KPI/card/gauge tiles &mdash; consumers receive email or Teams notifications when a tile crosses a threshold.</li>
</ul>
<p>To create one: open the workspace, choose <em>New &rarr; Dashboard</em>, then open any report and pin individual visuals to the dashboard.</p>
"""

LESSON_ADDITIONS = {
    'l1_get_data':       L1_ADDITION,
    'l2_transform':      L2_ADDITION,
    'l3_design_model':   L3_ADDITION,
    'l4_dax':            L4_ADDITION,
    'l6_visualizations': L6_ADDITION,
    'l7_enhance':        L7_ADDITION,
    'l9_deploy':         L9_ADDITION,
}

# ---------------------------------------------------------------------------
# New quiz questions (one per missing topic). Shape: (qtype, qhtml, opts, fb)
# ---------------------------------------------------------------------------

QUESTION_ADDITIONS = {
    'l1_get_data': [
        ('multiple_choice',
         'Your data lives in a Microsoft Fabric lakehouse as Delta-Parquet tables and is tens of gigabytes in size. Business users need sub-second interactivity and near-real-time freshness. Which storage mode should you choose for the semantic model?',
         [('Import &mdash; load the full dataset into memory on every refresh.', False),
          ('DirectQuery &mdash; issue SQL to the lakehouse on every visual interaction.', False),
          ('DirectLake &mdash; query the OneLake Delta files directly without import.', True),
          ('Live connection to an Analysis Services tabular model.', False)],
         'DirectLake is purpose-built for this scenario: it queries Delta-Parquet files in OneLake directly, giving Import-class performance with DirectQuery-class freshness, and avoids the 1&nbsp;GB Import-mode limit.'),
    ],

    'l2_transform': [
        ('multiple_choice',
         'You have 10&nbsp;million daily transaction rows in a Sales query and the report only needs total revenue and unit count per <strong>Product</strong> per <strong>Month</strong>. Which Power Query transformation should you apply before loading to keep the model small and fast?',
         [('Use <em>Remove Duplicates</em> on the Product column.', False),
          ('Use <em>Group By</em> on Product and Month, aggregating Amount (Sum) and Quantity (Sum).', True),
          ('Use <em>Merge Queries</em> against a Product dimension.', False),
          ('Use <em>Append Queries</em> to combine months into one table.', False)],
         '<strong>Group By</strong> rolls detail rows up to the required grain (Product &times; Month) and produces a much smaller fact table for the model. Remove Duplicates discards rows but does not aggregate; Merge and Append do not aggregate either.'),

        ('multiple_choice',
         'A REST API returns JSON where each customer record contains a nested <em>orders</em> array. You need one row per order in your model. What sequence of Power Query steps achieves this?',
         [('Promote headers, then change types.', False),
          ('Expand the customer record, then <em>Expand to New Rows</em> on the orders list, then expand the order record.', True),
          ('Use <em>Group By</em> on the customer id.', False),
          ('Use <em>Pivot Column</em> on the orders list.', False)],
         '<em>Expand to New Rows</em> is the key step that fans a list of records out into individual rows. Wrap it with record expansions on either side to land a flat, tabular shape.'),

        ('multiple_choice',
         'Your model has one large <em>Sales</em> table with denormalised customer, product, and date attributes repeated on every row. Reports are slow and DAX is hard to write. Which redesign should you apply?',
         [('Switch the table to DirectQuery mode.', False),
          ('Restructure as a star schema: a FactSales table linked to DimCustomer, DimProduct, and DimDate.', True),
          ('Add more calculated columns to the Sales table.', False),
          ('Move the table to a Power BI Premium workspace.', False)],
         'A <strong>star schema</strong> compresses dramatically better than a flat table, lets DAX use simple <code>RELATED</code>/<code>RELATEDTABLE</code> patterns, and is the recommended model shape for Power BI.'),
    ],

    'l3_design_model': [
        ('multiple_choice',
         'You need to classify each Customer row as "Under 25", "25-44", "45-64", or "65+" so users can slice by age band. The classification should be stored once at refresh time and never recomputed. Should you create a measure, a calculated column, or a calculated table?',
         [('A measure &mdash; aggregations only update when filters change.', False),
          ('A calculated column on the Customer table using <code>SWITCH(TRUE(), ...)</code>.', True),
          ('A calculated table that snapshots the customer list.', False),
          ('A Power Query custom column on the Sales fact table.', False)],
         'Slicer-friendly row-level attributes that depend on the row\'s own data should be <strong>calculated columns</strong>. Measures only return aggregations and cannot be placed on a slicer; calculated tables would duplicate the customer list unnecessarily.'),
    ],

    'l4_dax': [
        ('multiple_choice',
         'You are reporting the <em>Account Balance</em> from a banking fact table. Adding January\'s balance to February\'s balance produces a meaningless total. Which DAX pattern correctly returns the end-of-period balance for whatever date range is filtered?',
         [('<code>SUM(Finance[Balance])</code>', False),
          ('<code>AVERAGE(Finance[Balance])</code>', False),
          ('<code>CALCULATE(SUM(Finance[Balance]), LASTDATE(\'Date\'[Date]))</code>', True),
          ('<code>SUMX(Finance, Finance[Balance])</code>', False)],
         'Balances are <strong>semi-additive</strong>: additive across customers/accounts but not across time. Using <code>LASTDATE</code> inside <code>CALCULATE</code> returns the balance on the last date in the current filter context, which is the correct semantic.'),

        ('multiple_choice',
         'Your model has 40 measures and you need each of them to be reportable as Current, YTD, Prior Year, YoY $, and YoY %, with consistent formatting. Authoring 200 individual measures is unmaintainable. Which Power BI / tabular feature solves this elegantly?',
         [('Quick measures for each base measure.', False),
          ('Calculation groups defining one set of calculation items applied to any base measure.', True),
          ('A field parameter listing the measures.', False),
          ('Bookmarks toggling between visuals.', False)],
         '<strong>Calculation groups</strong> let you define a single set of calculation items (Current, YTD, PY, YoY $, YoY %) that apply to <em>any</em> measure on the model, drastically reducing the measure count and enforcing consistent formatting.'),
    ],

    'l6_visualizations': [
        ('multiple_choice',
         'You want a paragraph at the top of your report that reads "Sales grew 12% versus last quarter, driven by the East region" and that automatically rewrites itself as the user filters the page. Which Power BI feature produces this?',
         [('A text box with a measure embedded via the Q&amp;A visual.', False),
          ('A Smart Narrative visual whose summary is generated by Copilot.', True),
          ('A tooltip page configured on the matrix.', False),
          ('A KPI visual.', False)],
         '<strong>Smart Narrative</strong> with Copilot produces dynamic prose summaries that recompute on every filter change &mdash; the canonical "narrative visual with Copilot" listed in the PL-300 study guide.'),

        ('multiple_choice',
         'Finance needs a monthly statement that must export cleanly to a multi-page PDF with consistent page headers, page numbers, and exact layout, and that is emailed to 200 branch managers as a parameterised subscription. Which Power BI report type should you build?',
         [('A standard Power BI report in Power BI Desktop.', False),
          ('A paginated (.rdl) report authored in Power BI Report Builder.', True),
          ('A Power BI dashboard with pinned tiles.', False),
          ('A Power BI Embedded report.', False)],
         '<strong>Paginated reports</strong> are designed for pixel-perfect, multi-page, print-and-distribute scenarios with parameter-driven subscriptions &mdash; the exact use case described.'),

        ('multiple_choice',
         'Inside a matrix visual you want a column that shows the running total of <em>Sales</em> across the months on the visual, without adding a model measure. Which Power BI feature should you use?',
         [('A calculated column on the Sales table.', False),
          ('A visual calculation using <code>RUNNINGSUM</code> on the visual.', True),
          ('A model measure with <code>CALCULATE(SUM(...), DATESYTD(...))</code>.', False),
          ('A Quick Measure of type Running Total.', False)],
         '<strong>Visual calculations</strong> are DAX expressions scoped to the visual itself and have access to specialised functions such as <code>RUNNINGSUM</code>, <code>MOVINGAVERAGE</code>, and <code>PREVIOUS</code>. They are perfect for last-mile, visual-only calculations.'),
    ],

    'l7_enhance': [
        ('multiple_choice',
         'You publish a sensitive HR report and need to prevent consumers from exporting underlying row-level data, while still allowing them to view the report online. Where do you configure this?',
         [('Disable the report&apos;s drillthrough pages.', False),
          ('Turn off <em>Export data &rarr; Underlying data</em> in the report settings (and the matching tenant-level switch in the Admin Portal).', True),
          ('Remove the report from the workspace and re-share via email.', False),
          ('Switch the dataset to DirectQuery mode.', False)],
         'Export controls live in <em>File &rarr; Options &rarr; Report settings</em> and in the Power BI Admin Portal. Disabling underlying-data export blocks row-level export while still permitting summarised exports and online viewing.'),

        ('multiple_choice',
         'Sales managers want to change the visual type of a chart and swap in different measures, then save their preferred view &mdash; <em>without</em> affecting what other consumers see. Which feature should the report author enable?',
         [('Bookmarks created by the author.', False),
          ('<em>Personalize visuals</em>, which lets each consumer modify visuals and save personal bookmarks per user.', True),
          ('A separate workspace per sales manager.', False),
          ('Row-level security roles.', False)],
         '<strong>Personalize visuals</strong> empowers consumers to change visual type, measures, and fields, and to save their changes as personal bookmarks that are scoped to their own account.'),

        ('multiple_choice',
         'A trading desk dashboard must refresh every 30 seconds. The semantic model is in DirectQuery mode against Azure SQL on a Premium capacity. How do you implement this?',
         [('Schedule the dataset to refresh every 30 seconds in the Power BI Service.', False),
          ('Enable <em>Automatic page refresh</em> on the page and set a fixed interval of 30 seconds (or use change detection).', True),
          ('Use a streaming dataset and a tile push.', False),
          ('Set the report to <em>Auto-refresh on file open</em>.', False)],
         '<strong>Automatic page refresh</strong> at sub-minute intervals is the supported mechanism for near-real-time dashboards on DirectQuery sources with Premium capacity. Scheduled dataset refresh is capped at 48 times per day and cannot reach 30-second cadence.'),
    ],

    'l9_deploy': [
        ('multiple_choice',
         'A workspace contains 20 reports. The Finance team should see <em>only</em> the budget variance report; you do not want to make them workspace members. How do you grant access?',
         [('Promote the variance report so it appears at the top of search.', False),
          ('Use <em>Manage permissions</em> on the budget variance report to grant <em>Read</em> access to the Finance Microsoft Entra group (item-level permission).', True),
          ('Add the Finance group as Viewers of the workspace.', False),
          ('Move the budget variance report to a separate workspace and add Finance as Admins.', False)],
         '<strong>Item-level permissions</strong> let you share a single artifact with specific users or groups without granting any workspace role. Workspace roles, including Viewer, grant access to <em>everything</em> in the workspace.'),

        ('multiple_choice',
         'Your organisation classifies all customer PII reports as "Highly Confidential" and requires that classification to follow the file when exported to Excel or PowerPoint. Which Power BI feature should you apply to the report?',
         [('Row-level security roles in DAX.', False),
          ('A sensitivity label from Microsoft Purview Information Protection.', True),
          ('A bookmark restricting page visibility.', False),
          ('A Power BI app with the audience set to Finance.', False)],
         '<strong>Sensitivity labels</strong> from Microsoft Purview classify Power BI content and persist through every export, where Microsoft 365 apps honour the label (encryption, watermarks, access restrictions).'),

        ('multiple_choice',
         'You want a single landing canvas showing the most important tiles from three different reports, plus an alert when a KPI tile drops below a threshold. Which Power BI artifact should you build?',
         [('A paginated report.', False),
          ('A Power BI dashboard with tiles pinned from each report and a data alert configured on the KPI tile.', True),
          ('A Power BI app published from the workspace.', False),
          ('A bookmark navigator inside one of the reports.', False)],
         '<strong>Dashboards</strong> uniquely support pinning tiles from multiple reports/models and configuring <em>data alerts</em> on KPI/card/gauge tiles &mdash; the exact requirements listed.'),
    ],
}

# ---------------------------------------------------------------------------
# Final exam rebalance — add a Manage & Secure question (was 4/25, target 5/25)
# ---------------------------------------------------------------------------
FINAL_EXAM_ADDITIONS = [
    ('multiple_choice',
     'A regional manager must see only their own region&apos;s rows in every report built on the <em>Sales</em> semantic model. You implement Row-Level Security with a DAX filter on the Region table and need to assign each manager to the correct role automatically as people join and leave the team. What is the recommended approach?',
     [('Add each manager directly to the role membership in the Power BI Service.', False),
      ('Map each role to a Microsoft Entra (Azure AD) security group whose membership is maintained by HR.', True),
      ('Hard-code each manager&apos;s name into the DAX filter expression on the Region table.', False),
      ('Grant each manager <em>Build</em> permission on the semantic model.', False)],
     'Best practice is to assign <strong>Microsoft Entra security groups</strong> to RLS roles. HR maintains the group membership, and Power BI automatically picks up joiners/leavers &mdash; no Power BI admin work required for ongoing changes.'),
]
