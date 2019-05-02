# Pythagorean Theorem find the type of a triangle
from math import sqrt

def find_triangle_type(side_lengths):
    side_lengths = sorted(side_lengths)
    hypotenuse = sqrt(side_lengths[0]**2 + side_lengths[1]**2)
    if side_lengths[-1] == hypotenuse :
        return "R"
    elif side_lengths[-1] > hypotenuse :
        return "O"
    else :
        return "A"

triangle_count = int(input("How many trangles you want to define: "))

for i in range(triangle_count):
    side_list = []
    side_list.append(int(input("input side 1: ")))
    side_list.append(int(input("input side 2: ")))
    side_list.append(int(input("input side 3: ")))

    print(f'Type of this triangle is: {find_triangle_type(side_list)}')
    