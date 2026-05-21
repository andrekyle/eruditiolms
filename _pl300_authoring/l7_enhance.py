LESSON_HTML = """
<h2>Enhance Reports for Usability and Storytelling</h2>

<h3>1. Bookmarks</h3>
<p>Bookmarks capture the current state of your report—including filters, slicers, visual selections, and visibility settings. Use bookmarks to create guided tours, enable users to toggle between different analytical views, or provide jump points for storytelling.</p>
<ul>
  <li><strong>Create a bookmark:</strong> Configure report state (filters, page context, visual selections), then go to View &gt; Bookmarks &gt; Add to save the state.</li>
  <li><strong>Navigate via bookmark:</strong> Select a bookmark name from the Bookmarks pane to restore its saved state instantly.</li>
  <li><strong>Use bookmarks for storytelling:</strong> Build narrative sequences by layering bookmarks with navigation buttons for interactive report walkthroughs.</li>
</ul>

<h3>2. Custom Tooltips and Report-Page Tooltips</h3>
<p>Tooltips provide contextual information when users hover over visuals. Report-page tooltips are separate pages designed as rich, interactive contexts for a single data point.</p>
<ul>
  <li><strong>Basic tooltips:</strong> Format &gt; Tooltip, then enable and select a tooltip page.</li>
  <li><strong>Report-page tooltips:</strong> Design a dedicated tooltip page with visuals and measures. Link to it via Format &gt; Tooltip &gt; Tooltip page.</li>
  <li><strong>Tooltip measures:</strong> Use DAX to calculate dynamic values for tooltip display.</li>
</ul>
<p><strong>Example DAX for tooltip measure (Sales Count):</strong></p>
<pre><code>Sales Count = COUNTA(Sales[SalesID])</code></pre>

<h3>3. Visual Interactions</h3>
<p>Configure how one visual influences others on the page: filter (cross-filtering), highlight (cross-highlighting), or none (ignore interaction).</p>
<ul>
  <li><strong>Set interaction:</strong> Select a visual, then Format &gt; Edit interactions to define filter, highlight, or none for other visuals.</li>
  <li><strong>Filter:</strong> Selecting a value in one visual filters all connected visuals to show only related data.</li>
  <li><strong>Highlight:</strong> Selecting a value highlights matching data in other visuals while keeping context visible.</li>
  <li><strong>None:</strong> Disables interaction for visuals that should not influence each other.</li>
</ul>

<h3>4. Report Navigation</h3>
<p>Guide users through reports using navigation buttons, page navigators, and bookmark buttons.</p>
<ul>
  <li><strong>Navigation buttons:</strong> Insert &gt; Button, configure to navigate to another page, URL, or bookmark.</li>
  <li><strong>Page navigator:</strong> Insert &gt; Page Navigator to create a navigation list for multi-page reports.</li>
  <li><strong>Bookmark navigator:</strong> Insert &gt; Button with type 'Bookmark' to allow users to jump between bookmarked states.</li>
  <li><strong>Breadcrumb trails:</strong> Use buttons to show users their navigation path.</li>
</ul>

<h3>5. Sorting</h3>
<p>Apply sorting to visuals for better readability and analysis.</p>
<ul>
  <li><strong>Sort by column:</strong> Right-click a visual &gt; Sort &gt; Sort ascending/descending by data column.</li>
  <li><strong>Sort by measure:</strong> Sort by aggregated values (e.g., sort products by total sales revenue, not alphabetically).</li>
  <li><strong>Sort in Matrix/Table:</strong> Click column headers or Format &gt; Sort to define multi-level sort orders.</li>
</ul>

<h3>6. Sync Slicers Across Pages</h3>
<p>Synchronize slicer selections across multiple report pages for consistent filtering.</p>
<ul>
  <li><strong>Enable sync:</strong> Select slicer &gt; Format &gt; Slicer Header &gt; toggle 'Sync slicers'.</li>
  <li><strong>Configure pages:</strong> Choose which pages the slicer syncs to.</li>
  <li><strong>Visibility:</strong> Optionally hide the slicer on secondary pages while maintaining synchronization.</li>
</ul>

<h3>7. Selection Pane and Visual Grouping</h3>
<p>Organize and layer visuals for easier management and design consistency.</p>
<ul>
  <li><strong>Open Selection Pane:</strong> View &gt; Selection Pane to see all page objects in a hierarchical list.</li>
  <li><strong>Group visuals:</strong> Select multiple visuals &gt; Ctrl+G to group them for synchronized movement.</li>
  <li><strong>Layer management:</strong> Use Selection Pane to reorder layers (send to back/front).</li>
  <li><strong>Name objects:</strong> Double-click in Selection Pane to rename visuals for clarity.</li>
</ul>

<h3>8. Drill-down vs. Drillthrough</h3>
<p>Both enable deeper data exploration, but work differently:</p>
<table border='1' cellpadding='10'>
  <tr>
    <th>Feature</th>
    <th>Drill-down (Expand)</th>
    <th>Drillthrough</th>
  </tr>
  <tr>
    <td><strong>Navigation</strong></td>
    <td>Navigates within the same visual, expanding hierarchy levels</td>
    <td>Navigates to a different page or report to show related details</td>
  </tr>
  <tr>
    <td><strong>Scope</strong></td>
    <td>Single visual; same page</td>
    <td>Can cross pages; supports cross-report drillthrough</td>
  </tr>
  <tr>
    <td><strong>Setup</strong></td>
    <td>Requires hierarchical data structure (e.g., Year &gt; Quarter &gt; Month)</td>
    <td>Configure drillthrough columns; target page receives filtered context</td>
  </tr>
  <tr>
    <td><strong>Use Case</strong></td>
    <td>Explore aggregated data from summary to detail within a visual</td>
    <td>Link to detail pages, other reports, or specialized dashboards</td>
  </tr>
</table>
<p><strong>Cross-report drillthrough:</strong> Use Report Links to enable drillthrough actions that open related reports with filtered context passed via URL parameters or query parameters.</p>

<h3>9. Conditional Formatting</h3>
<p>Apply dynamic formatting to highlight data patterns and draw attention to key insights.</p>
<ul>
  <li><strong>Background color:</strong> Format cell background based on data values or rules (gradient, rule-based, or custom color scales).</li>
  <li><strong>Font color:</strong> Conditionally change text color for emphasis (e.g., red for negative values).</li>
  <li><strong>Data bars:</strong> Display in-cell bar charts to visualize magnitude without separate visuals.</li>
  <li><strong>Icons:</strong> Show icons (arrows, traffic lights, shapes) based on value ranges or thresholds.</li>
  <li><strong>Web URL:</strong> Convert text to clickable links based on conditions (e.g., hyperlink top-performing products).</li>
  <li><strong>Apply in Matrix/Table:</strong> Format &gt; Conditional formatting to choose the type and rule.</li>
</ul>

<h3>10. Slicing and Filtering</h3>
<p>Apply filters at multiple levels to control data scope:</p>
<ul>
  <li><strong>Visual-level filters:</strong> Filter &gt; Visual, affecting only the current visual.</li>
  <li><strong>Page-level filters:</strong> Filter &gt; Page, applied to all visuals on the page.</li>
  <li><strong>Report-level filters:</strong> Filter &gt; Report, applied across all pages.</li>
  <li><strong>Slicer objects:</strong> Interactive controls allowing end-users to adjust filters dynamically.</li>
  <li><strong>Lock filters:</strong> Prevent report readers from changing filters by setting permissions or locking slicers.</li>
</ul>

<h3>11. Mobile View Layouts</h3>
<p>Design optimized report layouts for mobile devices and tablets.</p>
<ul>
  <li><strong>Enable mobile layout:</strong> View &gt; Mobile Layout to create a dedicated mobile view.</li>
  <li><strong>Responsive design:</strong> Reposition and resize visuals for smaller screens; stack vertically for better scrolling.</li>
  <li><strong>Simplify for mobile:</strong> Remove non-essential visuals or filters to reduce clutter.</li>
  <li><strong>Test across devices:</strong> Preview the mobile layout on different screen sizes.</li>
  <li><strong>Maintain interactivity:</strong> Buttons, slicers, and drill actions remain functional on mobile.</li>
</ul>

<h3>12. Design for Accessibility</h3>
<p>Ensure reports are usable by all audiences, including those with visual or motor disabilities.</p>
<ul>
  <li><strong>Alt text:</strong> Select a visual &gt; Format &gt; General &gt; Alt text. Describe visual content, key insights, and purpose.</li>
  <li><strong>Tab order:</strong> View &gt; Selection Pane &gt; Tab order option to set logical keyboard navigation sequence.</li>
  <li><strong>Color contrast:</strong> Use colors with sufficient contrast (WCAG AA: 4.5:1 for text). Test with contrast checkers.</li>
  <li><strong>Text size:</strong> Use readable font sizes (minimum 11pt for body text, 14pt+ for headers).</li>
  <li><strong>Keyboard navigation:</strong> Ensure all interactive elements (buttons, slicers, drillthrough actions) are keyboard accessible.</li>
  <li><strong>Screen reader support:</strong> Provide alt text and semantic structure so screen readers can convey meaning.</li>
  <li><strong>Avoid color-only encoding:</strong> Don't use color alone to convey meaning; pair with labels, patterns, or icons.</li>
</ul>

<h3>Best Practices for Report Storytelling</h3>
<ul>
  <li>Use bookmarks to guide users through a narrative (e.g., "Key Findings" &gt; "Regional Breakdown" &gt; "Action Items").</li>
  <li>Combine bookmarks with navigation buttons for seamless storytelling experiences.</li>
  <li>Employ consistent color, font, and layout conventions across all pages.</li>
  <li>Use tooltips and report-page tooltips to provide context without cluttering main visuals.</li>
  <li>Design visual interactions to support analytical exploration while preventing confusion.</li>
  <li>Label buttons and navigation elements clearly so users understand what each action does.</li>
  <li>Test the entire report flow end-to-end with representative users before publishing.</li>
</ul>
"""

QUESTIONS = [
    (
        """<p>You want to save the current state of your report—including active filters, selected values, and visible visuals—so users can return to this exact view. Which feature should you use?</p>""",
        [
            ("Bookmarks", True),
            ("Page Navigator", False),
            ("Navigation Buttons", False),
            ("Sync Slicers", False),
        ],
        """<p>Correct! Bookmarks capture and preserve the complete state of a report at a point in time, including all filters, slicers, selections, and visual visibility. Users can click a bookmark to instantly restore that saved state.</p>""",
    ),
    (
        """<p>You have created multiple bookmarks representing different stages of a sales analysis story. How would you guide end-users to navigate between these bookmarks in sequence?</p>""",
        [
            ("Insert navigation buttons configured with bookmark actions, creating a clickable navigation flow", True),
            ("Use the page navigator feature to list all bookmarks automatically", False),
            ("Enable sync slicers across pages to connect bookmarks", False),
            ("Apply conditional formatting to highlight the active bookmark", False),
        ],
        """<p>Correct! Navigation buttons with bookmark actions provide a guided narrative experience. Users click through buttons in sequence to move between bookmarked states, creating a storytelling flow through your report analysis.</p>""",
    ),
    (
        """<p>You are building a detailed sales report. Users should be able to click a product name in one visual to see deeper detail about that product on a separate page. What feature enables this cross-page interaction?</p>""",
        [
            ("Drillthrough", True),
            ("Drill-down", False),
            ("Visual Interactions (Filter)", False),
            ("Conditional Formatting", False),
        ],
        """<p>Correct! Drillthrough enables navigation from one page (or report) to another detail page, passing context about the selected item. Drill-down expands hierarchy levels within a single visual, whereas drillthrough navigates to a different analytical context.</p>""",
    ),
    (
        """<p>Your report will be used by employees with various abilities, including some who rely on screen readers. What accessibility feature should you implement?</p>""",
        [
            ("Add alt text to all visuals describing key insights, data context, and purpose", True),
            ("Increase the number of visuals on each page to provide more data", False),
            ("Use bright colors to make the report stand out", False),
            ("Simplify the report by removing all filters and slicers", False),
        ],
        """<p>Correct! Alt text is essential for accessibility, enabling screen readers to convey visual content to users with vision impairments. Alt text should describe the visual type, main insights, and purpose of the data shown.</p>""",
    ),
    (
        """<p>You want to add contextual information that appears when users hover over a chart bar—showing sales count, revenue, and customer details for that data point. Which Power BI feature is best suited for this?</p>""",
        [
            ("Report-page tooltip with custom visuals and measures", True),
            ("Conditional formatting with data bars", False),
            ("Visual interactions with filter mode", False),
            ("Mobile layout configuration", False),
        ],
        """<p>Correct! Report-page tooltips are dedicated pages designed as rich, interactive contexts. They can include multiple visuals and DAX measures that dynamically show context for the hovered data point, providing detailed insights without cluttering the main report.</p>""",
    ),
    (
        """<p>In your report, clicking a region in one visual should filter related visuals to show only that region's data. How do you configure this?</p>""",
        [
            ("Select the source visual, then Format &gt; Edit interactions, and set target visuals to 'Filter' mode", True),
            ("Use sync slicers to automatically link all regions across pages", False),
            ("Create a bookmark for each region", False),
            ("Apply conditional formatting based on region values", False),
        ],
        """<p>Correct! Visual interactions with 'Filter' mode enable cross-filtering. When users click a value in the source visual, connected target visuals filter to display only related data, supporting guided exploration and analysis.</p>""",
    ),
    (
        """<p>You have created several conditional formatting rules in your table: red background for sales below target, and icons showing performance level (green arrow up, yellow dash, red arrow down). A colleague with color blindness says they cannot interpret the red/green formatting. What should you do?</p>""",
        [
            ("Combine color with additional visual elements like icons, patterns, or labels; avoid relying on color alone", True),
            ("Remove all conditional formatting to simplify the report", False),
            ("Increase the font size of all numbers", False),
            ("Switch to a mobile layout design", False),
        ],
        """<p>Correct! Accessibility best practice requires not using color alone to convey meaning. Pair colors with icons, text labels, or patterns so users with color blindness can still interpret the data. The combination of colors and icons ensures information is accessible to all users.</p>""",
    ),
    (
        """<p>You want your report slicer for 'Date Range' to filter visuals consistently across three different report pages without being visible on pages 2 and 3. What should you configure?</p>""",
        [
            ("Enable 'Sync slicers' and choose which pages synchronize; hide the slicer on pages 2 and 3 while maintaining the sync", True),
            ("Create three separate slicers, one on each page, with identical settings", False),
            ("Use a bookmark for each date range and have users switch bookmarks", False),
            ("Apply page-level filters instead of using a slicer", False),
        ],
        """<p>Correct! Sync slicers allows a single slicer selection to propagate across multiple pages while keeping the slicer itself hidden on secondary pages. This creates a unified filter experience without visual redundancy.</p>""",
    ),
]