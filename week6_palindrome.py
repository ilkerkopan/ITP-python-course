# week 6 palindrome exercise
print("input a text")
text=input()
middle_of_text = int(len(text)/2)
print(middle_of_text)

is_palindrome=True
for i in range(middle_of_text):
    if text[i]==text[-1-i] :
        is_palindrome=True
    else :
        is_palindrome=False
        break
        
if is_palindrome :
    print("%s is palindrome" % text)
else :
    print("%s is NOT a palindrome" % text)