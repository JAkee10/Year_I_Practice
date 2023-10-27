# Задача №35

# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes
number = int(input("Введите число для проверки: "))
i = number - 1


def is_simple_number(num, checker = number - 1):
    if checker == 1:
        return True   # or "yes"
    if num % checker != 0:
        return is_simple_number(num, checker - 1)
    return False   # or "no"

if number > 1 and is_simple_number(number):
    print("yes")
else:
    print("no")



# ----------------------------------------------------------НЕУДАЧНАЯ_ПОПЫТКА------------------------------------------------------------------------

# def is_simple_number(n):
#     n = 2
#     if end == n:
#         return True
#     if number % n != 0:
#         return is_simple_number(n + 1)
#     return False
