import random

# 1 Створити програму сортування списку чисел методом злиття в порядку зростання

mixed_list = random.sample(range(0, 100), 10)
print('mixed_list ', mixed_list)


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
    step = 1
    while step < len(mixed_list):
        rez_list = []
        iter = 0
        for i in range(len(mixed_list) // (step + 1)):
            left = iter + step
            right = iter + 2 * step
            if right > len(mixed_list):
                right = len(mixed_list)
            rez_list.extend(merge_up(mixed_list[iter:left], mixed_list[left:right]))
            iter = right
        step *= 2
        mixed_list = rez_list
    return mixed_list


print('Sorted list # 1 ', merge_sort(mixed_list))


# 2 Створити програму сортування списку чисел методом злиття (рекурсивно) в
# порядку спадання

def merge_sort_recursion(mixed_list):
    if len(mixed_list) >= 2:
        mixed_list = merge_up(merge_sort_recursion(mixed_list[:len(mixed_list) // 2]),
                              merge_sort_recursion(mixed_list[len(mixed_list) // 2:]))
    return mixed_list


print('Sorted list recursion', merge_sort_recursion(mixed_list))

# 3 Створити програму, яка генерує посортований список чисел, де парні елементи
# списку діляться на 3, а непарні елементи діляться на 5. Вхідним параметром є N -
# число, до якого генерувати список.


print(list(
    filter(lambda x: (x % 3 == 0 and x % 2 == 0) or (x % 2 != 0 and x % 5 == 0),
           range(int(input('Input N for # 3')) + 1))))

# 4 Створити програму яка поверне заданий список в зворотному порядку. Реалізувати
# рішення використовуючи рекурсію.

mixed_list = random.sample(range(0, 100), 6)
print('mixed_list for reverse ', mixed_list)


def reverse_recursion(mixed_list, iter=1):
    if len(mixed_list) // 2 >= iter:
        mixed_list[iter - 1], mixed_list[len(mixed_list) - iter] = mixed_list[len(mixed_list) - iter], mixed_list[
            iter - 1]
        return reverse_recursion(mixed_list, iter + 1)
    else:
        return mixed_list


print('reverse mixed list', reverse_recursion(mixed_list))


# 5 Створити програму для генерування послідовності Фібоначчі для числа N
# рекурсивно

def fib(n, fib_list=[0, 1]):
    if fib_list[-1] < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib(n, fib_list)
    else:
        return fib_list[:-1]  # if the last fibonachi number most be less N


print('Fibonachi list', fib(int(input('N for Fibonachi '))))
