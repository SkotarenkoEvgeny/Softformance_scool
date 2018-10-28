import random

# 1 Створити програму в середовищі Scratch для знаходження найбільшого спільного
# дільника для двох чисел A, B. Числа задаються користувачем (алгоритм Евкліда)

a, b= map(int, input('a b = ').split())

def ncd(a, b):
    if b == 0:
        return a
    while b !=0:
        if a>b:
            a -=b
        else:
            b -=a
    return a

print('найбільший спільний дільник', ncd(a, b))

# 2 Написати програму в сервісі Scratch яка сортує список довільних чисел за частотою
# входження у спадному порядку. Наприклад, маємо список [ 4, 3, 7, 4, 3, 4, 2, 7, 5, 4,
# 5, 7] і повинні отримати [4, 4, 4, 4, 7, 7, 7, 5, 5, 3, 3, 2]

mixed_list = [ 4, 3, 7, 4, 3, 4, 2, 7, 5, 4, 5, 7]

def sort_by_amount(mixed_list):
    dict = {}
    list_rez = []
    for i in mixed_list:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
    for j in sorted(dict.items(), key=lambda x: x[1], reverse=True):
        for f in range(j[1]):
            list_rez.append(j[0])
    return list_rez

print('сортування по частоті ', sort_by_amount(mixed_list))

# 3 Написати програму в сервісі Scratch яка генерує список довжини n та порахує
# скільки інверсій є в генерованому списку. Два елементи списку формують інверсію
# якщо a[i] > a[j] та i < j.

n = 10

mixed_list = [random.randint(0, 30) for i in range(n)]
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

# Написати програму я в посортованому списку знайде пару елементів сума яких
# буде найблищою до заданого числа n. Наприклад: [4,18,30,44,57], n = 65, пара (18,
# 44)

mixed_list = [random.randint(0, 30) for i in range(n)]
print('Список для пошуку суми ', mixed_list)
number = int(input('введіть число для пошуку максимального зближення'))

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