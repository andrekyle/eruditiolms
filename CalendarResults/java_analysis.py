import matplotlib.pyplot as plt
import numpy as np

# Data for Java exam scores
students = [
    "Oyame Mazaleni", "Amogelang Moletsane", "Tshepo Basini", "Prudence Phalafala", 
    "Liso Ngewendu", "Khanyisile Ntimane", "Mpho Modise", "Thabang Lenonyana",
    "Sihle Radebe", "Sinokuhle Mogale", "Tshegofatso Ditibane", "Tumiso Madia",
    "Vuyo Bezu", "Warren Goldstone", "William Keorekile", "Yoliswa Ngqukuvana",
    "Zena Nguwata", "Amangile Tinta", "Arnold Mukwevho", "Aviwe Kave",
    "Bokang Moloi", "Bophelo Sihlangu", "Carmen Bowers", "Cassey Muronga",
    "Charles Rathaba", "Chriselda Nleya", "Eithyn-Josh Walters", "Esau Bazini"
]

scores = [
    100, 73, 73, 98, 98, 97, 96, 95, 94, 94, 93, 92, 92, 91, 91, 90,
    90, 89, 88, 88, 87, 87, 86, 86, 85, 85, 84, 84
]

# Set figure style
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 10
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3

# Pie Chart: Score Categories
categories = {'90-100': 0, '80-89': 0, '70-79': 0}
for score in scores:
    if score >= 90:
        categories['90-100'] += 1
    elif score >= 80:
        categories['80-89'] += 1
    else:  # All remaining scores are 70-79 since minimum is 73
        categories['70-79'] += 1

plt.figure()
colors = ['#3498db', '#2ecc71', '#f1c40f']  # Blue, Green, Yellow
explode = None  # No explode effect

plt.pie(list(categories.values()), 
        explode=explode,
        labels=list(categories.keys()),
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        shadow=False)  # No shadow
plt.title('Score Categories Distribution', fontsize=14, pad=20)
plt.axis('equal')
plt.savefig('pie_chart.png', dpi=300, bbox_inches='tight')
plt.show()
