# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

arr = []
count = 0

for i in range(2, 10):
    for j in range(2, 100):
        if j % i == 0:
            arr.append(j)
            count += 1
    print(f"Для числа {i} кратны {count} чисел. Это числа {arr}")
    arr.clear()
    count = 0
