#построить треугольник, где строки содержат от одного до номера строки
get_size = input('enter the size: ')
size_of_t = int(get_size)
res = ''
for i in range (1,size_of_t + 1):
    res += str(i)
    print(res)



#2 вывести квадрат из # размером 4*4 из решоток
size_of_q = 4
while size_of_q > 0:
    if size_of_q == 3 or size_of_q == 2:
        print('#  #')
    else:
        print('####')
    size_of_q -= 1

#3 треугольник начиная с 5 звездочек до 1
brick = '*'
size = 5
while size > 0:
    print(brick * size)
    size -= 1
   