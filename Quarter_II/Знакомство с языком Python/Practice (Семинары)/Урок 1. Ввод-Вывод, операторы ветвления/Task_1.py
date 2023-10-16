# Задача №1.

# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

# Input:
# n = 700
# m = 750
# Output:
# 2

n = int(input(f"Введите расстояние которое проезжает машина за день: "))
m = int(input(f"Введите расстояние которое нужно проехать машине: "))
result = abs(-m//n)
# abs(-m//n) == -(-m//n)

print(f"result = {result}")

# Так же рабочий вариант:
# print(f"result = {(m + n - 1) // n}")