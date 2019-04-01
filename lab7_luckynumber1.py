import random
counter = 1
lucky_number = random.randint(1,11)
guess=0
while guess != lucky_number :
    print("your guess is wrong!")
    guess=int(input("Enter your guess: "))
print("You win!")