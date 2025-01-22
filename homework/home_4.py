#1 Сумма всех чисел от одного до ста включительно.
print(f'сумма от 1 до 100: {sum(num for num in range(101))}')

#2 Запрашивает строку и выводит каждый символ на новой строке.
result = [print(symbol) for symbol in input('enter a string: ')]

#3 Запрашиват число и выводит табл. умножения до 15
get_num = int(input('enter a number: '))
result = [print(f'{num} * {get_num} = {num * get_num}') for num in range(16)]

#4 Запрашивает число и выводит сумму всех четных чисел в этом диапазоне
get_end = int(input('enter number: '))
print(f'сумма всех четных в этом диапазоне = {sum(num for num in range(0, get_end + 1, 2))}')

#5 запрашивает число и найти сумму всех кратных 3 в диапозоне, через while
get_end = int(input('enter number: '))
print(f'сумма: {sum(num for num in range(0,get_end +1, 3))}')

#6 принимает число и проверяет простое оно или нет, с for  для деления
get_num = int(input('enter a number: '))
res = [get_num % dev for dev  in range(2, get_num)]
if 0 in res:
    print('Это не простое число')
else:
    print('Это простое число')


#8 Переворот строки
get_str = input('Введите строку: ')
print(''.join([get_str[num] for num in range(len(get_str) -1, -1, -1)]))

#10 Фраза полиндром или нет
get_str = input('Введите строку: ').replace(' ', '').upper()
turn_str = ''.join([get_str[num] for num in range(len(get_str) -1, -1, -1)])
if turn_str == get_str:
    print('Это полиндром!')
else:
    print('Это не полиндром')