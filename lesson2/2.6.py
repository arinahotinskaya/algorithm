# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

answer = random.randint(0, 100)
count = 1
condition = True

while condition:
    print("Попробуйте угадать число от 0 до 100! Введите число: ")
    your_number = int(input())
    if your_number == answer:
        print(f"Правильный ответ: {answer}. Вы угадали с {count} попытки!")
        condition = False
    elif your_number != answer:
        if your_number < answer:
            print("Введенное число меньше ответа")
            print(f"У вас осталось {10 - count} попыток.")
        elif your_number > answer:
            print("Введенное число больше ответа")
            print(f"У вас осталось {10 - count} попыток.")

    if count == 10:
        print("Вы проиграли!")
        condition = False
    count += 1
