

# print(print(1), print(2))

print('hello')
print(print('hello'))

hello = print('hello')
print(hello)

from operator import mul

def square(x):
    return mul( x, x )

print(square(5))

a = 1
b = 2
b, a = a+b, b

print(f'a is: {a}, b is {b}')

def pressure(v, t, n):
        """Compute the pressure in pascals of an ideal gas.

        Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v
    
help(pressure)