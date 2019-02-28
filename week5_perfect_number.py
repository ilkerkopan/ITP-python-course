# test a number is perfect
print("Enter a number to test if it is perfect")
number=int(input())
sum=0;

for i in range(1,number):
    if (number % i) == 0 :
        sum = sum + i

if sum == number :
    print("number is perfect")
else :
    print("Not perfect")