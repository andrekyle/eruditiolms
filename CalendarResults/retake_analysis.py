import matplotlib.pyplot as plt
import numpy as np

# Data: Student names, first attempt scores, and second attempt scores (if applicable)
students = [
    "Amangile Tinta", "Amogelang Moletsane", "Arnold Mukwevho", "Aviwe Kave", "Blessing Khabo",
    "Bokang Moloi", "Bophelo Sihlangu", "Carmen Bowers", "Cassey Muronga", "Charles Rathaba",
    "Chriselda Nleya", "Eithyn-Josh Walters", "Esau Bazini", "Fanele Sithole", "Hlonipho Bila",
    "Jessica Mathye", "Joseph Motshana", "Kamogelo Tsie", "Kamogelo Nonyane", "Karabo Ngubeni",
    "Katlego Sehata", "Katleho Motsitsi", "Keisha Sokanyile", "Kemelo Malau", "Kgotlello Nonyane",
    "Khanyisile Ntimane", "Khayalethu Dube", "Khensani Mzimela", "Laura Manhique", "Lerato Mathe",
    "Lindelwa Dlamini", "Lindokuhle Nzuza", "Liso Ngewendu", "Lizbeth Masanabo", "Luyanda Mthi",
    "Mady Mhuli", "Mahlatsi Makamo", "Malaika Nghona", "Matimu Chabangu", "Mbhoni Bvuma",
    "Mikateko Mammburu", "Minky Selowa", "Mmadikana Kgole", "Mpho Modise", "Mpho Mboweni",
    "Mxolisi Ngema", "Nokuthula Pilane", "Nthabeleng Makae", "Nthati Mokone", "Nthatisi Pheko",
    "Nyiko Nomvela", "Oarabile Mafu", "Ofentse Magoro", "Oyame Mazeleni", "Patricia Mahwebila",
    "Patricia Hlungwani", "Priscilla Dlamini", "Promise Lamola", "Prudence Phalafala", "Prudence Mongwe",
    "Rangani Mudau", "Rapelang Masanabo", "Reitumestse Mphahele", "Relebogile Mojela", "Sakhiwo Mbatha",
    "Sbongile Mazhaka", "Sibusiso Sekhoto", "Sihle Radebe", "Sinethemba Pheta", "Sinokuhle Mogale",
    "Sizwe Ndlovu", "Skhumbzo Mabasa", "Sthembile Radebe", "Tebogo Mashilo", "Thabang Lenonyana",
    "Thandeka Ngwenya", "Thando Mfenyane", "Thapelo Morata", "Thato Monchwe", "Tlhologelo Moremi",
    "ToniLee Manuel", "Tshegofatso Ditibane", "Tshepiso Hilane", "Tshilidzi Mudau", "Tumiso Madia",
    "Vuyo Bezu", "Warren Goldstone", "William Keorekile", "Yoliswa Ngqukuvana", "Zena Nguwata",
    "Zusiphesande Malunga"
]
first_scores = [
    56, 71, 83, 80, 69, 64, 88, 97, 84, 85, 76, 60, 92, 69, 69, 84, 82, 83, 65, 57,
    81, 68, 83, 72, 89, 81, 94, 79, 75, 93, 83, 87, 98, 95, 81, 89, 87, 56, 91, 59,
    77, 70, 85, 77, 58, 82, 87, 92, 71, 87, 92, 92, 77, 92, 75, 75, 75, 58, 98, 73,
    74, 75, 85, 77, 94, 74, 87, 90, 67, 81, 80, 81, 71, 76, 87, 69, 62, 70, 88, 88,
    57, 75, 53, 72, 64, 90, 73, 75, 83, 76, 77
]
second_scores = {
    "Amangile Tinta": 77, "Bokang Moloi": 76, "Eithyn-Josh Walters": 73, "Fanele Sithole": 86,
    "Hlonipho Bila": 76, "Kamogelo Nonyane": 65, "Karabo Ngubeni": 55, "Katleho Motsitsi": 73,
    "Malaika Nghona": 89, "Mpho Mboweni": 78, "Promise Lamola": 70, "Sinethemba Pheta": 81,
    "Thandeka Ngwenya": 57, "Thando Mfenyane": 86, "ToniLee Manuel": 75, "Tshepiso Hilane": 78,
    "Tumiso Madia": 86
}
passing_score = 70

# Set figure style
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 10
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3

# 1. Bar Chart: Individual Student Scores (First Attempt)
plt.figure()
bars = plt.bar(students, first_scores, color='skyblue')
plt.axhline(y=passing_score, color='red', linestyle='--', label=f'Passing Score ({passing_score}%)')
plt.title('Individual Student Scores (First Attempt)', fontsize=14, pad=20)
plt.xlabel('Students', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.xticks(rotation=90, ha='right', fontsize=8)
plt.legend()

# Color bars based on passing score
for i, bar in enumerate(bars):
    if first_scores[i] < passing_score:
        bar.set_color('salmon')

plt.tight_layout()
plt.savefig('bar_chart_first_attempt.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. Histogram: Score Distribution (First Attempt)
plt.figure()
plt.hist(first_scores, bins=10, edgecolor='black', color='lightgreen', alpha=0.7)
plt.axvline(x=passing_score, color='red', linestyle='--', label=f'Passing Score ({passing_score}%)')
plt.title('Score Distribution (First Attempt)', fontsize=14, pad=20)
plt.xlabel('Score Range', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('histogram_first_attempt.png', dpi=300, bbox_inches='tight')
plt.show()

# 3. Pie Chart: Score Categories (First Attempt)
categories = {'90-100': 0, '80-89': 0, '70-79': 0, 'Below 70': 0}
for score in first_scores:
    if score >= 90:
        categories['90-100'] += 1
    elif score >= 80:
        categories['80-89'] += 1
    elif score >= 70:
        categories['70-79'] += 1
    else:
        categories['Below 70'] += 1

plt.figure()
colors = ['#3498db', '#2ecc71', '#f1c40f', '#e74c3c']  # Blue, Green, Yellow, Red
explode = None  # Remove explode effect

plt.pie(list(categories.values()), 
        explode=explode,
        labels=list(categories.keys()),
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        shadow=False)  # Remove shadow
plt.title('Score Categories Distribution', fontsize=14, pad=20)
plt.axis('equal')
plt.savefig('pie_chart_first_attempt.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. Box Plot: Score Spread (First Attempt)
plt.figure()
box_plot = plt.boxplot(first_scores, 
                      vert=True,
                      patch_artist=True,
                      boxprops=dict(facecolor='lightblue', color='black'),
                      whiskerprops=dict(color='black'),
                      capprops=dict(color='black'),
                      medianprops=dict(color='darkred'))
plt.axhline(y=passing_score, color='red', linestyle='--', label=f'Passing Score ({passing_score}%)')
plt.title('Score Distribution (Box Plot)', fontsize=14, pad=20)
plt.ylabel('Score', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('box_plot_first_attempt.png', dpi=300, bbox_inches='tight')
plt.show()

# 5. Bar Chart: Comparison of First and Second Attempts
retake_students = list(second_scores.keys())
first_attempt_retake = [first_scores[students.index(student)] for student in retake_students]
second_attempt_retake = [second_scores[student] for student in retake_students]

x = np.arange(len(retake_students))
width = 0.35

plt.figure()
plt.bar(x - width/2, first_attempt_retake, width, label='First Attempt', color='#ff7675')
plt.bar(x + width/2, second_attempt_retake, width, label='Second Attempt', color='#74b9ff')
plt.axhline(y=passing_score, color='red', linestyle='--', label=f'Passing Score ({passing_score}%)')
plt.title('First vs Second Attempt Scores', fontsize=14, pad=20)
plt.xlabel('Students', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.xticks(x, retake_students, rotation=45, ha='right')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('comparison_retake.png', dpi=300, bbox_inches='tight')
plt.show()

# Print statistics
print("\nStatistical Analysis:")
print("-" * 50)
print(f"First Attempt Statistics:")
print(f"Average Score: {np.mean(first_scores):.2f}")
print(f"Median Score: {np.median(first_scores):.2f}")
print(f"Standard Deviation: {np.std(first_scores):.2f}")
print(f"Pass Rate: {(sum(1 for score in first_scores if score >= passing_score) / len(first_scores) * 100):.1f}%")

print("\nSecond Attempt Statistics:")
second_attempt_scores = list(second_scores.values())
print(f"Number of Retakes: {len(second_attempt_scores)}")
print(f"Average Score: {np.mean(second_attempt_scores):.2f}")
print(f"Median Score: {np.median(second_attempt_scores):.2f}")
print(f"Standard Deviation: {np.std(second_attempt_scores):.2f}")
print(f"Pass Rate: {(sum(1 for score in second_attempt_scores if score >= passing_score) / len(second_attempt_scores) * 100):.1f}%")
