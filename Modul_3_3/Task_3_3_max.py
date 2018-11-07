import random

# 1 Створити програму для обчислення n! рекурсивно

def fokterial(n, rez = 1, step = 1):
    if step <= n:
        rez *= n
        step += 1
        return fokterial(n, rez, step)
    return rez
print('fokterial N is ', fokterial(int(input('input N for fokterial '))))

# 2 Створити програму сортування списку чисел. Числа мають бути посортовані в
# зростаючому порядку спочатку непарні, а тоді парні числа. Для сортування
# використовувати алгоритм злиття.

mixed_list = [random.randint(0, 30) for i in range(10)]

print('mixed list for 2', mixed_list)


def merge_4(left_list, right_list):
    rez_list = []
    not_even_number = 0
    half = 0
    while left_list and right_list:
        if left_list[0]%2 != 0:
            i = 0
            flag = False
            while i<len(right_list):
                if right_list[i]%2 !=0:
                    break
                else:
                    flag = True
                i +=1
            if flag == True:
                rez_list.append(left_list[0])
                left_list.pop(0)
            elif left_list[0] <= right_list[i] and flag == False:
                rez_list.insert(half, left_list[0])
                left_list.pop(0)
            else:
                rez_list.insert(half, right_list[i])
                del right_list[i]
            half += 1
        else:
            i = 0
            flag = False
            while i < len(right_list):
                if right_list[i] % 2 == 0:
                    break
                else:
                    flag = True
                i += 1
            if flag == True:
                rez_list.append(right_list[0])
                right_list.pop(0)
            elif left_list[0] <= right_list[i] and flag == False:
                rez_list.append(left_list[0])
                left_list.pop(0)
            else:
                rez_list.append(right_list[i])
                right_list.pop(i)
    rez_list.extend(left_list)
    rez_list.extend(right_list)
    return rez_list

def merge_sort_4(mixed_list):
    if len(mixed_list) >= 2:
        center = len(mixed_list)//2
        mixed_list = merge_4(merge_sort_4(mixed_list[:center]), merge_sort_4(mixed_list[center:]))
    return mixed_list


print('merge sort for 2', merge_sort_4(mixed_list))

# 3 Написати програму, яка сортує список чисел у вигляді хвиль. Мається на увазі
# список, для якого правдива така умова a1 >= a2 <= a3 >= a4 < = ...

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

# 4 Створити програму сортування списку чисел. Спочатку парні числа в порядку
# спадання а тоді непарні числа в порядку зростання. Для сортування
# використовувати алгоритм швидкого сортування.

mixed_list = random.sample(range(0, 100), 10)
print('mixed list for # 4', mixed_list)

def quik_sort_1(mixed_list):
    for j in mixed_list:
        pivot = j
        less = []
        equail = []
        greater = []
        if pivot % 2 == 0:
            for i in mixed_list:
                if i % 2 == 0 and i > pivot:
                    less.append(i)
                elif i == pivot:
                    equail.append(i)
                else:
                    greater.append(i)
        else:
            for i in mixed_list:
                if i % 2 != 0 and i > pivot:
                    greater.append(i)
                elif i == pivot:
                    equail.append(i)
                else:
                    less.append(i)
        mixed_list = less + equail + greater
    return mixed_list

print('quik sort # 4', quik_sort_1(mixed_list))

# 5 Написати програму яка знаходить медіану двох посортованих списків довжини N та
# M.

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