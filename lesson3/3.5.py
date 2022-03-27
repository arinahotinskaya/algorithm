# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

print("Введите количество чисел:", end = ' ')
arr = []
n = int(input())

for el in range(1, n + 1):
    arr.append(random.randint(-1000, 1000))

print(f"Исходный массив: {arr}")
print(f"Максимальный отрицательный элемент - {min(arr)}")

max_el = min(arr)
count = 1
for el in arr:
    if int(el) == max_el:
        print(f"Максимальный орицательный элемент находится под индексом(Индексация начинается с 1) - {count}")
    count += 1
