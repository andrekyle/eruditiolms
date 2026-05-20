import matplotlib.pyplot as plt
import numpy as np

# Data: Student names and scores for Power BI exam
students = [
    "Aviwe Kave", "Bokang Moloi", "Bongani Moloi", "Bophelo Sihlangu", "Carmen Bowers",
    "Eithyn-Josh Walters", "Fanele Sithole", "Gugu Ngubeni", "Hlonipho Bila", "Jessica Mathye",
    "Kamogelo Tsie", "Kamogelo Nonyane", "Karabo Ngubeni", "Keisha Sokanyile", "Kemelo Malau",
    "Khensani Mzimela", "Koketso Otukile", "Laura Manhique", "Lindelwa Dlamini", "Lindokuhle Nzuza",
    "Liso Ngewendu", "Malaika Nghona", "Matimu Chabangu", "Mbhoni Bvuma", "Minky Selowa",
    "Mmadikana Kgole", "Mpho Modise", "Mpho Mboweni", "Nthabeleng Makae", "Nthati Mokone",
    "Nyiko Nomvela", "Oarabile Mafu", "Ofentse Magoro", "Patricia Mahwebila", "Patricia Hlungwani",
    "Priscilla Dlamini", "Promise Lamola", "Prudence Mongwe", "Rapelang Masanabo", "Sbongile Mazhaka",
    "Sibusiso Sekhoto", "Sinethemba Pheta", "Sinokuhle Mogale", "Sizwe Ndlovu", "Sithembiso Caleni",
    "Skhumbzo Mabasa", "Sthembile Radebe", "Tebogo Mashilo", "Thandeka Ngwenya", "Thando Mfenyane",
    "Thapelo Morata", "Tlotlego Mnguni", "ToniLee Manuel", "Tshegofatso Ditibane", "Tshepiso Hilane",
    "Tumiso Madia", "Warren Goldstone", "William Keorekile", "Yoliswa Ngqukuvana"
]

first_scores = [
    790, 710, 810, 760, "Never Wrote", 700, 710, 710, 740, 770,
    820, 782, 710, 633, 800, 800, 770, 750, 554, 409,
    "Rescheduled", 803, 750, 501, 686, 620, 860, 581, 770, 780,
    860, 720, 730, 840, 730, 673, 772, 850, 760, 647,
    741, 633, 810, "Missed Exam", 581, 686, 780, 820, 720, 647,
    790, 860, 515, 780, 567, "Missed Exam", 462, 710, 740
]

second_scores = {
    "Lindelwa Dlamini": 793,
    "Lindokuhle Nzuza": 813,
    "Minky Selowa": 782,
    "Priscilla Dlamini": 834,
    "Sbongile Mazhaka": 751,
    "Sinethemba Pheta": 824,
    "Thando Mfenyane": 834,
    "ToniLee Manuel": 710,
    "Tshepiso Hilane": 793,
    "Warren Goldstone": 466
}

passing_score = 700

# Set consistent style for all plots
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = [8, 5]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'white'

# Filter out non-attempts for statistical analysis
valid_first_scores = [score for score in first_scores if isinstance(score, (int, float)) and score > 0]


def sparse_student_labels(names, step=3):
    return [name if i % step == 0 else '' for i, name in enumerate(names)]


def short_name(full_name):
    parts = full_name.split()
    if len(parts) < 2:
        return full_name
    return f"{parts[0]} {parts[-1][0]}."

# 1. Bar Chart: Individual Student Scores
plt.figure(figsize=(20, 8))
numeric_scores = [score if isinstance(score, (int, float)) else 0 for score in first_scores]
x_positions = np.arange(len(students))
bars = plt.bar(x_positions, numeric_scores, color='#3498db', alpha=0.8)
plt.axhline(y=passing_score, color='#e74c3c', linestyle='--', label=f'Passing Score ({passing_score})')
for i, student in enumerate(students):
    if first_scores[i] in ["Never Wrote", "Rescheduled", "Missed Exam"]:
        bars[i].set_color('#95a5a6')
plt.title('Individual Student Scores (First Attempt)', pad=15)
plt.xlabel('Students')
plt.ylabel('Score')
short_labels = [short_name(name) for name in students]
plt.xticks(x_positions, sparse_student_labels(short_labels, step=5), rotation=25, ha='right', fontsize=9)
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.subplots_adjust(bottom=0.24)
plt.tight_layout()
plt.savefig('bar_chart_first_attempt.png', bbox_inches='tight')
plt.close()

# 2. Histogram: Score Distribution
plt.figure(figsize=(8, 5))
plt.hist(valid_first_scores, bins=15, color='#2ecc71', alpha=0.8, edgecolor='white')
plt.axvline(x=passing_score, color='#e74c3c', linestyle='--', label=f'Passing Score ({passing_score})')
plt.title('Score Distribution (First Attempt)', pad=15)
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('histogram_first_attempt.png', bbox_inches='tight')
plt.close()

# 3. Pie Chart: Score Categories
categories = {'800-1000': 0, '700-799': 0, 'Below 700': 0}
for score in valid_first_scores:
    if score >= 800:
        categories['800-1000'] += 1
    elif score >= 700:
        categories['700-799'] += 1
    else:
        categories['Below 700'] += 1

plt.figure(figsize=(6, 6))
colors = ['#3498db', '#2ecc71', '#f1c40f']
plt.pie(list(categories.values()), 
        labels=list(categories.keys()),
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 10})
plt.title('Score Categories Distribution', pad=15)
plt.axis('equal')
plt.savefig('pie_chart_first_attempt.png', bbox_inches='tight')
plt.close()

# 4. Comparison of First and Second Attempts
retake_students = list(second_scores.keys())
first_attempt_retake = [first_scores[students.index(student)] for student in retake_students]
first_attempt_retake = [0 if isinstance(score, str) else score for score in first_attempt_retake]
second_attempt_retake = [second_scores[student] for student in retake_students]

x = np.arange(len(retake_students))
width = 0.35

plt.figure(figsize=(8, 5))
plt.bar(x - width/2, first_attempt_retake, width, label='First Attempt', color='#3498db', alpha=0.8)
plt.bar(x + width/2, second_attempt_retake, width, label='Second Attempt', color='#2ecc71', alpha=0.8)
plt.axhline(y=passing_score, color='#e74c3c', linestyle='--', label=f'Passing Score ({passing_score})')
plt.title('First vs Second Attempt Scores', pad=15)
plt.xlabel('Students')
plt.ylabel('Score')
plt.xticks(x, retake_students, rotation=45, ha='right')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('comparison_retake.png', bbox_inches='tight')
plt.close()

# Calculate and print statistics
print("\nStatistical Analysis:")
print("-" * 50)
print(f"Total Students: {len(students)}")
print(f"Students with Valid First Attempts: {len(valid_first_scores)}")
print(f"Average Score (First Attempt): {np.mean(valid_first_scores):.2f}")
print(f"Median Score (First Attempt): {np.median(valid_first_scores):.2f}")
print(f"Standard Deviation (First Attempt): {np.std(valid_first_scores):.2f}")
print(f"Pass Rate (First Attempt): {(sum(1 for x in valid_first_scores if x >= passing_score) / len(valid_first_scores) * 100):.1f}%")
print(f"Number of Retakes: {len(second_scores)}")
print(f"Pass Rate (Second Attempt): {(sum(1 for x in second_scores.values() if x >= passing_score) / len(second_scores) * 100):.1f}%")
