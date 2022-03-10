# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def counter(digit, n):
    count = 0
    for el in digit:
        if int(el) == n:
            count += 1
    return count

list_digits = [el for el in input("Введите последовательность чисел: ").split()]
print(f"Ваша введенная последовательность чисел: {list_digits}")

digit = int(input("Введите цифру, у которой мы будем считать частоту появления в введенной последовательности чисел: "))
print(f"Ваша цифра, которую мы будем искать: {digit}")

max_count = 0
for el in list_digits:
    max_count += counter(el, digit)

print(f"{max_count} - столько раз появляется цифра {digit} в последовательности введенных чисел!")
