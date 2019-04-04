#week9 simple file operations
file = open("students.txt", encoding="UTF-8")
print(file.read())
file.close()

# same but requries less line of code
with open("students.txt", encoding="UTF-8") as file:
    print(file.read())
