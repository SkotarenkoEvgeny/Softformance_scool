"""
Реалізувати програму для розв’язку квадратного рівняння.
"""

from math import sqrt
# ax**2 + bx+c = 0

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + sqrt(d))/(2*a)
    x2 = (-b - sqrt(d))/(2*a)
    print('x1 =', x1, 'x2 =', x2)
elif d == 0:
    x = -(b/(2*a))
    print('x1, x2 =', x)
else:
    print('not solutions')