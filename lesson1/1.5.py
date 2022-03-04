# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

print("Введите 2 буквы")
print("Введите 1-ю букву в нижне регистре: ")
num_1 = input()
print("Введите 2-ю букву в нижнем регистре")
num_2 = input()

if ord('а') <= ord(num_2) <= ord('я') and ord('а') <= ord(num_1) <= ord('я') or num_1 == 'ё' and ord('а') <= ord(num_2) <= ord('я') or num_2 == 'ё' and ord('а') <= ord(num_1) <= ord('я') or num_1 == 'ё' and num_2 == 'ё':
    if ord(num_1) == 1105:
        print(f"Эта буква под номером {ord(num_1) - 1098}")
        a = ord(num_1) - 1098
    elif ord('а') <= ord(num_1) <= ord('е'):
        print(f"Эта буква под номером {ord(num_1) - 1071}")
        a = ord(num_1) - 1071
    elif ord('ж') <= ord(num_1) <= ord('я'):
        print(f"Эта буква под номером {ord(num_1) - 1070}")
        a = ord(num_1) - 1070

    if ord(num_2) == 1105:
        print(f"Эта буква под номером {ord(num_2) - 1098}")
        b = ord(num_2) - 1098
    elif ord('а') <= ord(num_2) <= ord('е'):
        print(f"Эта буква под номером {ord(num_2) - 1071}")
        b = ord(num_2) - 1071
    elif ord('ж') <= ord(num_2) <= ord('я'):
        print(f"Эта буква под номером {ord(num_2) - 1070}")
        b = ord(num_2) - 1070

    if 5 <= abs(a - b) - 1 <= 20 or 25 <= abs(a - b) - 1 <= 30:
        print(f"Между буквами {num_1} и {num_2} находиться {abs(a - b) - 1} букв")
    elif abs(a - b) - 1 == 1 or abs(a - b) - 1 == 21 or abs(a - b) - 1 == 31:
        print(f"Между буквами {num_1} и {num_2} находиться {abs(a - b) - 1} буква")
    elif 2 <= abs(a - b) - 1 <= 4 or 22 <= abs(a - b) - 1 <= 24:
        print(f"Между буквами {num_1} и {num_2} находиться {abs(a - b) - 1} буквы")
    elif a - b == 0:
        print(f"Буквы {num_1} и {num_2} одинаковые")

else:
    print("Таких букв не существует в русском алфавите")
