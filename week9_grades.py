#week9 read grades from file
user_grades = {}

with open("grades.csv") as file:
    file.readline()
    file.readline()
    count = 0
    sum = 0
    for line in file:
        user_grades[line.split(",")[1]] = int(line.split(",")[4])
        sum = sum + int(line.split(",")[4])
        count = count + 1
print(f'sum of all grades {sum}, number of grade {count}')
average = sum//count
print(f'average value is {average}')

print('-'*50)
for name, grade in user_grades.items():
    if grade >= average:
        print(name)