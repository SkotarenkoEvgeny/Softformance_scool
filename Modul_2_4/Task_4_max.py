import random

l = 10

# 1 Створити програму сортування списку чисел методом швидкого сортування в
# зворотньому порядку

mixed_list = [random.randint(0, 30) for i in range(l)]

print('mixed list for quik sort reverce', mixed_list)

def quik_sort_reverce(mixed_list):
    if len(mixed_list) <= 1:
        return mixed_list
    else:
        pivot = random.choice(mixed_list)
        less = [i for i in mixed_list if i < pivot]
        equail = [i for i in mixed_list if i == pivot]
        greater = [i for i in mixed_list if i > pivot]
        return quik_sort_reverce(greater)+equail+quik_sort_reverce(less)


print('quik sort', quik_sort_reverce(mixed_list))

# 2 Написати програму в середовищі Scratch, яка посортує список чисел у вигляді
# хвиль. Мається на увазі список, для якого правдива така умова a1 >= a2 <= a3 >=
# a4 < = ...
mixed_list = [random.randint(0, 30) for i in range(l)]

print('mixed list for vave sort', mixed_list)

def vave(mixed_list):
    for i in range(1, len(mixed_list),3):
        if mixed_list[i-1]<=mixed_list[i]<=mixed_list[i-1]:
            mixed_list[i - 1], mixed_list[i] = mixed_list[i],mixed_list[i-1]
        elif mixed_list[i-1]>=mixed_list[i]>=mixed_list[i-1]:
            mixed_list[i - 1], mixed_list[i] = mixed_list[i],mixed_list[i-1]

print('mixed list vave sort', vave(mixed_list))

# 3 Створити програму сортування списку чисел використовуючи алгоритм швидкого
#сортування. Реалізувати алгоритм таким чином щоб опорний елемент (той який
#розбиває список) вибирався випадковим чином.

'''
виконано в попередніх сортуваннях
'''
mixed_list = [random.randint(0, 30) for i in range(l)]

print('mixed list for quik sort', mixed_list)

def quik_sort(mixed_list):
    if len(mixed_list) <= 1:
        return mixed_list
    else:
        pivot = random.choice(mixed_list)
        less = [i for i in mixed_list if i < pivot]
        equail = [i for i in mixed_list if i == pivot]
        greater = [i for i in mixed_list if i > pivot]
        return quik_sort(less)+equail+quik_sort(greater)


print('quik sort', quik_sort(mixed_list))

# 4 Створити програму сортування списку чисел. Спочатку парні числа в порядку
#спадання а тоді непарні числа в порядку зростання. Для сортування
#використовувати алгоритм швидкого сортування.
mixed_list = [random.randint(0, 30) for i in range(l)]

print('mixed list for quik sort reverce', mixed_list)

def quik_sort_reverce(mixed_list):
    if len(mixed_list) <= 1:
        return mixed_list
    else:
        pivot = random.choice(mixed_list)
        less = [i for i in mixed_list if i < pivot]
        equail = [i for i in mixed_list if i == pivot]
        greater = [i for i in mixed_list if i > pivot]
        return quik_sort_reverce(greater)+equail+quik_sort_reverce(less)


print('quik sort', quik_sort_reverce(mixed_list))

# 5 Написати програму в середовищі Scratch яка знаходить медіану двох посортованих
# списків довжини N та M.

M = 10
N = 4
mixed_list_m = [random.randint(0, 50) for i in range(M)]
mixed_list_n = [random.randint(0, 50) for i in range(N)]
print('M = {} '.format(M), mixed_list_m)
print('N = {} '.format(N), mixed_list_n)

def mediana(mixed_list_m, mixed_list_n):
    rez_list = mixed_list_m + mixed_list_n
    rez_list.sort()
    if len(rez_list) % 2 != 0:
        return(rez_list[len(rez_list) // 2])
    else:
        return((rez_list[len(rez_list) // 2] + rez_list[len(rez_list) // 2 - 1]) / 2)