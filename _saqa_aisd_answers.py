# -*- coding: utf-8 -*-
"""Model answers (memorandum) for the practical labs of:

    SAQA 118792 — Occupational Certificate: Artificial Intelligence
    Software Developer

The :data:`LAB_ANSWERS` dict is keyed by 1-based lesson order and contains
ready-to-render HTML. Rendered by the teacher/admin-only route
``/teacher/lab-answers`` in :mod:`app`.

Authoring guidelines:
    * Use the same headings and prose style as the lesson content so the
      page looks native — ``<h3>`` for section breaks, ``<pre><code>`` for
      code, ``<ul>``/``<ol>`` for lists.
    * Never use dark-blue text. Use the lesson-content default colours.
"""

# Short, human-friendly lab titles. Keyed by 1-based lab number.
LAB_TITLES = {
    1:  "Lab 1 — Map an AI Application (PEAS, data, ethics)",
    2:  "Lab 2 — Descriptive Statistics and Hypothesis Testing",
    3:  "Lab 3 — Frame an AI Problem and Draft an SDD",
    4:  "Lab 4 — Clean and Analyse Sales Data with a Spreadsheet",
    5:  "Lab 5 — Empirical Algorithm Complexity",
    6:  "Lab 6 — SQL, Python and Web Scraping",
    7:  "Lab 7 — Choose the Right Machine-Learning Approach",
    8:  "Lab 8 — End-to-End Classifier with scikit-learn",
    9:  "Lab 9 — Train a Neural Network on MNIST in Keras",
    10: "Lab 10 — Design-Thinking Sprint for a Responsible AI Solution",
}

# Substring (case-insensitive) used to match the corresponding lesson row in the
# database, so the page can deep-link to the student-facing lesson page when it
# exists. Source lesson titles end in " — Practical Lab".
LAB_LESSON_HINTS = {
    1:  "Overview of Artificial Intelligence",
    2:  "Mathematics and Statistics",
    3:  "Analytical Thinking",
    4:  "Data, Databases",
    5:  "Computing Theory",
    6:  "SQL, Python and Data Scraping",
    7:  "AI, Machine Learning and Deep Learning Fundamentals",
    8:  "Machine Learning with Python",
    9:  "Deep Learning",
    10: "Governance, Ethics",
}

LAB_ANSWERS = {}

# ---------------------------------------------------------------------------
# Lesson 1 — Map an AI Application
# ---------------------------------------------------------------------------
LAB_ANSWERS[1] = """
<p><em>Worked example using Scenario 1 — Crop-yield prediction for
smallholder maize farmers in the Free State. Use it as a template; your own
submission must be in your own words and may use any of the four
scenarios.</em></p>

<h3>1. Problem statement</h3>
<p>Smallholder maize farmers in the Free State (≈ 200 000 households)
struggle to plan planting, fertiliser purchases and storage because yields
swing wildly with rainfall and pest outbreaks. A low yield often means a
family cannot repay input loans and faces food insecurity.
<strong>Success</strong> = giving each farmer, 6–8 weeks before harvest, a
yield forecast (t/ha) with ≤ 15 % error, delivered by SMS in
Sesotho / Afrikaans / English, so they can pre-sell, adjust top-dressing,
or apply for relief in time.</p>

<h3>2. AI branch</h3>
<p>Primary branch: <strong>Machine Learning (supervised regression)</strong>
combined with <strong>Computer Vision</strong> to interpret Sentinel-2
satellite tiles (NDVI / EVI vegetation indices). A small expert-rule layer
flags drought-stress thresholds. NLP is not required — outputs are numeric
and templated.</p>
<p><em>Justification:</em> the relationship between weather, vegetation
indices and soil class is non-linear and data-rich but lacks a closed-form
physical model — exactly where gradient-boosted trees or a CNN on
image tiles out-perform hand-coded rules.</p>

<h3>3. PEAS specification</h3>
<pre><code>P (Performance):  MAPE of yield forecast ≤ 15 %;
                  ≥ 90 % of SMSes delivered ≥ 6 weeks before harvest;
                  farmer satisfaction ≥ 4 / 5.
E (Environment):  Smallholder maize fields 0.5–10 ha, Free State,
                  growing season Oct–May, rainfall 400–700 mm,
                  intermittent 2G/3G, low-literacy users.
A (Actuators):    SMS gateway (Clickatell) with forecast + advisory;
                  dashboard for extension officers; CSV for Land Bank.
S (Sensors):      Sentinel-2 multispectral tiles (10 m, 5-day revisit);
                  SAWS daily rainfall &amp; temperature;
                  SoilGrids soil class; farmer USSD inputs
                  (planting date, cultivar); Grain SA yield history.</code></pre>

<h3>4. Data requirements</h3>
<table>
<thead><tr><th>Dataset</th><th>Source</th><th>Volume</th><th>Format</th><th>POPIA?</th></tr></thead>
<tbody>
<tr><td>Sentinel-2 imagery</td><td>ESA Copernicus Open Hub</td><td>~50 GB / season</td><td>GeoTIFF</td><td>No</td></tr>
<tr><td>Rainfall &amp; temperature</td><td>SAWS / CHIRPS</td><td>~100 MB / yr</td><td>CSV / NetCDF</td><td>No</td></tr>
<tr><td>Soil class &amp; pH</td><td>ISRIC SoilGrids 250 m</td><td>~2 GB</td><td>GeoTIFF</td><td>No</td></tr>
<tr><td>Historical yields</td><td>Grain SA + DALRRD</td><td>~20 000 rows</td><td>CSV</td><td><strong>Yes</strong> — farmer ID, GPS</td></tr>
<tr><td>USSD farmer registration</td><td>Own collection</td><td>grows weekly</td><td>JSON / Postgres</td><td><strong>Yes</strong> — name, cell, coords</td></tr>
</tbody></table>
<p>POPIA actions: lawful-processing notice on USSD opt-in, hashed IDs,
encrypted PII schema, Data Sharing Agreement with Grain SA, appointed
Information Officer, retain for the contracted season + 7 years (tax).</p>

<h3>5. Symbolic vs sub-symbolic</h3>
<p><strong>Hybrid, dominated by sub-symbolic.</strong> The yield model
(gradient boosting / CNN) is sub-symbolic — it learns weights from
examples. A thin symbolic layer encodes hard agronomic rules
(<em>e.g. if cumulative rainfall &lt; 250 mm by the V8 growth stage, cap
the forecast and raise a drought flag</em>) so domain knowledge is
preserved and extension officers can audit edge cases.</p>

<h3>6. Ethical considerations</h3>
<ol>
<li><strong>Bias</strong> — training data over-represents commercial
farms; the model may under-predict tiny irregular plots, costing
smallholders loan eligibility. Mitigation: stratified sampling, fairness
audit by farm size and district.</li>
<li><strong>Privacy / POPIA</strong> — combining GPS + cellphone + yield
creates a re-identifiable financial profile. Mitigation: hashing,
role-based access, minimum-necessary sharing with the Land Bank.</li>
<li><strong>Accountability</strong> — if a farmer over-orders fertiliser
on a wrong forecast and falls into debt, written limitation-of-liability,
versioned forecast logs and a human extension-officer override are
required.</li>
<li><strong>Inclusion</strong> — over-reliance on SMS excludes farmers
without phones and women whose husbands “own” the handset. Mitigation:
community-radio bulletins and printed pamphlets at co-ops.</li>
<li><strong>Environmental honesty</strong> — must not tune the model to
encourage over-fertilising. Performance measure stays
<em>accuracy</em>, not <em>yield maximisation</em>.</li>
</ol>

<h3>7. Block diagram</h3>
<pre><code>Sentinel-2  ┐
SAWS weather├─► Pre-processing ─► ML model ─► Rule layer ─► Forecast
SoilGrids   │   (NDVI, cloud)    (GBT+CNN)    (agronomic   │
USSD inputs ┘                                  thresholds) │
                                                           ├─► SMS to farmer
                                                           ├─► Officer dashboard
                                                           └─► Land Bank CSV</code></pre>

<h3>8. Reflection answers (model)</h3>
<ol>
<li><strong>Hardest PEAS row:</strong> <em>Performance measure</em>.
“Accurate yield” sounds obvious, but we had to balance statistical
accuracy (MAPE), timeliness (≥ 6 weeks lead time) and human trust
(satisfaction score) — three units that can fight each other.</li>
<li><strong>Accountability:</strong> primary responsibility sits with
the <strong>deploying organisation</strong>, which chooses the threshold
at which a forecast becomes a loan decision. The developer is
secondarily liable for negligent engineering. The farmer is liable only
if they ignored a clearly communicated uncertainty range.</li>
<li><strong>Plain-language Sesotho explanation:</strong>
<em>“Sesebediswa sena se sheba dinepe tsa satellite le pula ya beke le
beke, mme se hakanya hore poone ya hao e tla fana ka thekiso e kae pele
o e kotula. Ke thuso feela — e ka fosa, kahoo o lokela ho dula o etsa
qeto ya hao mmoho le motsamaisi wa hao wa temo.”</em></li>
</ol>
"""

# ---------------------------------------------------------------------------
# Lesson 2 — Statistics on a Real Dataset
# ---------------------------------------------------------------------------
LAB_ANSWERS[2] = """
<h3>Full <code>lab02_stats.py</code></h3>
<pre><code>import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Step 2 — load
df = pd.read_csv("scores.csv")
print(df.head())
print("Shape:", df.shape)

# Step 3 — descriptive stats per school
print(df.groupby("school")["score"].describe())

# Step 4 — histogram
alpha = df.loc[df["school"] == "Alpha", "score"]
beta  = df.loc[df["school"] == "Beta",  "score"]
plt.hist(alpha, bins=6, alpha=0.6, label="Alpha")
plt.hist(beta,  bins=6, alpha=0.6, label="Beta")
plt.xlabel("Score"); plt.ylabel("Learners"); plt.legend()
plt.title("Score distribution by school")
plt.savefig("scores_hist.png", dpi=120)

# Step 5 — Welch's t-test
t_stat, p_value = stats.ttest_ind(alpha, beta, equal_var=False)
print(f"t = {t_stat:.3f}   p = {p_value:.4f}")

# Step 7 — 95 % CI for the difference of means
diff = alpha.mean() - beta.mean()
se   = np.sqrt(alpha.var(ddof=1)/len(alpha) + beta.var(ddof=1)/len(beta))
print(f"Δ mean = {diff:.2f}   95 % CI = ({diff-1.96*se:.2f}, {diff+1.96*se:.2f})")
</code></pre>

<h3>Expected console output</h3>
<pre><code>Shape: (20, 2)
            count  mean   std   min   25%   50%    75%   max
school
Alpha        10.0 73.90  9.92 58.00 68.00 73.50 80.25 90.00
Beta         10.0 63.80  8.55 49.00 58.50 64.50 69.50 77.00
t = 2.443   p = 0.0258
Δ mean = 10.10   95 % CI = (1.39, 18.81)</code></pre>

<h3>Reflection answers</h3>
<ol>
<li><strong>Smaller sample (n = 3 per school)</strong> would <em>raise</em>
the p-value. The standard error is √(s²/n); shrinking n inflates the SE,
shrinks the t-statistic and makes the same 10-point gap easier to dismiss
as noise.</li>
<li><strong>Statistical vs practical:</strong> with 10 000 learners per
school a 0.3-point difference can be statistically significant
(p &lt; 0.001) yet meaningless to a teacher. Conversely, a 12-point
difference in a class of 4 may be practically huge but not significant.
Always report effect size + CI alongside the p-value.</li>
<li>Two threats: (a) <em>selection bias</em> — Alpha may stream stronger
learners; (b) <em>small, non-representative sample</em> — 10 learners
cannot speak for an entire schooling system. We can only generalise to
the population the sample was drawn from.</li>
<li>The colleague has fallen for the <strong>inverse-probability
fallacy</strong>. The p-value is P(data | H₀), not P(H₀ | data). It says
“if the schools were truly equal, only 2.6 % of repeated samples would
show a gap this big or bigger”. It does not say there is a 97.4 % chance
that Alpha is better — that would require a Bayesian prior we never
specified.</li>
<li>Swapping the lowest Alpha score with the highest Beta score moves
the p-value above 0.05 (typically ≈ 0.09). Small datasets are very
sensitive to individual points — another reason to report CIs and to
collect more data before acting.</li>
</ol>
"""

# ---------------------------------------------------------------------------
# Lesson 3 — Frame an AI Problem and Draft an SDD
# ---------------------------------------------------------------------------
LAB_ANSWERS[3] = """
<p><em>Worked memorandum using the <strong>Clinic no-shows</strong>
scenario.</em></p>

<h3>1. Problem in one sentence</h3>
<p>Twenty-five percent of booked antenatal appointments at the clinic are
missed, wasting nurse time and delaying care.</p>

<h3>2. 5W1H</h3>
<pre><code>Who:    Pregnant women booked at the antenatal clinic.
What:   Patient does not arrive for a confirmed slot.
Where:  Community clinic, Soweto.
When:   Slots Mon–Fri 08:00–15:00; misses cluster on Mondays.
Why:    Transport cost, childcare, forgotten dates, queue fatigue.
How measured today: nurses tick a paper register at end of day.</code></pre>

<h3>3. 5-Whys (root cause)</h3>
<ol>
<li>Why miss? — patient forgot / could not travel.</li>
<li>Why? — no reminder &amp; transport was unaffordable.</li>
<li>Why? — clinic has no SMS reminder system and no transport voucher.</li>
<li>Why? — IT budget was prioritised for stock control.</li>
<li>Why? — leadership lacked a costed business case.</li>
</ol>
<p>AI can address <em>part</em> of the symptom (reminders, risk
prediction) but transport affordability is structural and outside the
model’s reach — declared honestly in the SDD.</p>

<h3>4. Decomposition (four pillars)</h3>
<ul>
<li><strong>Decompose:</strong> (a) predict no-show risk per booking,
(b) trigger SMS reminder 24 h ahead, (c) over-book high-risk slots
intelligently.</li>
<li><strong>Pattern recognition:</strong> identical to airline overbooking
and dental-practice reminder systems.</li>
<li><strong>Abstraction:</strong> ignore exact diagnosis; keep only
appointment metadata + distance + prior attendance.</li>
<li><strong>Algorithm:</strong> 1. nightly export of next-day bookings →
2. score with model → 3. send template SMS in patient’s language →
4. flag top-risk for nurse call → 5. log outcome → 6. retrain monthly.</li>
</ul>

<h3>5. Target variable</h3>
<p><code>missed_appointment (yes/no)</code>, one row per booking.</p>

<h3>6. Metrics</h3>
<p><strong>Primary:</strong> Recall on the “missed” class ≥ 0.70.<br>
<strong>Guardrail:</strong> No more than 5 % of patients receive
&gt; 2 SMS reminders / week (to avoid notification fatigue).</p>

<h3>7. Data &amp; POPIA basis</h3>
<table>
<thead><tr><th>Source</th><th>Status</th><th>POPIA basis</th></tr></thead>
<tbody>
<tr><td>Clinic appointment system (12 months)</td><td>Available</td><td>Legitimate interest — health service delivery</td></tr>
<tr><td>Patient cellphone numbers</td><td>Available</td><td>Consent at registration</td></tr>
<tr><td>Distance to clinic</td><td>Derived from suburb only</td><td>Public data (no GPS)</td></tr>
<tr><td>Weather forecast</td><td>Missing — SAWS API</td><td>Public</td></tr>
<tr><td>Public-transport disruptions</td><td>Missing — manual log</td><td>n/a</td></tr>
</tbody></table>

<h3>8. Decision matrix</h3>
<table>
<thead><tr><th>Approach</th><th>Cost</th><th>Time</th><th>Accuracy</th><th>Explainability</th><th>Fairness</th></tr></thead>
<tbody>
<tr><td>Logistic regression</td><td>Low</td><td>2 weeks</td><td>★★★</td><td>★★★★★</td><td>★★★★</td></tr>
<tr><td>Gradient boosting</td><td>Low</td><td>3 weeks</td><td>★★★★</td><td>★★★</td><td>★★★</td></tr>
<tr><td>Rule-based reminder (no ML)</td><td>Very low</td><td>1 week</td><td>★★</td><td>★★★★★</td><td>★★★★★</td></tr>
</tbody></table>
<p><strong>Pick:</strong> logistic regression — best balance of
explainability (a nurse can read the top coefficients) and accuracy on a
small dataset.</p>

<h3>9. Top three risks</h3>
<ol>
<li><strong>Class imbalance</strong> (only 25 % positives) → use
<code>class_weight='balanced'</code> and report recall, not accuracy.</li>
<li><strong>Bias against patients without cellphones</strong> → keep a
manual call-back queue for that cohort.</li>
<li><strong>POPIA breach</strong> from SMS errors → strict template
language, no medical detail in the SMS body.</li>
</ol>

<h3>10. One-page SDD (sample)</h3>
<pre><code>1. Problem .......... 25 % antenatal no-shows
2. Stakeholders ..... patients, nurses, clinic manager
3. Target + metric .. missed=yes; recall ≥ 0.70
4. Data ............. 12 mo bookings + SMS log + weather
5. Constraints ...... R0 SMS budget via gov gateway
6. Risks ............ imbalance, exclusion, POPIA
7. Approach ......... logistic regression + reminder bot
8. Go/no-go ......... 8-week pilot, review against recall</code></pre>

<h3>Reflection answers</h3>
<ol>
<li><strong>Abstraction</strong> was hardest — letting go of
clinically interesting fields (diagnosis, blood pressure) to keep the
data set lawful and small.</li>
<li>Confirmation bias creeps in at the <em>evaluation</em> step if we
only test on the same Mondays the model was trained on. Prevent it by
holding out the final 4 weeks chronologically.</li>
<li>For the transport root cause we wrote: <em>“Out of scope for the AI
model; flagged to clinic management as a parallel intervention.”</em></li>
<li>If a false positive (sending an unnecessary reminder) cost 10 × a
false negative, we would switch the primary metric from recall to
<strong>precision</strong> and tune the threshold upward, accepting more
missed appointments to avoid notification fatigue.</li>
</ol>
"""

# ---------------------------------------------------------------------------
# Lesson 4 — Analyse Sales Data with a Spreadsheet
# ---------------------------------------------------------------------------
LAB_ANSWERS[4] = """
<h3>Cleaned data (after Steps 1–2)</h3>
<p>After <code>=TRIM(A2)</code>, <em>Remove Duplicates</em>, currency
formatting and data validation you should have 15 rows (the duplicate
Gauteng/Jan was removed and the rogue spaces in <em>“ Gauteng ”</em>
collapsed to <em>“Gauteng”</em>).</p>

<h3>Pivot table values (Step 3)</h3>
<pre><code>province_clean    Jan       Feb       Grand total
Eastern Cape    R 78 400   R 81 200   R 159 600
Free State            -    R 45 600   R  45 600
Gauteng        R 182 340  R 201 500   R 383 840
KwaZulu-Natal  R 121 050  R 133 900   R 254 950
Limpopo        R  52 800  R  58 100   R 110 900
Mpumalanga     R  61 400  R  64 900   R 126 300
North West     R  49 200         -    R  49 200
Northern Cape         -    R 28 700   R  28 700
Western Cape   R 154 200  R 167 800   R 322 000
Grand total    R 699 390  R 781 700  R 1 481 090</code></pre>

<h3>Three insights (Step 7)</h3>
<ol>
<li><strong>Gauteng dominates</strong> (≈ 26 % of national sales in
both months). Any logistics disruption there is a national risk.</li>
<li><strong>Every province grew Jan → Feb</strong> (national total
+11.8 %). Investigate the seasonal / promotional driver.</li>
<li><strong>Northern Cape and Free State under-trade</strong> (each
&lt; R 50 000/month). Decide: invest in marketing or accept the gap.</li>
</ol>

<h3>Reflection answers</h3>
<ol>
<li>Step 2 improved <strong>accuracy</strong> (removed a duplicated
sale), <strong>consistency</strong> (trimmed whitespace) and
<strong>validity</strong> (constrained month values). Measure by:
duplicate count → 0, unique provinces → 9, % invalid months → 0.</li>
<li>A clustered bar chart preserves <em>both</em> dimensions
(province × month) and lets the eye compare months <em>within</em> a
province as well as provinces against each other. A pie chart can only
show one dimension and collapses to ~9 slices that are visually hard to
rank.</li>
<li>The <strong>Data Validation</strong> list on the province column
(populated from a master list <code>provinces</code>) would reject
<em>“Kwazulu Natal”</em> at entry. As a back-stop, a
<code>=COUNTIF(masterlist, A2)=0</code> conditional-formatting rule
highlights any province not in the master list.</li>
<li>For a single-province store manager: filter the pivot to that
province by default; show a single KPI tile (this month vs last month),
a 12-month trend line, and the top-5 SKUs. Hide the national totals
entirely.</li>
</ol>
"""

# ---------------------------------------------------------------------------
# Lesson 5 — Empirical algorithm complexity
# ---------------------------------------------------------------------------
LAB_ANSWERS[5] = """
<h3>Expected <code>bench.py</code> output (typical laptop, varies ±50 %)</h3>
<pre><code>1000     linear 4.7e-05   binary 1.9e-06   hash 1.8e-07
10000    linear 4.5e-04   binary 2.7e-06   hash 1.8e-07
100000   linear 4.6e-03   binary 3.7e-06   hash 1.8e-07
1000000  linear 4.7e-02   binary 4.8e-06   hash 1.8e-07</code></pre>

<h3>Empirical exponents (Step 4)</h3>
<pre><code># Between n = 10³ and n = 10⁶
linear: k = log(4.7e-2 / 4.7e-5) / log(10⁶ / 10³)   ≈  1.00   → O(n)
binary: k = log(4.8e-6 / 1.9e-6) / log(10⁶ / 10³)   ≈  0.13   → O(log n)
hash  : k ≈ 0                                                  → O(1)</code></pre>

<h3>How the plot should look</h3>
<p>On log-log axes: linear search is a straight line of slope ≈ 1; binary
search is almost flat (slope ≈ 0.13, consistent with log growth on a
log-x axis); hash lookup is a flat horizontal line near 2 × 10⁻⁷ s.</p>

<h3>Reflection answers</h3>
<ol>
<li><strong>Binary search needs a sorted list</strong> because at every
step it discards half the search space based on order. Sorting costs
O(n log n) once, then each search is O(log n). If you search only
<em>once</em>, the total cost is O(n log n + log n) ≈ O(n log n), which
is <em>worse</em> than a single linear scan O(n). Binary search wins
only when the cost of the initial sort can be amortised over many
queries.</li>
<li>Hash-set lookup is <strong>amortised O(1)</strong> because the hash
function jumps straight to the bucket. It degrades to O(n) when the
hash function distributes poorly and every key lands in the same bucket
(adversarial keys, or a bad custom <code>__hash__</code>) — the bucket
becomes a linked list that must be scanned linearly.</li>
<li><strong>Average-case linear search</strong> on a random target is
O(n/2), so the curve halves in absolute value but keeps the same slope
of 1 on the log-log plot. The asymptotic class is unchanged.</li>
<li>For a 50 000-token vocabulary, choose a <strong>hash-based
structure</strong> (Python <code>dict</code> or <code>set</code>):
constant-time lookup, no pre-sort, and tokenisation must run millions
of times per training batch. Binary search would force the vocab to be
sorted and every lookup to be O(log n) ≈ 16 comparisons — slower for no
benefit.</li>
</ol>
"""

# ---------------------------------------------------------------------------
# Lesson 6 — Scrape + SQLite + CSV
# ---------------------------------------------------------------------------
LAB_ANSWERS[6] = """
<h3>Full <code>lab_scrape.py</code></h3>
<pre><code>import csv
import sqlite3
from bs4 import BeautifulSoup

SAMPLE_HTML = """ + '"""' + """
&lt;html&gt;&lt;body&gt;
  &lt;div class="job-card"&gt;
    &lt;h3&gt;Junior Python Developer&lt;/h3&gt;
    &lt;span class="company"&gt;Acme Data&lt;/span&gt;
    &lt;span class="location"&gt;Cape Town&lt;/span&gt;
    &lt;time datetime="2026-05-20"&gt;20 May&lt;/time&gt;
  &lt;/div&gt;
  &lt;div class="job-card"&gt;
    &lt;h3&gt;Data Engineer&lt;/h3&gt;
    &lt;span class="company"&gt;Beta Insights&lt;/span&gt;
    &lt;span class="location"&gt;Johannesburg&lt;/span&gt;
    &lt;time datetime="2026-05-22"&gt;22 May&lt;/time&gt;
  &lt;/div&gt;
  &lt;div class="job-card"&gt;
    &lt;h3&gt;ML Intern&lt;/h3&gt;
    &lt;span class="company"&gt;Acme Data&lt;/span&gt;
    &lt;span class="location"&gt;Remote&lt;/span&gt;
    &lt;time datetime="2026-05-21"&gt;21 May&lt;/time&gt;
  &lt;/div&gt;
&lt;/body&gt;&lt;/html&gt;
""" + '"""' + """

with sqlite3.connect("jobs.db") as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS jobs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL, company TEXT NOT NULL,
        location TEXT NOT NULL, posted_at TEXT NOT NULL)''')

    soup = BeautifulSoup(SAMPLE_HTML, "html.parser")
    records = [(c.select_one("h3").get_text(strip=True),
                c.select_one(".company").get_text(strip=True),
                c.select_one(".location").get_text(strip=True),
                c.select_one("time")["datetime"])
               for c in soup.select("div.job-card")]
    print("Extracted", len(records), "jobs")

    cur.executemany(
        "INSERT INTO jobs (title, company, location, posted_at) VALUES (?,?,?,?)",
        records)

    top = cur.execute('''SELECT title, company, location, posted_at
                         FROM jobs ORDER BY posted_at DESC LIMIT 5''').fetchall()
    for row in top:
        print(row)

with open("top_jobs.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["title", "company", "location", "posted_at"])
    w.writerows(top)
print("Wrote top_jobs.csv")
</code></pre>

<h3>Expected console output</h3>
<pre><code>Extracted 3 jobs
('Data Engineer', 'Beta Insights', 'Johannesburg', '2026-05-22')
('ML Intern', 'Acme Data', 'Remote', '2026-05-21')
('Junior Python Developer', 'Acme Data', 'Cape Town', '2026-05-20')
Wrote top_jobs.csv</code></pre>

<h3>Reflection answers</h3>
<ol>
<li><code>executemany</code> with <code>?</code> placeholders is
<strong>safer</strong> (the driver never substitutes the value into the
SQL string, so injection is impossible) and <strong>faster</strong>
(SQLite prepares the statement <em>once</em> and binds parameters in a
loop, avoiding per-row parse + plan + compile).</li>
<li><strong>Polite scraping:</strong>
  <ul>
    <li>Read <code>robots.txt</code> with
        <code>urllib.robotparser</code> and honour disallow rules.</li>
    <li>Set a real <code>User-Agent</code> identifying you + a contact
        e-mail.</li>
    <li>Throttle: <code>time.sleep(2)</code> between requests, plus
        randomised jitter.</li>
    <li>Implement exponential back-off on HTTP 429 / 5xx, max 3
        retries.</li>
    <li>Cache results (HTTP ETag / If-Modified-Since) so reruns don’t
        hit the site again.</li>
    <li>Run during off-peak hours; respect <code>Crawl-delay</code> if
        published.</li>
  </ul>
</li>
<li><strong>Legal / ethical:</strong>
  <ul>
    <li><strong>POPIA</strong> — recruiter names + e-mails are personal
        information. Need a lawful basis (consent, legitimate interest)
        and must minimise + secure the data.</li>
    <li><strong>Cybercrimes Act 19/2020 §3</strong> — unauthorised
        access to a computer system is criminal. T&amp;Cs that prohibit
        scraping convert technical access into <em>unauthorised</em>
        access.</li>
    <li><strong>Site T&amp;Cs</strong> — breaching them exposes you to
        civil claims even where the data is public.</li>
    <li><strong>Consent &amp; minimisation</strong> — don’t harvest
        fields you do not need (skip e-mails if titles + companies
        suffice).</li>
    <li><strong>Purpose limitation</strong> — if you collected for
        analytics, you may not later re-use for marketing.</li>
  </ul>
</li>
<li>Add a <code>company</code> table; replace <code>jobs.company</code>
with a foreign key <code>company_id</code>:
<pre><code>CREATE TABLE company (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    website TEXT
);
ALTER TABLE jobs ADD COLUMN company_id INTEGER REFERENCES company(id);

-- list jobs together with company details:
SELECT j.title, j.location, j.posted_at, c.name, c.website
FROM   jobs  j
INNER JOIN company c ON c.id = j.company_id
ORDER BY j.posted_at DESC;</code></pre>
The natural join here is <strong><code>INNER JOIN</code></strong>
(every job must have a company); use <code>LEFT JOIN</code> only if you
want orphan jobs whose company hasn’t been recorded yet.</li>
</ol>
"""

# ---------------------------------------------------------------------------
# Lesson 7 — Choose the right ML approach
# ---------------------------------------------------------------------------
LAB_ANSWERS[7] = """
<h3>Scenario 2 — Retail customer segmentation</h3>
<ul>
<li><strong>Problem type:</strong> Clustering (no labels).</li>
<li><strong>Paradigm:</strong> <strong>Unsupervised learning</strong> —
the business has no pre-existing “segment” column; the model must
discover natural groupings.</li>
<li><strong>Candidate algorithms:</strong> K-Means (fast baseline) and
Gaussian Mixture Models / HDBSCAN (handles non-spherical clusters
&amp; noise).</li>
<li><strong>Success metric:</strong> internal — silhouette score &gt; 0.4;
external — uplift in click-through on the next campaign by ≥ 15 %
versus the current generic mailer (A/B test).</li>
<li><strong>Data sources:</strong> loyalty-card RFM (recency, frequency,
monetary), basket composition (categories purchased), demographic
hints (postal-code-level income), channel (online / in-store).</li>
<li><strong>Evaluation plan:</strong> standardise features → fit K-Means
with k = 2 … 10 → choose k by elbow + silhouette → name &amp; profile
clusters with marketing → run a 4-week A/B test with one randomised
control segment. Deploy if uplift CI excludes 0.</li>
</ul>

<h3>Scenario 3 — Maize crop-yield prediction</h3>
<ul>
<li><strong>Problem type:</strong> Regression (continuous t/ha).</li>
<li><strong>Paradigm:</strong> <strong>Supervised learning</strong> —
historical seasons have ground-truth yields.</li>
<li><strong>Candidate algorithms:</strong> Gradient Boosting Regressor
(XGBoost / LightGBM) and a Random Forest as a robust baseline; a CNN
on satellite tiles if image data is available.</li>
<li><strong>Success metric:</strong> MAPE ≤ 15 % on the held-out
season; RMSE in t/ha reported alongside.</li>
<li><strong>Data sources:</strong> per-farm yield history, daily
rainfall &amp; temperature (SAWS), NDVI from Sentinel-2, soil class
(SoilGrids), planting date and cultivar.</li>
<li><strong>Evaluation plan:</strong> <em>chronological</em> hold-out —
train on seasons up to last year, validate on the most recent season.
Baseline = a 5-year farm-level mean. Deploy if MAPE beats baseline by
≥ 5 percentage points; monitor drift each season.</li>
</ul>

<h3>Reflection answers</h3>
<ol>
<li><strong>Segmentation</strong> was hardest because there is no
ground truth — “correct” depends on marketing acceptance, so we had
to plan an A/B test rather than a confusion matrix.</li>
<li>Ethical risks per scenario:
  <ul>
    <li>Fraud — <em>bias</em>: model may over-flag young / rural
        customers; mitigate with subgroup-level false-positive audit.</li>
    <li>Segmentation — <em>privacy / consent</em>: re-using loyalty
        data for targeting needs explicit POPIA consent text; offer
        opt-out.</li>
    <li>Yield — <em>exclusion</em>: model trained on commercial farms
        may misadvise smallholders; collect and weight smallholder data.</li>
  </ul>
</li>
<li>With only one month of data, prefer <strong>simple, low-variance
models</strong> (logistic regression, Naive Bayes, ridge regression)
and rely on strong cross-validation. Gradient boosting and deep nets
will over-fit at that scale.</li>
<li>To an executive, report a <strong>business KPI</strong>: “fraud
losses prevented per month (R)”, “campaign click-uplift (%)”, “Rand
saved per hectare avoided over-fertiliser”. Technical metrics
(F1, RMSE) confuse non-technical audiences and don’t tie to value.</li>
</ol>
"""

# ---------------------------------------------------------------------------
# Lesson 8 — Iris classifier
# ---------------------------------------------------------------------------
LAB_ANSWERS[8] = """
<h3>Full <code>iris_lab.py</code></h3>
<pre><code>import joblib
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

data = load_iris(as_frame=True)
df = data.frame
X, y = df.drop(columns="target"), df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf",    LogisticRegression(max_iter=1000)),
])

grid = GridSearchCV(pipe, {"clf__C": [0.01, 0.1, 1, 10, 100]},
                    cv=5, scoring="f1_macro")
grid.fit(X_train, y_train)

print("best C       :", grid.best_params_)
print("CV f1_macro  :", round(grid.best_score_, 3))
print("test accuracy:", round(grid.score(X_test, y_test), 3))

y_pred = grid.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=data.target_names))

joblib.dump(grid.best_estimator_, "iris_model.joblib")
print("predicted:", data.target_names[
    joblib.load("iris_model.joblib").predict([[5.1, 3.5, 1.4, 0.2]])[0]])
</code></pre>

<h3>Expected console output</h3>
<pre><code>best C       : {'clf__C': 10.0}
CV f1_macro  : 0.967
test accuracy: 0.967
[[10  0  0]
 [ 0  9  1]
 [ 0  0 10]]
              precision    recall  f1-score   support
      setosa       1.00      1.00      1.00        10
  versicolor       1.00      0.90      0.95        10
   virginica       0.91      1.00      0.95        10
    accuracy                           0.97        30
predicted: setosa</code></pre>

<h3>Reflection answers</h3>
<ol>
<li>If we scaled the whole dataset before <code>train_test_split</code>
the test set’s mean and standard deviation would leak into the
training data — <strong>data leakage</strong> — and the reported test
accuracy would be optimistically biased. Wrapping both steps in a
<code>Pipeline</code> guarantees the scaler is fit only on the training
fold inside each CV split.</li>
<li>For fraud detection switch to <strong>recall on the positive
class</strong>, or to <strong>average precision (PR-AUC)</strong>. F1
treats classes symmetrically but fraud is heavily imbalanced and
missing a fraud is far costlier than a false alarm.</li>
<li><strong>Bias / loan-decision risks &amp; mitigations:</strong>
  <ul>
    <li><em>Proxy variables for race / sex</em> — postal code and
        income often correlate with apartheid-era spatial inequalities.
        Mitigate: audit feature importance for proxies, drop or
        adversarially debias them; measure
        <em>equal-opportunity</em> (TPR parity) across groups.</li>
    <li><em>Feedback loops</em> — denying loans to a subgroup
        shrinks future training data for that subgroup, hardening the
        bias. Mitigate: keep a randomly approved “exploration” cohort
        (~2 %) and use those outcomes to retrain.</li>
    <li><em>Lack of recourse</em> — borrowers must be able to ask why
        they were denied. Mitigate: SHAP / LIME explanations attached
        to every decision plus a documented appeal path.</li>
    <li><em>Governance</em> — Model card, fairness report and an
        Information Officer sign-off before deployment; quarterly
        re-validation against new applicant data.</li>
  </ul>
</li>
</ol>
"""

# ---------------------------------------------------------------------------
# Lesson 9 — MNIST in Keras
# ---------------------------------------------------------------------------
LAB_ANSWERS[9] = """
<h3>Full <code>mnist_mlp.py</code></h3>
<pre><code>import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models

# 2. Load
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 3. Normalise to [0, 1]
x_train = x_train.astype("float32") / 255.0
x_test  = x_test.astype("float32")  / 255.0

# 4. MLP
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.2),
    layers.Dense(10, activation="softmax"),
])
model.summary()

# 5. Compile
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# 6. Fit
history = model.fit(x_train, y_train, epochs=5,
                    validation_split=0.1, verbose=2)

# 7. Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"Test loss : {test_loss:.4f}")
print(f"Test acc  : {test_acc:.4f}")

# 8. Plot
plt.plot(history.history["loss"],     label="train")
plt.plot(history.history["val_loss"], label="val")
plt.xlabel("epoch"); plt.ylabel("loss"); plt.legend()
plt.title("MNIST MLP — loss curves")
plt.savefig("mnist_loss.png", dpi=120)

# 10. Save + reload
model.save("mnist_mlp")
reloaded = tf.keras.models.load_model("mnist_mlp")
print("reload acc:", round(reloaded.evaluate(x_test, y_test, verbose=0)[1], 4))
</code></pre>

<h3>Expected output (your numbers will be close)</h3>
<pre><code>Epoch 1/5  loss: 0.2949 - acc: 0.9148 - val_loss: 0.1466 - val_acc: 0.9580
Epoch 5/5  loss: 0.0744 - acc: 0.9766 - val_loss: 0.0808 - val_acc: 0.9763
Test loss : 0.0731
Test acc  : 0.9773
reload acc: 0.9773</code></pre>

<h3>Reflection answers</h3>
<ol>
<li>First try a <strong>stronger regulariser</strong> in this order:
  <ul>
    <li>Increase Dropout from 0.2 → 0.4.</li>
    <li>Add <strong>early stopping</strong> on
        <code>val_loss</code> with <code>patience=2</code>.</li>
    <li>If gap persists, shrink the hidden layer (128 → 64) and / or
        add L2 weight decay (<code>kernel_regularizer=l2(1e-4)</code>).</li>
  </ul>
The training–validation gap of ~0.5 % is small — the lab is mostly
illustrating the diagnostic, not a real overfitting problem.</li>
<li><strong>MSE is wrong for a softmax classifier</strong> because:
  <ul>
    <li>It ignores the probabilistic interpretation of softmax outputs
        — penalising distance instead of log-likelihood gives a flatter
        gradient and slow learning.</li>
    <li>Its gradient w.r.t. softmax is small whenever the wrong class
        already has tiny probability, so confidently wrong predictions
        receive almost no signal.</li>
    <li>Cross-entropy is the maximum-likelihood loss for categorical
        labels; MSE assumes Gaussian residuals, which doesn’t hold for
        one-hot targets.</li>
  </ul>
</li>
<li><strong>CNN replacement and comparison:</strong>
<pre><code>cnn = models.Sequential([
    layers.Reshape((28, 28, 1), input_shape=(28, 28)),
    layers.Conv2D(32, 3, activation="relu"),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, activation="relu"),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(10, activation="softmax"),
])
cnn.compile(optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"])
cnn.fit(x_train, y_train, epochs=5, validation_split=0.1, verbose=2)</code></pre>
Typical results:
<table>
<thead><tr><th>Model</th><th>Params</th><th>Test acc</th><th>Epoch time (CPU)</th></tr></thead>
<tbody>
<tr><td>MLP</td><td>≈ 101 k</td><td>≈ 97.7 %</td><td>≈ 3 s</td></tr>
<tr><td>CNN</td><td>≈ 93 k</td><td>≈ 99.0 %</td><td>≈ 25 s</td></tr>
</tbody></table>
Why a CNN wins on images: convolutional filters exploit
<strong>locality</strong> (nearby pixels form edges &amp; strokes) and
<strong>translation invariance</strong> (the same filter detects a “3”
wherever it appears) through weight sharing. An MLP has to relearn each
shape at each position — it spends parameters on pixel locations
instead of features.</li>
</ol>
"""

# ---------------------------------------------------------------------------
# Lesson 10 — Design-thinking sprint
# ---------------------------------------------------------------------------
LAB_ANSWERS[10] = """
<p><em>Worked memorandum using the <strong>clinic booking chatbot</strong>
scenario.</em></p>

<h3>Step 1 — Persona</h3>
<pre><code>Name:        Thandi Mokoena
Age / role:  34, mother of two, cashier at Pick n Pay
Location:    Tembisa, Gauteng
Devices:     Entry-level Android, 2 GB data per month
Language:    isiZulu primary, English secondary
Goal:        Book an antenatal slot without queueing from 04:00
Pain points: Long queues, data cost, isiZulu preferred
Quote:       “I lose a day’s wages every time I visit the clinic.”</code></pre>

<h3>Step 2 — Three How-Might-We questions</h3>
<ol>
<li>HMW let Thandi book a slot in under two minutes on a low-end phone?</li>
<li>HMW communicate in isiZulu without expensive professional
translation?</li>
<li>HMW avoid storing more health data than the clinic strictly needs?</li>
</ol>

<h3>Step 3 — Crazy 8s (one-line descriptions)</h3>
<ol>
<li>WhatsApp bot using approved templates.</li>
<li>USSD menu *120*CLINIC# — works on any phone.</li>
<li>Voice-call IVR (DTMF-driven) in isiZulu and English.</li>
<li>Missed-call callback (caller dials, hangs up, clinic phones back).</li>
<li>Offline-first Android app, syncs when on Wi-Fi.</li>
<li>Community-health-worker tablet doing assisted bookings door-to-door.</li>
<li>Printed QR poster at the taxi rank linking to the booking page.</li>
<li>Telegram channel + bot for the small fraction of users on Telegram.</li>
</ol>
<p><strong>Pick first:</strong> WhatsApp bot — best reach in South Africa
and the lowest per-message data cost via Meta’s zero-rated tariffs.</p>

<h3>Step 4 — MVP wireframe (text version)</h3>
<pre><code>[Welcome]    “Sawubona Thandi! Reply 1 to book, 2 to cancel, 3 STOP.”
[Book]       “Choose a date: 1) Mon 27  2) Tue 28  3) Wed 29”
[Slot]       “Choose time: 1) 09:00  2) 10:00  3) 11:30”
[Confirm]    “Booked Mon 27 May 10:00 — Tembisa Clinic. Reply C to cancel.”
[Reminder]   T-24h: “Khumbula: appointment kusasa 10:00. Reply C to cancel.”</code></pre>
<p>Out of MVP: payments, full medical history, multi-clinic search,
specialist referrals.</p>

<h3>Step 5 — POPIA checklist</h3>
<table>
<thead><tr><th>Condition</th><th>How we satisfy it</th></tr></thead>
<tbody>
<tr><td>Lawful basis</td><td>Explicit consent captured on the first
WhatsApp message (“Reply YES to allow us to use your number for clinic
bookings”).</td></tr>
<tr><td>Purpose limitation</td><td>Booking and reminders only — not
marketing, not research.</td></tr>
<tr><td>Data minimisation</td><td>Name + cellphone + clinic + slot.
<strong>No diagnosis, no symptoms.</strong></td></tr>
<tr><td>Security safeguards</td><td>TLS in transit, AES-256 at rest,
RBAC on admin panel, audit log.</td></tr>
<tr><td>Information quality</td><td>Patient can reply MY DATA to view
what is stored and EDIT to update.</td></tr>
<tr><td>Data-subject rights</td><td>Reply STOP to delete; honoured
within 7 days.</td></tr>
<tr><td>Cross-border</td><td>Hosted in Azure South Africa North —
no cross-border transfer.</td></tr>
<tr><td>Accountability</td><td>Named Information Officer + DPIA on file.</td></tr>
</tbody></table>

<h3>Step 6 — Three ethical risks &amp; mitigations</h3>
<ol>
<li><strong>Language bias</strong> — model may misunderstand isiZulu
slang. Mitigation: human-reviewed isiZulu corpora, low-confidence
intents escalate to a human nurse-agent.</li>
<li><strong>Exclusion of feature-phone users</strong> — not everyone has
WhatsApp. Mitigation: parallel USSD channel with the same booking
logic.</li>
<li><strong>Hallucinated medical advice</strong> — an LLM might invent
symptoms. Mitigation: bot is <strong>scope-locked</strong> to
booking-related intents; any medical question receives the canned
reply <em>“I can only help with bookings — please call the clinic on
011 …”</em>.</li>
</ol>

<h3>Step 7 — Multidisciplinary team</h3>
<ul>
<li>Product Manager — owns the sprint and roadmap.</li>
<li>UX designer fluent in isiZulu — conversation flows + tone.</li>
<li>AI / NLP developer — intent classifier + WhatsApp integration.</li>
<li>Backend / MLOps engineer — booking service, monitoring, drift.</li>
<li>Clinic nurse-manager — domain expert, owns the slot calendar.</li>
<li>POPIA Information Officer — consent text, DPIA, breach drills.</li>
<li>QA tester — functional <em>and</em> fairness testing across
languages, age groups, devices.</li>
<li>Community liaison — recruits real users for testing &amp; feedback.</li>
</ul>

<h3>Step 8 — Reflection answers</h3>
<ol>
<li>HMW #2 (vernacular language) excited me most — it is where AI can
add the clearest equity benefit beyond what a paper form could ever do.</li>
<li><strong>Purpose limitation</strong> was the hardest POPIA condition:
the clinic manager wanted to “also use the data for outbreak research”,
which would require a new consent flow.</li>
<li>With one extra week I would test the riskiest assumption: that
patients trust a WhatsApp message from the clinic enough to act on it.
Run 50 in-person interviews + 100 dummy bookings and measure show-up
rate vs. the current paper baseline.</li>
<li>Escalate <strong>the LLM hallucination risk</strong> to the
Information Officer before launch — a wrong medical reply could cause
real harm and engages clinical-liability and POPIA security
obligations.</li>
</ol>
"""


def get_answer(lesson_order):
    """Return the HTML model answer for a 1-based lesson order, or ``None``."""
    return LAB_ANSWERS.get(int(lesson_order))
