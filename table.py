# for i in range(1, 10):
#     for j in range(1, 10):
#         result = i * j
#         temp_str = str(i) + " * " + str(j) + " = " + str(result)
#         print(temp_str)
# 1 вариант - все вычисления в столбик

q = int(input("Введите размер таблицы (если 10 на 10 - введите '10'): "))
for i in range(1, q+1):
     for j in range(i, i*q+1, i):
         print(j, end='\t')
     print()
# 2 вариант - получаем табличку, где изначально можем ввести размер таблицы