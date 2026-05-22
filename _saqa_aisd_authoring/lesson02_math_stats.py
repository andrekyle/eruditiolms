# -*- coding: utf-8 -*-
"""SAQA 118792 AI Software Developer - Lesson 02.

Covers SAQA modules:
  - KM-02 Introduction to Mathematics and Statistics (NQF4, 10 credits)
  - PM-01 Mathematics and Statistics for Programming (NQF4, 8 credits)
"""

LESSON_HTML = """
<h2>Mathematics and Statistics for AI</h2>

<p>Artificial Intelligence is, at its core, applied mathematics running on a
computer. Every model you will build &mdash; from a simple linear regression
to a deep neural network &mdash; is expressed in the language of
<strong>linear algebra</strong>, trained using <strong>calculus</strong>,
reasoned about using <strong>probability</strong>, and evaluated using
<strong>statistics</strong>. This lesson gives you the working vocabulary and
intuition you need before writing any ML code.</p>

<blockquote>
<p><em>You do not need to be a mathematician to build AI, but you do need to be
mathematically literate. If you cannot read the notation, you cannot read the
papers, the docs, or the error messages.</em></p>
</blockquote>

<h3>1. Linear Algebra &mdash; the language of data</h3>

<p>Data in AI is almost always represented as numbers arranged in rectangular
structures. Linear algebra is the toolkit for manipulating those structures
efficiently.</p>

<ul>
  <li><strong>Scalar</strong> &mdash; a single number, e.g. <code>3.14</code>.
      In ML this is often a learning rate, a loss value, or a single
      probability.</li>
  <li><strong>Vector</strong> &mdash; an ordered list of numbers, e.g.
      <code>[1.2, 0.7, -3.0]</code>. A single training example (one row of a
      dataset) is a vector. So is the set of weights for one neuron.</li>
  <li><strong>Matrix</strong> &mdash; a 2D grid of numbers. Your whole dataset
      is a matrix of shape <code>(n_samples, n_features)</code>. The weights
      of a fully-connected layer are a matrix.</li>
  <li><strong>Tensor</strong> &mdash; a generalisation to 3+ dimensions. An RGB
      image is a tensor of shape <code>(height, width, 3)</code>.</li>
</ul>

<h3>Key operations and why they matter</h3>

<table>
  <thead>
    <tr><th>Operation</th><th>What it does</th><th>Why ML cares</th></tr>
  </thead>
  <tbody>
    <tr><td>Dot product</td>
        <td>Multiply two vectors element-wise and sum the result.</td>
        <td>Measures similarity; computes the weighted sum inside every
            neuron.</td></tr>
    <tr><td>Matrix multiplication</td>
        <td>Combine two matrices into a new one following the row-by-column
            rule.</td>
        <td>One matrix multiplication runs an entire neural-network layer over
            a whole batch at once.</td></tr>
    <tr><td>Transpose</td>
        <td>Flip a matrix over its diagonal (rows become columns).</td>
        <td>Required to align shapes during backpropagation and in covariance
            matrices.</td></tr>
    <tr><td>Inverse</td>
        <td>The matrix that &ldquo;undoes&rdquo; another matrix.</td>
        <td>Appears in the closed-form solution of linear regression
            (<code>(X<sup>T</sup>X)<sup>-1</sup>X<sup>T</sup>y</code>).</td></tr>
    <tr><td>Eigenvalues / eigenvectors</td>
        <td>Directions that a matrix only stretches, never rotates.</td>
        <td>The foundation of PCA (dimensionality reduction) and of
            understanding how recurrent networks behave over time.</td></tr>
  </tbody>
</table>

<pre><code>import numpy as np

# A small dataset: 3 samples, 2 features
X = np.array([[1.0, 2.0],
              [3.0, 4.0],
              [5.0, 6.0]])
w = np.array([0.5, -0.25])      # weight vector
b = 0.1                          # bias scalar

# One matrix-vector multiplication computes predictions for ALL samples
y_pred = X @ w + b
print(y_pred)   # [0.1 0.6 1.1]
</code></pre>

<h3>2. Calculus &mdash; how models learn</h3>

<p>Training a model means searching for the parameters that make the
prediction error as small as possible. Calculus tells us which direction to
move the parameters in order to reduce error.</p>

<ul>
  <li><strong>Derivative</strong> &mdash; the slope of a function at a point.
      Tells you how much the output changes for a tiny change in the
      input.</li>
  <li><strong>Partial derivative</strong> &mdash; the derivative with respect
      to one variable while holding the others constant. Loss functions have
      thousands or millions of inputs (the weights), so we use partials.</li>
  <li><strong>Gradient</strong> &mdash; the vector of all partial derivatives.
      It points in the direction of steepest increase of the loss.</li>
  <li><strong>Chain rule</strong> &mdash; the rule for differentiating
      composed functions. Backpropagation is just the chain rule applied
      systematically through the layers of a network.</li>
</ul>

<p><strong>Gradient descent</strong> is the workhorse optimiser:
move every parameter a small step in the <em>opposite</em> direction of the
gradient, repeat until the loss stops decreasing.</p>

<pre><code>w  := w - learning_rate * gradient_of_loss_with_respect_to_w
</code></pre>

<h3>3. Probability &mdash; reasoning under uncertainty</h3>

<p>Real-world data is noisy. Probability lets us quantify how confident we are
in a prediction.</p>

<ul>
  <li><strong>Sample space</strong> (&Omega;) &mdash; the set of all possible
      outcomes of an experiment.</li>
  <li><strong>Event</strong> &mdash; any subset of the sample space.</li>
  <li><strong>Conditional probability</strong> &mdash;
      <code>P(A | B)</code> is the probability of A <em>given</em> that B has
      occurred.</li>
  <li><strong>Bayes&rsquo; theorem</strong> &mdash; lets us flip a conditional
      probability around:
      <code>P(A | B) = P(B | A) &middot; P(A) / P(B)</code>. This is the
      mathematical heart of spam filters, medical-test reasoning, and the
      naive-Bayes classifier.</li>
</ul>

<h3>Common distributions you must recognise</h3>

<table>
  <thead>
    <tr><th>Distribution</th><th>Models</th><th>Example in AI</th></tr>
  </thead>
  <tbody>
    <tr><td>Bernoulli</td><td>A single yes/no trial.</td>
        <td>Output of a binary classifier (spam vs. not spam).</td></tr>
    <tr><td>Binomial</td><td>Number of successes in <em>n</em> Bernoulli
        trials.</td><td>How many of 100 emails are spam.</td></tr>
    <tr><td>Normal (Gaussian)</td><td>Symmetric bell curve around a
        mean.</td><td>Initialisation of neural-network weights; modelling
        measurement noise.</td></tr>
    <tr><td>Poisson</td><td>Count of rare events in a fixed
        interval.</td><td>Number of requests per second hitting an API.</td></tr>
  </tbody>
</table>

<h3>4. Descriptive Statistics &mdash; summarising data</h3>

<ul>
  <li><strong>Mean</strong> &mdash; the arithmetic average.</li>
  <li><strong>Median</strong> &mdash; the middle value when sorted; robust to
      outliers.</li>
  <li><strong>Mode</strong> &mdash; the most frequent value.</li>
  <li><strong>Variance</strong> &mdash; the average squared distance from the
      mean.</li>
  <li><strong>Standard deviation</strong> &mdash; the square root of variance;
      same units as the data.</li>
  <li><strong>Percentiles &amp; IQR</strong> &mdash; the 25th, 50th and 75th
      percentiles split the data into quarters. The interquartile range
      (IQR = Q3 &minus; Q1) is a robust measure of spread used in box plots
      and outlier detection.</li>
</ul>

<pre><code>import statistics as st

scores = [52, 60, 67, 71, 71, 74, 80, 85, 91, 99]
print(st.mean(scores))      # 75.0
print(st.median(scores))    # 72.5
print(st.mode(scores))      # 71
print(st.pstdev(scores))    # ~13.86 (population std dev)
</code></pre>

<h3>5. Inferential Statistics &mdash; from sample to population</h3>

<p>We almost never have access to the whole population, only a
<strong>sample</strong>. Inferential statistics lets us make defensible
statements about the population from the sample.</p>

<ol>
  <li><strong>Sampling</strong> &mdash; the data must be representative;
      otherwise every conclusion is biased.</li>
  <li><strong>Hypothesis testing</strong> &mdash; you state a null hypothesis
      (H<sub>0</sub>: &ldquo;no effect&rdquo;) and an alternative
      (H<sub>1</sub>). You then compute a test statistic.</li>
  <li><strong>p-value</strong> &mdash; the probability of observing data at
      least as extreme as yours <em>if H<sub>0</sub> were true</em>. A small
      p-value (commonly &lt; 0.05) gives evidence to reject H<sub>0</sub>. A
      p-value is <em>not</em> the probability that H<sub>0</sub> is true.</li>
  <li><strong>Confidence interval</strong> &mdash; a range of plausible
      values for a population parameter. A 95% CI means that if we repeated
      the sampling many times, 95% of the constructed intervals would contain
      the true value.</li>
  <li><strong>Type I error</strong> &mdash; rejecting a true null
      (false alarm). <strong>Type II error</strong> &mdash; failing to reject
      a false null (missed detection).</li>
</ol>

<h3>6. Correlation vs. Causation</h3>

<p><strong>Correlation</strong> measures whether two variables move together
(Pearson&rsquo;s <em>r</em> ranges from &minus;1 to +1). <strong>Causation</strong>
means that changing one variable would actually change the other. Correlation
does <em>not</em> imply causation: ice-cream sales and drownings are
correlated, but both are driven by hot weather. Confusing the two is one of
the most common (and most damaging) mistakes a junior AI developer can
make.</p>

<h3>7. A taste of Information Theory &mdash; entropy</h3>

<p><strong>Entropy</strong> measures the average amount of &ldquo;surprise&rdquo;
in a probability distribution. A fair coin has 1 bit of entropy; a coin that
always lands heads has 0 bits. Entropy underpins decision-tree splits (the
ID3 / C4.5 algorithms), the cross-entropy loss used to train classifiers, and
the temperature setting of large language models.</p>

<p>For a discrete distribution with probabilities <code>p<sub>i</sub></code>:</p>

<pre><code>H = - sum( p_i * log2(p_i) )   for all i where p_i &gt; 0
</code></pre>

<h3>What to take away</h3>

<ul>
  <li>Linear algebra is the data structure of ML.</li>
  <li>Calculus is the engine that trains the model.</li>
  <li>Probability is how the model reasons about uncertainty.</li>
  <li>Statistics is how <em>you</em> reason about the model&rsquo;s results.</li>
</ul>
"""


QUESTIONS = [
    (
        "multiple_choice",
        "<p>You compute the dot product of two vectors of length 5. "
        "What is the shape of the result?</p>",
        [
            ("<p>A scalar (single number)</p>", True),
            ("<p>A vector of length 5</p>", False),
            ("<p>A 5&times;5 matrix</p>", False),
            ("<p>A vector of length 10</p>", False),
        ],
        "<p>The dot product multiplies the vectors element-wise and sums the "
        "results, producing a single scalar value.</p>",
    ),
    (
        "multiple_choice",
        "<p>A dataset matrix <code>X</code> has shape "
        "<code>(1000, 8)</code> and a weight vector <code>w</code> has shape "
        "<code>(8,)</code>. What is the shape of <code>X @ w</code>?</p>",
        [
            ("<p><code>(1000,)</code> &mdash; one prediction per sample</p>", True),
            ("<p><code>(8,)</code> &mdash; one value per feature</p>", False),
            ("<p><code>(1000, 8)</code> &mdash; same as X</p>", False),
            ("<p>The multiplication is undefined</p>", False),
        ],
        "<p>Matrix-vector multiplication of shape <code>(n, k)</code> with "
        "<code>(k,)</code> yields shape <code>(n,)</code>: one scalar prediction "
        "per sample, which is exactly what a linear model produces in a single "
        "vectorised step.</p>",
    ),
    (
        "multiple_choice",
        "<p>During gradient descent, why do we move parameters in the "
        "<em>opposite</em> direction of the gradient of the loss?</p>",
        [
            ("<p>Because the gradient points in the direction of steepest "
             "<strong>increase</strong>, so the negative gradient points toward "
             "lower loss.</p>", True),
            ("<p>Because the gradient is always negative for a valid loss "
             "function.</p>", False),
            ("<p>Because the chain rule reverses the sign of every "
             "derivative.</p>", False),
            ("<p>Because moving along the gradient would violate the learning "
             "rate constraint.</p>", False),
        ],
        "<p>The gradient is the direction of fastest ascent of a function. To "
        "<em>minimise</em> the loss we therefore take a step in the negative "
        "gradient direction, scaled by the learning rate.</p>",
    ),
    (
        "multiple_choice",
        "<p>A medical test for a rare disease has 99% sensitivity and 99% "
        "specificity. The disease affects 1 in 10 000 people. A random person "
        "tests positive. Roughly what is the probability they actually have "
        "the disease?</p>",
        [
            ("<p>About 1% &mdash; because the disease is so rare, most "
             "positives are false positives (Bayes' theorem).</p>", True),
            ("<p>About 99% &mdash; equal to the sensitivity of the test.</p>", False),
            ("<p>Exactly 50% &mdash; the test is either right or wrong.</p>", False),
            ("<p>About 99.99% &mdash; matches the rarity of the disease.</p>", False),
        ],
        "<p>Apply Bayes&rsquo; theorem. Out of 1 000 000 people, ~100 have the "
        "disease and ~99 test positive; ~999 900 are healthy and ~9 999 still "
        "test positive. So P(disease | positive) &asymp; 99 / (99 + 9 999) "
        "&asymp; 1%. This is the classic <em>base-rate fallacy</em>.</p>",
    ),
    (
        "multiple_choice",
        "<p>You are summarising household incomes in a suburb where a few "
        "billionaires live. Which measure of central tendency is the most "
        "informative for a &lsquo;typical&rsquo; household?</p>",
        [
            ("<p>The median, because it is robust to extreme outliers.</p>", True),
            ("<p>The mean, because it uses every data point.</p>", False),
            ("<p>The mode, because incomes are usually discrete.</p>", False),
            ("<p>The variance, because it measures spread.</p>", False),
        ],
        "<p>A small number of very large values pulls the mean far above what "
        "most households actually earn. The median &mdash; the middle value &mdash; "
        "is unaffected by such outliers and better represents a typical "
        "household.</p>",
    ),
    (
        "multiple_choice",
        "<p>A study reports <em>p</em> = 0.03 when comparing two teaching "
        "methods. Which interpretation is correct?</p>",
        [
            ("<p>If there were really no difference between the methods, there "
             "is a 3% chance of seeing data at least as extreme as ours.</p>", True),
            ("<p>There is a 97% chance the new method is better.</p>", False),
            ("<p>There is a 3% chance the null hypothesis is true.</p>", False),
            ("<p>The effect size is 3% of the original mean.</p>", False),
        ],
        "<p>The p-value is the probability of the observed data (or more "
        "extreme) <em>assuming the null hypothesis is true</em>. It is not the "
        "probability that the null is true, nor the probability that the "
        "alternative is true.</p>",
    ),
    (
        "true_false",
        "<p>A strong positive Pearson correlation between two variables proves "
        "that one variable causes the other.</p>",
        [
            ("<p>True</p>", False),
            ("<p>False</p>", True),
        ],
        "<p>Correlation measures only that two variables move together. A "
        "causal relationship requires additional evidence &mdash; typically a "
        "controlled experiment or careful causal inference &mdash; because the "
        "relationship could be driven by a confounding variable or pure "
        "coincidence.</p>",
    ),
    (
        "true_false",
        "<p>The entropy of a fair coin (<code>P(H) = P(T) = 0.5</code>) is "
        "exactly 1 bit, and the entropy of a coin that always lands heads is "
        "0 bits.</p>",
        [
            ("<p>True</p>", True),
            ("<p>False</p>", False),
        ],
        "<p>Entropy <code>H = -&sum; p<sub>i</sub> log<sub>2</sub> p<sub>i</sub></code>. "
        "For a fair coin: <code>-(0.5 log<sub>2</sub> 0.5 + 0.5 log<sub>2</sub> 0.5) "
        "= 1</code>. For a deterministic coin: <code>-(1 &middot; log<sub>2</sub> 1) "
        "= 0</code> &mdash; there is no uncertainty, hence no surprise.</p>",
    ),
]


PRACTICAL_HTML = """
<h2>Practical Lab \u2014 Statistics on a Real Dataset</h2>

<p>In this lab you will use Python's scientific stack &mdash;
<code>numpy</code>, <code>pandas</code>, <code>matplotlib</code> and
<code>scipy.stats</code> &mdash; to explore a small but realistic dataset of
learner test scores for two South African schools. You will compute
descriptive statistics, visualise the distribution, and run a hypothesis test
to decide whether one school's average is significantly higher than the
other's.</p>

<h3>Before you start</h3>

<ol>
  <li>Make sure you have Python 3.10+ installed.</li>
  <li>Install the required libraries:
      <pre><code>pip install numpy pandas matplotlib scipy</code></pre></li>
  <li>Create a working folder, e.g. <code>lesson02_lab/</code>, and open it
      in VS Code.</li>
</ol>

<h3>Step 1 &mdash; Create the dataset</h3>

<p>Create a file called <code>scores.csv</code> with the following content
(you can paste it directly):</p>

<pre><code>school,score
Alpha,58
Alpha,62
Alpha,67
Alpha,71
Alpha,73
Alpha,74
Alpha,78
Alpha,81
Alpha,85
Alpha,90
Beta,49
Beta,55
Beta,58
Beta,60
Beta,63
Beta,66
Beta,68
Beta,70
Beta,72
Beta,77
</code></pre>

<h3>Step 2 &mdash; Load the data with pandas</h3>

<pre><code>import pandas as pd

df = pd.read_csv("scores.csv")
print(df.head())
print("Shape:", df.shape)
</code></pre>

<p><strong>Expected output (first lines):</strong></p>

<pre><code>  school  score
0  Alpha     58
1  Alpha     62
2  Alpha     67
3  Alpha     71
4  Alpha     73
Shape: (20, 2)
</code></pre>

<h3>Step 3 &mdash; Compute descriptive statistics per school</h3>

<pre><code>summary = df.groupby("school")["score"].describe()
print(summary)
</code></pre>

<p><strong>Expected output (rounded):</strong></p>

<pre><code>        count   mean        std   min    25%   50%    75%   max
school
Alpha    10.0  73.90   9.92...  58.0  68.0  73.5  80.25  90.0
Beta     10.0  63.80   8.55...  49.0  58.5  64.5  69.50  77.0
</code></pre>

<p>Notice the mean, standard deviation, and the 25th / 50th (median) / 75th
percentiles. The difference in means is about <strong>10 points</strong>, but
is that difference <em>real</em> or could it be due to random variation in
who happened to be sampled? That is the question a hypothesis test answers.</p>

<h3>Step 4 &mdash; Visualise with a histogram</h3>

<pre><code>import matplotlib.pyplot as plt

alpha = df.loc[df["school"] == "Alpha", "score"]
beta  = df.loc[df["school"] == "Beta",  "score"]

plt.hist(alpha, bins=6, alpha=0.6, label="Alpha")
plt.hist(beta,  bins=6, alpha=0.6, label="Beta")
plt.xlabel("Score")
plt.ylabel("Number of learners")
plt.title("Score distribution by school")
plt.legend()
plt.savefig("scores_hist.png", dpi=120)
plt.show()
</code></pre>

<p>Open <code>scores_hist.png</code>. You should see two overlapping
distributions, with Alpha shifted noticeably to the right.</p>

<h3>Step 5 &mdash; Run an independent two-sample t-test</h3>

<p>We want to test:</p>

<ul>
  <li><strong>H<sub>0</sub></strong>: the two schools have the same mean
      score.</li>
  <li><strong>H<sub>1</sub></strong>: the means are different.</li>
</ul>

<pre><code>from scipy import stats

t_stat, p_value = stats.ttest_ind(alpha, beta, equal_var=False)
print("t statistic:", round(t_stat, 3))
print("p value    :", round(p_value, 4))
</code></pre>

<p><strong>Expected output (approximate):</strong></p>

<pre><code>t statistic: 2.44
p value    : 0.0258
</code></pre>

<h3>Step 6 &mdash; Interpret the p-value</h3>

<p>Using the conventional threshold of &alpha; = 0.05:</p>

<ul>
  <li>p &asymp; 0.026 is less than 0.05, so we <strong>reject H<sub>0</sub></strong>.</li>
  <li>We conclude there is statistically significant evidence that the two
      schools have different mean scores in this sample.</li>
  <li>This does <em>not</em> tell us <em>why</em> the difference exists, nor
      whether it would generalise to other schools, and it does <em>not</em>
      say the probability that H<sub>0</sub> is true.</li>
</ul>

<h3>Step 7 &mdash; Build a 95% confidence interval for the difference</h3>

<pre><code>import numpy as np

diff = alpha.mean() - beta.mean()
se   = np.sqrt(alpha.var(ddof=1)/len(alpha) + beta.var(ddof=1)/len(beta))
ci_low  = diff - 1.96 * se
ci_high = diff + 1.96 * se
print("Mean difference:", round(diff, 2))
print("95% CI:", (round(ci_low, 2), round(ci_high, 2)))
</code></pre>

<p>The interval should be roughly <code>(1.4, 18.8)</code>. Because zero is
<em>not</em> inside the interval, this is consistent with the t-test
rejecting the null.</p>

<h3>Reflection questions</h3>

<ol>
  <li>If we had only 3 learners per school instead of 10, would you expect
      the p-value to be smaller or larger? Why?</li>
  <li>What is the difference between &ldquo;statistically significant&rdquo;
      and &ldquo;practically important&rdquo;? Give an example where the two
      disagree.</li>
  <li>The sample contains 20 learners total. List two threats to the
      validity of generalising the conclusion to all learners in South
      Africa.</li>
  <li>Suppose a colleague says: &ldquo;The p-value of 0.026 means there is a
      97.4% chance that Alpha is genuinely better.&rdquo; Explain in one
      paragraph why this interpretation is incorrect.</li>
  <li>Re-run Step 5 after swapping two scores between the schools. How
      sensitive is the p-value to a small change in the data?</li>
</ol>

<h3>Submission</h3>

<p>Save your script as <code>lab02_stats.py</code> and submit it together
with the generated <code>scores_hist.png</code> and a short
<code>reflection.md</code> answering the five questions above.</p>
"""
