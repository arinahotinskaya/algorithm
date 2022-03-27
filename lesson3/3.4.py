# Определить, какое число в массиве встречается чаще всего.

print("Введите количество чисел:", end = ' ')
arr = []
n = int(input())

for el in range(1, n + 1):
    print(f"Введите значение массива под индексом {el}:", end = ' ')
    arr.append(int(input()))

print(arr)
max_number = 0
count_max = 0
count = 0
for i in arr:
    for j in arr:
        if i == j:
            count += 1
    if count >= count_max:
        count_max = count
        max_number = i
    count = 0

print(f"Число, которое чаще всего встречается в массиве - {max_number}")
