# Задача №3.

# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

studentCount = 0
inClassTableCount = 0
totalTableCount = 0
i = 1
flag = True

while (flag):
    if (i <= 3):
        studentCount = int(input(f"Введите количество учеников в {i} классе: "))
        inClassTableCount = -(-studentCount // 5)
        print("На {} студента(ов) в {} классе требуется минимум {} парт(а)".format(studentCount, i, inClassTableCount))
        print()
        totalTableCount += inClassTableCount
        i += 1
    else:
        print("На все 3 класса требуется минимум {} парт(а)".format(totalTableCount))
        flag = False