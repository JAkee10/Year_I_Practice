# Задача №25

# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d

# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()

user_input = "a a a b c a a d c d d"
user_output = ''

list_user_input = user_input.split()    #список
temp = set(user_input.replace(' ', ''))  #множество

for letter in temp:     #['a', 'b', 'c', 'd']
    counter = 0
    for i in range(len(list_user_input)):
        if letter == list_user_input[i]:
            counter += 1
        if counter > 1 and letter == list_user_input[i]:
            list_user_input[i] += '_' + str(counter - 1)

for i in range(len(list_user_input)):
    if i != range(len(list_user_input) - 1):
        user_output += (list_user_input[i] + ' ')
    else:
        user_output += (list_user_input[-1])

print(user_output)








# user_input = "a a a b c a a d c d d"

# list_user_input = user_input.split()
# temp = set(user_input)
# temp.discard(' ')
# # iter_count = 1

# for letter in temp:
#     counter = -1
#     # print(f"iter : {iter_count}")
#     # print(f"    1 for : letter = {letter}")
#     for i in range(len(list_user_input)):
#         # print(f"    2 for : i = {i}")
#         if letter == list_user_input[i]:
#             # print(f"        1 if : {letter} == {list_user_input[i]}")
#             counter += 1
#             # print(f"    {counter} += 1")
#         if counter > 0 and letter == list_user_input[i]:
#             # print(f"        2 if : {counter} > 0")
#             list_user_input[i] += '_' + str(counter)
#     # iter_count += 1

# # print(temp)
# print(list_user_input)