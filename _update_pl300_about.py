"""Replace PL-300 About lesson content with the April 20, 2026 Skills Measured outline."""
from app import app, db, Lesson

ABOUT_HTML = """
<h2>Purpose of this course</h2>
<p>This course prepares you for the <strong>Microsoft Certified: Power BI Data Analyst Associate (PL-300)</strong> certification. You will learn to deliver actionable insights by working with available data and applying domain expertise &mdash; providing business value through clear visualizations and enabling self-service analytics.</p>
<p>You will use <strong>Power Query</strong> and <strong>DAX</strong> to prepare, model, visualize, and analyze data, and you will learn how to manage and secure Power BI assets in a workspace.</p>

<h2>Useful links</h2>
<table>
  <thead>
    <tr><th>Resource</th><th>Link</th></tr>
  </thead>
  <tbody>
    <tr><td>Certification page</td><td><a href="https://learn.microsoft.com/credentials/certifications/data-analyst-associate/" target="_blank" rel="noopener">Microsoft Certified: Power BI Data Analyst Associate</a></td></tr>
    <tr><td>Exam page (PL-300)</td><td><a href="https://learn.microsoft.com/credentials/certifications/exams/pl-300/" target="_blank" rel="noopener">Exam PL-300: Microsoft Power BI Data Analyst</a></td></tr>
    <tr><td>Power BI documentation</td><td><a href="https://learn.microsoft.com/power-bi/" target="_blank" rel="noopener">learn.microsoft.com/power-bi</a></td></tr>
    <tr><td>Practice assessment</td><td><a href="https://learn.microsoft.com/credentials/certifications/exams/pl-300/practice/assessment" target="_blank" rel="noopener">PL-300 Practice Assessment</a></td></tr>
    <tr><td>Exam Readiness Zone</td><td><a href="https://learn.microsoft.com/shows/exam-readiness-zone/" target="_blank" rel="noopener">Exam Readiness Zone | Microsoft Learn</a></td></tr>
  </tbody>
</table>

<h2>About the exam</h2>
<blockquote><p><strong>Note:</strong> This page lists the Skills Measured <strong>as of April 20, 2026</strong>. Always check the official exam page for the latest version before sitting the exam.</p></blockquote>
<blockquote><p><strong>Note:</strong> The PL-300 exam validates your ability to deliver actionable insights using Power BI: preparing and modeling data, designing reports for usability and storytelling, identifying patterns and trends, and managing and securing Power BI content.</p></blockquote>

<h2>Skills measured as of April 20, 2026</h2>

<h3>Audience profile</h3>
<p>As a candidate for this exam, you should deliver actionable insights by working with available data and applying domain expertise. You should:</p>
<ul>
  <li>Provide meaningful business value through easy-to-comprehend data visualizations.</li>
  <li>Enable others to perform self-service analytics.</li>
</ul>
<p>As a Power BI data analyst, you work closely with business stakeholders to identify business requirements. You collaborate with analytics engineers and data engineers to identify and acquire data. You use Power BI to:</p>
<ul>
  <li>Prepare the data</li>
  <li>Model the data</li>
  <li>Visualize and analyze data</li>
  <li>Manage and secure Power BI</li>
</ul>
<p>You should be proficient at using <strong>Power Query</strong> and <strong>Data Analysis Expressions (DAX)</strong>.</p>

<h3>Skills at a glance</h3>
<table>
  <thead>
    <tr><th>Functional group</th><th>Weight</th></tr>
  </thead>
  <tbody>
    <tr><td>Prepare the data</td><td>25&ndash;30%</td></tr>
    <tr><td>Model the data</td><td>25&ndash;30%</td></tr>
    <tr><td>Visualize and analyze the data</td><td>25&ndash;30%</td></tr>
    <tr><td>Manage and secure Power BI</td><td>15&ndash;20%</td></tr>
  </tbody>
</table>

<h3>Prepare the data (25&ndash;30%)</h3>
<p><strong>Get or connect to data</strong></p>
<ul>
  <li>Identify and connect to data sources or a shared semantic model</li>
  <li>Change data source settings, including credentials and privacy levels</li>
  <li>Choose between <strong>DirectLake</strong>, <strong>DirectQuery</strong>, and <strong>Import</strong></li>
  <li>Create and modify parameters</li>
</ul>
<p><strong>Profile and clean the data</strong></p>
<ul>
  <li>Evaluate data, including data statistics and column properties</li>
  <li>Resolve inconsistencies, unexpected or null values, and data quality issues</li>
  <li>Resolve data import errors</li>
</ul>
<p><strong>Transform and load the data</strong></p>
<ul>
  <li>Select appropriate column data types</li>
  <li>Create and transform columns</li>
  <li>Group and aggregate rows</li>
  <li>Pivot, unpivot, and transpose data</li>
  <li>Convert semi-structured data to a table</li>
  <li>Create fact tables and dimension tables</li>
  <li>Identify when to use reference or duplicate queries and the resulting impact</li>
  <li>Merge and append queries</li>
  <li>Identify and create appropriate keys for relationships</li>
  <li>Configure data loading for queries</li>
</ul>

<h3>Model the data (25&ndash;30%)</h3>
<p><strong>Design and implement a data model</strong></p>
<ul>
  <li>Configure table and column properties</li>
  <li>Implement role-playing dimensions</li>
  <li>Define a relationship's cardinality and cross-filter direction</li>
  <li>Create a common date table</li>
  <li>Identify use cases for calculated columns and calculated tables</li>
</ul>
<p><strong>Create model calculations by using DAX</strong></p>
<ul>
  <li>Create single aggregation measures</li>
  <li>Use the <code>CALCULATE</code> function</li>
  <li>Implement time intelligence measures</li>
  <li>Use basic statistical functions</li>
  <li>Create semi-additive measures</li>
  <li>Create a measure by using quick measures</li>
  <li>Create calculated tables or columns</li>
  <li>Create calculation groups</li>
</ul>
<p><strong>Optimize model performance</strong></p>
<ul>
  <li>Improve performance by identifying and removing unnecessary rows and columns</li>
  <li>Identify poorly performing measures, relationships, and visuals by using <strong>Performance Analyzer</strong> and <strong>DAX query view</strong></li>
  <li>Improve performance by reducing granularity</li>
</ul>

<h3>Visualize and analyze the data (25&ndash;30%)</h3>
<p><strong>Create reports</strong></p>
<ul>
  <li>Select an appropriate visual</li>
  <li>Format and configure visuals</li>
  <li>Create a narrative visual with <strong>Copilot</strong></li>
  <li>Apply and customize a theme</li>
  <li>Apply conditional formatting</li>
  <li>Apply slicing and filtering</li>
  <li>Use Copilot to create a new report page</li>
  <li>Use Copilot to suggest content for a new report page</li>
  <li>Configure the report page</li>
  <li>Choose when to use a paginated report</li>
  <li>Create visual calculations by using DAX</li>
</ul>
<p><strong>Enhance reports for usability and storytelling</strong></p>
<ul>
  <li>Configure bookmarks</li>
  <li>Create custom tooltips</li>
  <li>Edit and configure interactions between visuals</li>
  <li>Configure navigation for a report</li>
  <li>Apply sorting to visuals</li>
  <li>Configure sync slicers</li>
  <li>Group and layer visuals by using the <strong>Selection</strong> pane</li>
  <li>Configure drillthrough navigation, including pages, filters, and buttons</li>
  <li>Configure export settings</li>
  <li>Design reports for mobile devices</li>
  <li>Enable personalization in a report, including personalized visuals</li>
  <li>Design and configure Power BI reports for accessibility</li>
  <li>Configure automatic page refresh</li>
</ul>
<p><strong>Identify patterns and trends</strong></p>
<ul>
  <li>Use the <strong>Analyze</strong> feature in Power BI</li>
  <li>Use grouping, binning, and clustering</li>
  <li>Use AI visuals</li>
  <li>Use reference lines, error bars, and forecasting</li>
  <li>Detect outliers and anomalies</li>
  <li>Use Copilot to summarize the underlying semantic model</li>
</ul>

<h3>Manage and secure Power BI (15&ndash;20%)</h3>
<p><strong>Create and manage workspaces and assets</strong></p>
<ul>
  <li>Create and configure a workspace</li>
  <li>Configure and update an app</li>
  <li>Publish, import, or update items in a workspace</li>
  <li>Create dashboards</li>
  <li>Choose a distribution method</li>
  <li>Configure subscriptions and data alerts</li>
  <li>Promote or certify Power BI content</li>
  <li>Identify when a gateway is required</li>
  <li>Configure a semantic model scheduled refresh</li>
</ul>
<p><strong>Secure and govern Power BI items</strong></p>
<ul>
  <li>Assign workspace roles</li>
  <li>Configure item-level access</li>
  <li>Configure access to semantic models</li>
  <li>Implement row-level security roles</li>
  <li>Configure row-level security group membership</li>
  <li>Apply sensitivity labels</li>
</ul>

<h2>Change log</h2>
<p>The table below summarizes the changes between the current and previous version of the skills measured.</p>
<table>
  <thead>
    <tr><th>Skill area prior to April 20, 2026</th><th>Skill area as of April 20, 2026</th><th>Change</th></tr>
  </thead>
  <tbody>
    <tr><td>Audience profile</td><td>Audience profile</td><td>No change</td></tr>
    <tr><td>Prepare the data</td><td>Prepare the data</td><td>No change</td></tr>
    <tr><td>Get or connect to data</td><td>Get or connect to data</td><td>Minor</td></tr>
    <tr><td>Visualize and analyze the data</td><td>Visualize and analyze the data</td><td>No change</td></tr>
    <tr><td>Enhance reports for usability and storytelling</td><td>Enhance reports for usability and storytelling</td><td>Minor</td></tr>
    <tr><td>Manage and secure Power BI</td><td>Manage and secure Power BI</td><td>No change</td></tr>
    <tr><td>Create and manage workspaces and assets</td><td>Create and manage workspaces and assets</td><td>Minor</td></tr>
  </tbody>
</table>

<h2>Study resources</h2>
<table>
  <thead>
    <tr><th>Study resource</th><th>Links to learning and documentation</th></tr>
  </thead>
  <tbody>
    <tr><td>Get trained</td><td><a href="https://learn.microsoft.com/training/courses/pl-300t00" target="_blank" rel="noopener">Self-paced learning paths and modules / instructor-led course (PL-300T00)</a></td></tr>
    <tr><td>Find documentation</td><td><a href="https://learn.microsoft.com/power-bi/" target="_blank" rel="noopener">Power BI documentation</a> &middot; <a href="https://learn.microsoft.com/power-platform/" target="_blank" rel="noopener">Power Platform documentation</a></td></tr>
    <tr><td>Ask a question</td><td><a href="https://learn.microsoft.com/answers/" target="_blank" rel="noopener">Microsoft Q&amp;A</a></td></tr>
    <tr><td>Get community support</td><td><a href="https://community.powerbi.com/" target="_blank" rel="noopener">Power BI Community</a></td></tr>
    <tr><td>Follow Microsoft Learn</td><td><a href="https://techcommunity.microsoft.com/category/microsoftlearn" target="_blank" rel="noopener">Microsoft Learn &mdash; Tech Community</a></td></tr>
    <tr><td>Find a video</td><td><a href="https://learn.microsoft.com/shows/exam-readiness-zone/" target="_blank" rel="noopener">Exam Readiness Zone</a> &middot; <a href="https://learn.microsoft.com/shows/less-code-more-power/" target="_blank" rel="noopener">#LessCodeMorePower</a></td></tr>
  </tbody>
</table>
""".strip()


def main():
    with app.app_context():
        L = Lesson.query.filter_by(course_id=4, order=1).first()
        if not L:
            raise SystemExit('PL-300 About lesson not found')
        L.content = ABOUT_HTML
        db.session.commit()
        print(f'updated lesson id={L.id} title={L.title!r} new_content_len={len(L.content)}')


if __name__ == '__main__':
    main()
