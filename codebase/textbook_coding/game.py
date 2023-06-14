
def square(n):
    """
    Returns the square of a number.

    >>> square(2)
    4
    >>> square(-3)
    9
    """
    return n ** 2

def greet(name):
    """
    Greets a person by their name.

    >>> greet("Alice")
    'Hello, Alice!'
    >>> greet("Bob")
    'Hello, Bob!'
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)



# def fib(n):
#     """Compute the nth Fibonacci number, for n >= 2."""
#     pred, curr = 0, 1   # Fibonacci numbers 1 and 2
#     k = 2               # Which Fib number is curr?
#     while k < n:
#         pred, curr = curr, pred + curr
#         k = k + 1
#     return curr

# result = fib(8)

# print(f'assert fib(8) == 13 ')



# result = []

# print(bool([]))

# x = [] == []
# if x:
#     print(f'{x} True')
# else:
#     print(f'{x} is False')


# # print(print(1), print(2))

# print('hello')
# print(print('hello'))

# hello = print('hello')
# print(hello)

# from operator import mul

# def square(x):
#     return mul( x, x )

# print(square(5))

# a = 1
# b = 2
# b, a = a+b, b

# print(f'a is: {a}, b is {b}')

# # def pressure(v, t, n):
# #         """Compute the pressure in pascals of an ideal gas.

# #         Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

# #         v -- volume of gas, in cubic meters
# #         t -- absolute temperature in degrees kelvin
# #         n -- particles of gas
# #         """
# #         k = 1.38e-23  # Boltzmann's constant
# #         return n * k * t / v
    
# # help(pressure)

# def absolute_value(x):
#     """Compute abs(x)."""
#     if x > 0:
#         return x
#     elif x == 0:
#         return 0
#     else:
#         return -x

# result = absolute_value(-2)

# # help(absolute_value)

# print('bool(0) is: ', bool(0)) # bool(0) is:  False
# print('bool(False) is: ', bool(False)) # bool(False) is:  False
# print('bool(None) is: ', bool(None)) # bool(None) is:  False
# print('bool("") is: ', bool("")) # bool("") is:  False
# print('bool([]) is: ', bool([])) # bool([]) is:  False
# print('bool({}) is: ', bool({})) # bool({}) is:  False

# print (f" '' == '' is: { '' == '' }") # '' == '' is: True
# print (f" [] == [] is: { [] == [] }") # [] == [] is: True
# # print (f" {} == {} is: { {} == {} }") #  SyntaxError: f-string: empty expression not allowed
# print (" {} == {} is:", {} == {} ) # {} == {} is: True