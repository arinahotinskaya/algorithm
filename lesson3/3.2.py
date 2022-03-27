# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2.
# То во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля).
# Т.к. именно в этих позициях первого массива стоят четные числа.

print("Введите количество чисел в массиве:", end = ' ')
n = int(input())
arr_1 = []

for el in range(1, n + 1):
    print(f"Введите {int(el)} значение элемента:", end = ' ')
    num = int(input())
    arr_1.append(num)
print(f"Первый массив: {arr_1}")

arr_2 = []
count = 1
for el in arr_1:
    if int(el) % 2 == 0:
        arr_2.append(count)
    count += 1
print(f"Индексы четных чисел первого массива (Индексация начинается с 1): {arr_2}")