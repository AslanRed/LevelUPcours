default_pas = '1234'
u_pass = input('Введите пароль: ')
while True:
    u_pass = input('Введите пароль: ')
    if default_pas == u_pass:
        print('Вход разрешен!')
        break