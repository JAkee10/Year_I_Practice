# Задача №33

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


# grades_count = int(input(f"Введи количество оценок: "))
# grades = [int(input(f"Оценка {i+1}: ")) for i in range(grades_count)]

# max_grade = str(max(grades))
# min_grade = str(min(grades))

# print(max_grade)

# string_grades = ''
# for el in grades:
#     string_grades += str(el) + " "
# new_grades = string_grades.replace(max_grade, min_grade).split()

# print(new_grades)