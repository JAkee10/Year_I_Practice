# Задача №17.
# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4] или [1, 1, -1, 1, -2, 1, 2, 0, 4, -1, 3, 1, 4, 4]
# Output: 6 или 7


number_list = [1, 1, -1, 1, -2, 1, 2, 0, 4, -1, 3, 1, 4, 4]
counter = 0

temp = [number_list[0]]

counter = 0

for el in number_list:
    for i in range(len(temp)):
        if el != temp[i]:
            counter += 1
    if counter == len(temp):
        temp.append(el)
    counter = 0
        
print(f"length = {len(temp)},   temp = {temp}")




#  
                                    # РАБОЧАЯ ВЕРСИЯ:

# for el in number_list:
#     for i in range(len(temp)):
#         counterI += 1
#         print(f"Длина temp = {len(temp)}")
#         print(f"Значение el = {el}")
#         print(f"Значение i = {i}")
#         print(f"------------------------")
#     temp.append(el)




                                    # НЕ ОЧЕНЬ РАБОЧАЯ ВЕРСИЯ:

# temp_list = [number_list[0]]
# number_list.pop(0)

# for i in number_list:
#     for j in range(len(temp_list)):
#         if i != temp_list[j]:
#             counter += 1
#             # print(counter)
#     if counter == len(temp_list):
#         temp_list.append(i)
#         counter = 0                           // ТУТ ЛИШНИЙ ПРОБЕЛ

# print(len(temp_list), temp_list)
# print(number_list)



                                    # ВЕРНОЕ РЕШЕНИЕ №1:

# num_list = set([1, 1, 2, 0, -1, 3, 4, 4])
# print(len(num_list), num_list)



                                    # ВЕРНОЕ РЕШЕНИЕ №2:
                                    
# number_list = [1, 1, -1, 1, -2, 1, 2, 0, 4, -1, 3, 1, 4, 4]
# counter = 0

# temp = [number_list[0]]

# counter = 0

# for el in number_list:
#     for i in range(len(temp)):
#         if el != temp[i]:
#             counter += 1
#     if counter == len(temp):
#         temp.append(el)
#     counter = 0
        

# print(f"temp : {temp},   counter = {counter},    length = {len(temp)},   temp = {temp}")












# for i in range(1, 10, 2), range(-10, 10, 1), range(1, 15, 2):
#     print(i.step)
    # for j in range(i.start, i.stop, i.step):
    #     print(i.)


# d = dict()
# d = {3: 15}
# print(d.key)