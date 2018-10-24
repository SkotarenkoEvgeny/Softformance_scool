import random

l = 10

mixed_list = [random.randint(0, 30) for i in range(l)]
'''
Написати програму в середовищі Scratch яка знайде перше число яке
повторюється в масиві довільних чисел.
'''
print('mixed_list = ', mixed_list)
flag = False
for i in range(len(mixed_list) - 1):
    if mixed_list[i] in mixed_list[i + 1:]:
        flag = True
        rez = mixed_list[i]
        break
if flag == True:
    print(rez, 'in mixed list')
else:
    print('Not found')


def insertion_sort(mixed_list):
    '''
    :param mixed_list:
    :return: Створити програму сортування списку чисел методом включення
    '''

    for i in range(len(mixed_list) - 1):
        left = i
        right = i + 1
        while left < len(mixed_list):
            if mixed_list[left] < mixed_list[right]:
                right = left
            left += 1
        temp = mixed_list[i]
        mixed_list[i], mixed_list[right] = mixed_list[right], mixed_list[i]
    return mixed_list


print('сортування включенням ', insertion_sort(mixed_list))

mixed_list = [random.randint(0, 30) for i in range(l)]
print('несортований рядок для функції сортування включенням (оприміованого)', mixed_list)

def change_optimisation(mixed_list):
    '''
    :param mixed_list:
    :return: Створити програму сортування списку чисел методом включення враховуючи зміну
(оптимізацію)
    '''

    for i in range(1, len(mixed_list)):
        if mixed_list[i] < mixed_list[i-1]:
            t = i
            while mixed_list[t] < mixed_list[t-1] and t > 0:
                mixed_list[t], mixed_list[t - 1] = mixed_list[t - 1], mixed_list[t]
                t-=1
    return mixed_list

print('сортування включенням (оптимізоване)', change_optimisation(mixed_list))

mixed_list = [random.randint(0, 30) for i in range(l)]
print('несортований рядок для функції реверсивного сортування ', mixed_list)


def insertion_sort(mixed_list):
    '''
    :param mixed_list:
    :return: Створити програму сортування списку чисел методом включення в реверсному
порядку.

    '''

    for i in range(len(mixed_list) - 1):
        left = i
        right = i + 1
        while left < len(mixed_list):
            if mixed_list[left] > mixed_list[right]:
                right = left
            left += 1
        temp = mixed_list[i]
        mixed_list[i], mixed_list[right] = mixed_list[right], mixed_list[i]
    return mixed_list


print('сортування включенням реверсивне', insertion_sort(mixed_list))

n = 19


def list_3_5(n):
    '''
    :param n:
    :return: Створити програму яка генерує список чисел від 1 до n де кожне число має дільник
3 або 5. Наприклад якщо n = 19 матимемо список [3, 5, 6, 9, 10, 12, 15, 18]
    '''
    rez = []
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            rez.append(i)
    return rez


print('дільник 3 або 5 ', list_3_5(n))
