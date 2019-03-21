# print input string until input is 'quit'
active_flag=True

while active_flag:
    user_input=input("Enter a word: ")
    print(user_input)
    active_flag = user_input.lower() != "quit"
    
