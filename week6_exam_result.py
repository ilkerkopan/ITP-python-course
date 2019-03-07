# Make a dictionary called midterm_results . Add 10 student name and score to dictionary . 
# Calculate midterm average.
# Print all the names whose grade is greater than average.
# Add two more people to dictionary and recalculate average.

midterm_results = {"Ezgi":83,
                   "Melis":100,
                   "Ceren":70,
                   "Elif":0,
                   "Mert":40,
                   "Mesut":60,
                   "Tuğra":54,
                   "Sislen":65,
                   "Şeyma":83,
                   "Ozan":75}
sum=0

for score in midterm_results.values() :
    sum = sum + score
    
average = sum / len(midterm_results)
print("Average score in midterm is:%f" % (average))

for name, score in midterm_results.items() :
    if score>=average :
        print("%s passed exam with %d" % (name,score))
        
print("Addin two more people")
midterm_results["Ömer"]=50
midterm_results["Ahmet"]=63
print()

sum=0
for score in midterm_results.values() :
    sum = sum + score
    
average = sum / len(midterm_results)
print("Average score in midterm is:%f" % (average))

for name, score in midterm_results.items() :
    if score>=average :
        print("%s passed exam with %d" % (name,score))