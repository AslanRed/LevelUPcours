import random
# Задачи с 1 по 6 включительно были выполненны на лекции.

#7 факториал числа через while
get_num = int(input('Введите чило, факториал которого вам нужен: '))
num = get_num
res = 1
while num > 0:
    res *= num
    num -= 1
print(f'факториал числа {get_num}: {res}')

#8 Переворот строки
get_str = input('Введите строку: ')
letter_ind = -1
res = ''
for i in get_str:
    res += get_str[letter_ind]
    letter_ind -= 1
print(res)

#9 Угадай число с подсказками
num_to_win = random.randint(1, 100)
while (get_guess := int(input('Угадайте число от 1 до 100: '))) != num_to_win:
    if get_guess <= num_to_win + 10 and get_guess >= num_to_win - 10:
        print('Горячо!')
        get_guess
    elif get_guess > num_to_win:
        print('Меньше.')
        get_guess
    else: 
        print('Больше')
print('Поздравляем, вы угадали')

#10 Фраза полиндром или нет
get_str = input('Введите строку: ')
str_for_test = get_str.replace(' ', '').upper()
last_let = -1
res = ''
for i in str_for_test:
    res += str_for_test[last_let]
    last_let -= 1
if res == str_for_test:
    print('Это полиндром!')
else:
    print('Это не полиндром')