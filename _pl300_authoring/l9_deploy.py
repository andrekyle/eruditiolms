LESSON_HTML = """
<style>
  .lsn-h2{font-size:1.5rem;font-weight:600;margin:32px 0 12px;letter-spacing:-0.005em;}
  .lsn-h3{font-size:1.25rem;font-weight:600;margin:24px 0 10px;letter-spacing:-0.005em;}
  .lsn-p{font-size:1.0625rem;line-height:1.7;margin:0 0 14px;}
  .lsn-ul{font-size:1.0625rem;line-height:1.7;margin:0 0 18px 1.25rem;padding:0;}
  .lsn-ul li{margin:6px 0;}
  .lsn-callout{background:rgba(127,127,127,.10);padding:14px 18px;border-radius:6px;margin:18px 0;}
  .lsn-warn{background:rgba(127,127,127,.14);padding:14px 18px;border-radius:6px;margin:18px 0;}
  .lsn-table{width:100%;border-collapse:collapse;margin:14px 0 22px;font-size:1rem;}
  .lsn-table th,.lsn-table td{border:1px solid rgba(127,127,127,.35);padding:10px 12px;text-align:left;vertical-align:top;}
  .lsn-table th{background:rgba(127,127,127,.10);font-weight:600;}
  .lsn-code{background:rgba(127,127,127,.08);padding:2px 6px;border-radius:3px;font-family:monospace;font-size:.95em;}
</style>

<p class='lsn-p'><strong>Deploying and maintaining Power BI assets</strong> requires understanding workspaces, dataset sharing strategies, security models, refresh pipelines, and monitoring. In this lesson you will learn how to establish governance, enable collaboration, secure data at row level, and keep reports and semantic models performing reliably in production.</p>

<div class='lsn-callout'><strong>Learning objectives.</strong> By the end of this lesson you should be able to: create and manage workspaces with appropriate role assignments; design a deployment lifecycle (Dev/Test/Prod); publish and manage Power BI Apps; share semantic models and configure row-level security; configure data refresh, alerts, and subscriptions; identify when gateways are required; and recommend endorsement strategies for content governance.</div>

<h2 class='lsn-h2'>1. Creating and Managing Workspaces</h2>

<h3 class='lsn-h3'>My Workspace vs Collaborative Workspaces</h3>

<p class='lsn-p'><strong>My Workspace</strong> is a personal workspace where you can develop reports and dashboards without sharing. It is bound to your user account and cannot be shared with others. Use it for prototyping and personal analysis.</p>

<p class='lsn-p'><strong>Collaborative Workspaces</strong> (sometimes called &quot;regular workspaces&quot;) are created at the tenant or organizational level and can be shared with multiple users. They support role-based access control, app publishing, and shared semantic models. Always use collaborative workspaces for team projects, reports meant for stakeholder consumption, and datasets that multiple reports will reference.</p>

<h3 class='lsn-h3'>Workspace Roles and Permissions</h3>

<p class='lsn-p'>Power BI defines four primary workspace roles. Each controls what a user can do with reports, dashboards, datasets, and other artifacts:</p>

<table class='lsn-table'>
  <thead>
    <tr>
      <th>Role</th>
      <th>Admin</th>
      <th>Member</th>
      <th>Contributor</th>
      <th>Viewer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Edit &amp; publish reports</strong></td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>-</td>
    </tr>
    <tr>
      <td><strong>Create/edit datasets</strong></td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>-</td>
    </tr>
    <tr>
      <td><strong>View &amp; interact</strong></td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>&#10004;</td>
    </tr>
    <tr>
      <td><strong>Manage workspace</strong></td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>-</td>
      <td style='text-align:center;'>-</td>
      <td style='text-align:center;'>-</td>
    </tr>
    <tr>
      <td><strong>Assign roles</strong></td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>-</td>
      <td style='text-align:center;'>-</td>
      <td style='text-align:center;'>-</td>
    </tr>
    <tr>
      <td><strong>Delete workspace</strong></td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>-</td>
      <td style='text-align:center;'>-</td>
      <td style='text-align:center;'>-</td>
    </tr>
    <tr>
      <td><strong>Build Power BI apps</strong></td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>&#10004;</td>
      <td style='text-align:center;'>-</td>
      <td style='text-align:center;'>-</td>
    </tr>
  </tbody>
</table>

<p class='lsn-p'><strong>Admin:</strong> Full control. Can add and remove users, change roles, update workspace settings, and delete the workspace. There must be at least one Admin per workspace.</p>

<p class='lsn-p'><strong>Member:</strong> Can create, edit, and publish content; cannot manage the workspace or assign roles. Members can publish Power BI apps.</p>

<p class='lsn-p'><strong>Contributor:</strong> Can create and edit content but <em>cannot publish Power BI apps</em>. Useful for report writers who feed content to Members who handle app publication.</p>

<p class='lsn-p'><strong>Viewer:</strong> Read-only access. Can view and interact with reports, dashboards, and datasets but cannot edit or publish anything.</p>

<h2 class='lsn-h2'>2. Development Lifecycle and Deployment Pipelines</h2>

<p class='lsn-p'>Production Power BI environments require discipline: code review, testing, and staged rollout. The recommended strategy uses three workspaces:</p>

<ul class='lsn-ul'>
  <li><strong>Development (Dev):</strong> Where report authors build and experiment. Data may be test or sample data. Frequent changes are expected.</li>
  <li><strong>Testing (Test/Staging):</strong> Where business users and stakeholders validate reports before release. Data is close to or identical to production. Strict change control applies.</li>
  <li><strong>Production (Prod):</strong> Live environment. Users consume published reports and apps. Access is restricted; only tested, approved changes deploy here.</li>
</ul>

<p class='lsn-p'>Use <span class='lsn-code'>git</span> or a version-control system to track report definitions and Power BI projects. Automate deployment using Power BI REST APIs, Azure Synapse Pipelines, or third-party CI/CD tools. This ensures auditability and rollback capability.</p>

<p class='lsn-p'>Microsoft Power BI Premium also supports <strong>Deployment Pipelines</strong> (a managed feature), which allows you to clone workspaces and promote content through Dev &rarr; Test &rarr; Prod with a single click, configurable validation rules, and optional parameter overrides for connection strings and data sources.</p>

<h2 class='lsn-h2'>3. Publishing, Importing, and Updating Assets</h2>

<p class='lsn-p'>Once a report or dashboard is authored in Power BI Desktop, you <strong>publish</strong> it to a workspace using &quot;Publish&quot; in the File menu. The semantic model (dataset) is published alongside the report. If a dataset with the same name already exists, you choose to replace it or create a new one.</p>

<p class='lsn-p'><strong>Updating assets:</strong> Edit the report or dataset in Desktop and publish again. If the schema changes (new columns, renamed measures), the update may fail if dashboards or other reports depend on the old structure. Coordinate with stakeholders and test in a non-production workspace first.</p>

<p class='lsn-p'><strong>Importing:</strong> You can also import Power BI Desktop files (.pbix) and Excel workbooks directly from the Power BI Service. Go to Workspaces &gt; Get Data &gt; Files. This creates a copy of the report and dataset in the workspace.</p>

<h2 class='lsn-h2'>4. Creating and Configuring Power BI Apps</h2>

<p class='lsn-p'>A <strong>Power BI App</strong> is a curated, versioned collection of reports and dashboards from a workspace, packaged for end-user consumption. Apps separate authoring (in the workspace) from consumption (the app). Users do not see the workspace; they only see the app.</p>

<p class='lsn-p'><strong>To create an app:</strong></p>

<ul class='lsn-ul'>
  <li>In the workspace, click &quot;Create app&quot; (top right).</li>
  <li>Name the app and add a description.</li>
  <li>Choose which reports and dashboards to include.</li>
  <li>Set navigation order and default landing page.</li>
  <li>Define permissions: &quot;Everyone&quot;, specific users/groups, or security groups.</li>
  <li>Publish the app.</li>
</ul>

<p class='lsn-p'>Once published, app users see a read-only experience (by default). They can view, filter, and export data but not edit reports or change the dataset connection. If you need to allow editing, enable &quot;Allow users to create copies of reports in this app&quot; &mdash; this lets users personalize their own copies.</p>

<p class='lsn-p'>Apps support role-based security. After publishing, you can update the app to change included artifacts or permissions without re-publishing.</p>

<h2 class='lsn-h2'>5. Sharing Semantic Models and Recommending Strategies</h2>

<p class='lsn-p'>A <strong>semantic model</strong> (formerly called a &quot;dataset&quot;) is a reusable, governed data layer that supports multiple reports. If one team maintains a comprehensive data model, other teams' report authors can build reports on top of it without managing ETL or data connections themselves.</p>

<p class='lsn-p'><strong>Build vs. Import modes:</strong></p>

<ul class='lsn-ul'>
  <li><strong>Build mode:</strong> Report author has Desktop, imports or creates the semantic model, publishes to workspace. Author owns the model and can modify it.</li>
  <li><strong>Import mode (shared model):</strong> A central team publishes a semantic model to a workspace. Other report authors, in different workspaces, connect to that shared model using &quot;Analyze in Excel&quot; or by creating a report &quot;based on this dataset&quot; in the Power BI Service. They build reports without owning or modifying the model.</li>
</ul>

<p class='lsn-p'><strong>Recommendation:</strong> For large organizations, establish a &quot;semantic model hub&quot; workspace. A data engineering team manages approved, high-quality datasets. Report authors discover and reuse them, reducing data silos and ensuring consistency. Apply row-level security (RLS) at the semantic model layer so users see only their authorized data.</p>

<h2 class='lsn-h2'>6. Configuring Subscriptions, Alerts, and Data-Driven Alerts</h2>

<p class='lsn-p'><strong>Subscriptions:</strong> Users can subscribe to a report or dashboard snapshot. On a schedule (daily, weekly, etc.), Power BI emails the user a .pdf, .pptx, or link to the current report. Useful for stakeholders who want periodic updates without logging into Power BI.</p>

<p class='lsn-p'><strong>Alerts:</strong> Users set a threshold on a KPI card or gauge visual. If the value crosses that threshold, Power BI sends an alert notification. For example: &quot;Notify me if sales drop below $100k.&quot;</p>

<p class='lsn-p'><strong>Data-driven alerts:</strong> Similar to alerts but triggered automatically when underlying data changes. Admins can configure these at the semantic model level and push them to users based on rules.</p>

<p class='lsn-p'>Configure subscriptions and alerts in the Power BI Service from the report or dashboard; set frequency, recipients, and conditions. Both features respect row-level security, so subscribers see only data they are authorized to view.</p>

<h2 class='lsn-h2'>7. Configuring Row-Level Security (RLS)</h2>

<p class='lsn-p'>Row-level security ensures users see only authorized rows of data. In a sales report, each region manager sees only their region; in HR, employees see only their own profile.</p>

<p class='lsn-p'><strong>How RLS works:</strong></p>

<ul class='lsn-ul'>
  <li>In Power BI Desktop, define a role with a DAX filter (e.g., <span class='lsn-code'>[Region] = USERNAME()</span>).</li>
  <li>Publish the report to the workspace.</li>
  <li>In the Power BI Service (Datasets tab), go to the dataset settings &gt; Security.</li>
  <li>Assign users or security groups to roles.</li>
</ul>

<p class='lsn-p'><strong>RLS applies when:</strong> A user views a report in the Power BI Service or embedded report. It does NOT apply in Power BI Desktop (the author sees all data) or when exporting to Excel (the exported file contains all rows unless specifically restricted).</p>

<p class='lsn-p'><strong>Best practices:</strong> Use Azure AD security groups, not individual users, for easier maintenance. Test RLS with a test user account before deployment. Document role definitions and assignments for compliance and audits.</p>

<h2 class='lsn-h2'>8. Promoting and Certifying Content (Endorsement)</h2>

<p class='lsn-p'>Power BI endorsement is a governance feature that signals content quality and trustworthiness:</p>

<ul class='lsn-ul'>
  <li><strong>Promoted:</strong> A workspace Admin or Member marks a report, dashboard, or dataset as &quot;promoted&quot; &mdash; a soft recommendation. Promoted content displays a &quot;promoted&quot; badge in search results and lists.</li>
  <li><strong>Certified:</strong> Only Admins with &quot;Certifier&quot; permissions can certify. A certified badge signals that the content meets organizational standards (data quality, security, testing). This is a stronger endorsement.</li>
</ul>

<p class='lsn-p'>Endorsement appears in Power BI mobile apps, the Power BI homepage, and app catalogs. Use it to guide users toward high-quality, approved datasets and reports, reducing confusion and supporting governance.</p>

<h2 class='lsn-h2'>9. Identifying When a Gateway Is Required</h2>

<p class='lsn-p'>Power BI connects to data sources. Some are cloud-based (Azure SQL, SharePoint Online, Dataverse); others are on-premises (SQL Server, Oracle, file shares). A <strong>gateway</strong> is a bridge.</p>

<table class='lsn-table'>
  <thead>
    <tr>
      <th>Scenario</th>
      <th>Gateway Required?</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Azure SQL Database</td>
      <td style='text-align:center;'>No</td>
      <td>Cloud-native</td>
    </tr>
    <tr>
      <td>SQL Server (on-premises)</td>
      <td style='text-align:center;'>Yes</td>
      <td>On-Prem Gateway</td>
    </tr>
    <tr>
      <td>SharePoint Online</td>
      <td style='text-align:center;'>No</td>
      <td>Cloud-native</td>
    </tr>
    <tr>
      <td>Excel file on local drive</td>
      <td style='text-align:center;'>Yes</td>
      <td>On-Prem Gateway</td>
    </tr>
    <tr>
      <td>Dynamics 365 (cloud)</td>
      <td style='text-align:center;'>No</td>
      <td>Cloud-native</td>
    </tr>
    <tr>
      <td>Teradata (on-premises)</td>
      <td style='text-align:center;'>Yes</td>
      <td>On-Prem Gateway</td>
    </tr>
    <tr>
      <td>SAP HANA (on-premises or VNet)</td>
      <td style='text-align:center;'>Yes</td>
      <td>On-Prem or VNet Gateway</td>
    </tr>
    <tr>
      <td>REST API (internet-accessible)</td>
      <td style='text-align:center;'>No</td>
      <td>Cloud-native</td>
    </tr>
  </tbody>
</table>

<p class='lsn-p'><strong>On-Premises Data Gateway:</strong> Installed on a machine within your network. Power BI Cloud connects to the gateway, which queries on-premises databases and returns results. Requires credentials and ongoing management (patching, monitoring). Typically installed on a dedicated server or VM for reliability.</p>

<p class='lsn-p'><strong>VNet Gateway (Power BI Premium):</strong> For Premium customers, a managed gateway hosted in an Azure Virtual Network. Used for connections to on-premises or private cloud data sources within the VNet. Reduces management overhead.</p>

<h2 class='lsn-h2'>10. Configuring Scheduled Refresh and Monitoring</h2>

<p class='lsn-p'>Power BI datasets can be refreshed on a schedule. Users see updated data without manual action. Refresh frequency and options depend on licensing and data source type.</p>

<p class='lsn-p'><strong>Refresh frequency limits (Power BI Pro):</strong> Up to 8 times per day (every 3 hours minimum). Premium supports up to 48 refreshes per day.</p>

<p class='lsn-p'><strong>Incremental refresh:</strong> If your dataset is large, refreshing all rows every time is slow and expensive. Use incremental refresh to refresh only new or changed data. Define a date column and a RangeStart/RangeEnd parameter. Power BI refreshes rows within the rolling window, improving performance and reducing query load on the source system.</p>

<p class='lsn-p'><strong>To configure scheduled refresh:</strong></p>

<ul class='lsn-ul'>
  <li>In Power BI Service, go to Datasets and select your dataset.</li>
  <li>Click Settings &gt; Scheduled refresh.</li>
  <li>Enable refresh, set frequency and time zone.</li>
  <li>Provide credentials for the data source (if needed).</li>
  <li>For incremental refresh, enable it and define the window and parameters in Desktop before publishing.</li>
</ul>

<p class='lsn-p'><strong>Monitoring refresh failures:</strong> Go to Datasets, click the three dots on your dataset, and select &quot;Refresh history.&quot; You see success/failure, duration, and error messages. Common issues: invalid credentials, gateway offline, query timeout, data source unavailable. Set up email notifications (Power BI Admin Portal) to alert you when a refresh fails. Proactively investigate and remedy to keep reports current.</p>

<div class='lsn-warn'><strong>Key takeaway:</strong> Deploy with discipline &mdash; use Dev/Test/Prod workspaces, share datasets wisely, secure data with RLS, monitor refresh and user activity, and endorse trusted content. A well-governed environment builds user confidence and organizational data literacy.</div>
"""

QUESTIONS = [
    (
        'multiple_choice',
        'A data analyst needs to create a shared semantic model for use by multiple report authors across the organization. Which workspace role should be assigned to the report authors who will build reports on the model but not modify it?',
        [
            ('Viewer', True),
            ('Contributor', False),
            ('Member', False),
            ('Admin', False),
        ],
        'Viewers can interact with and build reports on shared datasets without editing the dataset itself. Contributor and Member roles allow editing, which is unnecessary for report authors building on a central, governed semantic model. Admin is excessive.'
    ),
    (
        'multiple_choice',
        'Your organization uses a Dev/Test/Prod deployment pipeline. A new report has been approved in Test and is ready for production. Which of the following is <strong>most important</strong> before promoting to Prod?',
        [
            ('Verify that row-level security rules are correctly assigned to users and groups who will access the report.', True),
            ('Ensure the report is published from Power BI Mobile.', False),
            ('Confirm that all users have granted access to the dataset.', False),
            ('Check that the report name matches the dataset name exactly.', False),
        ],
        'Before moving a report to production, you must verify security, especially row-level security, to prevent unauthorized data access. The other options do not represent critical pre-deployment checks.'
    ),
    (
        'true_false',
        'An end user subscribed to a sales report has row-level security applied. The user will receive a snapshot of the full dataset in their subscription email, ignoring their RLS role.',
        [
            ('False', True),
            ('True', False),
        ],
        'Subscriptions respect row-level security. The user receives a snapshot of only the data rows they are authorized to view, even in email attachments. RLS is never bypassed by subscriptions, alerts, or exports.'
    ),
    (
        'multiple_choice',
        'Your organization stores customer data in an on-premises SQL Server database. Power BI Desktop connects to this data successfully. However, after publishing the report to the Power BI Service, the dataset cannot refresh. What is the most likely cause?',
        [
            ('An on-premises data gateway is not installed and configured to connect to the SQL Server.', True),
            ('The Power BI Service license tier is not Premium.', False),
            ('The report contains too many visuals for the Service to refresh.', False),
            ('Row-level security has not been configured for the dataset.', False),
        ],
        'On-premises SQL Server requires an on-premises data gateway for scheduled refresh in the Power BI Service. Without it, the Service cannot reach the database. Premium license and RLS do not determine refresh capability for on-premises sources.'
    ),
    (
        'multiple_choice',
        'A Contributor in a workspace wants to publish a new Power BI app to distribute reports to stakeholders. What will happen?',
        [
            ('The action will fail. Contributors cannot publish Power BI apps; only Members and Admins can.', True),
            ('The action will succeed, and the app will be published immediately.', False),
            ('The action will succeed only if a Member approves it first.', False),
            ('The action will succeed, but the app will be in draft mode until an Admin publishes it.', False),
        ],
        'Contributors can create and edit reports and datasets but cannot publish Power BI apps. Only Members and Admins have app publication rights. This separates content creation from distribution governance.'
    ),
    (
        'multiple_choice',
        'Your organization has a large, frequently-updated sales dataset that grows by thousands of rows every day. Refresh currently takes 90 minutes at 8 AM each morning, and stakeholders need more frequent updates. Which strategy will improve refresh speed and enable more frequent refreshing?',
        [
            ('Enable incremental refresh, restricting the refresh to rows within a rolling 7-day window.', True),
            ('Upgrade all users to Power BI Premium.', False),
            ('Split the dataset into two smaller datasets.', False),
            ('Move the data source from SQL Server to Azure SQL Database.', False),
        ],
        'Incremental refresh updates only new or recently changed rows within a time window, dramatically reducing query volume and refresh duration. This enables more frequent refreshes without straining the source system. Premium licensing is not required for incremental refresh, and splitting datasets introduces complexity.'
    ),
    (
        'multiple_choice',
        'A report author is publishing a new dataset from Power BI Desktop and receives a certificate approval badge request. The author is not an Admin. What should the author do?',
        [
            ('Ask a Power BI Admin with Certifier permissions to review and certify the dataset after it is published and has demonstrated quality and compliance.', True),
            ('Cancel the publish and rebuild the dataset with more aggregations.', False),
            ('Certify it themselves before publishing.', False),
            ('Promote it in the Power BI Service immediately after publishing.', False),
        ],
        'Only Power BI Admins with Certifier permissions can certify datasets. Authors can promote datasets, but certification requires Admin action and represents a formal quality and compliance seal. The author should publish, then request certification.'
    ),
    (
        'multiple_choice',
        'A semantic model contains sales data for multiple regions. You want to configure row-level security so that each regional manager sees only their region. Which DAX filter expression, assigned to a role and applied to the relevant table, would correctly implement this?',
        [
            ('[Region] = USERNAME()', True),
            ('[Region] = USERPRINCIPALNAME()', False),
            ('[Manager] = CURRENTUSER()', False),
            ('[Region] != "Other"', False),
        ],
        'The USERNAME() function returns the logged-in user&apos;s name (e.g., domain\\user). Filtering [Region] = USERNAME() restricts the user to rows matching their username as the region. USERPRINCIPALNAME() returns email; CURRENTUSER() does not exist in DAX. The fourth option filters out a single value, not by user.'
    ),
]


def upsert():
    with app.app_context():
        course = Course.query.filter(Course.title.like(COURSE_TITLE_LIKE)).first()
        if not course:
            print('PL-300 course not found.')
            return

        lesson = Lesson.query.filter_by(course_id=course.id, title=LESSON_TITLE).first()
        if lesson:
            lesson.content = LESSON_HTML
            lesson.content_type = 'lesson'
            print(f'updated lesson {lesson.id}')
        else:
            lesson = Lesson(
                title=LESSON_TITLE,
                content=LESSON_HTML,
                course_id=course.id,
                content_type='lesson',
                order=9,
                points=1.0,
            )
            db.session.add(lesson)
            db.session.flush()
            print(f'inserted lesson {lesson.id}')

        quiz = Quiz.query.filter_by(course_id=course.id, title=QUIZ_TITLE).first()
        if not quiz:
            quiz = Quiz(course_id=course.id, title=QUIZ_TITLE,
                        description='Check your understanding of workspaces, deployment pipelines, dataset sharing, row-level security, gateways, refresh, and content governance.')
            db.session.add(quiz)
            db.session.flush()
            print(f'inserted quiz {quiz.id}')
        else:
            print(f'quiz {quiz.id} already exists; rebuilding questions')
            for q in list(quiz.questions):
                db.session.delete(q)
            db.session.flush()

        for qtype, qhtml, opts, feedback in QUESTIONS:
            q = Question(quiz_id=quiz.id, question_type=qtype, question_html=qhtml,
                         points=1.0, feedback=feedback)
            db.session.add(q)
            db.session.flush()
            for i, (ohtml, correct) in enumerate(opts):
                db.session.add(QuestionOption(
                    question_id=q.id, option_html=ohtml, is_correct=correct, order=i
                ))

        exam = Lesson.query.filter_by(course_id=course.id, title=EXAM_LESSON_TITLE,
                                       content_type='exam').first()
        if exam:
            exam.quiz_id = quiz.id
            exam.order = 10
            print(f'updated exam lesson {exam.id}')
        else:
            exam = Lesson(
                title=EXAM_LESSON_TITLE,
                content=LESSON_HTML,
                course_id=course.id,
                content_type='exam',
                quiz_id=quiz.id,
                order=10,
                points=1.0,
            )
            db.session.add(exam)
            print(f'inserted exam lesson {exam.id}')

        db.session.commit()
        print('upsert complete')


if __name__ == '__main__':
    upsert()