# #Найдите первую заглавную букву в строке text. Если ее нет, выведите сообщение, что заглавных букв нет.
# test_text = 'tExt'
# flag = False
# for letter in test_text:
#     if letter.isupper():
#         print('Первая заглавная: {letter}')
#         flag = True
#         break
# if not flag:
#     print('Нет заглавных букв')

# #Удалить все восклицательные знаки в конце строки.
# text = 'Hello world!!!'

# # Удаление чисел из строки
# text = 'Python 3.9 is awsome 2025'
# result = ''
# for char in text:
#     if char.isdigit() == False:
#         result += char
# print(result)

# #Подсчет гласных и согласных
# text = 'Hello world'
# vowels = 'aeiou'
# v_count = 0
# c_count = 0
# for char in text:
#     if char.isalpha():
#         if char.lower() in vowels:


# #Пропуск слов с определенной длинной (4)
# text = "This is a simple Python string example"
# splited_text = text.split(' ')
# for word in splited_text:
#     if len(word) > 4:
#         print(word)

# #Пропуск символов по условию
# text = "This is a simple Python string example"
# result = ''
# for char in text:
#     if char.lower() != 'a':
#         result += char
# print(result)

# #Есть список мороженного, найти ванильное
# menu = ["шоколадное", "клубничное", "ванильное", "фисташковое"]
# if 'ванильное' in menu:
#     print('Yes')
# else:
#     print('No')

# #Высшая температура
# cities = ["Москва", "Сочи", "Якутск", "Казань"]
# temperatures = [-5, 15, -30, -2]
# result =cities[temperatures.index(max(temperatures))]
# print(result)

# # Список животных, посчитать сколько раз встречается каждое животное
# animals = ["слон", "тигр", "слон", "зебра", "тигр", "тигр", "зебра"]
# un_animals = []
# counter_list = []
# for animal in animals:
#     if animal not in un_animals:
#         un_animals.append(animal)
#         counter_list.append(1)
#     else:
#         index_of_animal = un_animals.index(animal)
#         counter_list[index_of_animal] += 1
# for i in range(len(un_animals)):
#     print(f'{un_animals[i]}: {counter_list[i]}')