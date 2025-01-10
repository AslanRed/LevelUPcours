import random

# Создать список от n до 0
starting_point = int(input('Enter a number: '))
result = []
for num in range(starting_point, -1, -1):
    result.append(num)
print(f'Here is your list: {result}')

# К динозаврам из списка добавить слово "пушистый" и записать в новый спичок
dinosaurs = ['Ти-рекс', 'Трицератопс', 'Велоцираптор', 'Брахиозавр']
fluf_dino = []
for word in dinosaurs:
    word += ' пушистый'
    fluf_dino.append(word)
print(fluf_dino)

# Случайно выбрать 3 ингридиента из списка, с помощью random.choice()
ingredients = ['сыр', 'яйца', 'помидоры', 'курица', 'рыба', 'грибы', 'лук']
result = []
for i in range(0, 3):
    result.append(random.choice(ingredients))
print(f'You have: {result}')

# Есть список кортежей, поменять местами имя и фамилию
names = [('Иванов', 'Иван'), ('Петров', 'Петр'), ('Сидоров', 'Сидор')]
result = []
for tup_in_list in names:
    (second_name, name) = tup_in_list
    turn_over = (name, second_name)
    result.append(turn_over)
print(result)

# Сгенерировать пароль из случайного набора символов, длинной 8
letters = 'abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
password = ''
for symbol in range(0, 8):
    password += random.choice(letters)
print(f'Your generated password is: {password}')

# Разделить список чисел на 2 списка - четных и нечетных
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_num = []
even_num = []
for number in numbers:
    test = number % 2
    if test == 0:
        even_num.append(number)
    else:
        odd_num.append(number)
print(f'Odd: {odd_num}')
print(f'Even: {even_num}')

# Разделить строку с книгой и главой на отдельные части
text = 'Гарри Поттер и Тайная комната - Глава 2'
book_title = ''
chapter_number = ''
lst_of_parts = text.split(' - ')
book_title = lst_of_parts[0]
chapter_number = lst_of_parts[1]
print(f'Книга: {book_title}, Глава: {chapter_number}')

# Выбрать случайное поздравление, если не содержат - "скучный"
greetings = ['С днем рождения!', 'С Новым годом!', 'Желаю успехов!', 'Скучный текст']
done = False
while done == False:
    rand_greet = random.choice(greetings)
    lst_of_words_in_greet = rand_greet.split(' ')
    for word in lst_of_words_in_greet:
        if word.lower() == 'скучный':
            done =False
            break
        done = True
if done:
    print(rand_greet)

# Заменть плохие слова звездочкой
text = 'Эта программа такая тупая! Вот блин!'
bad_words = ['тупая', 'блин']
for word in bad_words:
   text = text.replace(word, '*')
print(text)

# Удалить повторяющиеся элементы списка, сохранив порядок
words = ['яблоко', 'банан', 'яблоко', 'груша', 'банан', 'слива']
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
print(unique_words)

# Найти слово - "стоп", остановить цикл, посчитать сколько слов было до него
words = ['начало', 'путь', 'стоп', 'дальше', 'конец']
word_counter = 0
for word in words:
    if word.lower() != 'стоп':
        word_counter += 1
    else:
        break
print(f'You had {word_counter} words before stoping')