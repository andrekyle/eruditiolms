"""SAQA 118792 AI Software Developer (NQF 5)

Lesson 07 - Introduction to AI, Machine Learning and Deep Learning.

Covers:
    - KM-06 Introduction to AI, ML, DL (NQF4, 5 credits)
    - KM-07 Artificial Intelligence (NQF5, 12 credits)

Exports:
    LESSON_HTML    : str  -- the lesson body (>= 2200 chars)
    QUESTIONS      : list -- exactly 8 (qtype, qhtml, opts, fb) tuples
    PRACTICAL_HTML : str  -- the practical lab body (>= 1500 chars)
"""

LESSON_HTML = (
    "<h2>AI, Machine Learning and Deep Learning Fundamentals</h2>"
    "<p>Artificial Intelligence (AI), Machine Learning (ML) and Deep Learning (DL) are "
    "often used interchangeably in industry, but they describe <strong>nested</strong> "
    "fields. Think of three concentric circles: AI is the outermost circle &mdash; the "
    "broad goal of making machines behave intelligently. Inside AI sits ML, a family of "
    "techniques where the machine <em>learns patterns from data</em> instead of being "
    "explicitly programmed. Inside ML sits DL, a sub-family that uses multi-layer "
    "neural networks to learn hierarchical representations.</p>"
    "<blockquote>AI &supe; ML &supe; DL. Every deep-learning system is a machine-learning "
    "system, and every machine-learning system is an AI system &mdash; but not the other "
    "way around.</blockquote>"

    "<h3>1. Categories of AI</h3>"
    "<p><strong>By capability</strong> we distinguish three levels:</p>"
    "<ul>"
    "<li><strong>Narrow AI (ANI)</strong> &mdash; specialised for one task (spam filter, "
    "voice assistant, fraud-detection model). All AI in production today is narrow.</li>"
    "<li><strong>General AI (AGI)</strong> &mdash; hypothetical machine that can perform "
    "any intellectual task a human can, transferring knowledge between domains.</li>"
    "<li><strong>Super AI (ASI)</strong> &mdash; hypothetical intelligence surpassing "
    "humans across every dimension, including creativity and social skills.</li>"
    "</ul>"
    "<p><strong>By functionality</strong> AI systems are classified as:</p>"
    "<ol>"
    "<li><strong>Reactive machines</strong> &mdash; no memory, react to current input "
    "only (e.g. Deep Blue chess engine).</li>"
    "<li><strong>Limited memory</strong> &mdash; use recent past observations "
    "(self-driving cars, most modern ML models).</li>"
    "<li><strong>Theory of mind</strong> &mdash; understand emotions and intent of "
    "other agents (research stage).</li>"
    "<li><strong>Self-aware</strong> &mdash; conscious of own state (still theoretical).</li>"
    "</ol>"

    "<h3>2. Machine-Learning Paradigms</h3>"
    "<ul>"
    "<li><strong>Supervised learning</strong> &mdash; labelled data; the model maps "
    "<em>X &rarr; y</em>. Sub-types: <em>classification</em> (predict a category, e.g. "
    "fraud / not-fraud) and <em>regression</em> (predict a number, e.g. house price).</li>"
    "<li><strong>Unsupervised learning</strong> &mdash; unlabelled data; the model "
    "discovers structure. Sub-types: <em>clustering</em> (k-means, DBSCAN), "
    "<em>dimensionality reduction</em> (PCA, t-SNE, UMAP) and "
    "<em>association rule mining</em> (Apriori, FP-Growth for market-basket analysis).</li>"
    "<li><strong>Semi-supervised learning</strong> &mdash; a small labelled set combined "
    "with a large unlabelled set; common when labelling is expensive (medical images).</li>"
    "<li><strong>Reinforcement learning (RL)</strong> &mdash; an <strong>agent</strong> "
    "takes <strong>actions</strong> in an <strong>environment</strong> to maximise a "
    "cumulative <strong>reward</strong> signal. Used in robotics, game playing "
    "(AlphaGo), recommendation and dynamic pricing.</li>"
    "</ul>"

    "<h3>3. The ML Lifecycle</h3>"
    "<ol>"
    "<li><strong>Problem framing</strong> &mdash; is this classification, regression, "
    "clustering, or RL? What does success look like in business terms?</li>"
    "<li><strong>Data collection</strong> &mdash; from databases, APIs, sensors, logs.</li>"
    "<li><strong>Preprocessing</strong> &mdash; handle missing values, outliers, "
    "encoding, scaling.</li>"
    "<li><strong>Feature engineering</strong> &mdash; create informative inputs "
    "(ratios, time features, embeddings).</li>"
    "<li><strong>Model selection</strong> &mdash; pick candidate algorithms.</li>"
    "<li><strong>Training</strong> &mdash; fit parameters on the training set.</li>"
    "<li><strong>Evaluation</strong> &mdash; measure on validation / test sets.</li>"
    "<li><strong>Deployment</strong> &mdash; package as an API, batch job or edge model.</li>"
    "<li><strong>Monitoring</strong> &mdash; watch for data drift, concept drift, "
    "degraded metrics; retrain when needed.</li>"
    "</ol>"
    "<pre><code># ML lifecycle in pseudocode\n"
    "data = load_data(sources)\n"
    "data = clean(data)\n"
    "X, y = engineer_features(data)\n"
    "X_train, X_val, X_test, y_train, y_val, y_test = split(X, y)\n"
    "model = choose_algorithm(problem_type)\n"
    "model.fit(X_train, y_train)\n"
    "score = evaluate(model, X_val, y_val)\n"
    "if score &gt;= target:\n"
    "    deploy(model)\n"
    "    monitor(model, production_stream)\n"
    "else:\n"
    "    iterate()  # tune, add data, change algorithm\n"
    "</code></pre>"

    "<h3>4. Choosing the Right Algorithm</h3>"
    "<table>"
    "<thead><tr><th>Problem type</th><th>Typical algorithms</th><th>Example</th></tr></thead>"
    "<tbody>"
    "<tr><td>Binary classification</td><td>Logistic regression, Random Forest, "
    "Gradient Boosting (XGBoost)</td><td>Loan default yes/no</td></tr>"
    "<tr><td>Multi-class classification</td><td>Random Forest, SVM, Neural Network</td>"
    "<td>Crop type from satellite image</td></tr>"
    "<tr><td>Regression</td><td>Linear regression, Gradient Boosting, MLP</td>"
    "<td>Predict electricity demand</td></tr>"
    "<tr><td>Clustering</td><td>k-Means, DBSCAN, Gaussian Mixture</td>"
    "<td>Customer segmentation</td></tr>"
    "<tr><td>Dimensionality reduction</td><td>PCA, UMAP, autoencoder</td>"
    "<td>Visualise high-dim data</td></tr>"
    "<tr><td>Sequence / language</td><td>RNN, LSTM, Transformer</td>"
    "<td>Translate isiZulu &harr; English</td></tr>"
    "<tr><td>Image / vision</td><td>CNN, Vision Transformer</td>"
    "<td>X-ray classification</td></tr>"
    "<tr><td>Sequential decision</td><td>Q-learning, Policy gradient, PPO</td>"
    "<td>Warehouse robot</td></tr>"
    "</tbody></table>"

    "<h3>5. Train / Validation / Test &amp; Cross-Validation</h3>"
    "<p>A typical split is 70 / 15 / 15. The <strong>training set</strong> fits the "
    "model, the <strong>validation set</strong> tunes hyperparameters, and the "
    "<strong>test set</strong> gives an unbiased final estimate. When data is scarce, "
    "use <strong>k-fold cross-validation</strong>: split the data into k folds, train "
    "on k-1 and validate on the remaining fold, rotating k times, and average the score.</p>"

    "<h3>6. Bias-Variance Trade-off</h3>"
    "<p><strong>Bias</strong> is error from over-simplified assumptions "
    "(<em>underfitting</em>): the model is too rigid to capture the pattern. "
    "<strong>Variance</strong> is error from sensitivity to noise "
    "(<em>overfitting</em>): the model memorises the training data and fails on new "
    "data. Total error = bias&sup2; + variance + irreducible noise. The goal is the "
    "sweet spot.</p>"
    "<ul>"
    "<li>Symptoms of <strong>underfitting</strong>: high training error and high test "
    "error.</li>"
    "<li>Symptoms of <strong>overfitting</strong>: low training error but high test "
    "error.</li>"
    "<li>Remedies: collect more data, use a simpler model, apply <em>regularisation</em> "
    "(L1/L2, dropout), use <em>early stopping</em>, perform feature selection, or "
    "ensemble multiple models.</li>"
    "</ul>"

    "<h3>7. Evaluation Metrics</h3>"
    "<p><strong>Classification</strong>: <em>accuracy</em> (fraction correct), "
    "<em>precision</em> (TP / (TP+FP)), <em>recall</em> (TP / (TP+FN)), "
    "<em>F1</em> (harmonic mean of precision and recall) and <em>ROC-AUC</em> "
    "(area under the receiver-operating-characteristic curve, threshold-independent).</p>"
    "<p><strong>Regression</strong>: <em>MAE</em> (mean absolute error), "
    "<em>MSE</em> (mean squared error), <em>RMSE</em> (square root of MSE, same units "
    "as the target) and <em>R&sup2;</em> (proportion of variance explained).</p>"
    "<p>Always pick the metric that matches the business cost. In fraud detection, "
    "recall matters more than raw accuracy because missing fraud is expensive.</p>"

    "<h3>8. From ML to Deep Learning</h3>"
    "<p>A <strong>perceptron</strong> is the simplest neural unit: it takes inputs "
    "x&#8321;...x&#8345;, multiplies each by a <strong>weight</strong>, adds a bias, "
    "and passes the sum through an <strong>activation function</strong> "
    "(sigmoid, ReLU, tanh). Stack many perceptrons into <strong>layers</strong> "
    "(input &rarr; hidden &rarr; output) and you have a neural network. "
    "The <strong>forward pass</strong> computes predictions; the "
    "<strong>backward pass</strong> (back-propagation) uses gradient descent to "
    "update weights so the loss decreases. Deep networks have many hidden layers, "
    "letting the model learn features automatically rather than relying on manual "
    "feature engineering. We explore neural networks in depth in Lesson 9.</p>"
)


QUESTIONS = [
    (
        "mc",
        "<p>Which statement best describes the relationship between AI, ML and DL?</p>",
        [
            ("<p>They are three independent fields with no overlap.</p>", False),
            ("<p>AI is a subset of ML, which is a subset of DL.</p>", False),
            ("<p>DL is a subset of ML, which is a subset of AI.</p>", True),
            ("<p>ML and DL are synonyms; AI is unrelated.</p>", False),
        ],
        "<p>The correct nesting is AI &supe; ML &supe; DL. Deep learning is a "
        "specialised form of machine learning that uses multi-layer neural networks, "
        "and machine learning itself is one approach to building AI systems.</p>",
    ),
    (
        "mc",
        "<p>A team labels 2 000 customer reviews as <em>positive</em> or "
        "<em>negative</em> and trains a model to classify new reviews. Which "
        "ML paradigm is this?</p>",
        [
            ("<p>Unsupervised learning</p>", False),
            ("<p>Supervised learning (classification)</p>", True),
            ("<p>Reinforcement learning</p>", False),
            ("<p>Dimensionality reduction</p>", False),
        ],
        "<p>Labels are provided (positive / negative) and the output is a category, "
        "so this is supervised classification.</p>",
    ),
    (
        "mc",
        "<p>Which scenario is the best fit for <strong>reinforcement learning</strong>?</p>",
        [
            ("<p>Predicting tomorrow&apos;s rainfall in millimetres from weather "
             "history.</p>", False),
            ("<p>Grouping unlabelled shoppers by buying behaviour.</p>", False),
            ("<p>Training a robot to navigate a warehouse by trial and error using "
             "a reward signal.</p>", True),
            ("<p>Classifying emails as spam or not spam from labelled examples.</p>", False),
        ],
        "<p>Reinforcement learning involves an agent interacting with an environment "
        "and learning a policy that maximises cumulative reward &mdash; exactly the "
        "warehouse-robot setup.</p>",
    ),
    (
        "mc",
        "<p>A model achieves 99% accuracy on the training set but only 62% on the "
        "test set. What is most likely happening?</p>",
        [
            ("<p>Underfitting &mdash; the model is too simple.</p>", False),
            ("<p>Overfitting &mdash; the model has memorised the training data.</p>", True),
            ("<p>Data leakage from the test set into training.</p>", False),
            ("<p>The labels are wrong.</p>", False),
        ],
        "<p>A large gap with high training and low test performance is the classic "
        "signature of overfitting (high variance). Remedies include regularisation, "
        "more data, a simpler model, or early stopping.</p>",
    ),
    (
        "mc",
        "<p>For a <strong>fraud-detection</strong> classifier where missing a fraud "
        "case is far more costly than a false alarm, which metric should you "
        "optimise first?</p>",
        [
            ("<p>Plain accuracy</p>", False),
            ("<p>Precision only</p>", False),
            ("<p>Recall (and F1 / ROC-AUC)</p>", True),
            ("<p>Mean Squared Error</p>", False),
        ],
        "<p>Recall = TP / (TP + FN) measures how many actual fraud cases we catch. "
        "When the cost of a missed fraud (false negative) is high, recall is the "
        "priority metric, usually balanced with precision via F1 or ROC-AUC.</p>",
    ),
    (
        "mc",
        "<p>Which step of the ML lifecycle is most directly responsible for detecting "
        "<em>data drift</em> after a model is in production?</p>",
        [
            ("<p>Feature engineering</p>", False),
            ("<p>Model selection</p>", False),
            ("<p>Monitoring</p>", True),
            ("<p>Problem framing</p>", False),
        ],
        "<p>Monitoring tracks input distributions and prediction quality in "
        "production, raising alerts when data drift or concept drift degrades the "
        "model so it can be retrained.</p>",
    ),
    (
        "tf",
        "<p>True or False: Deep learning always outperforms classical machine learning, "
        "regardless of the amount of training data available.</p>",
        [
            ("<p>True</p>", False),
            ("<p>False</p>", True),
        ],
        "<p>False. Deep learning shines with very large datasets and complex inputs "
        "(images, audio, text). On small tabular datasets, classical methods such as "
        "gradient boosting or logistic regression usually match or beat deep "
        "networks while being faster and easier to interpret.</p>",
    ),
    (
        "tf",
        "<p>True or False: In a neural network, the <strong>backward pass</strong> "
        "uses gradient information to update the weights so that the loss decreases.</p>",
        [
            ("<p>True</p>", True),
            ("<p>False</p>", False),
        ],
        "<p>True. The forward pass computes predictions and the loss; the backward "
        "pass (back-propagation) computes gradients of the loss with respect to each "
        "weight, and an optimiser such as SGD or Adam updates the weights to reduce "
        "the loss.</p>",
    ),
]


PRACTICAL_HTML = (
    "<h2>Practical Lab \u2014 Choose the Right ML Approach</h2>"
    "<p>In this lab you will apply the ML lifecycle and algorithm-selection table "
    "to three real South African problems. You will <strong>not</strong> write code "
    "yet &mdash; the goal is to think like a data scientist <em>before</em> touching "
    "a keyboard. Scenario 1 is fully worked. Complete scenarios 2 and 3 yourself.</p>"

    "<h3>Scenarios</h3>"
    "<ol>"
    "<li><strong>Mobile-money fraud detection</strong> for a fintech that processes "
    "millions of transactions per day across South Africa.</li>"
    "<li><strong>Customer segmentation</strong> for a national retail chain that "
    "wants to personalise marketing for its loyalty members.</li>"
    "<li><strong>Maize crop-yield prediction</strong> for smallholder farmers in "
    "Mpumalanga, using weather, soil and satellite data.</li>"
    "</ol>"

    "<h3>Numbered steps (do this for each scenario)</h3>"
    "<ol>"
    "<li>State the <strong>problem type</strong> (classification, regression, "
    "clustering, RL, etc.).</li>"
    "<li>Choose the <strong>ML paradigm</strong> (supervised, unsupervised, "
    "semi-supervised, reinforcement) and justify in one sentence.</li>"
    "<li>List <strong>two candidate algorithms</strong> from the lesson table.</li>"
    "<li>Define a <strong>primary success metric</strong> aligned with business cost.</li>"
    "<li>Identify <strong>data sources</strong> you would need.</li>"
    "<li>Sketch an <strong>evaluation plan</strong>: how you split data, what baseline "
    "you compare against, and what would justify deployment.</li>"
    "</ol>"

    "<h3>Worked example \u2014 Scenario 1: Mobile-money fraud</h3>"
    "<ul>"
    "<li><strong>Problem type:</strong> binary classification (fraud / not fraud).</li>"
    "<li><strong>Paradigm:</strong> supervised learning &mdash; historical "
    "transactions are labelled by the fraud-investigation team.</li>"
    "<li><strong>Candidate algorithms:</strong> Gradient Boosting (XGBoost) and "
    "Logistic Regression as an interpretable baseline.</li>"
    "<li><strong>Success metric:</strong> Recall on the fraud class with precision "
    "&gt; 0.5; secondary metric ROC-AUC. Missing a fraud is far costlier than a "
    "false alarm.</li>"
    "<li><strong>Data sources:</strong> transaction log (amount, merchant, time, "
    "channel), device fingerprint, SIM age, customer profile, historical fraud "
    "labels from the investigations database.</li>"
    "<li><strong>Evaluation plan:</strong> time-based split (train on Jan-Sep, "
    "validate on Oct, test on Nov-Dec) to avoid leakage; baseline = current rules "
    "engine; deploy if recall improves by &gt;= 10 percentage points at equal "
    "precision; monitor weekly for data drift.</li>"
    "</ul>"

    "<h3>Your turn \u2014 Scenario 2: Retail customer segmentation</h3>"
    "<ul>"
    "<li><strong>Problem type:</strong> ____________________</li>"
    "<li><strong>Paradigm:</strong> ____________________</li>"
    "<li><strong>Candidate algorithms:</strong> ____________________</li>"
    "<li><strong>Success metric:</strong> ____________________</li>"
    "<li><strong>Data sources:</strong> ____________________</li>"
    "<li><strong>Evaluation plan:</strong> ____________________</li>"
    "</ul>"

    "<h3>Your turn \u2014 Scenario 3: Maize crop-yield prediction</h3>"
    "<ul>"
    "<li><strong>Problem type:</strong> ____________________</li>"
    "<li><strong>Paradigm:</strong> ____________________</li>"
    "<li><strong>Candidate algorithms:</strong> ____________________</li>"
    "<li><strong>Success metric:</strong> ____________________</li>"
    "<li><strong>Data sources:</strong> ____________________</li>"
    "<li><strong>Evaluation plan:</strong> ____________________</li>"
    "</ul>"

    "<h3>Hints</h3>"
    "<ul>"
    "<li>Segmentation has <em>no labels</em> &mdash; which paradigm does that "
    "suggest?</li>"
    "<li>Crop yield is measured in tonnes per hectare &mdash; a continuous number. "
    "Which family of algorithms predicts continuous values?</li>"
    "<li>For segmentation, consider how you would <em>validate</em> clusters when "
    "there is no ground truth (silhouette score, business review).</li>"
    "</ul>"

    "<h3>Reflection questions</h3>"
    "<ol>"
    "<li>Which scenario was hardest to frame and why?</li>"
    "<li>For each scenario, what is one <strong>ethical risk</strong> (bias, "
    "privacy, exclusion) you must mitigate before deployment?</li>"
    "<li>If you had only one month of data instead of two years, how would your "
    "algorithm choice change?</li>"
    "<li>Which metric would you report to a non-technical executive, and why?</li>"
    "</ol>"
)


assert LESSON_HTML.startswith("<h2>AI, Machine Learning and Deep Learning Fundamentals</h2>")
assert len(LESSON_HTML) >= 2200
assert len(QUESTIONS) == 8
assert PRACTICAL_HTML.startswith("<h2>Practical Lab \u2014 Choose the Right ML Approach</h2>")
assert len(PRACTICAL_HTML) >= 1500
for _q in QUESTIONS:
    _qtype, _qhtml, _opts, _fb = _q
    assert _qtype in ("mc", "tf")
    if _qtype == "mc":
        assert len(_opts) == 4
    else:
        assert len(_opts) == 2
    assert sum(1 for _o in _opts if _o[1]) == 1
assert sum(1 for _q in QUESTIONS if _q[0] == "mc") >= 6
assert sum(1 for _q in QUESTIONS if _q[0] == "tf") <= 2
