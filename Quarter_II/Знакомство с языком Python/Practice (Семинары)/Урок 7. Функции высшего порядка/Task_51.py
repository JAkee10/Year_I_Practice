# Задача №51

# Напишите функцию same_by(characteristic, objects), которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция 
# должна возвращать True. 
# Аргумент characteristic - это функция, которая 
# принимает объект и вычисляет его характеристику.

# Ввод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")

# Вывод:
# same

def same_by(characteristic, objects):
    if objects == []:
        return True
    else:
        true_count = 1
        false_count = 0
        temp = characteristic(objects[0])
        # print(f"temp = {temp}")
        for el in objects[1:]:
            # print(el)
            if characteristic(el) == temp:
                true_count += 1
            else:
                false_count += 1
        if not true_count or  not false_count:
            return True
        else:
            return False


values = [6, 1, 4]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")
