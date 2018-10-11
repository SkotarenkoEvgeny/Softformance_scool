"""
Реалізувати програму для знаходження середнього арифметичного для довільної
кількості чисел.
"""


i = int(input('Input a number '))


def fib_simple(i):

    try:
        assert i >0
        list_fib = []
        f1, f2 = 0, 1
        for i in range(i-1):
            f1, f2 = f2, f1+f2
            list_fib.append(f1)
    except AssertionError:
        list_fib = 'number most >0'

    return list_fib

print(fib_simple(i))
