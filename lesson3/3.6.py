# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

print("Введите количество чисел:", end = ' ')
arr = []
n = int(input())

for el in range(1, n + 1):
    arr.append(random.randint(-100, 100))

minimum = min(arr)
maximum = max(arr)
print(f"Изначальный массив: {arr}. Максимальный элемент - {maximum}. Минимальный элемент - {minimum}")

count_max = 1
count_min = 1
for el in arr:
    if int(el) == maximum:
        maximum = count_max
    if int(el) == minimum:
        minimum = count_min
    count_max += 1
    count_min += 1

# print(maximum)
# print(minimum)

if minimum > maximum:
    minimum, maximum = maximum, minimum


sum = 0
for el in range(minimum, maximum - 1):
    sum += arr[el]

print(f"Сумма элементов, находящихся между минимальным и максимальным элементами: {sum}")
