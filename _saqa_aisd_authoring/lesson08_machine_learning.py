"""SAQA 118792 AI Software Developer (NQF 5) - Lesson 08.

Covers:
    KM-08 Machine Learning (NQF5, 16 cr)
    PM-05 Build a simple AI solution using Python (NQF5, 8 cr)
    PM-07 Use Machine Learning to Build an AI Solution in Python (NQF5, 6 cr)
"""

LESSON_HTML = (
    "<h2>Machine Learning with Python</h2>"
    "<p>Machine learning (ML) is the discipline of building systems that learn"
    " patterns from data instead of being explicitly programmed with rules. In"
    " Python the de-facto starting point is <strong>scikit-learn</strong>, a"
    " mature library that exposes a consistent <code>fit</code> /"
    " <code>predict</code> / <code>transform</code> API across dozens of"
    " algorithms. Around it sits a rich ecosystem: <em>pandas</em> for tabular"
    " data, <em>NumPy</em> for arrays, <em>matplotlib</em> and"
    " <em>seaborn</em> for visualisation, <em>XGBoost</em> and"
    " <em>LightGBM</em> for gradient boosting, <em>imbalanced-learn</em> for"
    " resampling, and <em>joblib</em> for model persistence.</p>"

    "<h3>1. Data preprocessing</h3>"
    "<p>Real-world data is messy. Before any model can learn, you must clean"
    " and reshape the inputs.</p>"
    "<ul>"
    "<li><strong>Missing values</strong> &mdash; replace with"
    " <em>mean</em> (numeric, roughly symmetric), <em>median</em> (numeric"
    " with outliers or skew) or <em>mode</em> (categorical). scikit-learn"
    " offers <code>SimpleImputer</code> and <code>KNNImputer</code>.</li>"
    "<li><strong>Encoding categorical features</strong> &mdash;"
    " <em>one-hot</em> for nominal categories with low cardinality,"
    " <em>ordinal</em> when an order exists (e.g. small/medium/large), and"
    " <em>target encoding</em> for high-cardinality columns (replace each"
    " category with the mean of the target, with care to avoid leakage).</li>"
    "<li><strong>Feature scaling</strong> &mdash; <em>standardisation</em>"
    " (<code>StandardScaler</code>, zero mean / unit variance) suits"
    " algorithms that assume Gaussian-like inputs (logistic regression, SVM,"
    " PCA, k-NN). <em>Min-max normalisation</em> (<code>MinMaxScaler</code>,"
    " range 0&ndash;1) is useful for neural networks and distance metrics on"
    " bounded features. Tree-based models do not require scaling.</li>"
    "<li><strong>Outlier handling</strong> &mdash; detect with IQR, z-score"
    " or Isolation Forest; then clip, winsorise, transform (log) or drop"
    " depending on whether they are errors or genuine extreme cases.</li>"
    "</ul>"

    "<h3>2. Feature engineering and selection</h3>"
    "<p>Good features beat clever algorithms. Engineer interaction terms,"
    " ratios, date parts, text length, polynomial features"
    " (<code>PolynomialFeatures</code>) and domain-specific aggregates."
    " To prune useless or redundant columns, use one of three families of"
    " feature-selection methods:</p>"
    "<ul>"
    "<li><strong>Filter</strong> &mdash; rank features independently of any"
    " model (correlation, chi-squared, mutual information,"
    " <code>SelectKBest</code>).</li>"
    "<li><strong>Wrapper</strong> &mdash; train a model on subsets and"
    " evaluate (forward / backward selection, recursive feature elimination"
    " <code>RFE</code>). Accurate but expensive.</li>"
    "<li><strong>Embedded</strong> &mdash; selection happens inside the"
    " model: L1 (Lasso) regularisation, tree-based feature importances,"
    " <code>SelectFromModel</code>.</li>"
    "</ul>"

    "<h3>3. Supervised algorithms &mdash; when to pick which</h3>"
    "<table><thead><tr><th>Algorithm</th><th>Use it when</th></tr></thead>"
    "<tbody>"
    "<tr><td><strong>Linear regression</strong></td><td>Target is continuous"
    " and roughly linear in features; you need an interpretable baseline.</td></tr>"
    "<tr><td><strong>Logistic regression</strong></td><td>Binary or"
    " multinomial classification with mostly linear decision boundaries;"
    " coefficients are interpretable.</td></tr>"
    "<tr><td><strong>k-Nearest Neighbours</strong></td><td>Small to medium"
    " datasets, low-dimensional, when local similarity matters; no training"
    " phase but slow at prediction.</td></tr>"
    "<tr><td><strong>Decision tree</strong></td><td>You need a single"
    " interpretable model and can tolerate variance; handles mixed types"
    " without scaling.</td></tr>"
    "<tr><td><strong>Random forest</strong></td><td>Strong default for"
    " tabular data; robust to outliers, little tuning needed.</td></tr>"
    "<tr><td><strong>Gradient boosting (XGBoost, LightGBM)</strong></td>"
    "<td>Top performance on structured/tabular Kaggle-style problems; needs"
    " more tuning and care against overfitting.</td></tr>"
    "<tr><td><strong>Support Vector Machine</strong></td><td>Medium-sized"
    " datasets with clear margins; kernel trick for non-linear boundaries;"
    " slow on very large data.</td></tr>"
    "<tr><td><strong>Naive Bayes</strong></td><td>Text classification, spam"
    " filtering, very fast baseline when features are roughly"
    " independent.</td></tr>"
    "</tbody></table>"

    "<h3>4. Unsupervised algorithms</h3>"
    "<ul>"
    "<li><strong>k-Means</strong> &mdash; partition data into <em>k</em>"
    " spherical clusters; pick <em>k</em> with the elbow method or"
    " silhouette score.</li>"
    "<li><strong>Hierarchical clustering</strong> &mdash; build a dendrogram;"
    " no need to fix <em>k</em> upfront, but O(n&sup2;) memory.</li>"
    "<li><strong>DBSCAN</strong> &mdash; density-based; finds arbitrarily"
    " shaped clusters and labels noise points; great when cluster count is"
    " unknown.</li>"
    "<li><strong>PCA</strong> &mdash; linear dimensionality reduction for"
    " visualisation, denoising and speeding up downstream models.</li>"
    "</ul>"

    "<h3>5. Model evaluation</h3>"
    "<p>Never trust accuracy on the training set. Split data into"
    " <strong>train / validation / test</strong> (e.g. 60/20/20), or use"
    " <strong>k-fold cross-validation</strong> (typically k=5 or 10) for a"
    " more stable estimate. For classification with imbalanced classes use"
    " <strong>stratified</strong> CV so each fold preserves class ratios.</p>"
    "<ul>"
    "<li><strong>Classification metrics</strong>: confusion matrix,"
    " precision, recall, F1, ROC-AUC (threshold-independent ranking),"
    " PR-AUC (better than ROC-AUC for heavy imbalance).</li>"
    "<li><strong>Regression metrics</strong>: MAE (robust to outliers), MSE,"
    " RMSE (same units as target), R&sup2; (proportion of variance"
    " explained).</li>"
    "</ul>"

    "<h3>6. Hyperparameter tuning</h3>"
    "<ul>"
    "<li><strong>Grid search</strong> (<code>GridSearchCV</code>) &mdash;"
    " exhaustive over a small grid; guaranteed to find the best combination"
    " in the grid but expensive.</li>"
    "<li><strong>Random search</strong> (<code>RandomizedSearchCV</code>)"
    " &mdash; samples randomly from distributions; often matches grid search"
    " for a fraction of the cost.</li>"
    "<li><strong>Bayesian optimisation</strong> (Optuna, scikit-optimize)"
    " &mdash; builds a surrogate model of the score surface and picks the"
    " next trial intelligently; best for expensive models.</li>"
    "</ul>"

    "<h3>7. Pipelines and ColumnTransformer</h3>"
    "<p><code>Pipeline</code> chains preprocessing steps with a final"
    " estimator so that everything is fit on training data only, eliminating"
    " leakage. <code>ColumnTransformer</code> lets you apply different"
    " transformers to numeric and categorical columns. A full example:</p>"
    "<pre><code>"
    "from sklearn.pipeline import Pipeline\n"
    "from sklearn.compose import ColumnTransformer\n"
    "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n"
    "from sklearn.impute import SimpleImputer\n"
    "from sklearn.linear_model import LogisticRegression\n"
    "from sklearn.model_selection import train_test_split, GridSearchCV\n"
    "\n"
    "numeric = ['age', 'income']\n"
    "categorical = ['city', 'plan']\n"
    "\n"
    "pre = ColumnTransformer([\n"
    "    ('num', Pipeline([\n"
    "        ('imp', SimpleImputer(strategy='median')),\n"
    "        ('scale', StandardScaler()),\n"
    "    ]), numeric),\n"
    "    ('cat', Pipeline([\n"
    "        ('imp', SimpleImputer(strategy='most_frequent')),\n"
    "        ('oh', OneHotEncoder(handle_unknown='ignore')),\n"
    "    ]), categorical),\n"
    "])\n"
    "\n"
    "pipe = Pipeline([('pre', pre),\n"
    "                 ('clf', LogisticRegression(max_iter=1000))])\n"
    "\n"
    "X_tr, X_te, y_tr, y_te = train_test_split(\n"
    "    X, y, test_size=0.2, stratify=y, random_state=42)\n"
    "\n"
    "grid = GridSearchCV(pipe,\n"
    "                    {'clf__C': [0.1, 1.0, 10.0]},\n"
    "                    cv=5, scoring='f1_macro')\n"
    "grid.fit(X_tr, y_tr)\n"
    "print('best C =', grid.best_params_)\n"
    "print('test score =', grid.score(X_te, y_te))\n"
    "</code></pre>"

    "<h3>8. Handling class imbalance</h3>"
    "<p>When one class is rare (fraud, disease, churn) accuracy is misleading."
    " Mitigations:</p>"
    "<ul>"
    "<li><code>class_weight='balanced'</code> &mdash; tells the model to"
    " weight rare classes more heavily.</li>"
    "<li><strong>SMOTE</strong> (Synthetic Minority Oversampling Technique)"
    " from <em>imbalanced-learn</em> &mdash; creates synthetic minority"
    " samples; apply <em>inside</em> a pipeline so it only fits on training"
    " folds.</li>"
    "<li>Undersample the majority class for very large datasets.</li>"
    "<li>Pick threshold-independent metrics (PR-AUC, F1).</li>"
    "</ul>"

    "<h3>9. Persisting models</h3>"
    "<p>Once trained, save the fitted pipeline so it can be reloaded by a"
    " web service:</p>"
    "<pre><code>"
    "import joblib\n"
    "joblib.dump(grid.best_estimator_, 'model.joblib')\n"
    "# later, in app.py\n"
    "model = joblib.load('model.joblib')\n"
    "prediction = model.predict(new_data)\n"
    "</code></pre>"
    "<p><code>pickle</code> works too, but <code>joblib</code> is faster for"
    " NumPy-heavy objects. Always pin library versions &mdash; a model"
    " pickled with scikit-learn 1.4 may not load under 1.6.</p>"

    "<blockquote><strong>Rule of thumb:</strong> start with a simple, well"
    " regularised baseline (logistic regression or random forest) inside a"
    " Pipeline, evaluate honestly with stratified cross-validation, and only"
    " reach for gradient boosting or deep learning once the baseline is"
    " understood.</blockquote>"
)


QUESTIONS = [
    (
        "mc",
        "<p>Which scikit-learn class is the correct choice for chaining"
        " different preprocessing steps to <em>numeric</em> and"
        " <em>categorical</em> columns within a single estimator?</p>",
        [
            ("<code>ColumnTransformer</code>", True),
            ("<code>FeatureUnion</code>", False),
            ("<code>VotingClassifier</code>", False),
            ("<code>StackingRegressor</code>", False),
        ],
        "<p><code>ColumnTransformer</code> applies different transformers to"
        " specified column subsets and is usually wrapped inside a"
        " <code>Pipeline</code>.</p>",
    ),
    (
        "mc",
        "<p>You have a numeric feature with a few extreme outliers. Which"
        " imputation strategy is generally safest for filling its missing"
        " values?</p>",
        [
            ("Mean imputation", False),
            ("Median imputation", True),
            ("Mode imputation", False),
            ("Replace with zero", False),
        ],
        "<p>The median is robust to outliers, whereas the mean is pulled"
        " toward extreme values and would distort the imputed column.</p>",
    ),
    (
        "mc",
        "<p>For a highly imbalanced binary classification problem (say 2%"
        " positives), which metric is the <strong>least</strong> informative"
        " on its own?</p>",
        [
            ("Plain accuracy", True),
            ("Precision-Recall AUC", False),
            ("F1 score", False),
            ("Recall on the positive class", False),
        ],
        "<p>A model that always predicts the majority class scores 98%"
        " accuracy yet is useless. Prefer PR-AUC, F1 or recall on the rare"
        " class.</p>",
    ),
    (
        "mc",
        "<p>Which family of feature-selection methods performs selection"
        " <em>inside</em> the model training process itself, for example"
        " through L1 regularisation or tree feature importances?</p>",
        [
            ("Filter methods", False),
            ("Wrapper methods", False),
            ("Embedded methods", True),
            ("Ensemble methods", False),
        ],
        "<p>Embedded methods learn which features matter as part of fitting"
        " the model (Lasso, tree importances, <code>SelectFromModel</code>).</p>",
    ),
    (
        "mc",
        "<p>Which clustering algorithm does <strong>not</strong> require you"
        " to specify the number of clusters in advance and can also label"
        " noise points?</p>",
        [
            ("k-Means", False),
            ("DBSCAN", True),
            ("Gaussian Mixture Model", False),
            ("Mini-Batch k-Means", False),
        ],
        "<p>DBSCAN discovers clusters from density, decides the number"
        " automatically, and assigns low-density points the label"
        " <code>-1</code> (noise).</p>",
    ),
    (
        "mc",
        "<p>What is the main advantage of <code>RandomizedSearchCV</code>"
        " over <code>GridSearchCV</code> for hyperparameter tuning?</p>",
        [
            ("It guarantees the global optimum.", False),
            ("It explores a wide search space at a fraction of the"
             " computational cost.", True),
            ("It avoids the need for cross-validation.", False),
            ("It only works with tree-based models.", False),
        ],
        "<p>Random search samples combinations from distributions, so a"
        " modest budget can cover a much larger space than an exhaustive"
        " grid &mdash; often matching grid-search quality for far less"
        " compute.</p>",
    ),
    (
        "tf",
        "<p><strong>True or false:</strong> Tree-based models such as random"
        " forests and gradient boosting generally require their numeric"
        " features to be standardised (zero mean, unit variance) before"
        " training.</p>",
        [
            ("True", False),
            ("False", True),
        ],
        "<p>Tree splits depend only on feature ordering, not magnitude, so"
        " standardisation is unnecessary for tree-based models.</p>",
    ),
    (
        "tf",
        "<p><strong>True or false:</strong> When using SMOTE to oversample"
        " a minority class, you should resample the <em>entire</em> dataset"
        " before splitting it into training and test sets.</p>",
        [
            ("True", False),
            ("False", True),
        ],
        "<p>Resampling before splitting leaks synthetic information into the"
        " test set and inflates scores. Put SMOTE inside the pipeline so it"
        " is only fit on training folds.</p>",
    ),
]


PRACTICAL_HTML = (
    "<h2>Practical Lab \u2014 Build a Classifier on the Iris (or Wine)"
    " Dataset</h2>"
    "<p>In this lab you will take a small, well-known dataset all the way"
    " from raw arrays to a saved, reloadable classifier. The same recipe"
    " transfers directly to real business problems &mdash; only the data"
    " loader changes.</p>"

    "<h3>Step 1 &mdash; Load and explore</h3>"
    "<pre><code>"
    "import pandas as pd\n"
    "from sklearn.datasets import load_iris\n"
    "\n"
    "data = load_iris(as_frame=True)\n"
    "df = data.frame\n"
    "print(df.head())\n"
    "print(df.describe())\n"
    "print(df['target'].value_counts())\n"
    "</code></pre>"
    "<p>Confirm there are 150 rows, four numeric features and three"
    " perfectly balanced classes (50 each of <em>setosa</em>,"
    " <em>versicolor</em>, <em>virginica</em>).</p>"

    "<h3>Step 2 &mdash; Stratified train/test split</h3>"
    "<pre><code>"
    "from sklearn.model_selection import train_test_split\n"
    "\n"
    "X = df.drop(columns='target')\n"
    "y = df['target']\n"
    "\n"
    "X_train, X_test, y_train, y_test = train_test_split(\n"
    "    X, y, test_size=0.2, stratify=y, random_state=42)\n"
    "</code></pre>"
    "<p>Stratifying keeps the same class proportions in train and test,"
    " which matters even more on imbalanced datasets.</p>"

    "<h3>Step 3 &mdash; Build a Pipeline</h3>"
    "<pre><code>"
    "from sklearn.pipeline import Pipeline\n"
    "from sklearn.preprocessing import StandardScaler\n"
    "from sklearn.linear_model import LogisticRegression\n"
    "\n"
    "pipe = Pipeline([\n"
    "    ('scaler', StandardScaler()),\n"
    "    ('clf', LogisticRegression(max_iter=1000, multi_class='auto')),\n"
    "])\n"
    "pipe.fit(X_train, y_train)\n"
    "</code></pre>"

    "<h3>Step 4 &mdash; Evaluate</h3>"
    "<pre><code>"
    "from sklearn.metrics import classification_report, confusion_matrix\n"
    "\n"
    "y_pred = pipe.predict(X_test)\n"
    "print(confusion_matrix(y_test, y_pred))\n"
    "print(classification_report(\n"
    "    y_test, y_pred, target_names=data.target_names))\n"
    "</code></pre>"
    "<p><strong>Expected console output (approximate):</strong></p>"
    "<pre><code>"
    "[[10  0  0]\n"
    " [ 0 10  0]\n"
    " [ 0  0 10]]\n"
    "\n"
    "              precision    recall  f1-score   support\n"
    "      setosa       1.00      1.00      1.00        10\n"
    "  versicolor       1.00      0.90      0.95        10\n"
    "   virginica       0.91      1.00      0.95        10\n"
    "\n"
    "    accuracy                           0.97        30\n"
    "</code></pre>"
    "<p>Iris is an easy dataset, so expect accuracy in the 0.93&ndash;1.00"
    " range. On Wine (<code>load_wine</code>) expect around"
    " 0.95&ndash;0.99.</p>"

    "<h3>Step 5 &mdash; Tune <code>C</code> with GridSearchCV</h3>"
    "<pre><code>"
    "from sklearn.model_selection import GridSearchCV\n"
    "\n"
    "param_grid = {'clf__C': [0.01, 0.1, 1.0, 10.0, 100.0]}\n"
    "grid = GridSearchCV(pipe, param_grid, cv=5, scoring='f1_macro')\n"
    "grid.fit(X_train, y_train)\n"
    "\n"
    "print('best C       :', grid.best_params_)\n"
    "print('CV f1_macro  :', round(grid.best_score_, 3))\n"
    "print('test accuracy:', round(grid.score(X_test, y_test), 3))\n"
    "</code></pre>"
    "<p>Note the double-underscore in <code>'clf__C'</code> &mdash; that is"
    " how a <code>Pipeline</code> addresses parameters of its inner steps.</p>"

    "<h3>Step 6 &mdash; Save with joblib and reload</h3>"
    "<pre><code>"
    "import joblib\n"
    "\n"
    "joblib.dump(grid.best_estimator_, 'iris_model.joblib')\n"
    "\n"
    "# Later, in a different script or web app...\n"
    "model = joblib.load('iris_model.joblib')\n"
    "\n"
    "new_sample = [[5.1, 3.5, 1.4, 0.2]]  # sepal/petal cm\n"
    "pred = model.predict(new_sample)[0]\n"
    "print('predicted class:', data.target_names[pred])\n"
    "</code></pre>"
    "<p>You now have a portable artefact you could deploy behind a Flask or"
    " FastAPI endpoint, exactly like the apps you build elsewhere in this"
    " qualification.</p>"

    "<h3>Reflection questions</h3>"
    "<ol>"
    "<li>Why did we wrap <code>StandardScaler</code> and"
    " <code>LogisticRegression</code> in a single <code>Pipeline</code>"
    " rather than calling <code>fit_transform</code> on the whole dataset"
    " before splitting? What kind of error would the latter introduce?</li>"
    "<li>The grid search optimised <code>f1_macro</code>. On a different"
    " business problem (for example detecting fraudulent transactions),"
    " which scoring metric would you choose instead, and why?</li>"
    "<li><strong>Bias reflection:</strong> Imagine the dataset were not"
    " botanical measurements but demographic data (age, postal code, income,"
    " employment status) used to decide who gets a loan. What additional"
    " checks, fairness metrics or governance steps would you add before"
    " trusting the model's predictions? Identify at least two specific"
    " risks (e.g. proxy variables for race, feedback loops) and how you"
    " would mitigate each.</li>"
    "</ol>"
)
