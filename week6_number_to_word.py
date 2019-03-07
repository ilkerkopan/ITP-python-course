# week 6 number to words
numbers = {0:"zero",
          1:"one",
          2:"two",
          3:"three",
          4:"four",
          5:"five",
          6:"six",
          7:"seven",
          8:"eight",
          9:"nine",
          10:"ten",
          11:"eleven",
          12:"twelve",
          13:"thirteen",
          14:"fourteen",
          15:"fifteen",
          16:"sixteen",
          17:"seventeen",
          18:"eighteen",
          19:"nineteen",
          20:"twenty",
          30:"thirty",
          40:"fourty"
          
          }
my_number="549"

digit=int(my_number[0])
print(numbers[digit] + " hundred", end=' ')
digit = int(my_number[1])*10
print(numbers[digit], end=' ')
digit = int(my_number[2])
print(numbers[digit], end=' ')
