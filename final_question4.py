file = open("member.txt")
age_distribution = {}
for line in file:
    name = line.split(",")[0]
    age = int(line.split(",")[1]) // 10 * 10
    names = age_distribution.get(age, [])
    names.append(name)
    age_distribution[age] = names
for key,value in age_distribution.items():
    print(f'There are {len(value)} people between ages {key}-{key+10} and their names are: {value}')