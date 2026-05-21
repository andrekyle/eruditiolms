LESSON_HTML = """
<h2>Create Reports: Visualizations and Formatting</h2>

<p>Effective Power BI reports rely on choosing the right visualizations and formatting them appropriately for your audience. This lesson covers identifying the best chart type for your data, formatting and configuring visuals, customizing themes, and designing page layouts that guide users to insights.</p>

<h3>Choosing the Right Visualization</h3>

<p>The first step in creating effective reports is selecting the visualization that best communicates your data story. Each chart type excels at showing different relationships and patterns in data.</p>

<table border='1' cellpadding='10' cellspacing='0' style='width:100%; border-collapse:collapse;'>
  <thead>
    <tr style='background-color:#f0f0f0;'>
      <th>Visualization Type</th>
      <th>Best For</th>
      <th>Key Characteristics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Column/Bar Chart</strong></td>
      <td>Comparing values across categories</td>
      <td>Vertical or horizontal bars; easy comparison; categorical data on one axis</td>
    </tr>
    <tr>
      <td><strong>Line Chart</strong></td>
      <td>Showing trends over time</td>
      <td>Connected data points; ideal for time-series data; multiple lines for comparison</td>
    </tr>
    <tr>
      <td><strong>Pie/Donut Chart</strong></td>
      <td>Showing parts of a whole (percentages)</td>
      <td>Limited categories (2-5 ideal); shows proportion; donut variant is slightly better for readability</td>
    </tr>
    <tr>
      <td><strong>Treemap</strong></td>
      <td>Showing hierarchical data with proportional sizes</td>
      <td>Nested rectangles; combines hierarchy and values; useful for part-to-whole at multiple levels</td>
    </tr>
    <tr>
      <td><strong>Scatter Chart</strong></td>
      <td>Showing relationships between two continuous variables</td>
      <td>Points on X and Y axes; reveals correlation; supports bubble size and color dimensions</td>
    </tr>
    <tr>
      <td><strong>KPI Card</strong></td>
      <td>Displaying single key metric with trend indicator</td>
      <td>Large value; comparison to baseline; trend arrow showing increase/decrease</td>
    </tr>
    <tr>
      <td><strong>Card</strong></td>
      <td>Showing a single number or value</td>
      <td>Minimal, focused display; good for dashboards; supports one or more values</td>
    </tr>
    <tr>
      <td><strong>Table/Matrix</strong></td>
      <td>Displaying detailed data with rows and columns</td>
      <td>Exact values; drill-down capability; supports subtotals and row/column hierarchy</td>
    </tr>
    <tr>
      <td><strong>Gauge</strong></td>
      <td>Showing progress toward a goal or target</td>
      <td>Arc-based; target reference line; colored ranges for performance zones</td>
    </tr>
    <tr>
      <td><strong>Waterfall</strong></td>
      <td>Showing how an initial value changes through sequential steps</td>
      <td>Bridges between bars; shows contribution of each component; financial analysis</td>
    </tr>
    <tr>
      <td><strong>Funnel</strong></td>
      <td>Showing decreasing values through stages/steps</td>
      <td>Narrowing bars; often used for conversion or pipeline stages</td>
    </tr>
    <tr>
      <td><strong>Map</strong></td>
      <td>Displaying geographical data and regional patterns</td>
      <td>Geographic location; bubble or filled map; region-level or coordinate-based</td>
    </tr>
  </tbody>
</table>

<h3>Formatting and Configuring Visualizations</h3>

<p>Once you choose a visualization type, formatting makes it clear and professional:</p>

<ul>
  <li><strong>Titles and Labels:</strong> Add descriptive titles; enable data labels on bars/points to show exact values; configure label density to avoid clutter</li>
  <li><strong>Axes and Legends:</strong> Rename axes for clarity; remove redundant legends when obvious; set axis ranges to highlight meaningful differences</li>
  <li><strong>Conditional Formatting:</strong> Use background colors on tables/matrices to highlight high/low values; apply data bars within cells; set color scales based on thresholds</li>
  <li><strong>Sorting:</strong> Sort ascending/descending by value or custom order; sort matrix rows and columns to show most important data first</li>
  <li><strong>Colors:</strong> Use contrasting colors; follow your brand guidelines; use red/green sparingly (color-blind considerations); limit to 3-5 colors for clarity</li>
</ul>

<h3>Using Custom Visuals</h3>

<p>Beyond built-in visuals, Power BI supports custom visuals from AppSource and organizational visual libraries:</p>

<ul>
  <li>Access AppSource visuals through the ellipsis menu in the Visualizations pane</li>
  <li>Search for specific visualization types (e.g., 'advanced chart', 'KPI indicator')</li>
  <li>Organizational visuals allow your company to standardize branded or specialized visualizations</li>
  <li>Custom visuals support the same formatting options as built-in visuals</li>
  <li>Always test custom visuals with your data to ensure performance and compatibility</li>
</ul>

<h3>Applying and Customizing Themes</h3>

<p>Themes control the overall look and feel of your report—colors, fonts, and styling across all pages and visuals. Power BI ships with default themes, and you can create or upload custom JSON theme files.</p>

<p>To apply a theme: Home tab → Switch Theme (or upload custom JSON). Theme JSON controls colors, fonts, and visual properties:</p>

<pre><code class='language-json'>&lt;?json
{
  &quot;name&quot;: &quot;Corporate Brand&quot;,
  &quot;dataColors&quot;: [&quot;#1f77b4&quot;, &quot;#ff7f0e&quot;, &quot;#2ca02c&quot;, &quot;#d62728&quot;, &quot;#9467bd&quot;],
  &quot;background&quot;: {&quot;color&quot;: &quot;#ffffff&quot;},
  &quot;foreground&quot;: {&quot;color&quot;: &quot;#333333&quot;},
  &quot;tableAccent&quot;: {&quot;color&quot;: &quot;#1f77b4&quot;}
}
?&gt;</code></pre>

<p>Theme properties include dataColors (for chart series), background, foreground (text), fonts (family, size), and visual settings (borders, shadows). Create themes in JSON format and upload via the theme menu.</p>

<h3>Page Layout, Grids, and Alignment</h3>

<p>Organize your report pages for clarity and professionalism:</p>

<ul>
  <li><strong>Grid Layout:</strong> Enable grid and snap-to-grid (View menu) to align objects; choose grid size (small/medium/large)</li>
  <li><strong>Alignment Tools:</strong> Select multiple visuals and use alignment options (align left/right/top/bottom, distribute evenly)</li>
  <li><strong>Page Design:</strong> Set page size and orientation; consider standard sizes (16:9 widescreen for web viewing)</li>
  <li><strong>Margins and Spacing:</strong> Leave white space around visuals; group related visuals together; avoid overcrowding</li>
  <li><strong>Layering:</strong> Use page navigation to organize multi-page reports logically</li>
</ul>

<h3>Slicers and Filtering</h3>

<p>Slicers allow report consumers to filter data interactively:</p>

<ul>
  <li><strong>Adding Slicers:</strong> Insert → Slicer; choose a field (date, category, numeric); position on report page</li>
  <li><strong>Slicer Types:</strong> List (traditional multi-select), Dropdown (compact), Between (for ranges), Relative Date (for time periods)</li>
  <li><strong>Sync Slicers:</strong> Format → Sync Slicers to link multiple pages; changes on one page filter the same field on other pages</li>
  <li><strong>Filter Pane:</strong> Alternative filtering interface; shows all available filters hierarchically; supports basic and advanced filtering</li>
  <li><strong>Slicer Formatting:</strong> Control selection style (single vs. multiple), orientation, and appearance</li>
</ul>

<h3>Tooltips and Interactivity</h3>

<p>Tooltips provide contextual information when users hover over data points:</p>

<ul>
  <li><strong>Default Tooltips:</strong> Show measure values and categories automatically; built into most visuals</li>
  <li><strong>Custom Tooltip Pages:</strong> Create a dedicated report page as a tooltip; design a mini-dashboard that appears on hover; link via Visual → Tooltips</li>
  <li><strong>Report-Page Tooltips:</strong> Existing report page can serve as tooltip; set page tooltip property to 'On'</li>
  <li><strong>Cross-Filtering:</strong> Clicking one visual filters others; set interaction direction in Edit Interactions mode</li>
</ul>

"""

QUESTIONS = [
    (
        """<p><strong>Scenario:</strong> You have monthly sales data (Jan-Dec 2024) with values ranging from $50K to $200K. You need to show how revenue trends throughout the year. Which visualization is most appropriate?</p>""",
        [
            ("Line Chart", True),
            ("Pie Chart", False),
            ("Matrix Table", False),
            ("Gauge Chart", False),
        ],
        """<p><strong>Correct!</strong> A Line Chart is ideal for showing trends over time. The connected data points clearly display how revenue changes month-to-month. A pie chart shows parts of a whole (not appropriate here), a matrix shows detailed data, and a gauge shows progress to a target.</p>"""
    ),
    (
        """<p><strong>Question:</strong> You want to display a company's Q4 revenue composed of four product categories (each representing a different percentage of total revenue). The categories are roughly equal in size. Which visualization is most suitable?</p>""",
        [
            ("Column Chart", False),
            ("Donut Chart", True),
            ("Scatter Chart", False),
            ("Waterfall Chart", False),
        ],
        """<p><strong>Correct!</strong> A Donut Chart effectively shows parts of a whole (percentages). With 4 categories of roughly equal size, the donut provides clear visual comparison of each segment's contribution. A waterfall would show sequential changes, and a scatter chart shows relationships between two continuous variables—neither fits this requirement.</p>"""
    ),
    (
        """<p><strong>Scenario:</strong> Your manager wants to see which sales regions are performing above or below their Q3 budget targets. There are 12 regions, and you need to show actual vs. target quickly. Which chart type communicates this best?</p>""",
        [
            ("Gauge Chart", False),
            ("Bar Chart", True),
            ("Line Chart", False),
            ("Treemap", False),
        ],
        """<p><strong>Correct!</strong> A Bar Chart effectively compares actual to target values across 12 regions side-by-side. Horizontal bars make region names readable and comparison straightforward. A gauge shows progress toward one target, and a line chart is for trends over time. A treemap is better for hierarchical part-to-whole relationships.</p>"""
    ),
    (
        """<p><strong>Question:</strong> You've created a Power BI report with a blue and gray color scheme matching your company brand. You want every report in your organization to use these same colors, fonts, and styling automatically. What should you do?</p>""",
        [
            ("Create a custom JSON theme file and upload it via Home → Switch Theme or organizational visuals", True),
            ("Manually format each visual's colors every time you create a report", False),
            ("Change Power BI's default settings in Options", False),
            ("Use conditional formatting on each visualization individually", False),
        ],
        """<p><strong>Correct!</strong> Creating and uploading a custom JSON theme file is the standard way to enforce consistent branding across all reports in your organization. Once uploaded, the theme applies automatically to new reports, ensuring consistency. Manual formatting is inefficient, Power BI default settings can't be changed globally this way, and conditional formatting is for highlighting data—not overall styling.</p>"""
    ),
    (
        """<p><strong>Scenario:</strong> You have a product hierarchy (Category → Subcategory → Product) with sales values. You need to show each product's sales while maintaining the hierarchy, and you want to see which categories and subcategories contribute most to total sales. Which visualization works best?</p>""",
        [
            ("Matrix", False),
            ("Treemap", True),
            ("Line Chart", False),
            ("Funnel Chart", False),
        ],
        """<p><strong>Correct!</strong> A Treemap displays hierarchical data with rectangle sizes proportional to values—perfect for showing product sales within categories and subcategories. You can see the contribution of each level at a glance. A matrix table can show hierarchy too, but treemap's visual representation of relative sizes makes patterns more obvious. A funnel is for conversion stages, not hierarchies.</p>"""
    ),
    (
        """<p><strong>Question:</strong> You've added a Date slicer to filter your report by year. You want the same slicer to filter the same Date field on all three pages of your report. How do you set this up?</p>""",
        [
            ("Copy the slicer to each page manually", False),
            ("Use Format → Sync Slicers to link the slicer across pages", True),
            ("Create separate slicers on each page with the same field", False),
            ("Use a filter pane instead of a slicer", False),
        ],
        """<p><strong>Correct!</strong> Sync Slicers (Format menu, available when slicer is selected) links a slicer across multiple pages, so one selection filters all pages. This is more efficient than copying slicers or creating separate ones per page, and ensures consistency across your report.</p>"""
    ),
    (
        """<p><strong>Question:</strong> You want to show a customer's year-to-date revenue ($1.2M), their target for the year ($1.5M), and a visual indicator showing they are 80% of goal with an arrow pointing up (indicating growth). Which visualization should you use?</p>""",
        [
            ("Gauge Chart", False),
            ("KPI Card", True),
            ("Card", False),
            ("Waterfall Chart", False),
        ],
        """<p><strong>Correct!</strong> A KPI Card displays a single key metric with a comparison baseline and trend indicator (the up arrow)—exactly what you need. A regular Card shows just a value with no trend; a Gauge shows progress toward a target but doesn't compare to target as clearly; a waterfall shows sequential changes. The KPI card is designed for this scenario.</p>"""
    ),
    (
        """<p><strong>Scenario:</strong> You need to show how revenue flowed through your business: starting with gross revenue, subtracting costs, then deducting taxes, arriving at net revenue. The user should see the contribution of each deduction step. Which chart best visualizes this?</p>""",
        [
            ("Waterfall Chart", True),
            ("Stacked Column Chart", False),
            ("Funnel Chart", False),
            ("Area Chart", False),
        ],
        """<p><strong>Correct!</strong> A Waterfall Chart is designed to show how an initial value changes through sequential steps—perfect for revenue flows with costs and deductions. The bridges between bars clearly show the impact of each step. A stacked column could show parts of a whole, but doesn't clearly communicate the sequential nature or contribution of each step like a waterfall does.</p>"""
    ),
]