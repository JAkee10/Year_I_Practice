    # Задача №49

# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет 
# самую большую площадь. 

# Напишите функцию find_farthest_orbit(list_of_orbits), 
# которая среди списка орбит планет найдет ту, по которой 
# вращается самая далекая планета. Круговые орбиты не учитывайте: 
# вы знаете, что у вашей звезды таких планет нет, зато 
# искусственные спутники были запущены на круговые орбиты.

# Результатом функции должен быть кортеж, содержащий длины 
# полуосей эллипса орбиты самой далекой планеты. Каждая орбита 
# представляет из себя кортеж из пары чисел - полуосей ее 
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, 
# где a и b - длины полуосей эллипса. При решении задачи 
# используйте списочные выражения.

# Подсказка: проще всего будет найти эллипс в два шага: 
# сначала вычислить самую большую площадь эллипса, 
# а затем найти и сам эллипс, имеющий такую площадь. 
# Гарантируется, что самая далекая планета ровно одна

#     Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

#     Вывод:
# 2.5, 10

#---------------------------------------------------------------МОЁ_РЕШЕНИЕ--------------------------------------------------------------------------

# def find_farthest_orbit(list_of_orbits):
#     # list_of_square = list(map(lambda el: math.pi * el[0] * el[1], list_of_orbits))
#     # return orbits[list_of_square.index(max((list_of_square)))]
#     maximum = max(list_of_orbits, key= lambda x: x[0] * x[1] * (x[0] != x[1]))
#     return maximum

#-------------------------------------------------------------РЕШЕНИЕ_ПРЕПОДА------------------------------------------------------------------------

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(max(orbits, key= lambda x: x[0] * x[1] * (x[0] != x[1])))






# def find_farthest_orbit(list_of_orbits):
#     farthest = max(map(lambda el: math.pi * el[0] * el[1], list_of_orbits))
#     return filter(lambda x: x == farthest, list_of_orbits)

    # return list_of_orbits.remove(list_of_square.index)