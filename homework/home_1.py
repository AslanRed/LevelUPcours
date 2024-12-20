import random

#Задача 1. Приветствие с регистром. 
name_for_greeting = input('Введите свое имя: ')
rand = random.randint(1, 10)
if name_for_greeting.isalpha():
    if rand < 5:
        name_result = name_for_greeting.upper()
    else:
        name_result = name_for_greeting.lower()
    print(f'Здравствуйте, {name_result}.')
else:
    print('Введенны недопустимые символы!')


#Задача 2. Сравнение длинны слов
word_1 = input('Введите первое слово: ')
word_2 = input('Введите второе слово: ')
if word_1.isalpha() and word_2.isalpha():
    if len(word_1) == len(word_2):
        print('Слова одинаковой длинны.')
    elif len(word_1) > len(word_2):
        print(f'{word_1} длиннее.')
    else:
        print(f'{word_2} длиннее.')
else:
    print('Введенны недопустимые символы!')

#Задача 3. Бросок кубика
u_throw = input('Введите свое значение от 1 до 6: ')
cpu_throw = random.randint(1, 6)
if u_throw.isdigit() and (int(u_throw) > 0 and int(u_throw) <= 6):
    if int(u_throw) > cpu_throw:
        print('Вы победили!')
    elif int(u_throw) < cpu_throw:
        print('Вы проиграли.')
    else:
        print('Ничья!')
else:
    print('Ведено недопустимое значение!')

#Задача 4. Проверка треугольника.
side_a = input('Введите длинну первой стороны: ')
side_b = input('Введите длинну второй стороны: ')
side_c = input('Введите длинну третей стороны: ')
if side_a.isdigit() and side_b.isdigit() and side_c.isdigit():
    a = int(side_a)
    b = int(side_b)
    c = int(side_c)
    test_1 = a + b
    test_2 = a + c
    test_3 = b + c
    if test_1 > c and test_2 > b and test_3 > a:
        print('Такой треугольник может существовать.')
    else:
        print('Такой треугольник не может существовать.')
else:
    print('Ведено недопустимое значение!')

#Задача 5. Определение четверти на плоскости
coordinate_x = input('Введите первое значение координаты по х: ')
coordinate_y = input('Введите первое значение координаты по y: ')
x = int(coordinate_x)
y = int(coordinate_y)
if x > 0 and y > 0:
    print('Точка находится в первой четверти')
elif x < 0 and y > 0:
    print('Точка находится во второй четверти')
elif x < 0 and y < 0:
    print('Точка находится в третьей четверти')
elif x > 0 and y < 0:
    print('Точка находится в четвертой четверти')
else:
    print('Точка лежит на самой оси координат')