result=1
for i in range(1,6):
    result = result * i
    
print(result)

print("-"*20)
#be compiler 2
quote = "Before software can be reusable it first has to be usable" #Ralph Johnson
words = quote.split(" ")
print(len(words.pop()))


print("-"*20)
#be compiler 3
c = 0
for z in range(2):
    for x in ['a','b']:
        print (z,x,c)
        c+=1
        
print("-"*20)
#be compiler 4
odd_numbers=[]
for i in range(1,50,2):
    odd_numbers.append(i)
print(odd_numbers.pop())

print("-"*20)
#be compiler 5
grades = {
   "Rebbie" : 60,
   "Jackie" : 50,
   "Tito" : 70,
   "Jermaine": 45,
   "La Toya": 85,
   "Marlon": 75,
   "Michael": 100,
   "Randy": 34,
   "Janet ":   90
}

for name,grade in grades.items():
    if grade<50 :
        print(name + " failed.")

