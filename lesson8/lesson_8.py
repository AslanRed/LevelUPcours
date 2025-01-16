# список чисел, число, отфильтровать числа из списка, которые больше трешхолд, вернуть итоговый список
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
threshold = 4
fin_num = [num ** 2 for num in numbers if num > threshold]
print(fin_num)