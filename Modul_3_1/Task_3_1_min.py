# 1 Створити програму яка запитує користувача яке його імя та, отримавши відповідь,
# привітається з ним.

name = input('Your name is {}'.format(input('Enter Your name ')))

# 2 Створити програму яка запитує користувача його імя та вік та, отримавши відповіді
# повідомить користувача коли йому виповниться 100 років.
[name,  adge] = input('name adge ').split(' ')
try: int(adge)
except ValueError:
    name, adge = adge, name
print('Dear {}. After {} years you have 100 years old'.format(name, (100 - int(adge))))

# 3 Створити програму яка запитує користувача число та, отримавши відповідь виведе
# # чи це число є парним чи ні.

x = lambda x:"odd" if x%2!= 0 else "even"
print(x(int(input('Enter a number '))))

# 4 Створити програму яка запитує користувача слово та, отримавши відповідь,
# повідомить користувача чи це слово є паліндром чи ні.

x = lambda word:"polindrom" if word == word[::-1] else "not polindrom"
print(x(input('Enter a word ')))
