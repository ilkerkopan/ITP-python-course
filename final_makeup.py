#final make-up q1
print("\nQuestion 1:")
for i in range(1,100,2):
    print(i)
    
#q2
print("\nQuestion 2:")
lab1_scores = [5,2,1,1,3,4,1,2]
lab2_scores = [5,3,2,4,3,5,2,4]
summed_scores = []
for i in range(len(lab1_scores)):
    summed_scores.append(lab1_scores[i] + lab2_scores[i])
print(summed_scores)

#q3
print("\nQuestion 3:")
def minimum(a, b, c):
    if a<b and a<c :
        return a
    elif b<a and b<c :
        return b
    elif c<a and c<b :
        return c
print(minimum(7,3,5))
print(minimum(15,20,40))

#q4
print("\nQuestion 4:")
file = open("mobydick.txt")
words = set()
for line in file:
    for word in line.lower().split(" "):
        words.add(word)
print(len(words))
    
#q5
print("\nQuestion 5:")
nums = set([1,1,2,3,3,3,4])
print(len(nums))
print("----------")
name = "snow storm"
print(name[6:8])
print("----------")
for i in range(2):
    print(i)
for i in range(4,6):
    print(i)
print("----------")
country_counter = {}

def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

addone('China')
addone('Japan')
addone('Turkey')
addone('China')

print(len(country_counter))
print(country_counter.get('China'))
print("----------")
x = 12 // 5
if x <= 2:
    print('pass')
else :
    print('fail')
