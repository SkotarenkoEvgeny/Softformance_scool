import random

# 1 Написати програму котра видалить усі дублікати з списку довжиною N

# mixed_list = [random.randint(0,20) for  i in range(20)]
mixed_list = [2, 3, 3, 4, 2]
print('mixed list', mixed_list)


def remove_double(mixed_list):
    rez_list = []
    for i in range(len(mixed_list)):
        if mixed_list[i] not in rez_list:
            rez_list.append(mixed_list[i])
    return rez_list


print('remove double from mixed_list', remove_double(mixed_list))
print(set(mixed_list))  # variant 2

# 2 Написати програму яка знайде всі числа в діапазоні від 1500 до 3000
# включно, які діляться на 7 але не діляться на 3.
print(list(filter(lambda x: x % 7 == 0 and x % 3 != 0, [x for x in range(1500, 2001)])))

# 3 Задано два списки чисел довжиною N та M. Напсати програму котра
# створить список який міститиме числа які є спільними для обох заданих
# списків.

mixed_list_n = [random.randint(0, 20) for i in range(20)]
mixed_list_m = [random.randint(0, 20) for i in range(20)]

print('N ', mixed_list_n)
print('M ', mixed_list_m)


def double_number(mixed_list_n, mixed_list_m):
    rez_list = []
    for i in mixed_list_m:
        if i in mixed_list_n and i not in rez_list:
            rez_list.append(i)
    return rez_list


print('Double numbers is ', double_number(mixed_list_n, mixed_list_m))

# 4 Написати програму сортування списку чисел довжиною N використовуючи
# алгоритм сортування включенням

mixed_list = [random.randint(0, 30) for i in range(int(input('введіть довжину N ')))]
print('змішаний список довжиною N', mixed_list)


def insertion_sort(mixed_list):
    for i in range(len(mixed_list) - 1):
        left = i
        right = i + 1
        while left < len(mixed_list):
            if mixed_list[left] < mixed_list[right]:
                right = left
            left += 1
        mixed_list[i], mixed_list[right] = mixed_list[right], mixed_list[i]
    return mixed_list


print('сортування включенням ', insertion_sort(mixed_list))

# 5 Написати програму сортування списку чисел довжиною N використовуючи
# алгоритм сортування включенням у зворотньому порядку.

mixed_list = [random.randint(0, 30) for i in range(int(input('введіть довжину N ')))]
print('змішаний список довжиною N реверс', mixed_list)


def insertion_sort(mixed_list):
    for i in range(len(mixed_list) - 1):
        left = i
        right = i + 1
        while left < len(mixed_list):
            if mixed_list[left] > mixed_list[right]:
                right = left
            left += 1
        mixed_list[i], mixed_list[right] = mixed_list[right], mixed_list[i]
    return mixed_list


print('сортування включенням реверс', insertion_sort(mixed_list))

# 6 Модифікувати алгоритм обміну таким чином щоб перша частина
# посортованого списку складалась з парних чисел а друга з непарних.
# Приклад: [ 5, 1, 7, 3, 2, 4, 0, 8, 9] повинні отримати [0, 2, 4, 8, 1, 3, 5, 7, 9]

mixed_list = [random.randint(0, 30) for i in range(9)]
print('змішаний список для 6', mixed_list)

def change(mixed_list):
    for i in range(len(mixed_list)):
        for j in range(len(mixed_list) - 1):
            if mixed_list[j] % 2 == mixed_list[j + 1] % 2 and mixed_list[j] > mixed_list[j + 1]:
                mixed_list[j], mixed_list[j + 1] = mixed_list[j + 1], mixed_list[j]
            elif mixed_list[j] % 2 != 0 and mixed_list[j + 1] % 2 == 0:
                mixed_list[j], mixed_list[j + 1] = mixed_list[j + 1], mixed_list[j]
    return mixed_list

print('sorted list for task 6', change(mixed_list))
