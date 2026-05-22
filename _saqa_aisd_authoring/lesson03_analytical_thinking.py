# -*- coding: utf-8 -*-
"""SAQA 118792 AI Software Developer (NQF 5)
Lesson 03 -- Analytical Thinking and Problem Definition
Covers KM-03 (NQF4, 3 cr) + PM-02 (NQF4, 2 cr).
"""

LESSON_HTML = (
    "<h2>Analytical Thinking and Problem Definition</h2>"
    "<p><strong>Analytical thinking</strong> is the disciplined practice of breaking a complex, "
    "often messy situation into smaller, well-defined parts so that each part can be examined with "
    "evidence rather than opinion. For an AI software developer this skill is not optional: most "
    "real-world requests arrive as vague business wishes (<em>'we want to use AI to grow sales'</em>) "
    "and must be translated into a precise, measurable machine-learning or software problem before a "
    "single line of code is written.</p>"

    "<h3>1. Why analytical thinking matters in AI projects</h3>"
    "<ul>"
    "<li>AI systems amplify whatever problem you give them &mdash; a poorly framed problem produces a "
    "technically excellent model that solves the wrong thing.</li>"
    "<li>Data, compute and human attention are scarce; analytical thinking forces you to spend them "
    "on the highest-value part of the problem.</li>"
    "<li>Stakeholders (clinic managers, spaza-shop owners, school principals) rarely speak the "
    "language of features and labels &mdash; the developer must bridge that gap.</li>"
    "</ul>"

    "<h3>2. Computational thinking &mdash; the four pillars</h3>"
    "<p>Computational thinking is the cognitive toolkit that underpins all software and AI work. "
    "It has four widely-accepted pillars:</p>"
    "<table>"
    "<thead><tr><th>Pillar</th><th>What it means</th><th>AI example</th></tr></thead>"
    "<tbody>"
    "<tr><td><strong>Decomposition</strong></td><td>Split a big problem into smaller sub-problems "
    "that can be tackled independently.</td><td>Split 'predict learner drop-out' into data "
    "collection, feature engineering, model training, deployment, monitoring.</td></tr>"
    "<tr><td><strong>Pattern recognition</strong></td><td>Spot similarities with problems you have "
    "already solved.</td><td>Drop-out prediction shares structure with customer-churn prediction "
    "&mdash; reuse the churn pipeline template.</td></tr>"
    "<tr><td><strong>Abstraction</strong></td><td>Hide irrelevant detail; keep only what matters for "
    "the decision.</td><td>Represent a learner as a vector of attendance, marks and bursary status "
    "rather than a full life history.</td></tr>"
    "<tr><td><strong>Algorithm design</strong></td><td>Define a clear, repeatable sequence of steps "
    "to reach the solution.</td><td>For each new term: pull data &rarr; clean &rarr; score &rarr; "
    "rank top-50 at-risk learners &rarr; alert lecturer.</td></tr>"
    "</tbody></table>"

    "<h3>3. Problem framing techniques</h3>"
    "<p>Before modelling, frame the problem with at least one structured tool:</p>"
    "<ul>"
    "<li><strong>5W1H</strong> &mdash; ask <em>Who</em> is affected, <em>What</em> is happening, "
    "<em>Where</em>, <em>When</em>, <em>Why</em>, and <em>How</em> it is measured today.</li>"
    "<li><strong>Root cause / 5-Whys</strong> &mdash; for each symptom keep asking 'why?' until you "
    "reach a cause you can actually act on. Stops you from building AI for a symptom.</li>"
    "<li><strong>Fishbone (Ishikawa) diagram</strong> &mdash; group possible causes under standard "
    "branches (People, Process, Data, Technology, Environment, Measurement) to make sure no major "
    "source of the problem is forgotten.</li>"
    "</ul>"

    "<h3>4. From vague request to measurable ML problem</h3>"
    "<p>Translate the business wish into a precise specification with three mandatory elements:</p>"
    "<ol>"
    "<li><strong>Target variable</strong> &mdash; the exact thing you will predict or classify "
    "(e.g. <em>'Will this learner withdraw before end of semester? yes/no'</em>).</li>"
    "<li><strong>Success metric</strong> &mdash; one primary metric tied to business value "
    "(e.g. recall on the at-risk class &ge; 0.75 at precision &ge; 0.4) plus a guardrail metric "
    "(e.g. no demographic group's false-positive rate may exceed the overall rate by more than "
    "20%).</li>"
    "<li><strong>Constraints</strong> &mdash; latency, budget, interpretability, POPIA compliance, "
    "available data, on-device vs cloud.</li>"
    "</ol>"
    "<blockquote>Rule of thumb: if you cannot write the target variable as a single column you could "
    "add to a spreadsheet, the problem is not yet framed.</blockquote>"

    "<h3>5. Decision-making frameworks</h3>"
    "<ul>"
    "<li><strong>Cost-benefit analysis</strong> &mdash; list every quantifiable cost (data labelling, "
    "GPU hours, staff time) against expected benefit (rand value of prevented drop-outs, hours "
    "saved). Proceed only if benefit clearly exceeds cost across a sensible time horizon.</li>"
    "<li><strong>Decision matrix</strong> &mdash; score each candidate solution against weighted "
    "criteria (accuracy, cost, time-to-deploy, explainability). The highest weighted score wins, "
    "and the matrix becomes part of the audit trail.</li>"
    "<li><strong>Expected value</strong> &mdash; for risky choices compute "
    "<code>EV = &Sigma; (probability &times; payoff)</code>. Useful when comparing 'build a model' "
    "vs 'buy an API' vs 'keep the manual process'.</li>"
    "</ul>"

    "<h3>6. Cognitive biases that derail AI projects</h3>"
    "<table>"
    "<thead><tr><th>Bias</th><th>How it shows up</th><th>Counter-measure</th></tr></thead>"
    "<tbody>"
    "<tr><td>Confirmation bias</td><td>You only look at metrics that confirm the model is good.</td>"
    "<td>Pre-register the success metric before training; report it whatever it says.</td></tr>"
    "<tr><td>Anchoring</td><td>The first accuracy number you see becomes the benchmark forever.</td>"
    "<td>Establish a baseline (majority class, simple rule) <em>before</em> any ML.</td></tr>"
    "<tr><td>Automation bias</td><td>Users trust the model's output even when it is obviously "
    "wrong.</td><td>Show confidence scores; require human sign-off on high-impact decisions.</td>"
    "</tr>"
    "<tr><td>Survivorship bias</td><td>Training data only contains customers who stayed, learners "
    "who graduated, machines that survived.</td><td>Actively search for the missing 'dead' "
    "records; document data exclusions.</td></tr>"
    "</tbody></table>"

    "<h3>7. The Solution Design Document (SDD)</h3>"
    "<p>An SDD is the one document that captures the result of all the thinking above. A minimal "
    "SDD has these sections:</p>"
    "<ol>"
    "<li>Problem statement (1 paragraph, plain language)</li>"
    "<li>Stakeholders and decisions they will make</li>"
    "<li>Target variable and success metric (with guardrails)</li>"
    "<li>Data sources, owners and POPIA basis</li>"
    "<li>Constraints (latency, cost, fairness, regulatory)</li>"
    "<li>Risks and mitigations</li>"
    "<li>Proposed approach and alternatives considered</li>"
    "<li>Go / no-go decision and sign-off</li>"
    "</ol>"
    "<p>The SDD is reviewed before any model code is written, and updated whenever a major "
    "assumption changes.</p>"
)


QUESTIONS = [
    (
        "multiple_choice",
        "<p>A spaza-shop owner says: <em>'I want AI to help my business.'</em> "
        "What is the <strong>first</strong> analytical step the developer should take?</p>",
        [
            ("<p>Train a large language model on the shop's WhatsApp messages.</p>", False),
            ("<p>Frame the request into a specific, measurable problem (e.g. predicting which "
             "products will stock-out next week) with a target variable and success metric.</p>", True),
            ("<p>Buy a cloud GPU subscription so the team is ready to train.</p>", False),
            ("<p>Collect every possible data source the shop has, then decide what to do.</p>", False),
        ],
        "<p>Analytical thinking starts with <strong>problem framing</strong>. Without a precise "
        "target variable and success metric, any model or data effort is premature.</p>",
    ),
    (
        "multiple_choice",
        "<p>Which option correctly lists the four pillars of computational thinking?</p>",
        [
            ("<p>Decomposition, pattern recognition, abstraction, algorithm design.</p>", True),
            ("<p>Collection, cleaning, modelling, deployment.</p>", False),
            ("<p>Plan, do, check, act.</p>", False),
            ("<p>Supervised, unsupervised, reinforcement, generative.</p>", False),
        ],
        "<p>The classic four pillars are decomposition, pattern recognition, abstraction and "
        "algorithm design. The other lists describe pipelines, PDCA or ML paradigms.</p>",
    ),
    (
        "multiple_choice",
        "<p>A TVET principal reports: <em>'Too many first-year learners are dropping out.'</em> "
        "You apply the 5-Whys and end with <em>'because they cannot afford transport in week 3 "
        "when bursary payments are late.'</em> What does this tell you about an AI solution?</p>",
        [
            ("<p>You should still build a churn-prediction model first because AI always helps.</p>",
             False),
            ("<p>The root cause is operational (bursary timing); AI may help by flagging the "
             "highest-risk learners early, but the real fix is a process change &mdash; the SDD "
             "must say so.</p>", True),
            ("<p>Drop a deep neural network on attendance data and ignore the bursary issue.</p>",
             False),
            ("<p>Recommend that the college stop offering bursaries to reduce dependency.</p>", False),
        ],
        "<p>The 5-Whys exposes a root cause AI cannot fix on its own. Good analytical thinking "
        "documents this and scopes the AI component honestly.</p>",
    ),
    (
        "multiple_choice",
        "<p>Which of the following is the <strong>best</strong> written target variable for an ML "
        "problem?</p>",
        [
            ("<p>'Improve customer happiness.'</p>", False),
            ("<p>'Use AI to optimise the business.'</p>", False),
            ("<p>'For each active customer at month-end, will they make at least one purchase in "
             "the next 30 days? (yes / no)'</p>", True),
            ("<p>'Predict the future.'</p>", False),
        ],
        "<p>A usable target variable is a single, unambiguous column that can be computed from "
        "data &mdash; here a binary label per customer per month.</p>",
    ),
    (
        "multiple_choice",
        "<p>Your team must choose between three solutions: (A) buy a vendor API, (B) train a "
        "custom model, (C) keep the current manual process. Which framework is most appropriate "
        "for making this choice transparent and defensible?</p>",
        [
            ("<p>Pick whichever option the senior developer prefers.</p>", False),
            ("<p>A weighted <strong>decision matrix</strong> scoring each option against criteria "
             "such as cost, accuracy, time-to-deploy and explainability.</p>", True),
            ("<p>Toss a coin to remove bias.</p>", False),
            ("<p>Always choose the cheapest option.</p>", False),
        ],
        "<p>A decision matrix forces explicit criteria and weights, making the choice auditable "
        "and reducing personal bias.</p>",
    ),
    (
        "multiple_choice",
        "<p>A bank trains a loan-default model only on customers whose loans were approved in the "
        "past. It then claims excellent accuracy. Which cognitive / data bias is most clearly at "
        "work?</p>",
        [
            ("<p>Anchoring bias.</p>", False),
            ("<p>Survivorship bias &mdash; the rejected applicants are missing from training "
             "data, so the model only learns about a filtered population.</p>", True),
            ("<p>Automation bias.</p>", False),
            ("<p>Recency bias.</p>", False),
        ],
        "<p>Only 'survivors' of the previous approval process appear in the data, so the model "
        "cannot generalise to the full applicant pool.</p>",
    ),
    (
        "true_false",
        "<p>A Solution Design Document (SDD) should be finalised and signed off <strong>before</strong> "
        "significant model-development effort begins, and updated when major assumptions change.</p>",
        [
            ("<p>True</p>", True),
            ("<p>False</p>", False),
        ],
        "<p>True. The SDD captures the framed problem, success metric, constraints and risks; "
        "writing code before it exists almost always leads to rework.</p>",
    ),
    (
        "true_false",
        "<p>If a deployed AI model produces a recommendation, end-users should always accept it "
        "without question because the model has been validated on test data.</p>",
        [
            ("<p>True</p>", False),
            ("<p>False</p>", True),
        ],
        "<p>False. Blind trust in model output is <strong>automation bias</strong>. Validated "
        "models still make mistakes, and high-impact decisions should keep a human in the loop "
        "with visible confidence scores.</p>",
    ),
]


PRACTICAL_HTML = (
    "<h2>Practical Lab \u2014 Frame an AI Problem and Draft an SDD</h2>"
    "<p>In this lab you will take a real South-African small-organisation problem and walk it "
    "through the analytical-thinking pipeline you learned in the lesson, ending with a one-page "
    "<strong>Solution Design Document</strong> that a non-technical stakeholder could read.</p>"

    "<h3>Scenario options (pick ONE)</h3>"
    "<ul>"
    "<li><strong>Spaza-shop stock-outs</strong> &mdash; Mama Dlamini's spaza in Khayelitsha keeps "
    "running out of bread and airtime on weekends, losing roughly R600 per weekend in walk-away "
    "customers.</li>"
    "<li><strong>TVET learner drop-out</strong> &mdash; A TVET college in Mthatha sees 30% of "
    "first-year IT learners withdraw before the June exams; lecturers want early warnings.</li>"
    "<li><strong>Clinic no-shows</strong> &mdash; A community clinic in Soweto loses 25% of booked "
    "antenatal appointments to no-shows, wasting nurse time.</li>"
    "</ul>"

    "<h3>Numbered steps</h3>"
    "<ol>"
    "<li><strong>Restate the problem in one sentence</strong> using plain language. No jargon, no "
    "mention of AI yet.</li>"
    "<li><strong>Apply 5W1H</strong> &mdash; write Who, What, Where, When, Why, How is it measured "
    "today. Keep each answer to one line.</li>"
    "<li><strong>Run the 5-Whys</strong> on the main symptom. Stop when you reach a cause the "
    "organisation can act on. Note honestly whether AI can address the root cause or only a "
    "symptom.</li>"
    "<li><strong>Decompose</strong> the work using the four pillars: list the sub-problems, look "
    "for patterns from problems you already know, decide which details to abstract away, and "
    "sketch the algorithm in 4-6 steps.</li>"
    "<li><strong>Define the target variable</strong> as a single column you could add to a "
    "spreadsheet, e.g. <code>will_stock_out_next_weekend (yes/no)</code>.</li>"
    "<li><strong>Pick a primary success metric and one guardrail metric</strong>, both with "
    "numeric thresholds tied to business value.</li>"
    "<li><strong>List data sources</strong> already available, plus what is missing. Mark each "
    "with its POPIA basis (consent, legitimate interest, etc.).</li>"
    "<li><strong>Score 2-3 candidate approaches</strong> in a small decision matrix (criteria: "
    "cost, time-to-deploy, accuracy, explainability, fairness).</li>"
    "<li><strong>Identify the top 3 risks</strong> (data, bias, adoption, regulatory) and a "
    "mitigation for each.</li>"
    "<li><strong>Write the one-page SDD</strong> using the eight-section template from the "
    "lesson.</li>"
    "</ol>"

    "<h3>Example partial SDD (spaza-shop scenario)</h3>"
    "<div style=\"font-family:inherit; font-size:inherit; line-height:1.55; "
    "padding:1rem 1.25rem; border:1px solid rgba(127,127,127,0.35); "
    "border-left:4px solid #198754; border-radius:8px; "
    "background:rgba(127,127,127,0.06); margin:0.75rem 0;\">"
    "<p><strong>1. Problem statement</strong><br>"
    "Mama Dlamini's spaza in Khayelitsha runs out of bread and airtime on Sat/Sun, losing "
    "~R600 per weekend. She wants to know on Friday morning what to restock.</p>"
    "<p><strong>2. Stakeholders</strong></p>"
    "<ul><li>Owner (decides Friday order)</li>"
    "<li>Supplier (must be notified by 10:00 Fri)</li></ul>"
    "<p><strong>3. Target variable + success metric</strong><br>"
    "y = will product X stock out before Sun 18:00? (yes/no), evaluated weekly.<br>"
    "Primary: Recall on 'yes' class &ge; 0.80<br>"
    "Guardrail: Precision &ge; 0.50 (avoid over-ordering perishables)</p>"
    "<p><strong>4. Data</strong></p>"
    "<ul><li>6 months of till-roll CSVs (owner-supplied, consented)</li>"
    "<li>Local weather (public API)</li>"
    "<li>Pay-day calendar (public)</li></ul>"
    "<p><strong>5. Constraints</strong></p>"
    "<ul><li>Must run on owner's Android phone, offline-capable</li>"
    "<li>Total cost &lt; R200/month</li>"
    "<li>Output must be a simple shopping list, not a dashboard</li></ul>"
    "<p><strong>6. Risks &amp; mitigations</strong></p>"
    "<ul><li>Sparse data on rare items &rarr; group into categories</li>"
    "<li>Owner distrust &rarr; show last-week accuracy each Friday</li></ul>"
    "<p><strong>7. Proposed approach</strong><br>"
    "Logistic regression baseline, then gradient-boosted trees if needed.<br>"
    "Alternatives considered: rule-based reorder point (kept as fallback).</p>"
    "<p><strong>8. Go / no-go</strong><br>"
    "Go for a 6-week pilot on top-20 SKUs. Review against success metric.</p>"
    "</div>"

    "<h3>Reflection questions</h3>"
    "<ol>"
    "<li>Which of the four computational-thinking pillars did you find hardest to apply, and "
    "why?</li>"
    "<li>Where in your SDD could <em>confirmation bias</em> creep in during evaluation, and how "
    "would you prevent it?</li>"
    "<li>If the 5-Whys revealed a root cause AI cannot solve, what did you write in the SDD "
    "instead of promising an AI fix?</li>"
    "<li>How would your success metric change if the cost of a false positive were ten times the "
    "cost of a false negative?</li>"
    "</ol>"

    "<h3>Submission</h3>"
    "<p>Submit your one-page SDD (PDF or Markdown) plus a short paragraph (max 150 words) "
    "answering the reflection questions. Your facilitator will score the SDD on clarity of "
    "problem framing, measurability of the success metric, honesty about risks, and quality of "
    "the decision matrix.</p>"
)


assert LESSON_HTML.startswith("<h2>Analytical Thinking and Problem Definition</h2>")
assert len(LESSON_HTML) >= 1800
assert len(QUESTIONS) == 8
assert PRACTICAL_HTML.startswith("<h2>Practical Lab \u2014 Frame an AI Problem and Draft an SDD</h2>")
assert len(PRACTICAL_HTML) >= 1400
for _qtype, _qhtml, _opts, _fb in QUESTIONS:
    assert _qtype in ("multiple_choice", "true_false")
    if _qtype == "multiple_choice":
        assert len(_opts) == 4
    else:
        assert len(_opts) == 2
    assert sum(1 for _h, _b in _opts if _b) == 1
