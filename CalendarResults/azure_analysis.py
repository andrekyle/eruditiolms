import matplotlib.pyplot as plt
import numpy as np

# Data: Student names, first attempt scores, and second attempt scores (if applicable)
students = [
    "Amangile Tinta", "Amogelang Moletsane", "Arnold Mukwevho", "Aviwe Kave", "Bokang Moloi",
    "Bophelo Sihlangu", "Carmen Bowers", "Cassey Muronga", "Charles Rathaba", "Chriselda Nleya",
    "Eithyn-Josh Walters", "Esau Bazini", "Fanele Sithole", "Hlonipho Bila", "Jessica Mathye",
    "Joseph Motshana", "Kamogelo Tsie", "Katlego Sehata", "Katleho Motsitsi", "Keisha Sokanyile",
    "Kemelo Malau", "Kgotlello Nonyane", "Khanyisile Ntimane", "Khayalethu Dube", "Khensani Mzimela",
    "Laura Manhique", "Lerato Mathe", "Lindelwa Dlamini", "Lindokuhle Nzuza", "Liso Ngewendu",
    "Lizbeth Masanabo", "Luyanda Mthi", "Mady Mhuli", "Mahlatsi Makamo", "Malaika Nghona",
    "Matimu Chabangu", "Mbhoni Bvuma", "Mikateko Mammburu", "Minky Selowa", "Mmadikana Kgole",
    "Mpho Modise", "Mpho Mboweni", "Mxolisi Ngema", "Nokuthula Pilane", "Nthabeleng Makae",
    "Nthati Mokone", "Nthatisi Pheko", "Nyiko Nomvela", "Oarabile Mafu", "Ofentse Magoro",
    "Oyame Mazeleni", "Patricia Mahwebila", "Patricia Hlungwani", "Priscilla Dlamini",
    "Promise Lamola", "Prudence Phalafala", "Prudence Mongwe", "Rangani Mudau", "Rapelang Masanabo",
    "Reitumestse Mphahele", "Relebogile Mojela", "Sakhiwo Mbatha", "Sbongile Mazhaka",
    "Sibusiso Sekhoto", "Sihle Radebe", "Sinethemba Pheta", "Sinokuhle Mogale", "Sizwe Ndlovu",
    "Skhumbzo Mabasa", "Sthembile Radebe", "Tebogo Mashilo", "Thabang Lenonyana", "Thando Mfenyane",
    "Thapelo Morata", "Thato Monchwe", "Tlhologelo Moremi", "ToniLee Manuel", "Tshegofatso Ditibane",
    "Tshepiso Hilane", "Tshilidzi Mudau", "Tumiso Madia", "Vuyo Bezu", "Warren Goldstone",
    "William Keorekile", "Yoliswa Ngqukuvana", "Zena Nguwata", "Zusiphesande Malunga"
]

first_scores = [
    560, 710, 830, 800, 640, 880, 970, 840, 850, 760, "Did Not Write", 920, 690, 690, 840, 820, 830, 810, 680, 830,
    720, 890, 810, 940, 790, 750, 930, 830, 870, 980, 950, 810, 890, 870, 560, 910, "Did Not Write", 770, 700, 850,
    770, 580, 820, 870, 920, 710, 870, 920, 920, 770, 920, 750, 750, 750, 580, 980, 730, 740, 750, 850, 770, 940, 740,
    870, 900, 670, 810, 800, 810, 710, 760, 870, 620, 700, 880, 880, 570, 750, 530, 720, 640, 900, 730, 750, 830, 760, 770
]

second_scores = {
    "Amangile Tinta": 770, "Bokang Moloi": 760, "Fanele Sithole": 860, "Hlonipho Bila": 760,
    "Katleho Motsitsi": 730, "Malaika Nghona": 890, "Mpho Mboweni": 780, "Promise Lamola": 700,
    "Sinethemba Pheta": 810, "Thando Mfenyane": 860, "ToniLee Manuel": 750, "Tshepiso Hilane": 680,
    "Tumiso Madia": 860
}

passing_score = 700  # 70% of 1000

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
    if first_scores[i] == "Did Not Write":
        bars[i].set_color('#95a5a6')
plt.title('Individual Student Scores (First Attempt)', pad=15)
plt.xlabel('Students')
plt.ylabel('Score (out of 1000)')
short_labels = [short_name(name) for name in students]
plt.xticks(x_positions, sparse_student_labels(short_labels, step=5), rotation=25, ha='right', fontsize=9)
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.subplots_adjust(bottom=0.24)
plt.tight_layout()
plt.savefig('azure_bar_chart.png', bbox_inches='tight')
plt.close()

# 2. Histogram: Score Distribution
plt.figure(figsize=(8, 5))
plt.hist(valid_first_scores, bins=[500, 600, 700, 800, 900, 1000], color='#2ecc71', alpha=0.8, edgecolor='white')
plt.axvline(x=passing_score, color='#e74c3c', linestyle='--', label=f'Passing Score ({passing_score})')
plt.title('Score Distribution (First Attempt)', pad=15)
plt.xlabel('Score Range')
plt.ylabel('Number of Students')
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('azure_histogram.png', bbox_inches='tight')
plt.close()

# 3. Pie Chart: Score Categories
categories = {'900-1000': 0, '700-899': 0, 'Below 700': 0}
for score in valid_first_scores:
    if score >= 900:
        categories['900-1000'] += 1
    elif score >= 700:
        categories['700-899'] += 1
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
plt.savefig('azure_pie_chart.png', bbox_inches='tight')
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
plt.savefig('azure_comparison.png', bbox_inches='tight')
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
