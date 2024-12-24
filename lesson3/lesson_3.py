default_pas = '1234'
while True:
    u_pass = input('Введите пароль: ')
    if default_pas == u_pass:
        print('Вход разрешен!')
        break