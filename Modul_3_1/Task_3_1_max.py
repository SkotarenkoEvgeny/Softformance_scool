import random
# 1 Створити програму для вгадування числа. Програма запитує користувача число,
# яке він повинен відгадати. Якщо користувач відповів не вірно, програма виводить
# підказку, повідомляє чи число є більшим чи меншим за те, яке потрібно вгадати і
# запитує ще раз. Програма повинна працювати доки користувач не введе вірну
# відповідь.

def game():
    number = random.randint(0, 100)
    print(number)
    atempt = 5
    while atempt > 0:
        response = int(input('Input a number '))
        if response > number:
            print('need less')
        elif response < number:
            print('nees more')
        else:
            print('you win')
            break
        atempt -= 1
        if atempt == 0:
            print('you loose')
    print('game over')

#game()


# 2 Створити програму яка згенерує послідовність Фібоначчі для заданого числа N

n = 20

def fib(n, i =0, list = [0, 1]):
    if list[i+1] >= n:
        return list
    else:
        list.append(list[i]+list[i+1])
        i += 1
        return fib(n, i, list)
print(fib(n))


# 3 Реалізувати алгоритм сортування обміном.
mixed_list = [random.randint(0, 30) for i in range(l)]
print('mixed list ', mixed_list)

def simple_buble(mixed_list):
    '''
    :param mixed_list:
    :return: Створити програму сортування списку чисел методом обміну в сервісі scratch.
    '''

    iter_value = 0
    for i in range(len(mixed_list)):
        for j in range(len(mixed_list) - 1):
            if mixed_list[j + 1] < mixed_list[j]:
                temp = mixed_list[j]
                mixed_list[j] = mixed_list[j + 1]
                mixed_list[j + 1] = temp
            iter_value += 1
    print('simple iter ', iter_value)
    return mixed_list


print('sorted list (simple)', simple_buble(mixed_list))
# 4 Реалізувати алгоритм сортування вибором.
mixed_list = [random.randint(0, 30) for i in range(l)]
print('mixed list ', mixed_list)

def sort_by_choice(mixed_list):
    '''
    :param mixed_list:
    :return: сортування списку чисел методом вибору
    '''
    k = 0
    min = mixed_list[0]
    while k < len(mixed_list) - 1:
        for i in range(k, len(mixed_list)):
            if mixed_list[i] <= min:
                min = mixed_list[i]
                temp_i = i
        temp = mixed_list[k]
        mixed_list[k] = min
        mixed_list[temp_i] = temp
        k += 1
        min = mixed_list[k]
    return mixed_list


print('List sorted by choice ', sort_by_choice(mixed_list))
# 5 Спробувати самостійно розібратись із алгоритмом обходження графа. Зокрема,
# методом обходу в ширину.
def search(dad, sonn, dl, vay=[]):
    vay = vay+[sonn]
    if dad == sonn:
        return "Yes"
    elif sonn not in dl.keys():
        return "No"
    shortkey = "No"
    for d in dl[sonn]:
        if d not in vay:
            new_search = search(dad, d, dl, vay=[])
            if new_search:
                if new_search == "Yes":
                    return "Yes"
                shortkey = new_search
    return shortkey


a = int(input())
dl = {}
for i in range(a):
    s = [f for f in input().split(" : ")]
    if len(s) == 1:
        dl[s[0]] = s[0]  # chek variants
    else:
        dl[s[0]] = s[1].split()
b = int(input())
for i in range(b):
    ansver = input().split()
    g = search(ansver[0], ansver[1], dl, vay=[])
    print(g)

'''
https://stepik.org/lesson/24462/step/7?unit=6768

завдання 
15
G : F
A
B : A
C : A
D : B C
E : D
F : D
X
Y : X A
Z : X
V : Z Y
W : V
Q : P 
Q : R
Q : S
9
A G
A Z
A W
X W
X QWE
A X
X X
1 1
Q

Відпвіді:
Yes
No
Yes
Yes
No
No
Yes
No
Yes
'''