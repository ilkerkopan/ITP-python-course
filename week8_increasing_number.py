# function that tests a number is increasing or not
def is_increasing_number(number):
    while number > 10:
        last=number % 10
        previous = (number //10) % 10
        if last >= previous :
            is_increasing = True
        else :
            is_increasing = False
            break
        number = number //10
    return is_increasing

print(is_increasing_number(12345555567899999))
        