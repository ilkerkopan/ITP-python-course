import random
counter = 1
lucky_number = random.randint(1,11)
guess=0
try_count=0
while guess != lucky_number and try_count<3:
    print("your guess is wrong!")
    guess=int(input("Enter your guess: "))
    try_count += 1
if guess== lucky_number:
    print("You win!")
else :
    print("You lose. Lucky number was: %d" % lucky_number)