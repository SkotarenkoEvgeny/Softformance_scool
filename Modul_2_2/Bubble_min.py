import random

l = 10

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


def reverse_buble(mixed_list):
    '''
    :param mixed_list:
    :return: Створити програму сортування списку чисел методом обміну у реверсному порядку
    '''

    iter_value = 0
    for i in range(len(mixed_list)):
        for j in range(len(mixed_list) - 1):
            if mixed_list[j + 1] > mixed_list[j]:
                temp = mixed_list[j]
                mixed_list[j] = mixed_list[j + 1]
                mixed_list[j + 1] = temp
            iter_value += 1
    print('reverse iter ', iter_value)
    return mixed_list


print('sorted list (reverse)', reverse_buble(mixed_list))


def optimize_buble(mixed_list):
    '''
    :param mixed_list:
    :return: Створити програму сортування списку чисел методом обміну використовуючи
    оптимізований алгоритм
    '''

    iter_value = 0
    for i in range(len(mixed_list)):
        for j in range((len(mixed_list) - 1) - i):
            if mixed_list[j + 1] < mixed_list[j]:
                temp = mixed_list[j]
                mixed_list[j] = mixed_list[j + 1]
                mixed_list[j + 1] = temp
            iter_value += 1
    print('optimize iter ', iter_value)
    return mixed_list


print('sorted list (optimise)', optimize_buble(mixed_list))


def modif_buble(mixed_list):
    '''
    :param mixed_list:
    :return: перша частина посортованого
    списку складалась з парних чисел а друга з непарних.
    '''
    
    iter_value = 0
    for i in range(len(mixed_list)):

        for j in range(len(mixed_list) - 1):

            if mixed_list[j] % 2 != 0:
                temp = mixed_list[j]
                mixed_list[j] = mixed_list[j + 1]
                mixed_list[j + 1] = temp
            if mixed_list[j + 1] % 2 == mixed_list[j] % 2 and mixed_list[j + 1] < mixed_list[j]:
                    temp = mixed_list[j]
                    mixed_list[j] = mixed_list[j + 1]
                    mixed_list[j + 1] = temp
            iter_value += 1
    print('simple iter ', iter_value)
    return mixed_list


print('sorted list (modif)', modif_buble(mixed_list))
