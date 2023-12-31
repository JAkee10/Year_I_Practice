# Задача №45

# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящеее 10(в 5 степени). 
# Программа должна вывести все пары дружественных чисел, 
# каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

# Ввод: 
# 300 

# Вывод:
# 220 284


k = int(input("Введи число k: "))

div_sum = list()
frined_num = list()

for i in range(1, k):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    div_sum.append((i, sum))

for i in range(len(div_sum)):
    for j in range(i + 1, len(div_sum)):
        if div_sum[i][0] == div_sum[j][1] and div_sum[i][1] == div_sum[j][0]:
            frined_num.append((div_sum[i][0], div_sum[i][1]))
            

for case in frined_num:
    for num in case:
        print(f"{num} ", end="")
    print(end="\n")

# print(frined_num)