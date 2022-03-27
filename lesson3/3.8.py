# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
matrix = []
n = 4
for i in range(n):
    matrix.append([])
    sum = 0
    for j in range(n):
        digit = int(input(f"Введите элемент {i+1}|{j+1}: "))
        sum += digit
        matrix[i].append(digit)
    matrix[i].append(sum)

print("В 5 столбце находятся суммы каждой строки")
for el in matrix:
    print(el)
