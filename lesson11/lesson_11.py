# # Написать функцию list_sum(numbers), которая  с исп. рекурсии вычисляет сумму всех эл
# def list_sum(numbers):
#     if not numbers:
#         return 0
#     return numbers[0] + list_sum(numbers[1:])

# print(list_sum([1, 2, 3]))

# # Используя лямбду, отфильтровать список слов связ. с пиццей
# words = ['пицца', 'бургер', 'пепперони', 'суши', 'сыр']
# print(list(filter(lambda word: 'пицца' in word or 'пепперони' in word or 'сыр' in word, words)))

# # лямбда принимает 2 числа возвр суму плюс 42
# wrong_calc = lambda x,y: x + y + 42
# print(wrong_calc(2, 3)) 

# # написать лямбду - кол-во задач.
# laz = lambda x: 'lazi' if x < 3 else 'worker'
# print(laz(4))