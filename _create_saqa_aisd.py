"""Create the SAQA Occupational Certificate: Artificial Intelligence Software Developer course.

Idempotent: re-running updates the course title/description and the
About lesson's content rather than creating duplicates.

Source: SAQA Qual ID 118792, EXCO 0522/24.
"""
from app import app, db, Course, Lesson

COURSE_TITLE = 'SAQA 118792: Occupational Certificate: Artificial Intelligence Software Developer'
COURSE_DESCRIPTION = (
    'NQF Level 5, 209 credits. SAQA-registered Occupational Certificate (QCTO / MICT SETA) '
    'that prepares learners to operate as Artificial Intelligence Software Developers. '
    'Covers AI, machine learning, deep learning, Python, SQL, TensorFlow, mathematics and '
    'statistics for programming, design thinking, governance and ethics, plus workplace '
    'experience in AI solution design, testing, and deployment.'
)
TEACHER_ID = 1

ABOUT_TITLE = 'About this course'
ABOUT_HTML = """
<h2>SAQA registered qualification</h2>
<p>This course is structured around the South African Qualifications Authority (SAQA) registered qualification <strong>Occupational Certificate: Artificial Intelligence Software Developer</strong>.</p>

<table>
  <thead>
    <tr><th>Attribute</th><th>Detail</th></tr>
  </thead>
  <tbody>
    <tr><td>SAQA Qual ID</td><td>118792</td></tr>
    <tr><td>Originator</td><td>Development Quality Partner &mdash; MICT SETA</td></tr>
    <tr><td>NQF Sub-Framework</td><td>OQSF &mdash; Occupational Qualifications Sub-framework</td></tr>
    <tr><td>Qualification Type</td><td>Occupational Certificate</td></tr>
    <tr><td>Field</td><td>Field 10 &mdash; Physical, Mathematical, Computer and Life Sciences</td></tr>
    <tr><td>Subfield</td><td>Information Technology and Computer Sciences</td></tr>
    <tr><td>NQF Level</td><td>NQF Level 05</td></tr>
    <tr><td>Minimum Credits</td><td>209</td></tr>
    <tr><td>Qual Class</td><td>Regular-ELOAC</td></tr>
    <tr><td>SAQA Decision Number</td><td>EXCO 0522/24</td></tr>
    <tr><td>Registration Status</td><td>Passed the End Date &mdash; status was &ldquo;Registered&rdquo;</td></tr>
    <tr><td>Registration Start Date</td><td>2022-02-03</td></tr>
    <tr><td>Registration End Date</td><td>2025-12-31</td></tr>
    <tr><td>Last Date for Enrolment</td><td>2026-12-31</td></tr>
    <tr><td>Last Date for Achievement</td><td>2029-12-31</td></tr>
    <tr><td>Curriculum code</td><td>251201-002-00-00</td></tr>
    <tr><td>Assessment Quality Partner (AQP)</td><td>MICT SETA</td></tr>
  </tbody>
</table>

<blockquote><p><strong>Note:</strong> All qualifications and part qualifications registered on the National Qualifications Framework are public property. The only payment that can be made for them is for service and reproduction. It is illegal to sell this material for profit. If the material is reproduced or quoted, the South African Qualifications Authority (SAQA) should be acknowledged as the source.</p></blockquote>

<h2>Purpose</h2>
<p>The purpose of the Occupational Certificate: Artificial Intelligence Software Developer is to prepare a learner to operate as an Artificial Intelligence Software Developer.</p>
<p>AI Software Developers build AI functionality into software applications by integrating and implementing AI algorithms and logic into the deliverables of an IT project. Developers teach the machine to solve problems the way a human would through the use of programming. They create, test, and deploy code, and also assist in converting machine learning APIs so that other applications can use them.</p>
<p>A qualified learner will be able to:</p>
<ul>
  <li>Interpret solution design documentation and develop an AI solution.</li>
  <li>Train the AI model through a machine learning process and test performance to ensure that model accuracy is strictly maintained within the selection framework.</li>
  <li>Deploy the AI solution and maintain the solution to ensure model accuracy is strictly maintained.</li>
</ul>

<h2>Rationale</h2>
<p>This qualification was developed in response to the report of the Presidential Commission on the 4th Industrial Revolution (4IR), which forefronts human capital and the future of work and refers to growing skills instability. The extent of 4IR today and its impact on businesses and the economy is unparalleled, implying that companies need to urgently prepare as AI will shape the future of our world more powerfully than any other innovation this century.</p>
<p>Research findings indicate that businesses are expected to hire more technology and automation professionals in the future, pointing to the need for well-qualified developers in the AI field. The most sought-after areas of expertise include artificial intelligence, digital customer experience, the internet of things, and the cloud.</p>
<p>A Master&rsquo;s degree in Machine Learning and Artificial Intelligence already exists. This Occupational Certificate is unique in filling a glaring gap at the entry level of this specialist field and career path.</p>
<p>Typical learners include school leavers, qualified learners from TVET colleges, new entrants into the sector, and existing employees who have experience in this field but without formal recognition of skills and competencies. Professionals who want to augment their careers may also access this qualification.</p>
<p>AI Software Developers can be employed as AI Researchers, Machine Learning Engineers, Machine Learning Researchers, AI Architects, AI Engineers, AI Technicians, AI Developers, Business Intelligence (BI) Developers, and in engineering teams in the field of intelligent robotics.</p>

<h2>Entry requirements and RPL</h2>
<p><strong>Minimum entry requirement:</strong> NQF Level 4 qualification.</p>
<p><strong>Recognition of Prior Learning (RPL):</strong> Yes. Learners may gain access to the qualification through RPL for Access, as provided for in the QCTO RPL Policy, conducted by an accredited education institution, skills development provider, or workplace accredited to offer the qualification or part qualification. Learners who have acquired competencies of the modules of a qualification or part qualification will be credited for those modules through RPL. For access to the external integrated summative assessment, accredited providers and approved workplaces must apply the internal assessment criteria specified in the related curriculum document to establish and confirm prior learning, and must confirm prior learning by issuing a statement of result.</p>

<h2>Qualification rules</h2>
<p>This qualification is made up of compulsory Knowledge, Practical Skill, and Work Experience Modules.</p>

<h3>Knowledge Modules (86 credits)</h3>
<table>
  <thead><tr><th>Code</th><th>Module</th><th>NQF Level</th><th>Credits</th></tr></thead>
  <tbody>
    <tr><td>251201-002-00-KM-01</td><td>Overview of Artificial Intelligence</td><td>4</td><td>2</td></tr>
    <tr><td>251201-002-00-KM-02</td><td>Introduction to Mathematics and Statistics</td><td>4</td><td>10</td></tr>
    <tr><td>251201-002-00-KM-03</td><td>Analytical Thinking and Problem Solving</td><td>4</td><td>3</td></tr>
    <tr><td>251201-002-00-KM-04</td><td>Data, Databases and Data Visualisation</td><td>4</td><td>8</td></tr>
    <tr><td>251201-002-00-KM-05</td><td>Computing Theory</td><td>4</td><td>8</td></tr>
    <tr><td>251201-002-00-KM-06</td><td>Introduction to Artificial Intelligence, Machine Learning, Deep Learning</td><td>4</td><td>5</td></tr>
    <tr><td>251201-002-00-KM-10</td><td>Introduction to Governance, Legislation and Ethics</td><td>4</td><td>1</td></tr>
    <tr><td>251201-002-00-KM-11</td><td>Fundamentals of Design Thinking and Innovation</td><td>4</td><td>1</td></tr>
    <tr><td>251201-002-00-KM-12</td><td>4IR and Future Skills</td><td>4</td><td>4</td></tr>
    <tr><td>251201-002-00-KM-07</td><td>Artificial Intelligence</td><td>5</td><td>12</td></tr>
    <tr><td>251201-002-00-KM-08</td><td>Machine Learning</td><td>5</td><td>16</td></tr>
    <tr><td>251201-002-00-KM-09</td><td>Deep Learning</td><td>5</td><td>16</td></tr>
  </tbody>
</table>

<h3>Practical Skill Modules (63 credits)</h3>
<table>
  <thead><tr><th>Code</th><th>Module</th><th>NQF Level</th><th>Credits</th></tr></thead>
  <tbody>
    <tr><td>251201-002-00-PM-01</td><td>Mathematics and Statistics for Programming</td><td>4</td><td>8</td></tr>
    <tr><td>251201-002-00-PM-02</td><td>Problem Definition, Analytical Thinking and Decision-Making</td><td>4</td><td>2</td></tr>
    <tr><td>251201-002-00-PM-03</td><td>Access, Analyse and Visualise Structured Data Using Spreadsheets</td><td>4</td><td>4</td></tr>
    <tr><td>251201-002-00-PM-04</td><td>Use SQL to Communicate with a Database</td><td>5</td><td>4</td></tr>
    <tr><td>251201-002-00-PM-05</td><td>Build a simple AI solution using Python</td><td>5</td><td>8</td></tr>
    <tr><td>251201-002-00-PM-06</td><td>Use Python Data Scraping to Populate Database Table in SQL</td><td>5</td><td>4</td></tr>
    <tr><td>251201-002-00-PM-07</td><td>Use Machine Learning to Build an AI solution in Python</td><td>5</td><td>6</td></tr>
    <tr><td>251201-002-00-PM-08</td><td>Use Deep Learning to Build an AI Neural Network Architecture in Python</td><td>5</td><td>10</td></tr>
    <tr><td>251201-002-00-PM-09</td><td>Use Deep Learning to Build an AI Neural Network Architecture in TensorFlow</td><td>5</td><td>10</td></tr>
    <tr><td>251201-002-00-PM-10</td><td>Function Ethically and Effectively as a Member of a Multidisciplinary Team</td><td>4</td><td>3</td></tr>
    <tr><td>251201-002-00-PM-11</td><td>Participate in a Design Thinking for Innovation Workshop</td><td>4</td><td>4</td></tr>
  </tbody>
</table>

<h3>Work Experience Modules (60 credits)</h3>
<table>
  <thead><tr><th>Code</th><th>Module</th><th>NQF Level</th><th>Credits</th></tr></thead>
  <tbody>
    <tr><td>251201-002-00-WM-01</td><td>AI Solution Design Interpretation and Development</td><td>5</td><td>20</td></tr>
    <tr><td>251201-002-00-WM-02</td><td>AI Solution Performance Testing</td><td>5</td><td>20</td></tr>
    <tr><td>251201-002-00-WM-03</td><td>AI Solution Deployment, Modification and Improvement</td><td>5</td><td>20</td></tr>
  </tbody>
</table>

<h2>Exit Level Outcomes</h2>
<ol>
  <li>Gather and interpret data from various sources to define an AI solution to a real-life world problem.</li>
  <li>Critically analyse data and create a Solution Design Document (SDD) that defines an AI solution that solves a real-life world problem.</li>
  <li>Choose a type or category of AI learning and the relevant algorithm to analyse data, gain insight, and make a subsequent prediction or determination with it.</li>
  <li>Train the AI model through a machine learning process and ensure that model accuracy is strictly maintained within the selection framework.</li>
  <li>Select a machine learning system and build an AI solution to a real-life world problem.</li>
  <li>Implement and run the AI solution on a selected platform and check the prediction results in real-life use, then select and run the AI solution on a platform.</li>
</ol>

<h2>Associated Assessment Criteria</h2>

<h3>Exit Level Outcome 1</h3>
<ul>
  <li>Verify sources from where data can be collected and identify the quantitative and qualitative quality of such data.</li>
  <li>Identify a critical thinking and problem-solving process through which the data can be reviewed for the purpose of arriving at an informed conclusion, and its significance and implications.</li>
  <li>Implement a critical thinking and problem-solving process through which the data can be reviewed for the purpose of arriving at an informed conclusion, and identify its significance and implications.</li>
  <li>Decide the scale of measurement for the data, as this will have a long-term impact on data interpretation and Return on Investment (ROI).</li>
  <li>Prepare data by cleaning, moving, checking, and organising such data using appropriate tools.</li>
</ul>

<h3>Exit Level Outcome 2</h3>
<ul>
  <li>Write a query to extract data from an operational platform and place it in a flat file (CSV) or spreadsheet to determine what the data looks like, what type of data it is, and how it ties up with other tables.</li>
  <li>Use a software tool to look at and interpret data structure and the relationships between data.</li>
  <li>Analyse datasets (resultant data from a query) using appropriate tools and criteria: access data; add over time on new datasets; how much effort is required to clean/organise data into a usable set; create a Software Design Document (SDD) describing the AI solution envisioned for the identified problem.</li>
</ul>

<h3>Exit Level Outcome 3</h3>
<ul>
  <li>Analyse data, then determine and classify the problem type to match the data set (groupings of data either at source or destination) to the identified problem.</li>
  <li>Solve the type of problem &mdash; classification, regression, anomaly detection, dimensionality reduction &mdash; and determine the AI algorithm that works best for each type.</li>
  <li>Apply basic machine learning types to determine the algorithm to be used: supervised, unsupervised, semi-supervised, and reinforced learning.</li>
  <li>Decide on the level of visibility needed in the AI solution and choose either decision trees or neural networks.</li>
  <li>Use and compare a few different algorithms to determine which delivers the most accurate results, and select an algorithm for employment.</li>
</ul>

<h3>Exit Level Outcome 4</h3>
<ul>
  <li>Train the chosen algorithm through machine learning by using the data and by incrementally improving the predictions within the selection framework.</li>
  <li>Maintain accuracy within the selected framework by setting minimal acceptable thresholds for the application and applying statistical discipline in training to ensure accuracy.</li>
  <li>Train and retrain the AI system to ensure that the algorithm achieves the desired accuracy.</li>
  <li>Test the trained models through cross-validation or by splitting the dataset (70:30), with one portion devoted to training and the rest to testing.</li>
  <li>Validate the model using the chosen metric or combination of metrics to measure the objective performance of a model.</li>
</ul>

<h3>Exit Level Outcome 5</h3>
<ul>
  <li>Utilise Python&rsquo;s framework and libraries to solve common programming tasks and simplify the development process.</li>
  <li>Determine the machine learning libraries to be used in building the AI model &mdash; a good set of libraries means less time writing the algorithm and more time actually building the AI model.</li>
  <li>Select a machine learning platform that will ease the machine learning process and facilitate building the models to build an AI system.</li>
</ul>

<h3>Exit Level Outcome 6</h3>
<ul>
  <li>Plan, prepare, and execute the implementation process before implementation by creating a plan to describe all tasks to be completed.</li>
  <li>Minimise the ongoing risk of implementing a new solution by keeping, maintaining, and monitoring a risk schedule.</li>
  <li>Deploy functional resources to key locations to provide on-site support at an implementation.</li>
  <li>Launch the AI solution, ensuring the implementation is operating according to set outcomes and criteria.</li>
  <li>Provide support at implementation and share knowledge on whether the intended solution is achieved.</li>
</ul>

<h2>Integrated Assessment</h2>
<p><strong>Formative:</strong> The skills development provider uses the curriculum to guide internal assessment criteria and weighting, and applies the scope of practical skills and applied knowledge stipulated by the internal assessment criteria. Formative assessment together with work experience leads to entrance into the integrated external summative assessment.</p>
<p><strong>Summative:</strong> An external integrated summative assessment, conducted through the relevant QCTO Assessment Quality Partner, is required for the issuing of this qualification. It focuses on the exit level outcomes and associated assessment criteria, and is conducted as a theoretical assessment plus evaluation of practical tasks at decentralised approved assessment sites in a simulated environment, by an assessor registered with the relevant AQP.</p>

<h2>International comparability</h2>
<p>The qualification was compared with:</p>
<ul>
  <li><strong>Grey Campus (with IBM) &mdash; Certificate Program in Artificial Intelligence:</strong> A foundational, self-paced program blending Data Science, Machine Learning, Deep Learning, and AI. Covers data structures and ML libraries, supervised and unsupervised learning, classification and regression, time series, Python ML libraries, TensorFlow, neural networks, NLP, and Convolutional Neural Networks. <em>Difference:</em> targets business analysts/architects and experienced professionals; self-paced with no prerequisites; no regulated workplace learning. <em>Similarity:</em> entry-level, covers similar topics, includes theory and practice.</li>
  <li><strong>Microsoft Certified: Azure AI Fundamentals (with Cloud Academy preparatory):</strong> A blended-learning preparation for the Microsoft certification exam. Tests introduction to AI, machine learning (hands-on on Azure), computer vision, NLP workloads on Azure, conversational AI workloads on Azure, and responsible AI principles. <em>Difference:</em> Azure-specific; some sections assume basic mathematics; programming experience is beneficial. <em>Similarity:</em> covers similar content and includes a practical aspect.</li>
</ul>
<p><strong>Conclusion:</strong> The South African Occupational Certificate: Artificial Intelligence Software Developer compares favourably with the competencies covered in the USA and UAE qualifications.</p>

<h2>Articulation</h2>
<ul>
  <li><strong>Horizontal:</strong> Occupational Certificate: Computer Technician; NQF Level 5.</li>
  <li><strong>Vertical:</strong> Diploma in Information Technology; NQF Level 6.</li>
</ul>

<h2>Notes</h2>
<ul>
  <li><strong>Qualifying for external assessment:</strong> Learners must provide proof of completion of all required knowledge and practical modules by means of statements of result, and a record of completed work experience.</li>
  <li><strong>Additional legal or physical entry requirements:</strong> None.</li>
  <li><strong>Accreditation of providers:</strong> Accreditation is done against the criteria reflected in the relevant curriculum on the QCTO website. Curriculum title and code: <em>Artificial Intelligence Software Developer: 251201-002-00-00</em>.</li>
  <li><strong>Encompassed trade:</strong> Not a trade qualification.</li>
  <li><strong>Assessment Quality Partner (AQP):</strong> MICT SETA.</li>
  <li><strong>Learning programmes recorded against this qualification:</strong> None.</li>
  <li><strong>Providers currently accredited to offer this qualification:</strong> None on record at SAQA.</li>
</ul>
""".strip()


def main():
    app.app_context().push()
    course = Course.query.filter(Course.title.like('SAQA 118792%')).first()
    if course is None:
        course = Course(
            title=COURSE_TITLE,
            description=COURSE_DESCRIPTION,
            teacher_id=TEACHER_ID,
        )
        db.session.add(course)
        db.session.flush()
        print(f'created course id={course.id}: {course.title}')
    else:
        course.title = COURSE_TITLE
        course.description = COURSE_DESCRIPTION
        print(f'updated existing course id={course.id}: {course.title}')

    about = Lesson.query.filter_by(course_id=course.id, title=ABOUT_TITLE).first()
    if about is None:
        about = Lesson(
            course_id=course.id,
            title=ABOUT_TITLE,
            content=ABOUT_HTML,
            content_type='lesson',
            order=1,
            points=1.0,
        )
        db.session.add(about)
        db.session.flush()
        print(f'  created About lesson id={about.id}')
    else:
        about.content = ABOUT_HTML
        about.content_type = 'lesson'
        about.order = 1
        print(f'  updated About lesson id={about.id}')

    db.session.commit()
    print('done.')


if __name__ == '__main__':
    main()
