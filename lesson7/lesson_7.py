n = int(input())
a = [int(x) for x in input().split()]

min, small_min = 2 * 1e9, 2 * 1e9
for num in a:
    if num < min:
       small_min = min
       min = num
    elif num < small_min:
        small_min = num
print(small_min, min)