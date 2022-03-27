# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

print("Введите количество чисел:", end = ' ')
arr = []
n = int(input())

for el in range(1, n + 1):
    arr.append(random.randint(1, 100))

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

arr[minimum - 1], arr[maximum - 1] = arr[maximum - 1], arr[minimum - 1]
print(f"Массив после смены мест минимального и максимального элемента: {arr}.")
