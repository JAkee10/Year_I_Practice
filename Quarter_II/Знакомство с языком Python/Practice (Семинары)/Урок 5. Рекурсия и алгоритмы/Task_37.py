# Задача №37

# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

num_count = int(input("Введи количество чисел: "))
    
def regular_output(size, text = ''):
    if size > 0:
        el = input("Введи число: ") + " "
        return regular_output(size - 1, el + text)
    return text

print(regular_output(num_count))




# value = 5
# c = 0
# flag = False
# def nums(n):
#     num = input('введите число')
#     if n > 2:
#         nums(n - 1)
#     return num
# print(nums(value))











# def reverse_output(size, temp, i = 0):
#     temp = ''
#     if size > 0:
#         el = str(input("Введи число: ")) + " "
#         return reverse_output(size - 1, el + temp, i)
#     return temp






# num_count = int(input("Введи количество чисел: "))
# flag = True
# def reverse_output(f, size):
#     if f:
#         temp = input("Введи число: ")
#         return print(temp)
#     elif size < 0:
#         return reverse_output(f, size - 1)
#     flag = False
#     return "END"







# num_count = int(input("Введи количество чисел: "))
# def reverse_output(size):
#     if size != 0:
#         temp = input("Введи число: ")
#         return print(temp)
#     return reverse_output(size - 1)





# def fill_list(size):
#     if size == 0:
#         return num_list
#     num_list.append(int(input("Введи число:")))
#     return fill_list(size - 1)

# def reverse_list(orig_list, i = 0):
#     if i == len(orig_list):
#         return orig_list[-i]
#     orig_list[i] = reverse_list(orig_list, i + 1)
#     return orig_list


# num_list = list()
# res = fill_list(num_count)
# res = reverse_list(res)
# print(res)
