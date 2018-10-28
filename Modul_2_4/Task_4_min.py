import random

l = 8
#  1) Створити програму сортування списку чисел методом злиття в порядку зростання
mixed_list = [random.randint(0, 30) for i in range(l)]

print('mixed list for merge sort', mixed_list)


def merge_up(left_list, right_list):
    rez_list = []
    left_index = 0
    right_index = 0
    while left_index <= len(left_list) - 1 and right_index <= len(right_list) - 1:
        if left_list[left_index] <= right_list[right_index]:
            rez_list.append(left_list[left_index])
            left_index += 1
        else:
            rez_list.append(right_list[right_index])
            right_index += 1
    rez_list.extend(left_list[left_index:])
    rez_list.extend(right_list[right_index:])
    return rez_list

def merge_sort(mixed_list):
    if len(mixed_list) >= 2:
        center = len(mixed_list)//2
        mixed_list = merge_up(merge_sort(mixed_list[:center]), merge_sort(mixed_list[center:]))
    return mixed_list


print('merge sort', merge_sort(mixed_list))

# 2) Створити програму сортування списку чисел методом злиття в порядку зростання

mixed_list = [random.randint(0, 30) for i in range(l)]

print('mixed list for merge down sort', mixed_list)

def merge_down(left_list, right_list):
    rez_list = []
    left_index = 0
    right_index = 0
    while left_index <= len(left_list) - 1 and right_index <= len(right_list) - 1:
        if left_list[left_index] >= right_list[right_index]:
            rez_list.append(left_list[left_index])
            left_index += 1
        else:
            rez_list.append(right_list[right_index])
            right_index += 1
    rez_list.extend(left_list[left_index:])
    rez_list.extend(right_list[right_index:])
    return rez_list

def merge_sort_down(mixed_list):
    if len(mixed_list) >= 2:
        center = len(mixed_list)//2
        mixed_list = merge_down(merge_sort_down(mixed_list[:center]), merge_sort_down(mixed_list[center:]))
    return mixed_list


print('merge sort down', merge_sort_down(mixed_list))

# 3) Створити програму, яка генерує посортований список чисел, де парні елементи
# списку діляться на 3, а непарні елементи діляться на 7. Вхідним параметром є N -
# число, до якого генерувати список.

number = int(input('Input a number '))

print(list(filter(lambda i: (i%3 == 0 and i%2 == 0) or (i%7 == 0 and i%2 != 0), range(number+1))))

# 4) Створити програму сортування списку чисел. Числа мають бути посортовані в
# зростаючому порядку спочатку непарні, а тоді парні числа. Для сортування
# використовувати алгоритм злиття.

mixed_list = [random.randint(0, 30) for i in range(l)]

print('mixed list for 4', mixed_list)


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


print('merge sort for 4', merge_sort_4(mixed_list))

#Створити програму сортування списку чисел методом швидкого сортування в сервісі Scratch

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
