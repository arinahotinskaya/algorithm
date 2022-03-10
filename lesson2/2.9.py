# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def summary(digit):
    sum = 0
    for el in digit:
        sum += int(el)
    return sum

list_digits = [el for el in input("Введите натуральные числа через пробел: ").split()]
print(list_digits)

max_digit = 0
max_sum = 0
for el in list_digits:
    if summary(el) >= max_sum:
        max_sum = summary(el)
        max_digit = el

print(f"Самое большое натуральное число по сумме цифр: {max_digit}. Сумма его цифр равна: {max_sum}")
