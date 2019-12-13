numbers=[14,33,41,99,3,20,9]
max=0
for number in numbers:
    if max < number :
        max = number
print("Max number is %d" % max)