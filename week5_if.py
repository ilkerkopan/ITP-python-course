# read input and test if it is positive
print("Enter a number:")
number=int(input())

if number>0 :
    print("number is positive")
    
# check grade print fail or pass
print("Enter grade:")
grade=int(input())

if grade>=60 :
    print("passed")
else:
    print("failed")
    print("we are in else block")
print("we are outside if-else block")