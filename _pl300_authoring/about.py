ABOUT_HTML = '''
<div class='course-about'>
  <h1>Microsoft PL-300: Power BI Data Analyst</h1>

  <h2>Welcome</h2>
  <p>This comprehensive course prepares you to pass the <strong>Microsoft PL-300 (Power BI Data Analyst)</strong> certification exam. The exam validates your ability to prepare, model, visualize, and maintain Power BI solutions in production environments.</p>

  <h2>Course Structure</h2>
  <p>The course is organized into <strong>9 topic lessons</strong>, each with an <strong>8-question quiz</strong> to reinforce key concepts. After completing all lessons, you will face a <strong>25-question cumulative final exam</strong> that mirrors the style and difficulty of the official certification exam.</p>
  <ul>
    <li><strong>Lesson 1:</strong> Get data from data sources</li>
    <li><strong>Lesson 2:</strong> Clean, transform, and load data with Power Query</li>
    <li><strong>Lesson 3:</strong> Design and implement a data model</li>
    <li><strong>Lesson 4:</strong> Create model calculations using DAX</li>
    <li><strong>Lesson 5:</strong> Optimize model performance</li>
    <li><strong>Lesson 6:</strong> Create reports &mdash; visualizations and formatting</li>
    <li><strong>Lesson 7:</strong> Enhance reports for usability and storytelling</li>
    <li><strong>Lesson 8:</strong> Identify patterns and trends &mdash; analytics and AI visuals</li>
    <li><strong>Lesson 9:</strong> Deploy and maintain assets &mdash; workspaces, datasets, sharing</li>
  </ul>

  <h2>About the Exam</h2>
  <p><strong>Format:</strong> 40&ndash;60 multiple-choice and multiple-select questions</p>
  <p><strong>Duration:</strong> 100 minutes for the exam; 130 minutes total seat time (includes check-in and tutorial)</p>
  <p><strong>Passing Score:</strong> 700 out of 1000</p>
  <p><strong>Delivery:</strong> Pearson VUE (online or at testing centers worldwide)</p>
  <p><strong>Language:</strong> English (with some regional translations available)</p>

  <h2>Skills Measured</h2>
  <p>The exam assesses four key competencies, with the following weightings:</p>
  <ul>
    <li><strong>Prepare the Data (25&ndash;30%):</strong> Connect to data sources, handle authentication, import and transform data, and apply data quality checks.</li>
    <li><strong>Model the Data (25&ndash;30%):</strong> Design tables and relationships, create hierarchies, define roles and row-level security, and optimize schema design.</li>
    <li><strong>Visualize and Analyze the Data (25&ndash;30%):</strong> Create reports, build interactive visuals, apply formatting and conditional logic, and tell stories with data.</li>
    <li><strong>Deploy and Maintain Assets (15&ndash;20%):</strong> Publish to Power BI Service, configure workspaces, manage datasets, set up sharing and row-level security, and monitor performance.</li>
  </ul>

  <h2>Official Microsoft Exam-Prep Video Series</h2>
  <p>Microsoft's <em>Exam Readiness Zone</em> publishes a free 4-part video walkthrough for PL-300, one episode per skills domain. Watching these alongside the lessons below is highly recommended.</p>
  <ul>
    <li><a href='https://learn.microsoft.com/en-us/shows/exam-readiness-zone/preparing-for-pl-300-prepare-the-data' target='_blank' rel='noopener'>Part 1 of 4 &mdash; Prepare the Data</a> (Lessons 1&ndash;2)</li>
    <li><a href='https://learn.microsoft.com/en-us/shows/exam-readiness-zone/preparing-for-pl-300-model-the-data' target='_blank' rel='noopener'>Part 2 of 4 &mdash; Model the Data</a> (Lessons 3&ndash;5)</li>
    <li><a href='https://learn.microsoft.com/en-us/shows/exam-readiness-zone/preparing-for-pl-300-visualize-and-analyze-the-data' target='_blank' rel='noopener'>Part 3 of 4 &mdash; Visualize and Analyze the Data</a> (Lessons 6&ndash;8)</li>
    <li><a href='https://learn.microsoft.com/en-us/shows/exam-readiness-zone/preparing-for-pl-300-manage-and-secure-power-bi' target='_blank' rel='noopener'>Part 4 of 4 &mdash; Manage and Secure Power BI</a> (Lesson 9)</li>
  </ul>

  <h2>Study Resources</h2>
  <p>Use these official Microsoft resources to supplement your learning:</p>
  <ul>
    <li><a href='https://learn.microsoft.com/en-us/credentials/certifications/exams/pl-300' target='_blank' rel='noopener'>Microsoft Learn: PL-300 Study Guide</a></li>
    <li><a href='https://www.microsoft.com/en-us/download/details.aspx?id=58494' target='_blank' rel='noopener'>Power BI Desktop (free download)</a></li>
    <li><a href='https://app.powerbi.com' target='_blank' rel='noopener'>Power BI Service</a></li>
    <li><a href='https://learn.microsoft.com/en-us/answers/topics/power-bi.html' target='_blank' rel='noopener'>Microsoft Q&amp;A: Power BI</a></li>
    <li><a href='https://learn.microsoft.com/en-us/shows/exam-readiness-zone/' target='_blank' rel='noopener'>Exam Readiness Zone (all videos)</a></li>
  </ul>

  <h2>How This Course is Organized</h2>
  <p>Each lesson combines <strong>conceptual explanations</strong> with <strong>hands-on practice</strong> to build your skills progressively. The first 6 lessons focus on core data preparation, modeling, and visualization. Lessons 7&ndash;9 cover advanced topics: user experience, analytics, and production deployment.</p>
  <p>Take the quiz after each lesson to identify gaps in your knowledge. Review the explanations for any incorrect answers. When you have completed all 9 lessons, take the final exam to assess your readiness for the official certification.</p>
  <p><strong>Good luck in your Power BI journey!</strong></p>

  <hr>

  <h1>Official Microsoft Study Guide for Exam PL-300</h1>
  <p><em>Reproduced from Microsoft Learn &mdash; last updated 03/20/2026; skills measured as of April 20, 2026.</em></p>

  <h2>Purpose of this document</h2>
  <p>This study guide should help you understand what to expect on the exam and includes a summary of the topics the exam might cover and links to additional resources. The information and materials in this document should help you focus your studies as you prepare for the exam.</p>

  <h2>Useful links</h2>
  <table class='table table-bordered table-sm'>
    <thead><tr><th>Link</th><th>Description</th></tr></thead>
    <tbody>
      <tr><td><a href='https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/' target='_blank' rel='noopener'>How to earn the certification</a></td><td>Some certifications only require passing one exam, while others require passing multiple exams.</td></tr>
      <tr><td><a href='https://learn.microsoft.com/en-us/credentials/certifications/renew-your-microsoft-certification' target='_blank' rel='noopener'>Certification renewal</a></td><td>Microsoft associate, expert, and specialty certifications expire annually. You can renew by passing a free online assessment on Microsoft Learn.</td></tr>
      <tr><td><a href='https://learn.microsoft.com/en-us/users/me/' target='_blank' rel='noopener'>Your Microsoft Learn profile</a></td><td>Connecting your certification profile to Microsoft Learn allows you to schedule and renew exams and share and print certificates.</td></tr>
      <tr><td><a href='https://learn.microsoft.com/en-us/credentials/certifications/exam-scoring-reports' target='_blank' rel='noopener'>Exam scoring and score reports</a></td><td>A score of 700 or greater is required to pass.</td></tr>
      <tr><td><a href='https://aka.ms/examdemo' target='_blank' rel='noopener'>Exam sandbox</a></td><td>You can explore the exam environment by visiting our exam sandbox.</td></tr>
      <tr><td><a href='https://learn.microsoft.com/en-us/credentials/certifications/request-accommodations' target='_blank' rel='noopener'>Request accommodations</a></td><td>If you use assistive devices, require extra time, or need modification to any part of the exam experience, you can request an accommodation.</td></tr>
      <tr><td><a href='https://learn.microsoft.com/en-us/credentials/certifications/exams/pl-300/practice/assessment?assessment-type=practice&amp;assessmentId=38' target='_blank' rel='noopener'>Take a free Practice Assessment</a></td><td>Test your skills with practice questions to help you prepare for the exam.</td></tr>
    </tbody>
  </table>

  <h2>Updates to the exam</h2>
  <p>Our exams are updated periodically to reflect skills that are required to perform a role. We have included two versions of the Skills Measured objectives depending on when you are taking the exam.</p>
  <p>We always update the English language version of the exam first. Some exams are localized into other languages, and those are updated approximately eight weeks after the English version is updated. Although Microsoft makes every effort to update localized versions as noted, there may be times when the localized versions of an exam are not updated on this schedule. Other available languages are listed in the Schedule Exam section of the Exam Details webpage. If the exam isn't available in your preferred language, you can request an additional 30 minutes to complete the exam.</p>
  <p><strong>Note:</strong> The bullets that follow each of the skills measured are intended to illustrate how we are assessing that skill. Related topics may be covered in the exam.</p>
  <p><strong>Note:</strong> Most questions cover features that are general availability (GA). The exam may contain questions on Preview features if those features are commonly used.</p>

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
  <p>You should be proficient at using Power Query and Data Analysis Expressions (DAX).</p>

  <h3>Skills at a glance</h3>
  <ul>
    <li>Prepare the data (25&ndash;30%)</li>
    <li>Model the data (25&ndash;30%)</li>
    <li>Visualize and analyze the data (25&ndash;30%)</li>
    <li>Manage and secure Power BI (15&ndash;20%)</li>
  </ul>

  <h3>Prepare the data (25&ndash;30%)</h3>
  <p><strong>Get or connect to data</strong></p>
  <ul>
    <li>Identify and connect to data sources or a shared semantic model</li>
    <li>Change data source settings, including credentials and privacy levels</li>
    <li>Choose between DirectLake, DirectQuery, and Import</li>
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
    <li>Use the CALCULATE function</li>
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
    <li>Identify poorly performing measures, relationships, and visuals by using Performance Analyzer and DAX query view</li>
    <li>Improve performance by reducing granularity</li>
  </ul>

  <h3>Visualize and analyze the data (25&ndash;30%)</h3>
  <p><strong>Create reports</strong></p>
  <ul>
    <li>Select an appropriate visual</li>
    <li>Format and configure visuals</li>
    <li>Create a narrative visual with Copilot</li>
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
    <li>Group and layer visuals by using the Selection pane</li>
    <li>Configure drillthrough navigation, including pages, filters, and buttons</li>
    <li>Configure export settings</li>
    <li>Design reports for mobile devices</li>
    <li>Enable personalization in a report, including personalized visuals</li>
    <li>Design and configure Power BI reports for accessibility</li>
    <li>Configure automatic page refresh</li>
  </ul>
  <p><strong>Identify patterns and trends</strong></p>
  <ul>
    <li>Use the Analyze feature in Power BI</li>
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

  <h2>Study resources</h2>
  <p>We recommend that you train and get hands-on experience before you take the exam. We offer self-study options and classroom training as well as links to documentation, community sites, and videos.</p>
  <table class='table table-bordered table-sm'>
    <thead><tr><th>Study resources</th><th>Links to learning and documentation</th></tr></thead>
    <tbody>
      <tr><td>Get trained</td><td><a href='https://learn.microsoft.com/en-us/training/browse/?expanded=power-platform&amp;products=power-bi' target='_blank' rel='noopener'>Choose from self-paced learning paths and modules</a> or take an instructor-led course</td></tr>
      <tr><td>Find documentation</td><td><a href='https://learn.microsoft.com/en-us/power-bi/' target='_blank' rel='noopener'>Power BI documentation</a> &middot; <a href='https://learn.microsoft.com/en-us/power-apps/' target='_blank' rel='noopener'>Microsoft Power Apps documentation</a></td></tr>
      <tr><td>Ask a question</td><td><a href='https://learn.microsoft.com/en-us/answers/' target='_blank' rel='noopener'>Microsoft Q&amp;A | Microsoft Docs</a></td></tr>
      <tr><td>Get community support</td><td><a href='https://powerusers.microsoft.com/t5/Power-Apps-Community/ct-p/PowerApps1' target='_blank' rel='noopener'>Power Apps</a> &middot; <a href='https://powerusers.microsoft.com/t5/Power-Query/bd-p/Power_Query' target='_blank' rel='noopener'>Power Query</a> &middot; <a href='https://powerusers.microsoft.com/t5/Building-Power-Apps/bd-p/PowerAppsForum1' target='_blank' rel='noopener'>Building Power Apps</a></td></tr>
      <tr><td>Follow Microsoft Learn</td><td><a href='https://techcommunity.microsoft.com/t5/microsoft-learn/ct-p/MicrosoftLearn' target='_blank' rel='noopener'>Microsoft Learn &mdash; Microsoft Tech Community</a></td></tr>
      <tr><td>Find a video</td><td><a href='https://learn.microsoft.com/en-us/shows/exam-readiness-zone/' target='_blank' rel='noopener'>Exam Readiness Zone | Microsoft Learn</a> &middot; <a href='https://learn.microsoft.com/en-us/shows/less-code-more-power/' target='_blank' rel='noopener'>#LessCodeMorePower</a> &middot; <a href='https://learn.microsoft.com/en-us/shows/browse' target='_blank' rel='noopener'>Browse other Microsoft Learn shows</a></td></tr>
    </tbody>
  </table>

  <h2>Change log</h2>
  <p>The table below summarizes the changes between the current and previous version of the skills measured.</p>
  <table class='table table-bordered table-sm'>
    <thead><tr><th>Skill area prior to April 20, 2026</th><th>Skill area as of April 20, 2026</th><th>Change</th></tr></thead>
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

  <h2>Additional resources</h2>
  <ul>
    <li><strong>Practice Assessment:</strong> <a href='https://learn.microsoft.com/en-us/credentials/certifications/exams/pl-300/practice/assessment?assessment-type=practice&amp;assessmentId=38' target='_blank' rel='noopener'>PL-300 Practice Assessment</a></li>
    <li><strong>Training &mdash; Learning path:</strong> <a href='https://learn.microsoft.com/en-us/training/paths/solution-architect-design-power-platform-solutions/' target='_blank' rel='noopener'>Solution Architect: Design Microsoft Power Platform solutions</a> &mdash; Learn how a solution architect designs solutions.</li>
    <li><strong>Certification:</strong> <a href='https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/' target='_blank' rel='noopener'>Microsoft Certified: Power BI Data Analyst Associate</a> &mdash; Demonstrate methods and best practices that align with business and technical requirements for modeling, visualizing, and analyzing data with Microsoft Power BI.</li>
  </ul>
  <p><em>Last updated on 03/20/2026.</em></p>
</div>
'''
