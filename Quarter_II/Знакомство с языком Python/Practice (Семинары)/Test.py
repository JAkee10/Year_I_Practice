# 2. Сложите два числа

# Даны два непустых связных списка, представляющих два неотрицательных целых числа. 
# Цифры хранятся в обратном порядке, и каждый из их узлов содержит одну цифру. 
# Сложите два числа и верните сумму в виде связанного списка.

# Можно предположить, что эти два числа не содержат ни одного нуля в начале, кроме самого числа 0.

# Пример 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Пример 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Пример 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
    


# def addTwoNumbers(l1, l2):
#     num1 = ''
#     for i in range(len(l1) - 1, -1, -1):
#         num1 += str(l1[i])


#     num2 = ''
#     for i in range(len(l2) - 1, -1, -1):
#         num2 += str(l2[i])


#     num1 = int(num1)
#     num2 = int(num2)

#     res = [int(x) for x in str(num1 + num2)]
#     return res[::-1]

# print(addTwoNumbers(l1, l2))

# result = l1

with open('test.txt', 'w', encoding= 'utf-8') as data:
    data.write("line 1\n")
    data.write('line 2\n')