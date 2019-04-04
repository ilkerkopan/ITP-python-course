# read alice.txt and count words
words = {}
count = 0
with open("alice.txt") as file:
    for line in file:
        for word in line.split():
            word = word.lower()
            word = word.replace(",","")
            if words.get(word) == None:
                words[word] = 1
            else:
                words[word] = words[word] + 1
            count = count + 1
            
print(f'number of words in alice.txt is {count}')
for key, value in words.items():
    print(f'{key} has occured {value} times')