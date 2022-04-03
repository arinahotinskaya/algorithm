# Выбрана задача 4 задача из 2 урока
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

import cProfile
import timeit

def multiplication(n):
    sum = 0
    now_digit = 1
    el = 0
    for el in range(n):
        sum += now_digit
        now_digit *= -0.5
        el += 1
    return sum
# O(n) – линейная сложность. Время работы алгоритма не зависет от размера входных данных. Тогда сложность обозначим как O(1). 
# На его вычисление для любого количества данных нужно одно и то же время.

def division(n):
    sum = 0
    now_digit = 1
    el = 0
    for el in range(n):
        sum += now_digit
        now_digit /= -2
        el += 1
    return sum
# O(n) – линейная сложность. Время работы алгоритма не зависит от размера входных данных. Тогда сложность обозначим как O(1). 
# На его вычисление для любого количества данных нужно одно и то же время.

def arr(n):
    arr = []
    sum = 0
    number = 1
    arr.append(sum)
    for el in range(0,n):
        arr.append(number)
        number /= -2
    for el in arr:
        sum += float(el)
    return sum
# По сравнению с другими функциями выполняет работу почти в 2 раза дольше, хотя также является линейной сложностью
# Функции multiplication() и division() одинаковые по сложности, так как разница в коде только в умножении/делении.
# Но функция multiplication() работает немного быстрее функции division()

print("Введите количество элементов n: ")
n = int(input())
print(f"Сумма {n} элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... равна {multiplication(n)}")
print(f"Сумма {n} элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... равна {division(n)}")
print(f"Сумма {n} элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... равна {arr(n)}")

NUMBER_EXECUTIONS = 1
TEST_VALUE = 1000

time1 = timeit.timeit(f'multiplication({TEST_VALUE})',
                      setup='from __main__ import multiplication',
                      number=NUMBER_EXECUTIONS)
time2 = timeit.timeit(f'division({TEST_VALUE})',
                      setup='from __main__ import division',
                      number=NUMBER_EXECUTIONS)
time3 = timeit.timeit(f'arr({TEST_VALUE})',
                      setup='from __main__ import arr',
                      number=NUMBER_EXECUTIONS)

print(f"Время за которое сработала функция MULTIPLICATION() - {time1}")
print(f"Время за которое сработала функция DIVISION() - {time2}")
print(f"Время за которое сработала функция ARR() - {time3}")

'''
При n = 10:
Время за которое сработала функция MULTIPLICATION() - 0.0002150830000000603
Время за которое сработала функция DIVISION() - 0.00022900000000003473
Время за которое сработала функция ARR() - 0.00040537500000015214

При n = 100:
Время за которое сработала функция MULTIPLICATION() - 0.00016425000000008794
Время за которое сработала функция DIVISION() - 0.00017420800000023107
Время за которое сработала функция ARR() - 0.0002969579999998473

При n = 1000:
Время за которое сработала функция MULTIPLICATION() - 0.0002050829999999948
Время за которое сработала функция DIVISION() - 0.0002120840000001678
Время за которое сработала функция ARR() - 0.0003796250000003276

При n = 10000:
Время за которое сработала функция MULTIPLICATION() - 0.0001766669999998527
Время за которое сработала функция DIVISION() - 0.00018233300000014552
Время за которое сработала функция ARR() - 0.0003229160000000064
'''
