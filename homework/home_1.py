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
coordinate_1_x = input('Введите первое значение координаты по х: ')
coordinate_1_y = input('Введите первое значение координаты по y: ')

coordinate_2_x = input('Введите второе значение координаты по х: ')
coordinate_2_y = input('Введите второе значение координаты по y: ')

coordinate_3_x = input('Введите третье значение координаты по х: ')
coordinate_3_y = input('Введите третье значение координаты по y: ')

if coordinate_1_x.isdigit() and coordinate_1_y.isdigit() and coordinate_2_x.isdigit() and coordinate_2_y.isdigit() and coordinate_3_x.isdigit() and coordinate_3_y.isdigit():
    coordinate_1_x = int(coordinate_1_x)
    coordinate_1_y = int(coordinate_1_y)

    coordinate_2_x = int(coordinate_2_x)
    coordinate_2_y = int(coordinate_2_y)

    coordinate_3_x = int(coordinate_3_x)
    coordinate_3_y = int(coordinate_3_y)
else:
    print('Введено недопустимое значение!')

# проверка первой точки
if coordinate_1_x > 0:
    x_1 = 1
elif coordinate_1_x < 0:
    x_1 = -1
else:
    x_1 = 0
if coordinate_1_y > 0:
    y_1 = 1
elif coordinate_1_y < 0:
    y_1 = -1
else:
    y_1 = 0

# проверка второй точки
if coordinate_2_x > 0:
    x_2 = 1
elif coordinate_2_x < 0:
    x_2 = -1
else:
    x_2 = 0
if coordinate_2_y > 0:
    y_2 = 1
elif coordinate_2_y < 0:
    y_2 = -1
else:
    y_2 = 0

# проверка третей точки
if coordinate_3_x > 0:
    x_3 = 1
elif coordinate_3_x < 0:
    x_3 = -1
else:
    x_3 = 0
if coordinate_3_y > 0:
    y_3 = 1
elif coordinate_1_y < 0:
    y_3 = -1
else:
    y_3 = 0

# нахождение четверти, в которой находиться точка
f_point = x_1 + y_1
s_point = x_2 + y_2
t_point = x_3 + y_3

# первая точка
if f_point == 2:
    point_1_in = 1
elif f_point == -2:
    point_1_in = 3
elif f_point == 0:
    if x_1 == -1:
        point_1_in = 2
    else:
        point_1_in = 4
else:
    point_1_in = 0

# вторая точка
if s_point == 2:
    point_2_in = 1
elif s_point == -2:
    point_2_in = 3
elif s_point == 0:
    if x_2 == -1:
        point_2_in = 2
    else:
        point_2_in = 4
else:
    point_2_in = 0

# третья точка
if t_point == 2:
    point_3_in = 1
elif t_point == -2:
    point_3_in = 3
elif t_point == 0:
    if x_3 == -1:
        point_3_in = 2
    else:
        point_3_in = 4
else:
    point_3_in = 0

# нахождение места прямой
sum_of_points = point_1_in + point_2_in + point_3_in
if sum_of_points == 2:
    print('Прямая находится в первой четверти.')
elif sum_of_points == 6:
    print('Прямая находится во второй четверти.')
elif sum_of_points == 9:
    print('Прямая находится в третей четверти.')
elif sum_of_points == 12:
    print('Прямая находится в четвертой четверти.')
else:
    print('Прямая находится в двух четвертях.')
        