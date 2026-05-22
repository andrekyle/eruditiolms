"""Lesson spec for SAQA 118792 AI Software Developer course.

Maps the 12 Knowledge + 11 Practical + 3 Work Experience modules into
10 thematic lessons. Each lesson module must export:
  - LESSON_HTML : str  (>=1500 chars)
  - QUESTIONS  : list of 8 tuples (qtype, qhtml, opts, fb)
                 qtype in ('multiple_choice','true_false')
                 opts: list of (option_html, is_correct) ; len 4 for mc, 2 for tf
                 exactly 1 correct option
  - PRACTICAL_HTML : str  (>=1200 chars) hands-on lab walkthrough
"""

LESSONS = [
    {
        'module': 'lesson01_overview_of_ai',
        'title': 'Lesson 1 \u2014 Overview of Artificial Intelligence',
        'quiz_desc': '8 questions on AI definitions, history, application areas, narrow vs general AI, agents and environments.',
        'covers': 'KM-01 Overview of Artificial Intelligence (NQF4, 2 cr).',
    },
    {
        'module': 'lesson02_math_stats',
        'title': 'Lesson 2 \u2014 Mathematics and Statistics for AI',
        'quiz_desc': '8 questions on linear algebra, calculus, probability, descriptive and inferential statistics applied to AI.',
        'covers': 'KM-02 Introduction to Mathematics and Statistics (NQF4, 10 cr) + PM-01 Mathematics and Statistics for Programming (NQF4, 8 cr).',
    },
    {
        'module': 'lesson03_analytical_thinking',
        'title': 'Lesson 3 \u2014 Analytical Thinking, Problem Definition and Decision-Making',
        'quiz_desc': '8 questions on structured problem solving, decomposition, pattern recognition, abstraction, decision frameworks.',
        'covers': 'KM-03 Analytical Thinking and Problem Solving (NQF4, 3 cr) + PM-02 Problem Definition, Analytical Thinking and Decision-Making (NQF4, 2 cr).',
    },
    {
        'module': 'lesson04_data_databases_viz',
        'title': 'Lesson 4 \u2014 Data, Databases and Visualisation (spreadsheets)',
        'quiz_desc': '8 questions on data types, relational vs NoSQL, ETL, spreadsheet analysis, charting, dashboards.',
        'covers': 'KM-04 Data, Databases and Data Visualisation (NQF4, 8 cr) + PM-03 Access, Analyse and Visualise Structured Data Using Spreadsheets (NQF4, 4 cr).',
    },
    {
        'module': 'lesson05_computing_theory',
        'title': 'Lesson 5 \u2014 Computing Theory',
        'quiz_desc': '8 questions on computer architecture, OS concepts, algorithms, data structures, complexity, networking basics.',
        'covers': 'KM-05 Computing Theory (NQF4, 8 cr).',
    },
    {
        'module': 'lesson06_sql_python_scraping',
        'title': 'Lesson 6 \u2014 SQL, Python and Data Scraping',
        'quiz_desc': '8 questions on SQL DDL/DML, joins, aggregation, Python data access, BeautifulSoup / requests, populating SQL from scraped data.',
        'covers': 'PM-04 Use SQL to Communicate with a Database (NQF5, 4 cr) + PM-06 Use Python Data Scraping to Populate Database Table in SQL (NQF5, 4 cr).',
    },
    {
        'module': 'lesson07_ai_ml_dl_intro',
        'title': 'Lesson 7 \u2014 AI, Machine Learning and Deep Learning Fundamentals',
        'quiz_desc': '8 questions on supervised/unsupervised/reinforcement learning, model lifecycle, neural network basics, AI categories.',
        'covers': 'KM-06 Introduction to AI, ML, DL (NQF4, 5 cr) + KM-07 Artificial Intelligence (NQF5, 12 cr).',
    },
    {
        'module': 'lesson08_machine_learning',
        'title': 'Lesson 8 \u2014 Machine Learning with Python',
        'quiz_desc': '8 questions on regression, classification, clustering, train/test split, cross-validation, metrics, scikit-learn pipelines.',
        'covers': 'KM-08 Machine Learning (NQF5, 16 cr) + PM-05 Build a simple AI solution using Python (NQF5, 8 cr) + PM-07 Use ML to Build an AI Solution in Python (NQF5, 6 cr).',
    },
    {
        'module': 'lesson09_deep_learning_tensorflow',
        'title': 'Lesson 9 \u2014 Deep Learning with Python and TensorFlow',
        'quiz_desc': '8 questions on neural network architectures, activation/loss/optimizers, CNN, RNN, training in TensorFlow/Keras.',
        'covers': 'KM-09 Deep Learning (NQF5, 16 cr) + PM-08 DL Neural Network in Python (NQF5, 10 cr) + PM-09 DL Neural Network in TensorFlow (NQF5, 10 cr).',
    },
    {
        'module': 'lesson10_governance_ethics_4ir',
        'title': 'Lesson 10 \u2014 Governance, Ethics, Design Thinking, 4IR and Multidisciplinary Teamwork',
        'quiz_desc': '8 questions on AI governance, POPIA/GDPR, bias and fairness, design thinking phases, 4IR skills, team collaboration.',
        'covers': 'KM-10 Governance, Legislation and Ethics (1 cr) + KM-11 Design Thinking and Innovation (1 cr) + KM-12 4IR and Future Skills (4 cr) + PM-10 Multidisciplinary Team (3 cr) + PM-11 Design Thinking Workshop (4 cr).',
    },
]

FINAL_EXAM_MODULE = 'final_exam'
FINAL_EXAM_TITLE = 'Final Exam \u2014 Integrated Summative Assessment (30 questions)'
FINAL_EXAM_DESC = (
    'Cumulative 30-question practice exam aligned to the six Exit Level Outcomes and the '
    'Work Experience Modules WM-01 Solution Design Development, WM-02 Performance Testing, '
    'WM-03 Deployment and Improvement. Pass mark suggestion: 70%.'
)
