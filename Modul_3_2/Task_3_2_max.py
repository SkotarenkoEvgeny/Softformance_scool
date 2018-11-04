import random


# 1 Створити програму сортування списку чисел Фібоначчі методом включення.
# Програма повинна генерувати список заданої довжини - n
# Кожен елемент списку це число вибране випадковим чином з послідовності
# Фібоначчі згенерованої для n * 5
# Далі програма сортує список чисел Фібоначчі методом включення

def fib(n, fib_list=[0, 1]):
    if fib_list[-1] >= 5 * n:
        return [fib_list[random.randint(0, len(fib_list) - 1)] for i in range(n)]
    else:
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib(n, fib_list)


fib_list = fib(6)
print(fib_list)


def insert_sort(fib_list):
    for i in range(len(fib_list) - 1):
        left = i
        right = i + 1
        while left < len(fib_list):
            if fib_list[left] < fib_list[right]:
                right = left
            left += 1
        fib_list[i], fib_list[right] = fib_list[right], fib_list[i]
    return fib_list


print(insert_sort(fib_list))

# 2 Написати програму для пошуку заданого елементу в згенерованому списку
# довжини n. Використати алгоритм бінарного пошуку.

n = 20
sample_list = random.sample(range(0, 100), n)
sample_list.sort()
print('sample list', sample_list)


def binary_search(sample_list, number):
    center = int(len(sample_list) / 2)
    if number < sample_list[0] or number > sample_list[len(sample_list) - 1]:
        return '{} not in sample list'.format(number)
    elif number > sample_list[center]:
        return binary_search(sample_list[center:], number)
    elif number < sample_list[center]:
        return binary_search(sample_list[:center], number)
    else:
        return '{} in sample list'.format(number)


print(binary_search(sample_list, int(input('enter a number '))))

# 3 Створити програму для знаходження найбільшого спільного дільника для двох
# чисел A, B. Числа задаються користувачем (алгоритм Евкліда)

a, b= map(int, input('a b = ').split())

def ncd(a, b):
    if b == 0:
        return a
    elif a > b:
        return ncd(b,a-b)
    else:
        return ncd(a, b-a)


print('найбільший спільний дільник', ncd(a, b))

# 4 Написати програму яка сортує список довільних чисел за частотою входження у
# спадному порядку. Наприклад, маємо список [ 4, 3, 7, 4, 3, 4, 2, 7, 5, 4, 5, 7] і повинні
# отримати [4, 4, 4, 4, 7, 7, 7, 5, 5, 3, 3, 2]

mixed_list = [4, 3, 7, 4, 3, 4, 2, 7, 5, 4, 5, 7]


def sort_by_frequence(mixed_list):
    cons_dict = {}
    list_rez = []
    for i in mixed_list:
        if i in cons_dict.keys():
            cons_dict[i] += 1
        else:
            cons_dict[i] = 1
    for j in sorted(cons_dict.items(), key=lambda x: x[1], reverse=True):
        for f in range(j[1]):
            list_rez.append(j[0])
    return list_rez


print('сортування по частоті ', sort_by_frequence(mixed_list))

# 5 Написати програму яка генерує список довжини n та порахує скільки інверсій є в
# генерованому списку. Два елементи списку формують інверсію якщо a[i] > a[j] та i
# < j.

n = 10

mixed_list = random.sample(range(0, 100), n)
print('Список для підрахунку інверсій ', mixed_list)

def inverce(mixed_list):
    rez = -1 #не враховуємо 1-й напрямок
    temp = None
    for i in range(len(mixed_list) - 1):
        if mixed_list[i] >= mixed_list[i + 1]:
            flag = False
        else:
            flag = True
        if (temp == None or temp == True and flag == False) or (temp == None or temp == False and flag == True):
            rez += 1
        temp = flag
    return rez
print('Кількість інвесій ', inverce(mixed_list))

# 6 А тепер спробуйте реалізувати алгоритм обходження графа. Методом обходу в
# ширину. Тим методом, який ми просили вас розібрати в якості максимального
# домашнього завдання із попереднього уроку.

def search(dad, sonn, graf, vay=[]):
    vay = vay+[sonn]
    if dad == sonn:
        return "Yes"
    elif sonn not in graf.keys():
        return "No"
    shortkey = "No"
    for d in graf[sonn]:
        if d not in vay:
            new_search = search(dad, d, graf, vay=[])
            if new_search:
                if new_search == "Yes":
                    return "Yes"
                shortkey = new_search
    return shortkey

graf = {'G': ['F'], 'A': 'A', 'B': ['A'], 'C': ['A'], 'D': ['B', 'C'], 'E': ['D'], 'F': ['D'], 'X': 'X', 'Y': ['X', 'A'], 'Z': ['X'], 'V': ['Z', 'Y'], 'W': ['V'], 'Q': ['S']}
question =['A G', 'A Z', 'A W', 'X W', 'X QWE', 'A X', 'X X', '1 1']

for i in question:
    ansver = i.split()
    g = search(ansver[0], ansver[1], graf, vay=[])
    print(g)


