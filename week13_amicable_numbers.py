# find Amicable numbers

def sum_of_proper_divisors(number):
    sum_of_divisors = 0
    for i in range(1,number):
        if (number % i) == 0:
            sum_of_divisors += i
    return sum_of_divisors

numbers = list(range(1,10000))
for i in numbers:
    sum1 = sum_of_proper_divisors(i)
    sum2 = sum_of_proper_divisors(sum1)
    if i==sum2 and i!=sum1:
        print(f'{i} is an amicable number with {sum1}')
        numbers.remove(sum1)