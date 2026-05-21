LESSON_HTML = """
<style>
  .lsn-h2{font-size:1.5rem;font-weight:600;margin:32px 0 12px;letter-spacing:-0.005em;}
  .lsn-h3{font-size:1.25rem;font-weight:600;margin:24px 0 10px;}
  .lsn-p{font-size:1.0625rem;line-height:1.7;margin:0 0 14px;}
  .lsn-ul{font-size:1.0625rem;line-height:1.7;margin:0 0 18px 1.25rem;padding:0;}
  .lsn-callout{background:rgba(127,127,127,.10);padding:14px 18px;border-radius:6px;margin:18px 0;}
  .lsn-warn{background:rgba(127,127,127,.14);padding:14px 18px;border-radius:6px;margin:18px 0;}
  .lsn-table{width:100%;border-collapse:collapse;margin:14px 0 22px;font-size:0.95rem;}
  .lsn-table th,.lsn-table td{border:1px solid rgba(127,127,127,.35);padding:10px 12px;text-align:left;vertical-align:top;}
  .lsn-table th{background:rgba(127,127,127,.10);font-weight:600;}
  .lsn-code{font-family:monospace;background:rgba(127,127,127,.05);padding:2px 6px;border-radius:3px;}
</style>

<p class="lsn-p">A well-designed data model is the foundation of effective Power BI analytics. This lesson covers the core concepts and techniques for designing and implementing models that support both performance and usability: configuring table and column metadata, defining relationships with appropriate cardinality and filtering, implementing star schema architecture, managing role-playing dimensions, creating date tables, and implementing row-level security.</p>

<div class="lsn-callout"><strong>Learning objectives.</strong> By the end of this lesson you should be able to: configure table and column properties; define relationships and their cardinality; implement a star schema design; manage multiple relationship contexts with role-playing dimensions; create and mark date tables; and implement row-level security roles.</div>

<h2 class="lsn-h2">1. Understanding the Star Schema</h2>

<p class="lsn-p">A <strong>star schema</strong> organizes data into a central <em>fact table</em> (containing measures and foreign keys) surrounded by <em>dimension tables</em> (containing attributes). This design optimizes query performance and simplifies calculations.</p>

<p class="lsn-p"><strong>Star schema example:</strong></p>

<table class="lsn-table">
  <thead>
    <tr>
      <th colspan='4' style='text-align:center;'>STAR SCHEMA — Sales Analytics</th>
    </tr>
    <tr>
      <th style='width:25%;'>Dimension: Date</th>
      <th style='width:25%;'>Fact: Sales (Center)</th>
      <th style='width:25%;'>Dimension: Product</th>
      <th style='width:25%;'>Dimension: Customer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>DateKey</code> (PK)<br><code>Date</code><br><code>Year</code><br><code>Month</code><br><code>Quarter</code></td>
      <td><code>SalesKey</code> (PK)<br><code>DateKey</code> (FK)<br><code>ProductKey</code> (FK)<br><code>CustomerKey</code> (FK)<br><code>Amount</code><br><code>Quantity</code></td>
      <td><code>ProductKey</code> (PK)<br><code>ProductName</code><br><code>Category</code><br><code>SubCategory</code><br><code>Price</code></td>
      <td><code>CustomerKey</code> (PK)<br><code>CustomerName</code><br><code>Country</code><br><code>City</code><br><code>Region</code></td>
    </tr>
  </tbody>
</table>

<p class="lsn-p"><strong>Benefits of star schema:</strong></p>
<ul class="lsn-ul">
  <li>Simpler queries &mdash; fewer joins across fewer tables.</li>
  <li>Better performance &mdash; dimension tables are typically small and highly cacheable.</li>
  <li>Easier to understand &mdash; clear separation of facts (measures) and descriptive attributes.</li>
  <li>Scalable calculations &mdash; measures aggregated along multiple dimensions without complex logic.</li>
</ul>

<p class="lsn-p">A <strong>snowflake schema</strong> further normalizes dimensions into sub-tables. While it saves storage, it increases query complexity and reduces performance. For Power BI, a pure star schema is preferred.</p>

<h2 class="lsn-h2">2. Defining Relationships and Cardinality</h2>

<p class="lsn-p">Relationships connect tables so that filters and calculations flow correctly. Each relationship has two critical properties: <strong>cardinality</strong> and <strong>cross-filter direction</strong>.</p>

<h3 class="lsn-h3">Cardinality Types</h3>

<table class="lsn-table">
  <thead>
    <tr><th>Cardinality</th><th>Description</th><th>Typical Use</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>One-to-Many (1:*)</strong></td>
      <td>One row in the first table can match many rows in the second. This is the <em>most common</em> cardinality.</td>
      <td>Dimension &rarr; Fact (e.g., one Date to many Sales)</td>
    </tr>
    <tr>
      <td><strong>Many-to-One (*:1)</strong></td>
      <td>Equivalent to 1:* but with tables reversed in direction.</td>
      <td>Fact &rarr; Dimension (e.g., many Sales from one Product)</td>
    </tr>
    <tr>
      <td><strong>Many-to-Many (*:*)</strong></td>
      <td>Rows in both tables can match many rows in the other. Requires careful implementation.</td>
      <td>Employees to Projects (one employee on many projects, one project has many employees)</td>
    </tr>
    <tr>
      <td><strong>One-to-One (1:1)</strong></td>
      <td>Each row in one table matches exactly one row in the other. Rare in analytics.</td>
      <td>Employee ID &rarr; Unique SocialSecurityNumber</td>
    </tr>
  </tbody>
</table>

<h3 class="lsn-h3">Cross-Filter Direction</h3>

<p class="lsn-p">Cross-filter direction determines how filters propagate between tables:</p>

<ul class="lsn-ul">
  <li><strong>Single</strong> (default): Filters flow <em>from</em> the primary table <em>to</em> the related table. Example: filter Date table &rarr; affects Sales fact table. Dimension filters impact fact measures.</li>
  <li><strong>Both</strong>: Filters flow in <em>both</em> directions. Use cautiously; can create ambiguous calculations and slower queries. Common in peer-to-peer relationships.</li>
</ul>

<div class="lsn-callout">In most star schemas, set cross-filter direction to <strong>Single</strong> from dimension to fact. Use <strong>Both</strong> only when necessary to avoid unexpected filter interactions.</div>

<h2 class="lsn-h2">3. Configuring Table and Column Properties</h2>

<p class="lsn-p">Power BI stores metadata about tables and columns to optimize display and calculation:</p>

<h3 class="lsn-h3">Table Properties</h3>

<ul class="lsn-ul">
  <li><strong>Display folder</strong>: Organize related tables in the field list hierarchy. Example: put &ldquo;Customer&rdquo;, &ldquo;Product&rdquo; and &ldquo;Region&rdquo; in a &ldquo;Dimensions&rdquo; folder.</li>
  <li><strong>Row label</strong>: Designates which column uniquely identifies rows (used in some visuals for identity display).</li>
  <li><strong>Row image</strong>: Column containing images to display in certain visuals.</li>
</ul>

<h3 class="lsn-h3">Column Properties</h3>

<table class="lsn-table">
  <thead>
    <tr><th>Property</th><th>Purpose</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Data Category</strong></td>
      <td>Tells Power BI what the column represents: <code>Uncategorized</code>, <code>Address</code>, <code>City</code>, <code>Continent</code>, <code>Country</code>, <code>County</code>, <code>Date</code>, <code>Image</code>, <code>URL</code>, etc. Used for map visuals and smart defaults.</td>
    </tr>
    <tr>
      <td><strong>Default Summarization</strong></td>
      <td>Sets how the column aggregates by default: <code>Sum</code>, <code>Average</code>, <code>Min</code>, <code>Max</code>, <code>Count</code>, <code>Count (Distinct)</code>, or <code>Don&apos;t Summarize</code>. Set dimension keys to <code>Don&apos;t Summarize</code>.</td>
    </tr>
    <tr>
      <td><strong>Sort By Column</strong></td>
      <td>Specifies a second column to sort by when this column is used. Example: sort Month Name by Month Number.</td>
    </tr>
    <tr>
      <td><strong>Display Folder</strong></td>
      <td>Organize columns within a table hierarchy in the field pane. Keep fact columns separate from dimensions.</td>
    </tr>
    <tr>
      <td><strong>Hidden</strong></td>
      <td>Remove columns from the field list if they are only for internal calculations or lookups.</td>
    </tr>
  </tbody>
</table>

<h2 class="lsn-h2">4. Implementing a Date Table</h2>

<p class="lsn-p">A <strong>date table</strong> is a special dimension containing every date in your analysis range, with pre-calculated attributes like Year, Month, Quarter, and fiscal periods. Power BI can then optimize time-based calculations.</p>

<h3 class="lsn-h3">Marking a Table as a Date Table</h3>

<ol class="lsn-ul">
  <li>Create or import a table with a single Date column (one row per date, no duplicates).</li>
  <li>Ensure the column is of data type <code>Date</code> (not <code>DateTime</code>).</li>
  <li>In Power BI Desktop, select the table in the Data view, then go to <strong>Table Tools &rarr; Mark as Date Table</strong>. Select the date column.</li>
  <li>Power BI will validate and cache the table for use in time-intelligence functions.</li>
</ol>

<div class="lsn-warn"><strong>Important:</strong> A model can have <em>only one</em> date table marked as the default. If you need multiple date contexts (e.g., Order Date, Ship Date), you must manage them with <strong>role-playing dimensions</strong> (see below).</div>

<p class="lsn-p"><strong>Example date table attributes:</strong></p>
<pre><code class='language-dax'>Date (PK)       | Year | Quarter | Month | MonthName | DayOfWeek | DayName | WeekNum | FiscalYear
2023-01-01      | 2023 |    Q1   |  1    |  January  |     1     | Sunday  |   52    |  2023
2023-01-02      | 2023 |    Q1   |  1    |  January  |     2     | Monday  |   1     |  2023
</code></pre>

<h2 class="lsn-h2">5. Role-Playing Dimensions</h2>

<p class="lsn-p">A <strong>role-playing dimension</strong> is a single dimension table used in multiple relationship contexts. The classic example is a Date dimension used for &ldquo;Order Date&rdquo;, &ldquo;Ship Date&rdquo;, and &ldquo;Delivery Date&rdquo; simultaneously.</p>

<h3 class="lsn-h3">Why Role-Playing Dimensions Matter</h3>

<p class="lsn-p">Without role-playing, you would need separate copies of the date table (DateOrder, DateShip, DateDelivery), which wastes storage and complicates maintenance.</p>

<h3 class="lsn-h3">Implementation Steps</h3>

<ol class="lsn-ul">
  <li>Create one Date dimension with DateKey and all attributes.</li>
  <li>Create multiple foreign-key columns in the fact table: <code>OrderDateKey</code>, <code>ShipDateKey</code>, <code>DeliveryDateKey</code>.</li>
  <li>Create separate relationships: one from Date[DateKey] to Sales[OrderDateKey], another to Sales[ShipDateKey], etc.</li>
  <li><strong>Important:</strong> Deactivate all but one relationship by default. Power BI can only have one active path at a time.</li>
</ol>

<h3 class="lsn-h3">Using USERELATIONSHIP in DAX</h3>

<p class="lsn-p">When you have multiple relationships, you need to explicitly activate the correct one in your measure:</p>

<pre><code class='language-dax'>OrderCount = 
    CALCULATE(
        COALESCE(SUM(Sales[Quantity]), 0),
        USERELATIONSHIP(Sales[OrderDateKey], Date[DateKey])
    )

ShipCount = 
    CALCULATE(
        COALESCE(SUM(Sales[Quantity]), 0),
        USERELATIONSHIP(Sales[ShipDateKey], Date[DateKey])
    )
</code></pre>

<p class="lsn-p">The <code>USERELATIONSHIP()</code> function activates a specific (normally inactive) relationship for the duration of the calculation.</p>

<h2 class="lsn-h2">6. Implementing Row-Level Security (RLS)</h2>

<p class="lsn-p"><strong>Row-Level Security</strong> restricts which rows a user can see in Power BI based on their identity. Common use: sales managers see only their region's data.</p>

<h3 class="lsn-h3">Setting Up RLS Roles</h3>

<ol class="lsn-ul">
  <li>In Power BI Desktop, go to the <strong>Modeling</strong> tab and select <strong>Manage Roles</strong>.</li>
  <li>Create a new role (e.g., &ldquo;SalesWest&rdquo;).</li>
  <li>Select a table and write a DAX filter expression. The filter returns <code>TRUE</code> for rows the user can see.</li>
</ol>

<h3 class="lsn-h3">Example RLS DAX Filter</h3>

<pre><code class='language-dax'>[Region] = &quot;West&quot;
</code></pre>

<p class="lsn-p">This filter on the Region table ensures users in the &ldquo;SalesWest&rdquo; role see only rows where Region equals &ldquo;West&rdquo;. The filter cascades through relationships to fact tables.</p>

<h3 class="lsn-h3">Advanced RLS: Using USERNAME()</h3>

<p class="lsn-p">You can integrate RLS with user directory identities using the <code>USERNAME()</code> function:</p>

<pre><code class='language-dax'>[ManagerEmail] = USERNAME()
</code></pre>

<p class="lsn-p">This allows Power BI to automatically match the logged-in user with their manager record and restrict data accordingly.</p>

<div class="lsn-callout"><strong>Best practice:</strong> Always test RLS by clicking &ldquo;View as Role&rdquo; in Desktop before publishing to the service.</div>

<h2 class="lsn-h2">7. Many-to-Many Relationships</h2>

<p class="lsn-p">A many-to-many (M:M) relationship exists when both tables can have multiple matches. Example: a Students table and a Courses table, where one student takes many courses and one course has many students.</p>

<p class="lsn-p"><strong>Implementation:</strong> Use a <em>junction table</em> (also called bridge or lookup table) to connect them. The junction table contains foreign keys from both sides and has one-to-many relationships with each.</p>

<table class="lsn-table">
  <thead>
    <tr><th>Students</th><th>StudentCourse (Junction)</th><th>Courses</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>StudentID (PK)</code><br><code>Name</code></td>
      <td><code>StudentID (FK)</code><br><code>CourseID (FK)</code><br><code>Enrollment Date</code></td>
      <td><code>CourseID (PK)</code><br><code>Title</code></td>
    </tr>
  </tbody>
</table>

<p class="lsn-p">Then create relationships: Students[StudentID] → StudentCourse[StudentID] and Courses[CourseID] → StudentCourse[CourseID], both one-to-many.</p>

<h2 class="lsn-h2">8. Summary</h2>

<ul class="lsn-ul">
  <li>Use a <strong>star schema</strong> with a central fact table and surrounding dimension tables for optimal query performance.</li>
  <li>Define relationships with correct <strong>cardinality</strong> (1:*, *:1, 1:1, *:*) and <strong>cross-filter direction</strong> (Single or Both).</li>
  <li>Configure <strong>column properties</strong>: data category, default summarization, sort-by column, and display folders to improve usability.</li>
  <li><strong>Mark a date table</strong> and use it for all time-based calculations to enable time-intelligence functions.</li>
  <li>Implement <strong>role-playing dimensions</strong> using multiple relationships and <code>USERELATIONSHIP()</code> to handle multiple date contexts.</li>
  <li>Implement <strong>RLS roles</strong> with DAX filters to restrict row visibility by user identity.</li>
  <li>Use a <strong>junction table</strong> to implement many-to-many relationships cleanly.</li>
</ul>
"""

QUESTIONS = [
    (
        'multiple_choice',
        'Which best describes the difference between a <strong>star schema</strong> and a <strong>snowflake schema</strong>?',
        [
            ('A star schema has one fact table with direct joins to denormalized dimensions, while a snowflake further normalizes dimensions into hierarchical sub-tables.', True),
            ('A star schema uses many-to-many relationships; a snowflake uses only one-to-many.', False),
            ('A snowflake schema is always faster because it is more normalized.', False),
            ('They are identical; the terms are just different names for the same design.', False),
        ],
        'A star schema prioritizes query simplicity and performance with denormalized dimensions. A snowflake normalizes further, reducing redundancy but increasing join complexity. For Power BI, a pure star schema is recommended.'
    ),
    (
        'multiple_choice',
        'In a star schema, fact tables typically contain&hellip;',
        [
            ('&hellip;foreign keys (to dimensions) and measures (numeric values for aggregation).', True),
            ('&hellip;only descriptive attributes and no numeric data.', False),
            ('&hellip;all denormalized dimension attributes to eliminate joins.', False),
            ('&hellip;a single numeric column and many text columns for filtering.', False),
        ],
        'Fact tables hold quantitative measures (sales amount, quantity) and foreign keys linking to dimension tables. Dimensions hold descriptive attributes (product name, region).'
    ),
    (
        'multiple_choice',
        'When defining a relationship with <strong>Many-to-One (</strong>*<strong>:1) cardinality</strong> and <strong>Single</strong> cross-filter direction, filters flow&hellip;',
        [
            ('&hellip;from the &ldquo;One&rdquo; table to the &ldquo;Many&rdquo; table only.', True),
            ('&hellip;from the &ldquo;Many&rdquo; table to the &ldquo;One&rdquo; table only.', False),
            ('&hellip;in both directions simultaneously.', False),
            ('&hellip;based on the order tables are added to a visual.', False),
        ],
        'Single direction filters flow from the primary key side (the &ldquo;One&rdquo;) to the foreign key side (the &ldquo;Many&rdquo;). Use the side with the 1 as your filter source.'
    ),
    (
        'multiple_choice',
        'A table contains three date columns: <code>OrderDate</code>, <code>ShipDate</code>, and <code>DeliveryDate</code>. All three need to relate to a single Date dimension. How should you implement this?',
        [
            ('Create three separate relationships (one for each date key) and deactivate all but one by default. Use <code>USERELATIONSHIP()</code> in measures to activate the correct relationship as needed.', True),
            ('Create three separate Date dimensions (DateOrder, DateShip, DateDelivery).', False),
            ('Create one relationship and configure it to use &ldquo;Both&rdquo; cross-filter direction.', False),
            ('Use column-level security to restrict which date column each user can access.', False),
        ],
        'This is a role-playing dimension. Multiple relationships to the same table require careful management: only one active by default, with <code>USERELATIONSHIP()</code> to switch contexts in DAX calculations.'
    ),
    (
        'true_false',
        'When you mark a table as a <strong>Date Table</strong>, Power BI automatically creates a column hierarchy and enables time-intelligence DAX functions like <code>SAMEPERIODLASTYEAR()</code>.&nbsp;<code>YTD()</code>, and <code>TOTALYTD()</code>.',
        [
            ('True', True),
            ('False', False),
        ],
        'Marking a date table registers it as the default time dimension, enabling time-intelligence functions and optimizing date-based calculations and hierarchies.'
    ),
    (
        'multiple_choice',
        'Which column property should you set to <code>Don&apos;t Summarize</code>?',
        [
            ('Dimension key columns (like ProductID, CustomerID) that uniquely identify rows but are not meant for aggregation.', True),
            ('Numeric measures like SalesAmount or Quantity.', False),
            ('Text attributes like ProductName or Region.', False),
            ('Any column used in a relationship as a foreign key.', False),
        ],
        'Key columns should never be summed or averaged. Setting <code>Don&apos;t Summarize</code> prevents accidental aggregation and ensures they behave as identifiers, not measures.'
    ),
    (
        'multiple_choice',
        'Row-Level Security (RLS) is configured by&hellip;',
        [
            ('&hellip;creating roles in Power BI Desktop and writing DAX filter expressions that determine which rows each role can see.', True),
            ('&hellip;using column-level encryption in the data source.', False),
            ('&hellip;filtering data in the Power Query editor before loading into the model.', False),
            ('&hellip;applying SharePoint permissions to the report.', False),
        ],
        'RLS is a Power BI modeling feature: define roles, assign DAX filter expressions, and test with &ldquo;View as Role&rdquo;. Filters cascade through relationships to restrict row access by user identity.'
    ),
    (
        'multiple_choice',
        'Which is the <strong>most common cardinality</strong> for relationships between dimension and fact tables in a star schema?',
        [
            ('One-to-Many (1:*) — each dimension row matches many fact rows.', True),
            ('Many-to-Many (*:*) — dimensions and facts both have multiple matches.', False),
            ('One-to-One (1:1) — each dimension row matches exactly one fact row.', False),
            ('Many-to-One (*:1) — fact tables link to dimension rows many-to-one.', False),
        ],
        'In a star schema, dimension tables (one side) have one-to-many relationships to the central fact table (many side). This design enables efficient filtering and aggregation.'
    ),
]


def upsert():
    with app.app_context():
        course = Course.query.filter(Course.title.like(COURSE_TITLE_LIKE)).first()
        if not course:
            print('PL-300 course not found.')
            return

        # 1. Lesson body
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
                order=3,
                points=1.0,
            )
            db.session.add(lesson)
            db.session.flush()
            print(f'inserted lesson {lesson.id}')

        # 2. Quiz
        quiz = Quiz.query.filter_by(course_id=course.id, title=QUIZ_TITLE).first()
        if not quiz:
            quiz = Quiz(course_id=course.id, title=QUIZ_TITLE,
                        description='Check your understanding of data model design, relationships, and best practices.')
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

        # 3. Exam lesson linking to the quiz
        exam = Lesson.query.filter_by(course_id=course.id, title=EXAM_LESSON_TITLE,
                                       content_type='exam').first()
        if exam:
            exam.quiz_id = quiz.id
            exam.order = 4
            print(f'updated exam lesson {exam.id}')
        else:
            exam = Lesson(
                title=EXAM_LESSON_TITLE,
                content='',
                course_id=course.id,
                content_type='exam',
                quiz_id=quiz.id,
                order=4,
                points=1.0,
            )
            db.session.add(exam)
            db.session.flush()
            print(f'inserted exam lesson {exam.id}')

        db.session.commit()
        print('done.')


if __name__ == '__main__':
    upsert()