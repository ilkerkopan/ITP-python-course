import matplotlib.pyplot as plt

grade_counts = [0,0,0,0,0,0,0,0,0,0]
groups=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100']

with open("grades.csv") as file:
    file.readline()
    file.readline()
    for line in file:
        score = int(line.split(",")[4])
        index = score // 10
        grade_counts[index] += 1
        
print(f'Total grade counts {grade_counts}')

plt.title("Score Frequency", fontsize=24)
plt.xlabel("Score Groups", fontsize=14)
plt.ylabel("Number of Students", fontsize=14)
plt.bar(groups, grade_counts)
plt.show()