# Задача №19
# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.

# Input: [1, 2, 3, 4, 5] k = 3
# Output: [3, 4, 5, 1, 2]


list_1 = [i for i in range(1, int(input("Количество чисел: ")) + 1)]
k = int(input("Сдвиг на "))
print()

for i in range(k):
    temp_list = [list_1[-1],]
    for j in range(len(list_1) - 1):
        temp_list.append(list_1[j])
    list_1 = temp_list
print(list_1)