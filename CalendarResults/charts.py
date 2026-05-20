import matplotlib.pyplot as plt
import numpy as np

# Data: Student names and scores
students = [
    "Oyame Mazaleni", "Cassey Muronga", "Prudence Phalafala", "Tlhologelo Moremi", 
    "Chriselda Nleya", "Lerato Mathe", "Lizbeth Masanabo", "Khaya Dube", 
    "Elaine Moobi", "Thabang Lenonyane", "Sihle Radebe", "Thato Monchwe", 
    "Jospeh Motshana", "Nthatisi Pheko", "Lehlogonolo Motsopje", "Luyanda Mthi", 
    "Mxolisi Ngema", "Charles Rathaba", "Rangani Mudau", "Reitumetse Mphahlele", 
    "Khanyisile Ntimane", "Mady Mhluli", "Arnold Mukwevho", "Lerato Ndlovu", 
    "Vuyo Bezu", "Katlego Sehata", "Amogelang Moletsane", "Tshepo Basini"
]
scores = [
    100, 98, 98, 96, 96, 96, 96, 96, 96, 96, 93, 91, 91, 91, 91, 89, 89, 89, 
    89, 89, 88, 88, 82, 79, 79, 75, 73, 73
]
passing_score = 65  # Passing threshold

# 1. Bar Chart: Individual Student Scores
plt.figure(figsize=(12, 6))
plt.bar(students, scores, color='skyblue')
plt.axhline(y=passing_score, color='red', linestyle='--', label=f'Passing Score ({passing_score}%)')
plt.title('Individual Student Scores', fontsize=14)
plt.xlabel('Students', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.xticks(rotation=90, ha='right', fontsize=8)
plt.legend()
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()

# 2. Histogram: Score Distribution
plt.figure(figsize=(10, 6))
plt.hist(scores, bins=[70, 75, 80, 85, 90, 95, 100], edgecolor='black', color='lightgreen')
plt.axvline(x=passing_score, color='red', linestyle='--', label=f'Passing Score ({passing_score}%)')
plt.title('Score Distribution', fontsize=14)
plt.xlabel('Score Range', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig('histogram.png')
plt.show()

# 3. Pie Chart: Score Categories
categories = {'High (90-100)': 0, 'Medium (80-89)': 0, 'Low (70-79)': 0}
for score in scores:
    if score >= 90:
        categories['High (90-100)'] += 1
    elif score >= 80:
        categories['Medium (80-89)'] += 1
    else:
        categories['Low (70-79)'] += 1

labels = categories.keys()
sizes = categories.values()
colors = ['#ff9999', '#66b3ff', '#99ff99']
explode = (0.1, 0, 0)  # Explode the 'High' slice

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Score Categories', fontsize=14)
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.show()

# 4. Box Plot: Score Spread
plt.figure(figsize=(8, 6))
plt.boxplot(scores, vert=True, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.axhline(y=passing_score, color='red', linestyle='--', label=f'Passing Score ({passing_score}%)')
plt.title('Score Spread', fontsize=14)
plt.ylabel('Score', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig('box_plot.png')
plt.show()

# Print basic statistics for verification
print(f"Average Score: {np.mean(scores):.2f}")
print(f"Median Score: {np.median(scores):.2f}")
print(f"Standard Deviation: {np.std(scores):.2f}")
