# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = []
arr = []
print("Введите количество строк:", end = ' ')
n = int(input())
print("Введите количество столбцов:", end = ' ')
m = int(input())

for i in range(n):
    matrix.append([])
    for j in range(m):
        digit = random.randint(0, 100)
        matrix[i].append(digit)

print("Исходная матрица равна: ")
for el in matrix:
    print(el)
print("\n")

# Транспанируем матрицу
trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        trans_matrix[j][i] = matrix[i][j]

print("Транспонированная матрица равна: ")
for el in trans_matrix:
    print(el)
print("\n")

minimum = 1000
for i in range(len(trans_matrix)):
    for j in range(len(trans_matrix[0])):
        if trans_matrix[i][j] <= minimum:
            minimum = trans_matrix[i][j]
    arr.append(minimum)
    minimum = 1000

print(f"Массив минимальных элементов столбцов матрицы:", end = ' ')
print(arr)
print(f"Самый минимальный элемент из минимальных элементов столбцов матрицы равен - {min(arr)}")
