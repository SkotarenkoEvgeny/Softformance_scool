import random

l = 10

mixed_list = [random.randint(0, 30) for i in range(l)]

print('mixed list ', mixed_list)

def sort_by_choice (mixed_list):
    '''
    :param mixed_list:
    :return: сортування списку чисел методом вибору
    '''

    k = 0
    while k < len(mixed_list):
        min = mixed_list[k]
        for i in range(k, len(mixed_list)):
            if mixed_list[i] < min:
                min = mixed_list[i]
                temp_i = i
        temp = mixed_list[k]
        mixed_list[k] = min
        mixed_list[temp_i] = temp
        k+=1
    return mixed_list

print('List sorted by choice ', sort_by_choice(mixed_list))

def sort_by_choice_reverse (mixed_list):
    '''
    :param mixed_list:
    :return: сортування списку чисел методом вибору
    '''

    k = 0
    while k < len(mixed_list):
        max = mixed_list[k]
        for i in range(k, len(mixed_list)):
            if mixed_list[i] > max:
                max = mixed_list[i]
                temp_i = i
        temp = mixed_list[k]
        mixed_list[k] = max
        mixed_list[temp_i] = temp
        k+=1
    return mixed_list

print('List sorted by choice reverse ', sort_by_choice_reverse(mixed_list))

tt = 10

def random_fibonachi(n):
    '''
    :param n:
    :return: create random fibonachi list
    '''
    assert n > 0
    list_fib = []
    f1, f2 = 0, 1
    for i in range(n*5 - 1):
        f1, f2 = f2, f1 + f2
        list_fib.append(f1)
    mixed_fibonachi_list = [list_fib[random.randint(0, n*5-1)] for j in range(n)]
    return mixed_fibonachi_list

print ('Random fibonachi list ', random_fibonachi(tt))
g = random_fibonachi(tt)
print('Sorted fibonachi list ', sort_by_choice(g))


