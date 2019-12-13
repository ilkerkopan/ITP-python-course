# be compiler
numbers = [1]
for i in range(2,10,2):
    numbers.append(i**2)
print(numbers.pop())

# string exerise
quote = "Whatever the mind of man can conceive and believe, it can achieve." #Napoleon Hill
words = quote.upper().split(" ")
print(words.pop())

# print triangle
space_count=4
asterisk_count=1
for line in range(4):
    for i in range(space_count):
        print("_", end="")
    for j in range(asterisk_count):
        print("*", end="")
    space_count -= 1
    asterisk_count += 2
    print()
        
# dictionary exercise 1
numbers = { '1' : '2', '2': '3', '3': '4', '4' : '10'}
print(numbers[numbers['3']])

# dictionary exercise 2
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
phonebook["Arven"]=955772213
print(phonebook)

