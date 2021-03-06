# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. 
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

num_1 = 1
num_2 = 6

print(f"Выполним логические побитовые операции над числами 5 и 6:\n"
      f"(Битовый оператор и): 5 & 6 = {num_1 & num_2}\n"
      f"(Битовый оперетор исключающее или): 5 ^ 6 = {num_1 ^ num_2}\n"
      f"(Битовый оператор или): 5 | 6 = {num_1 | num_2}\n"
      f"(Инверсия числа 5): ~5 = {~num_1}\n"
      f"(Инверсия числа 6): ~6 = {~num_2}\n"
      f"(Побитовый сдвиг влево числа 5 на 2 единицы): 5<<2 = {num_1 << 2}\n"
      f"(Побитовый сдвиг вправо числа 5 на 2 единицы): 5>>2 = {num_1 >> 2}")
