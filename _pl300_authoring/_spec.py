"""Spec for the PL-300 course: nine topic lessons in objective order."""

LESSONS = [
    {
        'module': 'l1_get_data',
        'title': 'Get data from data sources',
        'quiz_desc': 'Test your knowledge of connecting to various data sources, handling authentication, and choosing between Import, DirectQuery, and Dual storage modes.',
    },
    {
        'module': 'l2_transform',
        'title': 'Clean, transform, and load data with Power Query',
        'quiz_desc': 'Validate your skills in using Power Query to clean, shape, merge, append, and transform raw data for analysis.',
    },
    {
        'module': 'l3_design_model',
        'title': 'Design and implement a data model',
        'quiz_desc': 'Assess your understanding of star schemas, relationships, cardinality, cross-filter direction, and role-playing dimensions.',
    },
    {
        'module': 'l4_dax',
        'title': 'Create model calculations using DAX',
        'quiz_desc': 'Evaluate your proficiency with DAX measures, calculated columns, filter context, CALCULATE, iterators, and time intelligence.',
    },
    {
        'module': 'l5_optimize',
        'title': 'Optimize model performance',
        'quiz_desc': 'Check your knowledge of Performance Analyzer, Vertipaq, aggregations, incremental refresh, and cardinality tuning.',
    },
    {
        'module': 'l6_visualizations',
        'title': 'Create reports \u2014 visualizations and formatting',
        'quiz_desc': 'Test your ability to choose the right visual for a scenario, format visuals, apply themes, and design report pages.',
    },
    {
        'module': 'l7_enhance',
        'title': 'Enhance reports for usability and storytelling',
        'quiz_desc': 'Verify your skills in bookmarks, navigation, drill-through, custom tooltips, conditional formatting, and accessibility.',
    },
    {
        'module': 'l8_analytics',
        'title': 'Identify patterns and trends \u2014 analytics and AI visuals',
        'quiz_desc': 'Assess your capability to use Key Influencers, Decomposition Tree, Q&A, Smart Narrative, forecasting, anomaly detection, and clustering.',
    },
    {
        'module': 'l9_deploy',
        'title': 'Deploy and maintain assets \u2014 workspaces, datasets, sharing',
        'quiz_desc': 'Evaluate your understanding of workspace roles, deployment pipelines, apps, gateways, scheduled refresh, RLS in the service, and endorsement.',
    },
]
