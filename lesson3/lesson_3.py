# # default_pas = '1234'
# # while True:
# #     u_pass = input('Введите пароль: ')
# #     if default_pas == u_pass:
# #         print('Вход разрешен!')
# #         break

#1 Сумма всех чисел от одного до ста включительно.
res = 0
for i in range(1, 101):
    res += i
print(f'сумма от 1 до 100: {res}')

#2 Запрашивает строку и выводит каждый символ на новой строке.
get_string = input('enter a string: ')
for i in get_string:
    print(i)

#3 Запрашиват число и выводит табл. умножения до 15
get_num = int(input('enter a number: '))
for i in range(0, 16):
    res = get_num * i
    print (f'{get_num} * {i} = {res}')

#4 Запрашивает число и выводит сумму всех четных чисел в этом диапазоне
get_end = int(input('enter number: '))
res = 0
for i in range(0, get_end + 1, 2):
    res += i
print(f'сумма всех четных в этом диапазоне = {res}')

#5 запрашивает число и найти сумму всех кратных 3 в диапозоне, через while
get_end = int(input('enter number: '))
res = 0 
i = get_end
while i == get_end:
    for n in range(get_end + 1):
        devi = n % 3
        if devi == 0:
            res += n
    i -= 1
print(f'сумма: {res}')

#6 принимает число и проверяет простое оно или нет, с for  для деления
get_num = int(input('enter a number: '))
res = 0
for i in range(2, get_num):
    res = get_num % i
    if res == 0:
        print('это число не простое')
        break
    else:
        print('Число простое')

#7 проверка полиндрома
get_str = input('enter a word: ')
str_for_test = get_str.upper()
last_s = -1
res = ''
for i in str_for_test:
    res += str_for_test[last_s]
    last_s -= 1
if res == str_for_test:
    print('Это полиндром')
else:
    print('Это не полиндром')
    