# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

print("Введите любой год: ")
year = int(input())

if year % 4 == 0 and year % 100 != 0 and year > 0 or year % 400 == 0 and year > 0:
    print(f"Год {year} - високосный")
else:
    print(f"Год {year} - невисокосный")
