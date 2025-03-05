# Задача 1. принимает дату рождения, выдает день недели, формат гггг-дд-мм
import datetime

birth_day = input('Enter your birthday (y d m): ')
b_day = datetime.datetime.strptime(birth_day, '%Y %d %B')
 

print(b_day.strftime("%A"))

# Задача 2. Пришельцы прилетают через 4321 день, когда это?
arival_after = datetime.timedelta(days = 4321)
today = datetime.datetime.today()
arival_day = today + arival_after
print(arival_day)

# Задача 3. Найти ближайшую дату. когда следующая пятница - 13.
start = datetime.datetime.today()
month_n = 1
year_n = 2025
while True:
    month_n += 1
    start.replace(month= month_n)
    if start.weekday() == 4:
        print(start)
        break
    if start.month > 12:
        year_n += 1
        start.replace(year=year_n, month= 1)
        month_n = 0
        