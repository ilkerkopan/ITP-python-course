magicians = ['alice', 'david', 'carolina', 'harun', 'ayse']
for magician in magicians:
    print("My favorite magician is "+magician.title())
    print("--------------------------")
print("list is over")
print()

# square numbers from 1 to 10
square_values=[]
for x in range(1,11):
    square_values.append(x**2)
print(square_values)
# getting a slice of list
first3_element=square_values[3:5]
print(first3_element)
    