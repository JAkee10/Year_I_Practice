# Дано натуральное число A > 1. Определите, каким по счету 
# числом Фибоначчи оно является, то есть выведите такое 
# число n, что φ(n)=A. Если А не является числом Фибоначчи, 
# выведите число -1.

# Input: 5

# Output: 6


A = int(input("Введите натуральное число: "))

num1 = 0
num2 = 1
result = 1
n = 0
flag = True

if A == 1:
    print(0)

if n == 0:
    n += 1
    print("--", num1)
if n == 1:
    n += 1
    print("--", num2)

while flag:
    result = num1 + num2
    num1 = num2
    num2 = result
    n += 1
    print("--", result)
    if result == A:
        print(f"n = {n}")
        print(f"F({n}) = {A}")
        flag = False
    elif result > A:
        print(-1)
        flag = False