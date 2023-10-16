# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 
# 0! = 1 Решить задачу используя цикл while


# Input: 5

# Output: 120

N = int(input("Введите неотрицательное число: "))
flag = True
i = 1
result = 1

if N == 0:
    flag = False
    print(f"{N}! = {result}")
elif N < 0:
    print("ERROR: Введено отрицательное число")
else:
    while flag:
        result *= i
        if i != N:
            i += 1
        else:
            flag = False
            print(f"{N}! = {result}")
    
