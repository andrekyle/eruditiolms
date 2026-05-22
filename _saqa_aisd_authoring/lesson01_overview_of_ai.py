"""SAQA 118792 — Occupational Certificate: AI Software Developer (NQF 5)
Knowledge Module KM-01: Overview of Artificial Intelligence (NQF4, 2 credits)

Exports:
    LESSON_HTML   — theory lesson (HTML string)
    QUESTIONS     — list of 8 assessment item tuples
    PRACTICAL_HTML — hands-on lab (HTML string)
"""

LESSON_HTML = """<h2>Overview of Artificial Intelligence</h2>
<p><strong>Artificial Intelligence (AI)</strong> is the branch of computer science concerned with building machines and software that perform tasks normally requiring human intelligence — perceiving, reasoning, learning, planning, communicating in natural language, and acting in the world. A widely used working definition is <em>"the study and construction of rational agents that perceive their environment and take actions that maximise the chance of achieving their goals"</em> (Russell &amp; Norvig).</p>

<h3>1. A Brief History</h3>
<ul>
  <li><strong>1950</strong> — Alan Turing publishes <em>Computing Machinery and Intelligence</em> and proposes the <strong>Turing Test</strong> as an operational test for machine intelligence.</li>
  <li><strong>1956</strong> — The <strong>Dartmouth Summer Research Project</strong>, organised by John McCarthy, Marvin Minsky, Claude Shannon and Nathaniel Rochester, formally names the field <em>"Artificial Intelligence"</em>.</li>
  <li><strong>1960s–1970s</strong> — Early symbolic systems (Logic Theorist, ELIZA, SHRDLU) and the rise of <strong>expert systems</strong> such as MYCIN.</li>
  <li><strong>1974–1980 and 1987–1993</strong> — The two <strong>"AI winters"</strong>: funding and interest collapsed after early promises went unmet.</li>
  <li><strong>1997</strong> — IBM's <em>Deep Blue</em> defeats world chess champion Garry Kasparov.</li>
  <li><strong>~2012</strong> — The <strong>deep-learning resurgence</strong> begins when AlexNet wins the ImageNet competition, triggered by large labelled datasets, GPUs, and better training techniques.</li>
  <li><strong>2017 onward</strong> — The Transformer architecture leads to large language models (GPT, BERT) and the modern wave of generative AI.</li>
</ul>

<h3>2. Categories of AI</h3>
<table>
  <thead><tr><th>Type</th><th>Description</th><th>Status</th></tr></thead>
  <tbody>
    <tr><td><strong>Narrow AI (ANI)</strong></td><td>Performs one specific task well (spam filter, face recognition, chatbot).</td><td>All AI in production today.</td></tr>
    <tr><td><strong>General AI (AGI)</strong></td><td>Matches human cognitive flexibility across any intellectual task.</td><td>Hypothetical / research goal.</td></tr>
    <tr><td><strong>Super AI (ASI)</strong></td><td>Exceeds the best human minds in every field.</td><td>Speculative.</td></tr>
  </tbody>
</table>

<h3>3. Symbolic vs Sub-symbolic AI</h3>
<ul>
  <li><strong>Symbolic AI</strong> ("Good Old-Fashioned AI") represents knowledge as explicit symbols and rules — logic programs, expert systems, knowledge graphs. Strengths: transparent reasoning. Weaknesses: brittle, hard to scale.</li>
  <li><strong>Sub-symbolic AI</strong> learns statistical patterns directly from data — neural networks, deep learning, evolutionary algorithms. Strengths: robust to noise, scales with data. Weaknesses: opaque ("black box"), data-hungry.</li>
  <li>Modern <strong>neuro-symbolic</strong> systems combine both.</li>
</ul>

<h3>4. Rational Agents and the PEAS Framework</h3>
<p>An <strong>agent</strong> is anything that perceives its environment through <em>sensors</em> and acts upon it through <em>actuators</em>. A <strong>rational agent</strong> chooses the action that is expected to maximise its performance measure given its percept history. We specify an agent's task environment using <strong>PEAS</strong>:</p>
<ul>
  <li><strong>P</strong>erformance measure — what counts as success?</li>
  <li><strong>E</strong>nvironment — what world does it operate in?</li>
  <li><strong>A</strong>ctuators — how can it act?</li>
  <li><strong>S</strong>ensors — how does it perceive?</li>
</ul>
<p>Example — an automated taxi-dispatch agent for Johannesburg minibus taxis:</p>
<pre><code>P: trips completed, fuel used, passenger wait time, safety
E: Gauteng road network, traffic, weather, passengers
A: route choice, pickup signal, fare quote
S: GPS, mobile booking app, traffic feed, fuel sensor</code></pre>

<h3>5. Main Branches of AI</h3>
<ol>
  <li><strong>Machine Learning (ML)</strong> — algorithms that improve from data (supervised, unsupervised, reinforcement).</li>
  <li><strong>Natural Language Processing (NLP)</strong> — understanding and generating human language; relevant to South Africa's 11 official languages.</li>
  <li><strong>Computer Vision</strong> — interpreting images and video (e.g. number-plate recognition on the N1).</li>
  <li><strong>Robotics</strong> — physical agents that sense, plan and act.</li>
  <li><strong>Expert Systems</strong> — rule-based reasoning in narrow domains (e.g. clinical triage).</li>
  <li><strong>Planning and Search</strong> — finding action sequences to reach goals.</li>
</ol>

<h3>6. Real-world Applications (with South African relevance)</h3>
<ul>
  <li><strong>Healthcare</strong> — TB and tuberculosis screening from chest X-rays; HIV viral-load prediction; triage chatbots at public clinics.</li>
  <li><strong>Finance</strong> — credit scoring for the unbanked, real-time fraud detection at Capitec, Standard Bank and FNB.</li>
  <li><strong>Agriculture</strong> — satellite-based crop-yield prediction in the Free State maize belt, pest detection in citrus orchards in Limpopo, drought-risk modelling for smallholder farmers.</li>
  <li><strong>Education</strong> — adaptive tutoring in vernacular languages, automated marking, dropout-risk early-warning systems for TVET colleges.</li>
  <li><strong>Autonomous vehicles</strong> — driver-assistance, fleet routing, mine-haul truck automation at Sishen and Mogalakwena.</li>
  <li><strong>Public sector</strong> — Home Affairs queue prediction, SARS tax-fraud detection, Eskom load-forecasting.</li>
</ul>

<h3>7. Benefits and Risks</h3>
<table>
  <thead><tr><th>Benefits</th><th>Risks</th></tr></thead>
  <tbody>
    <tr><td>Higher productivity and 24/7 service</td><td>Job displacement, especially in routine work</td></tr>
    <tr><td>Better decisions from large datasets</td><td>Algorithmic bias against under-represented groups</td></tr>
    <tr><td>Access to expertise where specialists are scarce</td><td>Privacy erosion; POPIA compliance burden</td></tr>
    <tr><td>New industries and skilled jobs</td><td>Concentration of power in a few tech firms</td></tr>
    <tr><td>Scientific discovery (e.g. AlphaFold)</td><td>Misuse: deepfakes, autonomous weapons, disinformation</td></tr>
  </tbody>
</table>

<h3>8. AI, the 4IR and South Africa</h3>
<p>The <strong>Fourth Industrial Revolution (4IR)</strong> describes the fusion of physical, digital and biological technologies — AI, IoT, robotics, blockchain, additive manufacturing. In 2019 President Cyril Ramaphosa established the <strong>Presidential Commission on the 4th Industrial Revolution (PC4IR)</strong>, chaired by Prof. Tshilidzi Marwala, to position South Africa to benefit from these technologies. The Commission's 2020 report recommended investing in human capital, building an AI institute, modernising the policy framework (including data protection under <strong>POPIA</strong>), and prioritising inclusive growth so AI does not widen the country's already extreme inequality.</p>
<blockquote><em>"AI is too important to be left only to technologists. As future AI software developers in South Africa, you carry responsibility for building systems that are fair, transparent, locally relevant and aligned with the Constitution."</em></blockquote>

<h3>Summary</h3>
<ul>
  <li>AI builds rational agents that perceive and act to achieve goals.</li>
  <li>It evolved from 1950s symbolic logic to today's data-driven deep learning.</li>
  <li>All deployed AI is <strong>narrow</strong>; AGI remains a research goal.</li>
  <li>The <strong>PEAS</strong> framework structures any agent design.</li>
  <li>Major branches: ML, NLP, computer vision, robotics, expert systems, planning.</li>
  <li>South Africa applies AI across healthcare, finance, agriculture, education and the public sector — guided by PC4IR and POPIA.</li>
</ul>
"""


QUESTIONS = [
    (
        'multiple_choice',
        '<p>Which historical event is most directly credited with <strong>naming</strong> the field of Artificial Intelligence?</p>',
        [
            ('<p>Alan Turing\u2019s 1950 paper proposing the Turing Test.</p>', False),
            ('<p>The 1956 Dartmouth Summer Research Project organised by John McCarthy and colleagues.</p>', True),
            ('<p>IBM Deep Blue defeating Garry Kasparov in 1997.</p>', False),
            ('<p>AlexNet winning the ImageNet competition in 2012.</p>', False),
        ],
        '<p>The term <em>"Artificial Intelligence"</em> was coined and the field formally launched at the 1956 Dartmouth workshop. Turing\u2019s paper (1950) influenced the field but predated its naming; Deep Blue and AlexNet are later milestones.</p>',
    ),
    (
        'multiple_choice',
        '<p>A self-driving mine-haul truck at Sishen is best classified as which type of AI?</p>',
        [
            ('<p>Artificial General Intelligence (AGI), because it operates without a human driver.</p>', False),
            ('<p>Artificial Super Intelligence (ASI), because it outperforms humans at driving in dust.</p>', False),
            ('<p>Artificial Narrow Intelligence (ANI), because it is specialised for one task.</p>', True),
            ('<p>Symbolic AI, because it follows the rules of the road.</p>', False),
        ],
        '<p>All AI systems deployed today \u2014 including autonomous vehicles \u2014 are <strong>narrow</strong>: they excel at a single well-defined task. AGI and ASI remain hypothetical. Symbolic vs sub-symbolic is a separate dimension describing <em>how</em> the system represents knowledge, not its scope.</p>',
    ),
    (
        'multiple_choice',
        '<p>You are designing an AI agent that screens chest X-rays for tuberculosis at a public clinic. Using the <strong>PEAS</strong> framework, which item is the <em>Performance measure</em>?</p>',
        [
            ('<p>The digital X-ray images supplied to the model.</p>', False),
            ('<p>The convolutional neural network architecture used.</p>', False),
            ('<p>Diagnostic accuracy, false-negative rate and turnaround time.</p>', True),
            ('<p>The radiology workstation and PACS database.</p>', False),
        ],
        '<p>In PEAS, the <strong>Performance measure</strong> defines what counts as success. X-ray images are <em>Sensors/percepts</em>, the network is an implementation detail, and the workstation is part of the <em>Environment</em>. Diagnostic accuracy and turnaround time are the success criteria.</p>',
    ),
    (
        'multiple_choice',
        '<p>Which statement best contrasts <strong>symbolic</strong> and <strong>sub-symbolic</strong> AI?</p>',
        [
            ('<p>Symbolic AI learns from raw data; sub-symbolic AI uses hand-coded rules.</p>', False),
            ('<p>Symbolic AI uses explicit rules and symbols and is generally more interpretable; sub-symbolic AI learns statistical patterns from data and is typically more opaque.</p>', True),
            ('<p>Symbolic AI requires GPUs; sub-symbolic AI runs only on CPUs.</p>', False),
            ('<p>They are identical \u2014 the terms are synonyms for machine learning.</p>', False),
        ],
        '<p>Symbolic AI (expert systems, logic programs) reasons with explicit human-readable symbols and is transparent but brittle. Sub-symbolic AI (neural networks) learns distributed numerical representations from data \u2014 powerful but often a "black box".</p>',
    ),
    (
        'multiple_choice',
        '<p>Which application best matches the <strong>Natural Language Processing</strong> branch of AI in a South African context?</p>',
        [
            ('<p>Counting maize plants in a drone photograph of a Free State farm.</p>', False),
            ('<p>A chatbot that answers SARS tax questions in isiZulu and Afrikaans.</p>', True),
            ('<p>Path-planning for a delivery drone in Sandton.</p>', False),
            ('<p>Predicting Eskom load demand from historical consumption data.</p>', False),
        ],
        '<p>NLP deals with understanding and generating human language \u2014 a multilingual SARS chatbot is a clear NLP application. Counting plants is computer vision, drone path-planning is robotics/planning, and load forecasting is general machine learning on numeric time-series.</p>',
    ),
    (
        'multiple_choice',
        '<p>Which of the following is a <strong>risk</strong> of AI deployment that is particularly relevant to South Africa\u2019s context of high inequality and POPIA compliance?</p>',
        [
            ('<p>AI systems always run faster than human workers.</p>', False),
            ('<p>Algorithmic bias and privacy violations can entrench existing inequality and breach data-protection law.</p>', True),
            ('<p>AI eliminates the need for any human oversight.</p>', False),
            ('<p>AI guarantees fairer credit scoring than any human reviewer.</p>', False),
        ],
        '<p>Models trained on historically biased data can disadvantage already-marginalised groups, while careless data handling can breach the <strong>Protection of Personal Information Act (POPIA)</strong>. The PC4IR report explicitly warns against these risks. The other options are myths.</p>',
    ),
    (
        'true_false',
        '<p>The South African <strong>Presidential Commission on the 4th Industrial Revolution (PC4IR)</strong>, chaired by Prof. Tshilidzi Marwala, was established to advise government on how the country should respond to technologies such as AI.</p>',
        [
            ('True', True),
            ('False', False),
        ],
        '<p>Correct. President Ramaphosa established the PC4IR in 2019; its 2020 report recommended an AI institute, human-capital investment and policy modernisation including data protection.</p>',
    ),
    (
        'true_false',
        '<p>Artificial General Intelligence (AGI) is already widely deployed in South African banks for fraud detection.</p>',
        [
            ('True', False),
            ('False', True),
        ],
        '<p>False. Bank fraud-detection systems are examples of <strong>narrow AI</strong> \u2014 highly specialised pattern recognisers. AGI, which would match human cognitive flexibility across any task, does not yet exist.</p>',
    ),
]


PRACTICAL_HTML = """<h2>Practical Lab \u2014 Map an AI Application</h2>
<p><strong>Duration:</strong> approximately 90 minutes &nbsp;|&nbsp; <strong>Deliverable:</strong> a one-page solution outline (PDF or Word) uploaded to the LMS.</p>
<p>In this lab you will take a real South African problem and design \u2014 on paper \u2014 an AI agent to address it. You will not write code yet; the goal is to practise <em>thinking like an AI software developer</em>: choosing the right branch of AI, specifying the agent with PEAS, listing the data you would need, and reflecting on the ethics of deploying the system.</p>

<h3>Scenario Options (choose ONE)</h3>
<ol>
  <li><strong>Crop-yield prediction</strong> for smallholder maize farmers in the Free State, using satellite imagery and weather data.</li>
  <li><strong>Minibus-taxi route optimisation</strong> in Johannesburg, reducing passenger wait times during peak hours.</li>
  <li><strong>Fraud detection</strong> for card-not-present transactions at a South African retail bank.</li>
  <li><strong>Your own scenario</strong> \u2014 any local problem (e.g. clinic queue prediction at Chris Hani Baragwanath, illegal-dumping detection in Cape Town, dropout-risk early warning at a TVET college). Clear it with your facilitator first.</li>
</ol>

<h3>Step-by-Step Tasks</h3>
<ol>
  <li><strong>Describe the problem</strong> in 3\u20134 sentences. Who is affected? What does success look like for them?</li>
  <li><strong>Identify the AI branch(es)</strong> that best fit (Machine Learning, NLP, Computer Vision, Robotics, Expert System, Planning). Justify your choice in one paragraph.</li>
  <li><strong>Write a PEAS specification</strong> for your agent. Use this template:
    <pre><code>P (Performance measure): ...
E (Environment):         ...
A (Actuators):           ...
S (Sensors / percepts):  ...</code></pre>
  </li>
  <li><strong>List the data you would need</strong> to train and evaluate the system. For each dataset note: source, approximate volume, format, and whether it contains personal information under POPIA.</li>
  <li><strong>Classify your agent</strong> as primarily <em>symbolic</em>, <em>sub-symbolic</em>, or <em>hybrid</em>, and explain why.</li>
  <li><strong>List at least four ethical considerations</strong>. Cover bias, privacy/POPIA, accountability ("who is responsible if it gets it wrong?"), and impact on jobs or vulnerable groups.</li>
  <li><strong>Sketch a simple block diagram</strong> on paper or in a drawing tool: data sources \u2192 model \u2192 decisions \u2192 affected users. Photograph or export it and include it in your one-pager.</li>
  <li><strong>Compile your one-page solution outline</strong> (maximum 1 page of A4, 11pt) containing: problem statement, AI branch, PEAS table, data list, ethics list, and the diagram. Upload it to the LMS.</li>
</ol>

<h3>Expected Output</h3>
<ul>
  <li>A single PDF or Word document, one A4 page, clearly structured with the headings <em>Problem</em>, <em>AI Branch</em>, <em>PEAS</em>, <em>Data</em>, <em>Ethics</em>, and <em>Diagram</em>.</li>
  <li>The PEAS table must have all four rows filled in with content specific to your scenario \u2014 generic answers will be marked down.</li>
  <li>At least four distinct ethical considerations, each in one sentence.</li>
</ul>

<h3>Marking Guide (10 marks)</h3>
<table>
  <thead><tr><th>Criterion</th><th>Marks</th></tr></thead>
  <tbody>
    <tr><td>Clear problem statement grounded in a South African context</td><td>2</td></tr>
    <tr><td>Correct identification of AI branch with justification</td><td>2</td></tr>
    <tr><td>Complete and scenario-specific PEAS table</td><td>2</td></tr>
    <tr><td>Realistic data list with POPIA awareness</td><td>2</td></tr>
    <tr><td>Thoughtful ethical analysis and diagram</td><td>2</td></tr>
  </tbody>
</table>

<h3>Reflection Questions</h3>
<p>Add short answers (2\u20133 sentences each) at the bottom of your one-pager OR submit them as a separate text file:</p>
<ol>
  <li>Which part of the PEAS specification was hardest to define, and why?</li>
  <li>If your agent\u2019s recommendation harms a user (e.g. denies them credit or misses a TB diagnosis), who do <em>you</em> think should be held accountable \u2014 the developer, the deploying organisation, or the user? Justify your view.</li>
  <li>How would you explain your proposed system to a non-technical community member affected by it, in plain language and in a South African official language other than English?</li>
</ol>

<blockquote><em>Tip: Keep this one-pager. In later lessons you will return to your chosen scenario, gather a small dataset for it, and build a working prototype.</em></blockquote>
"""
