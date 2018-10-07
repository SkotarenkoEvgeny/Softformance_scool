"""
Реалізувати програму для знаходження середнього арифметичного для довільної
кількості чисел.
"""

x = int(input('Input a number '))
i = 2
f = True
list_rep = [2]
while i < x:
    i +=1
    for j in list_rep:
        if i//j > 1  and i%j == 0:
            f = False
    if f == True:
        list_rep.append(i)
    f = True
list_rep.insert(0,1)
print(list_rep)
