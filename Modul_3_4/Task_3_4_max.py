import random

# 1 Написати алгоритм сортування методом швидкого сортування. Елемент розбиття
# вибирати довільно.

mixed_list = [random.randint(0, 30) for i in range(10)]

print('mixed list for quik sort reverce', mixed_list)


def quik_sort_reverce(mixed_list):
    if len(mixed_list) <= 1:
        return mixed_list
    else:
        pivot = random.choice(mixed_list)
        less = [i for i in mixed_list if i > pivot]
        equail = [i for i in mixed_list if i == pivot]
        greater = [i for i in mixed_list if i < pivot]
        return quik_sort_reverce(greater) + equail + quik_sort_reverce(less)


print('quik sort', quik_sort_reverce(mixed_list))

# 2 Написати програму, яка в посортованому списку знайде пару елементів сума яких
# буде найблищою до заданого числа n. Наприклад: [4,18,30,44,57], n = 65, пара (18,
# 44)

mixed_list = [random.randint(0, 30) for i in range(10)]
print('Список для пошуку суми ', mixed_list)
number = int(input('введіть число для пошуку максимального зближення '))


def max_convergence(mixed_list, number):
    temp_number = mixed_list[0] + mixed_list[1]
    for i in range(len(mixed_list)):
        for j in range(i + 1, len(mixed_list)):
            temp = mixed_list[i] + mixed_list[j]
            if abs(number - temp) <= abs(number - temp_number):
                number_1 = mixed_list[i]
                number_2 = mixed_list[j]
                temp_number = temp
    print(number_1, number_2)


max_convergence(mixed_list, number)

# 3 Задано список цифр (0-9) довільної довжини. Знайти найменшу суму двох чисел які
# сформовані з списку цифр. Наприклад: [4, 3, 8, 6, 1] сума - 184 (148 + 36)

list_for_search = [4, 3, 8, 6, 1]
number = 184


def find_min(list_for_search):
    min = list_for_search[0]
    for i in range(1, len(list_for_search)):
        if list_for_search[i] < min:
            min = list_for_search[i]
    return min


def min_sum_two_numbers(list_for_search):
    long_first = len(list_for_search) % 2 + len(list_for_search) // 2
    long_second = len(list_for_search) // 2
    flag = True
    first_number = 0
    second_number = 0

    while len(list_for_search) > 0:
        if flag == True:
            temp = find_min(list_for_search)
            list_for_search.remove(temp)
            first_number += temp * 10 ** (long_first - 1)
            long_first -= 1
        elif flag == False:
            temp = find_min(list_for_search)
            list_for_search.remove(temp)
            second_number += temp * 10 ** (long_second - 1)
            long_second -= 1
        if flag == True:
            flag = False
        elif flag == False:
            flag = True
    return first_number + second_number


print('# 3 Min summ two numbers is ', min_sum_two_numbers(list_for_search))

# 4 Розібрати алгоритм сортування пірамідою та написати програму яка сортує список
# чисел методом піраміди.

test_list = [random.randint(0, 30) for i in range(10)]

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

print(heapSort(test_list))