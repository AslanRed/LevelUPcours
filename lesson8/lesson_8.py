# список чисел, число, отфильтровать числа из списка, которые больше трешхолд, вернуть итоговый список
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
threshold = 4
fin_num = [num ** 2 for num in numbers if num > threshold]
print(fin_num)

# список фруктов(5), создать словарь - ключ -слово, значение - длина
fruits = ['лимон', 'банан', 'яблоко', 'груша', 'нектарин']
fruits_dict = {word : len(word) for word in fruits }
print(fruits_dict)

#

nums = [1, 2, 3, 4, 5, 15, 16]
gen_for_nums = ('FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in nums)
for value in gen_for_nums:
    print(value)