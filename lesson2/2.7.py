# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число

def left(amount):
      # Возвращаем сумму арифметической прогрессии, то есть 1+2+...+n:
      return (1 + amount) * amount / 2

def right(amount):
      # Возвращаем n(n+1)/2:
      return amount * (amount + 1) / 2

for el in range(10000):
      n = el + 1
      if left(n) == right(n):
            print(f"При n = {n} равенство 1+2+...+n = n(n+1)/2 верно")
      elif left(n) != right(n):
            print(f"При n = {n} равенство 1+2+...+n = n(n+1)/2 неверно")
