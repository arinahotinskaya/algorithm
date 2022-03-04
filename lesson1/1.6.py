# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

print("Введите любое число от 1 до 33: ")
num_of_el = int(input())

if 1 <= num_of_el <= 33:
    if num_of_el == 7:
        print(f"Это буква {chr(num_of_el + 1098)}")
    elif 1 <= num_of_el <= 6:
        print(f"Это буква {chr(num_of_el + 1071)}")
    elif 8 <= num_of_el <= 33:
        print(f"Это буква {chr(num_of_el + 1070)}")
else:
    print("Буквы под таким номером не существует в алфавите")
