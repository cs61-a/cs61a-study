# Call expressions
print(f"max(2, 3): {max(2, 3)}")
print(f"min(1, -2, 3, -4, 5): {min(1, -2, 3, -4, 5)}")
print(f"pow(100, 2): {pow(100, 2)}")
print(f"pow(2, 100): {pow(2, 100)}")

# Imports
from math import pi
print(f"pi * 71 / 223: {pi * 71 / 223}")
from math import sin
print(f"sin(pi/2): {sin(pi/2)}")

# Assignment
radius = 10
print(f"2 * radius: {2 * radius}")
area, circ = pi * radius * radius, 2 * pi * radius
print(f"area: {area}, circ: {circ}")
radius = 20

# Function values
max
max(3, 4)
f = max
f
f(3, 4)
max = 7
f(3, 4)
f(3, max)
f = 2
# f(3, 4)
__builtins__.max

# User-defined functions
from operator import add, mul

def square(x):
    return mul(x, x)

square(21)
square(add(2, 5))
square(square(3))

def sum_squares(x, y):
    return add(square(x), square(y))
sum_squares(3, 4)
sum_squares(5, 12)

# area function
def area():
    return pi * radius * radius
area()
radius = 20
area()
radius = 10
area()

# Name conflicts
def square(square):
    return mul(square, square)
square(4)


# create a list using list comprehension
# [expression for name in sequence if condition]
lst = [x * x for x in range(1, 7) if x % 2 == 0]

# print the list
print(lst)