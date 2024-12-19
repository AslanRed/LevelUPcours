#task 1 which is biger
a = int(input('enter first num: '))
b = int(input('enter second num: '))
if a > b:
    print(f'{a} is biger')
else:
    print(f'{b} is biger')

#task 2
a = int(input('enter num: '))
res = a % 2 
if res == 0:
    print(f'{a} is even')
else:
    print(f'{a} is not even')
#task 3 negative? positive or 0
a = int(input('enter num: '))
if a > 0:
    print(f'{a} is positive')
elif a < 0:
    print(f'{a} is negative')
else:
    print(f'{a} is zero')

#task 4 calculator
a = int(input('enter first num: '))
b = int(input('enter second num: '))
o = input('enter operator: ')
if o == '+':
    result = a + b
    print(f'{result} is your result')
elif o == '-':
    result = a - b
    print(f'{result} is your result')
elif o == '*':
    result = a * b
    print(f'{result} is your result')
elif o == '/' and b != 0:
    result = a / b 
    print(f'{result} is your result')
elif o == '/' and b == 0:
    print('cant devide with 0')
else: 
    print('eror: no such operator')

#task 5 what kind of year leap or not
a = int(input('enter a year: '))
b = a % 4
c = a % 100
d = a % 400
if b == 0 and c > 0:
    print(f'{a} is a leap year')
elif d == 0 :
    print(f'{a} is a leap year')
else:
    print(f'{a} is not a leap year')

#task 6  evening, morning or day
time_of_day = int(input('enter your time: '))
if time_of_day >= 6 and time_of_day <= 11:
    print('Good morning')
elif time_of_day > 11 and time_of_day <= 17:
    print('Good afternoon')
elif time_of_day > 17 and time_of_day <= 23:
    print('Good evening')
else:
    print('Good night')

#task 7 password comperation
p = input('enter password: ')
default_pas = 'secret123'
if p == default_pas:
    print('Доступ разрешен.')
else:
    print('Доступ запрешен.')
