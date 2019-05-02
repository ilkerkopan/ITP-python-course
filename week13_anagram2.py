# anagrams in a text file
anagrams = {}
with open("wordlist.txt") as file:
    for line in file:
        word = line.lower().replace("\n","")
        key = ''.join(sorted(list(word)))
        if key in anagrams:
            anagrams[key].add(word)
        else:
            anagrams[key] = {word}
            
anagram_count = 0
for anagram_list in anagrams.values():
    if len(anagram_list)>1:
        anagram_count += 1
    if len(anagram_list)>10:
        print(f'{len(anagram_list)}  {anagram_list}')
        
print(f'We have {anagram_count} number of anagrams')