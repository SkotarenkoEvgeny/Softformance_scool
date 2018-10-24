import random

l = 10

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

def sort_by_choice_reverse(mixed_list):
    '''
    :param mixed_list:
    :return: сортування списку чисел методом вибору реверсивне
    '''
    min = mixed_list[0]
    k = 0
    while k < len(mixed_list) - 1:
        for i in range(k, len(mixed_list)):
            if mixed_list[i] >= min:
                min = mixed_list[i]
                temp_i = i
        temp = mixed_list[k]
        mixed_list[k] = min
        mixed_list[temp_i] = temp
        k += 1
        min = mixed_list[k]
    return mixed_list


print('List sorted by choice reverse ', sort_by_choice_reverse(mixed_list))

n = 10


def random_fibonachi(n):
    '''
    :param n:
    :return: create random fibonachi list
    '''
    assert n > 0
    list_fib = []
    f1, f2 = 0, 1
    for i in range(n * 5 - 1):
        f1, f2 = f2, f1 + f2
        list_fib.append(f1)
    mixed_fibonachi_list = [int(list_fib[random.randint(0, n * 5 - 2)]) for j in range(n)]
    return mixed_fibonachi_list


random_fibonachi_list = random_fibonachi(n)
print ('Random fibonachi list ', random_fibonachi_list)
print('Sorted fibonachi list ', sort_by_choice(random_fibonachi_list))

mixed_list = [random.randint(0, 30) for i in range(l)]

print('mixed list (відмінний від алгоритму сортування обміном)', mixed_list)


def sort_by_choice_even(mixed_list):
    '''
    :param mixed_list:
    :return: Придумати власний алгоритм сортування (відмінний від алгоритму сортування
обміном) таким чином щоб перша частина посортованого списку складалась з
парних чисел а друга з непарних. Приклад: [ 5, 1, 7, 3, 2, 4, 0, 8, 9] повинні отримати
[0, 2, 4, 8, 1, 3, 5, 7, 9]
    '''

    left = 0
    right = len(mixed_list) - 1
    k = 0
    while right - left > 0:
        # print('l=', left, 'r=', right, 'k=', k)
        # print('start ', mixed_list[left:right + 1])
        max = 0
        if mixed_list[left] % 2 == 0:
            min = mixed_list[left]
            i_min = left
            for i in range(left, right + 1):
                if mixed_list[i] < min and mixed_list[i] % 2 == 0:
                    min = mixed_list[i]
                    i_min = i
            mixed_list[left], mixed_list[i_min] = mixed_list[i_min], mixed_list[left]
            left += 1
        elif mixed_list[left] % 2 != 0:
            for i in range(left, right + 1):
                if mixed_list[i] >= max and mixed_list[i] % 2 != 0:
                    max = mixed_list[i]
                    i_max = i
            mixed_list[right], mixed_list[i_max] = mixed_list[i_max], mixed_list[right]
            right -= 1
        # print('finish  ', mixed_list)
        k += 1

    return mixed_list


print('List sorted by choice (відмінний від алгоритму сортування обміном)', sort_by_choice_even(mixed_list))

sorted_list = sorted([random.randint(0, 30) for i in range(l)])
print('sorted list ', sorted_list)

number = int(input('Inpet a number 0-30 '))


def binary_search(number, sorted_list):
    center = int((len(sorted_list)) / 2)
    if number > sorted_list[len(sorted_list) - 1] or number < sorted_list[0]:
        return False
    elif sorted_list[center] < number:
        return binary_search(number, sorted_list[center:])
    elif sorted_list[center] > number:
        return binary_search(number, sorted_list[:center])
    else:
        return True


print(binary_search(number, sorted_list))
