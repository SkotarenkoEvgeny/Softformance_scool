import random

# 1 Написати програму яка рекурсивно перевірить чи заданий список чисел є
# посортовано.

mixed_list = [1, 2, 3, 4]  # sorted


# mixed_list = [1, 2, 3, 4] # not sorted

def direction(start, next):
    if start <= next:
        return True
    else:
        return False


def sorted_test(mixed_list, flag=None):
    while len(mixed_list) >= 2:
        value = direction(mixed_list[0], mixed_list[1])
        if value == flag or flag == None:
            return sorted_test(mixed_list[1:], value)
        else:
            return 'not sorted'
    return 'sorted'


print(sorted_test(mixed_list))

# 2 Написати програму яка отримує від користувача стрічку, рахує скільки разів
# зустрічається те чи інше слово та виводить результат у постортованому порядку.
# Наприклад, користувач задав стрічку: Hello, my name is Taras. yes, yes, Taras.
# Taras has 5 letters! Результат - це список: [5:1, Hello:1, Taras:3, has:1, is:1, letters:1,
# my:1, name:1, yes:2]

text = 'Hello, my name is Taras. yes, yes, Taras. Taras has 5 letters!'
text_list = list(filter(lambda x: x != '', [i.strip(',.$;?!') for i in text.split()]))

# var 1

rez_list = []
for i in set(text_list):
    rez_list.append(i + ':' + str(text_list.count(i)))
print('Task 2. The list according to example ', rez_list)

# var 2

rez_dict = dict.fromkeys(set(text_list), 0)
for i in rez_dict.keys():
    rez_dict[i] = text_list.count(i)
rez_list_1 = []
for i in sorted(rez_dict.items(), key=lambda x: x[1], reverse=True):
    rez_list_1.append(i[0] + ':' + str(i[1]))
print('Task 2. The list sorted by frequency ', rez_list_1)

# 3 Створити програму сортування списку чисел методом швидкого сортування в
# порядку зростання

mixed_list = random.sample(range(0, 100), 10)
print('mixed list for # 3', mixed_list)


def quik_sort_1(mixed_list):
    for j in mixed_list:
        pivot = j
        less = []
        equail = []
        greater = []
        for i in mixed_list:
            less = [i for i in mixed_list if i < pivot]
            equail = [i for i in mixed_list if i == pivot]
            greater = [i for i in mixed_list if i > pivot]
        mixed_list = less + equail + greater
    return mixed_list


print('quik sort # 3', quik_sort_1(mixed_list))

# 4 Створити програму сортування списку чисел методом швидкого сортування
# (рекурсивно) в порядку спадання

mixed_list = [random.randint(0, 30) for i in range(10)]

print('mixed list for quik sort reverse', mixed_list)


def quik_sort(mixed_list):
    if len(mixed_list) <= 1:
        return mixed_list
    else:
        pivot = random.choice(mixed_list)
        less = [i for i in mixed_list if i > pivot]
        equail = [i for i in mixed_list if i == pivot]
        greater = [i for i in mixed_list if i < pivot]
        return quik_sort(less) + equail + quik_sort(greater)


print('quik sort reverse', quik_sort(mixed_list))
