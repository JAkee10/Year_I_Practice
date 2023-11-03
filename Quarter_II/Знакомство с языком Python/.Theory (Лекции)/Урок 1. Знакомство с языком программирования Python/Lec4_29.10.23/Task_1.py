# 1. 
# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар 
# (число; квадрат числа).

# Пример: 1 2 3 5 8 15 23 38

# Получить: [(2, 4), (8, 64), (38, 1444)]













# nums = list(x for x in range(1, 20))
# nums = list(map(lambda x: x + 10, nums))
# print(nums)






# nums = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# pow = lambda l: l * l

# for num in nums:
#     if num % 2 == 0:
#         res.append((num, pow(num)))

# print(res)