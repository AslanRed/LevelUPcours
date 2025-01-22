from itertools import combinations
from sys import stdin

# # список чисел от 1 до 4, найти все комбинации длинной 2
# num_lst = [1, 2, 3, 4]
# result = list(combinations(num_lst, 2))
# print(result)

# пользователь вводит несколько строк, найти для каждой строки , уникальные слова
lines = stdin.read().split('\n')
for line in lines:
    result = set(line.split())
print(''.join(result))