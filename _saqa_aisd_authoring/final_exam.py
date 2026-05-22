QUESTIONS = [
    # ===== L1 Overview of AI (2) =====
    (
        'multiple_choice',
        '<p>A South African retailer wants a system that improves its product recommendations as more customers shop. Which AI paradigm BEST fits this requirement?</p>',
        [
            ('<p>Symbolic rule-based expert system with hand-coded IF-THEN rules</p>', False),
            ('<p>Machine learning that adapts from historical and streaming purchase data</p>', True),
            ('<p>Static lookup tables populated by the marketing team</p>', False),
            ('<p>A deterministic finite-state machine</p>', False),
        ],
        '<p>Recommendation quality that <em>improves with more data</em> is the defining characteristic of machine learning. Rule-based and static approaches cannot generalise to new buying patterns without manual updates.</p>',
    ),
    (
        'true_false',
        '<p>Narrow (weak) AI systems are designed to perform a specific task and cannot transfer their learned competence to unrelated tasks without retraining.</p>',
        [('True', True), ('False', False)],
        '<p>Narrow AI is task-specific; general AI (AGI), which can transfer skills across arbitrary domains, has not yet been achieved.</p>',
    ),

    # ===== L2 Mathematics & Statistics (3) =====
    (
        'multiple_choice',
        '<p>A dataset of monthly salaries contains a few extreme outliers from executive pay. Which measure of central tendency is MOST robust for describing a typical salary?</p>',
        [
            ('<p>Arithmetic mean</p>', False),
            ('<p>Median</p>', True),
            ('<p>Range</p>', False),
            ('<p>Standard deviation</p>', False),
        ],
        '<p>The median is unaffected by extreme values, while the mean is pulled toward outliers. Range and standard deviation are measures of dispersion, not central tendency.</p>',
    ),
    (
        'multiple_choice',
        '<p>You compute a Pearson correlation of r = -0.92 between hours spent on social media and exam scores. What can you legitimately conclude?</p>',
        [
            ('<p>Social media use causes lower exam scores</p>', False),
            ('<p>There is a strong negative linear association between the two variables</p>', True),
            ('<p>The two variables are statistically independent</p>', False),
            ('<p>92% of the variation in scores is explained by social media</p>', False),
        ],
        '<p>Correlation measures the strength and direction of a linear association but does not establish causation. The coefficient of determination (r squared = 0.846) is also distinct from r itself.</p>',
    ),
    (
        'multiple_choice',
        '<p>In a binary classifier, the probability of class 1 given features x is modelled as p = 1 / (1 + e^(-z)). Which function is this, and where is it used?</p>',
        [
            ('<p>ReLU activation, used in hidden layers of deep networks</p>', False),
            ('<p>Sigmoid (logistic) function, used to map a linear score to a probability</p>', True),
            ('<p>Softmax function, used for multi-class classification</p>', False),
            ('<p>Hyperbolic tangent, used to centre outputs around zero</p>', False),
        ],
        '<p>The expression 1 / (1 + e^(-z)) is the sigmoid/logistic function and squashes any real number into the interval (0, 1), making it suitable for binary probability estimates.</p>',
    ),

    # ===== L3 Analytical Thinking / SDD (2) =====
    (
        'multiple_choice',
        '<p>During the <strong>analysis</strong> phase of the Software Development Lifecycle, what is the PRIMARY deliverable?</p>',
        [
            ('<p>Production source code and unit tests</p>', False),
            ('<p>A documented set of functional and non-functional requirements</p>', True),
            ('<p>A deployed minimum viable product</p>', False),
            ('<p>A trained machine learning model</p>', False),
        ],
        '<p>Analysis focuses on eliciting and documenting what the system must do (functional) and how well it must do it (non-functional). Coding and deployment occur in later phases.</p>',
    ),
    (
        'true_false',
        '<p>Decomposing a complex problem into smaller, well-defined sub-problems is a core computational thinking technique that supports clearer algorithm design.</p>',
        [('True', True), ('False', False)],
        '<p>Decomposition, together with pattern recognition, abstraction, and algorithmic thinking, forms the foundation of computational and analytical problem-solving.</p>',
    ),

    # ===== L4 Data, Databases & Visualisation (3) =====
    (
        'multiple_choice',
        '<p>You need to store semi-structured JSON event logs from millions of IoT devices with flexible schemas. Which database type is MOST appropriate?</p>',
        [
            ('<p>A normalised relational (SQL) database with rigid schemas</p>', False),
            ('<p>A document-oriented NoSQL database such as MongoDB</p>', True),
            ('<p>A flat CSV file on a single server</p>', False),
            ('<p>An in-memory key-value cache as the system of record</p>', False),
        ],
        '<p>Document stores handle variable schemas and high write throughput well. Relational databases enforce rigid schemas, and CSV files cannot scale to millions of concurrent writes.</p>',
    ),
    (
        'multiple_choice',
        '<p>Which chart type is BEST for showing how a single numeric variable is distributed across its range?</p>',
        [
            ('<p>Pie chart</p>', False),
            ('<p>Histogram</p>', True),
            ('<p>Line chart of time vs. value</p>', False),
            ('<p>Scatter plot of two unrelated variables</p>', False),
        ],
        '<p>A histogram groups continuous values into bins and shows their frequency, revealing skewness, modality, and spread.</p>',
    ),
    (
        'multiple_choice',
        '<p>A column called <code>email</code> contains values like " Alice@X.com", "alice@x.com", and NULL. What is the MOST appropriate data-cleaning step before analysis?</p>',
        [
            ('<p>Drop the column entirely</p>', False),
            ('<p>Trim whitespace, normalise case, and handle missing values explicitly</p>', True),
            ('<p>Replace all NULLs with the string "unknown" without inspection</p>', False),
            ('<p>Encrypt the values so they cannot be read</p>', False),
        ],
        '<p>Standardising case and whitespace ensures duplicate detection works, while NULLs should be handled with an informed strategy (imputation, removal, or flagging) rather than blindly.</p>',
    ),

    # ===== L5 Computing Theory (2) =====
    (
        'multiple_choice',
        '<p>An algorithm performs a nested loop over n items inside another loop over n items. What is its time complexity in Big-O notation?</p>',
        [
            ('<p>O(log n)</p>', False),
            ('<p>O(n)</p>', False),
            ('<p>O(n^2)</p>', True),
            ('<p>O(1)</p>', False),
        ],
        '<p>Two nested loops each iterating n times produce n * n = n^2 operations, which is quadratic time complexity.</p>',
    ),
    (
        'true_false',
        '<p>RAM is volatile memory, meaning its contents are lost when the computer loses power, whereas SSD storage is non-volatile.</p>',
        [('True', True), ('False', False)],
        '<p>RAM stores running program state and is cleared on power loss; SSDs (and HDDs) retain data without power and are used for persistent storage.</p>',
    ),

    # ===== L6 SQL & Python scraping (3) =====
    (
        'multiple_choice',
        '<p>Which SQL clause is used to filter <em>groups</em> produced by GROUP BY, as opposed to filtering individual rows?</p>',
        [
            ('<p>WHERE</p>', False),
            ('<p>HAVING</p>', True),
            ('<p>ORDER BY</p>', False),
            ('<p>SELECT</p>', False),
        ],
        '<p>WHERE filters rows before aggregation; HAVING filters the aggregated groups after GROUP BY has been applied.</p>',
    ),
    (
        'multiple_choice',
        '<p>You write a Python scraper using <code>requests</code> and <code>BeautifulSoup</code> to pull product prices from a public site. Which practice is MOST ethically and legally responsible?</p>',
        [
            ('<p>Ignore the site&rsquo;s robots.txt and send hundreds of requests per second</p>', False),
            ('<p>Respect robots.txt, rate-limit requests, and check the site&rsquo;s terms of use</p>', True),
            ('<p>Spoof user-agent strings to bypass anti-bot defences</p>', False),
            ('<p>Republish the scraped data commercially without attribution</p>', False),
        ],
        '<p>Responsible scraping respects robots.txt, applies polite rate limits, and complies with the site&rsquo;s terms of service and applicable copyright/data-protection laws.</p>',
    ),
    (
        'multiple_choice',
        '<p>Given the query <code>SELECT customer_id, COUNT(*) AS orders FROM sales GROUP BY customer_id HAVING COUNT(*) &gt; 5;</code>, what does it return?</p>',
        [
            ('<p>All customers and their total orders</p>', False),
            ('<p>Customers who have placed more than five orders, with their order counts</p>', True),
            ('<p>The first five customers in the sales table</p>', False),
            ('<p>A single row containing the total number of orders</p>', False),
        ],
        '<p>The GROUP BY aggregates orders per customer, and HAVING filters out groups with five or fewer orders, leaving only frequent customers.</p>',
    ),

    # ===== L7 AI/ML/DL fundamentals (3) =====
    (
        'multiple_choice',
        '<p>Which scenario BEST illustrates <strong>unsupervised learning</strong>?</p>',
        [
            ('<p>Predicting house prices from labelled historical sales</p>', False),
            ('<p>Segmenting customers into groups based on purchasing behaviour without predefined labels</p>', True),
            ('<p>Classifying emails as spam using a labelled training set</p>', False),
            ('<p>Training an agent to play a game through rewards</p>', False),
        ],
        '<p>Clustering customers without target labels is a classic unsupervised task. The other examples are supervised learning and reinforcement learning respectively.</p>',
    ),
    (
        'multiple_choice',
        '<p>A model achieves 99% accuracy on training data but only 62% on unseen test data. What is MOST likely happening?</p>',
        [
            ('<p>Underfitting due to an overly simple model</p>', False),
            ('<p>Overfitting: the model memorised training noise and fails to generalise</p>', True),
            ('<p>Data leakage from the test set into training</p>', False),
            ('<p>The optimiser converged correctly and no action is needed</p>', False),
        ],
        '<p>A large gap between high training accuracy and lower test accuracy is the hallmark of overfitting. Remedies include regularisation, more data, simpler models, or cross-validation.</p>',
    ),
    (
        'true_false',
        '<p>Deep learning is a subfield of machine learning that uses multi-layer neural networks to learn hierarchical feature representations directly from data.</p>',
        [('True', True), ('False', False)],
        '<p>Deep learning lies within machine learning, which itself sits within the broader field of AI. Its defining feature is automatic feature learning through layered neural networks.</p>',
    ),

    # ===== L8 Machine Learning with Python (4) =====
    (
        'multiple_choice',
        '<p>For a highly imbalanced fraud-detection dataset (0.5% fraud), which evaluation metrics are MOST informative?</p>',
        [
            ('<p>Overall accuracy alone</p>', False),
            ('<p>Precision, recall, F1-score, and ROC-AUC</p>', True),
            ('<p>Mean squared error</p>', False),
            ('<p>R-squared</p>', False),
        ],
        '<p>With severe class imbalance, accuracy is misleading because predicting &ldquo;not fraud&rdquo; for everything scores ~99.5%. Precision, recall, F1, and ROC-AUC properly reflect minority-class performance.</p>',
    ),
    (
        'multiple_choice',
        '<p>Which scikit-learn workflow correctly prevents data leakage when scaling features for a model evaluated with cross-validation?</p>',
        [
            ('<p>Fit the scaler on the entire dataset, then split into folds</p>', False),
            ('<p>Wrap the scaler and estimator in a <code>Pipeline</code> so scaling is fit only on training folds</p>', True),
            ('<p>Scale the test set first and then the training set</p>', False),
            ('<p>Skip scaling because tree-based models always require it</p>', False),
        ],
        '<p>A Pipeline ensures preprocessing parameters (such as mean/variance for StandardScaler) are estimated only from the training fold, preventing information from the validation fold leaking into the model.</p>',
    ),
    (
        'multiple_choice',
        '<p>You optimise a logistic regression by iteratively updating weights in the direction that reduces the loss. Which algorithm is this?</p>',
        [
            ('<p>k-Nearest Neighbours search</p>', False),
            ('<p>Gradient descent</p>', True),
            ('<p>Decision-tree splitting on Gini impurity</p>', False),
            ('<p>Principal Component Analysis</p>', False),
        ],
        '<p>Gradient descent computes the gradient of the loss with respect to the parameters and steps in the opposite direction, scaled by a learning rate, until convergence.</p>',
    ),
    (
        'true_false',
        '<p>k-fold cross-validation gives a more reliable estimate of a model&rsquo;s generalisation performance than a single train/test split, especially on small datasets.</p>',
        [('True', True), ('False', False)],
        '<p>By averaging performance over k different train/validation partitions, k-fold CV reduces the variance of the estimate and uses the data more efficiently.</p>',
    ),

    # ===== L9 Deep Learning & TensorFlow (4) =====
    (
        'multiple_choice',
        '<p>Which neural network architecture is specifically designed to exploit the spatial structure of images?</p>',
        [
            ('<p>Recurrent Neural Network (RNN)</p>', False),
            ('<p>Convolutional Neural Network (CNN)</p>', True),
            ('<p>Multilayer Perceptron with only dense layers</p>', False),
            ('<p>k-Means clustering network</p>', False),
        ],
        '<p>CNNs use convolutional filters that share weights across spatial locations, capturing local patterns such as edges and textures efficiently &mdash; ideal for image data.</p>',
    ),
    (
        'multiple_choice',
        '<p>You have only 2,000 medical images but need a strong classifier. Which deep-learning strategy is MOST suitable?</p>',
        [
            ('<p>Train a very large CNN from random initialisation</p>', False),
            ('<p>Apply transfer learning by fine-tuning a model pretrained on ImageNet</p>', True),
            ('<p>Use a single-layer perceptron because the dataset is small</p>', False),
            ('<p>Skip deep learning entirely and use linear regression</p>', False),
        ],
        '<p>Transfer learning reuses features learned from a large source dataset, dramatically reducing the data and compute needed to achieve good performance on a smaller target task.</p>',
    ),
    (
        'multiple_choice',
        '<p>In TensorFlow / Keras, which loss function is appropriate for a multi-class classification problem with integer-encoded labels?</p>',
        [
            ('<p><code>mean_squared_error</code></p>', False),
            ('<p><code>binary_crossentropy</code></p>', False),
            ('<p><code>sparse_categorical_crossentropy</code></p>', True),
            ('<p><code>cosine_similarity</code></p>', False),
        ],
        '<p>For multi-class problems with integer labels, sparse categorical crossentropy is the standard choice; categorical crossentropy is used with one-hot labels, and binary crossentropy is for two-class problems.</p>',
    ),
    (
        'true_false',
        '<p>Dropout is a regularisation technique that randomly deactivates a fraction of neurons during training to reduce overfitting in deep neural networks.</p>',
        [('True', True), ('False', False)],
        '<p>By randomly masking activations during training, dropout forces the network to learn redundant, more robust representations, which improves generalisation.</p>',
    ),

    # ===== L10 Governance, Ethics, POPIA, Design Thinking, 4IR, Teamwork (3) =====
    (
        'multiple_choice',
        '<p>Under South Africa&rsquo;s POPIA (Protection of Personal Information Act), which practice is MOST aligned with the law when building an AI model on customer data?</p>',
        [
            ('<p>Collect as much personal data as possible &ldquo;just in case&rdquo;</p>', False),
            ('<p>Process only the minimum personal data necessary for a specified, lawful purpose with informed consent</p>', True),
            ('<p>Share raw customer records with any third-party vendor without contracts</p>', False),
            ('<p>Retain personal data indefinitely after the purpose has been fulfilled</p>', False),
        ],
        '<p>POPIA enshrines principles of minimality, purpose specification, lawful processing, and limited retention. Excessive collection and indefinite retention violate these conditions.</p>',
    ),
    (
        'multiple_choice',
        '<p>In Design Thinking, which phase focuses on deeply understanding users&rsquo; needs, contexts, and pain points before any solution is proposed?</p>',
        [
            ('<p>Prototype</p>', False),
            ('<p>Empathise</p>', True),
            ('<p>Test</p>', False),
            ('<p>Deploy</p>', False),
        ],
        '<p>Empathise is the first stage of the Design Thinking process, ensuring solutions are grounded in real user needs rather than assumptions.</p>',
    ),
    (
        'true_false',
        '<p>A biased training dataset can cause an AI system to produce systematically unfair outcomes for certain groups, making bias auditing an ethical responsibility for developers.</p>',
        [('True', True), ('False', False)],
        '<p>Models inherit and can amplify biases present in their training data. Responsible AI practice requires bias detection, mitigation, and ongoing fairness assessment.</p>',
    ),

    # ===== Work Experience Modules synthesis (1) =====
    (
        'multiple_choice',
        '<p>A deployed credit-scoring model&rsquo;s predictive performance has gradually degraded as customer behaviour shifted post-deployment. Which MLOps practice DIRECTLY addresses this?</p>',
        [
            ('<p>Increase the training learning rate without retraining</p>', False),
            ('<p>Continuous monitoring for model drift, with automated retraining and A/B testing of new versions</p>', True),
            ('<p>Delete the production logs to save storage</p>', False),
            ('<p>Disable logging to improve inference latency</p>', False),
        ],
        '<p>Model drift &mdash; when the relationship between inputs and the target changes over time &mdash; is detected through monitoring and remedied by retraining on fresh data and validating the new model via A/B testing before full rollout.</p>',
    ),
]
