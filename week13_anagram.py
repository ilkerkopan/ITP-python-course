anagrams = {}
anagram_count=0
with open("C:/Users/ilker/Downloads/wordlist.txt") as file:
    for line in file:
        try:
            word = line.lower().replace("'","").replace("\n","")
            sorted_line = ''.join(sorted(list(word)))
            if sorted_line in anagrams:
                anagrams[sorted_line].add(word)
            else:
                anagrams[sorted_line] = {word}
        except:
            print(f'Exception in {word} {sorted_line}')


for key, value in anagrams.items():
    if len(value)>1:
        anagram_count += 1
    if len(value)>10:
        print(f'{len(value)}  {value}')
print(f'Total number of anagrams {anagram_count}')