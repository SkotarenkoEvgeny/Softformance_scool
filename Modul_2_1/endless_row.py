"""
Реалізувати програму для знаходження середнього арифметичного для довільної
кількості чисел.
"""

counter = 0
sum = 0
while True:
    a = input("Input a number (if you input 'stop', you get response) ")
    if a == 'stop':
        try:
            print('average =', sum/counter)
            break
        except ZeroDivisionError:
            print("Pleaze, enter a number ")
            continue
    else:
        sum += int(a)
        counter += 1