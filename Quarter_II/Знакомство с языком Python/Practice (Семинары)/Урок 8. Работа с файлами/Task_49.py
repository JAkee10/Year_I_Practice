    # Задача №49

# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
#    текстовом файле
# 3. Пользователь может ввести одну из
#   характеристик для поиска определенной
#   записи(Например имя или фамилию
#   человека)
# 4. Использование функций. Ваша программа
#   не должна быть линейной

import os.path

os.system('cls')

def ToCreate():                               # Создание нового файла(справочника) 
    with open('tel_directory.txt', 'w') as data:
        data.writelines("Directory: \n")

def ToAdd():                                  # Добавление записи в справочник 
    os.system('cls')

    tel = input(f"Введи номер телефона: ")
    name = input(f"Введи имя владельца: ")
    s_name = input(f"Введи фамилию владельца: ")
    t_name = input(f"Введи отчество владельца: ")
    user = f"{tel}, {name}, {s_name}, {t_name};\n"
    if IsInDirectory(user):
        pass
    else:
        with open('tel_directory.txt', 'a') as data:
            print(user)
            data.writelines(user)
    
def IsInDirectory(user_to_check):             # Проверка на наличие данной записи 
    with open('tel_directory.txt', 'r') as data:
        counter = 0
        for i in data:
            if user_to_check == i:
                hit = i
                counter += 1
        if counter == 0:
            print(f"\nНовая запись успешно создана")
            return False
        else:
            print(f"\n\033[1mДанная запись уже имеется\033[0m")
            print(f"{hit}")
            return True

def ToPrint():                                # Вывод всего справочника 
    os.system('cls')

    with open('tel_directory.txt', 'r') as data:
        counter = 0
        
        for i in data:
            if counter == 0:
                print(f'{i}')
            else:
                print(f'{counter} - {i}')
            counter += 1
        
def ToFind():                                 # Поиск записи по одной из характеристик 
    os.system('cls')

    var = input(f"Введи одну из характеристик для поиска: ")
    file = list()

    with open('tel_directory.txt', 'r') as data:
        file = [x.replace(';\n', '') for x in data]

    file.pop(0)

    counter = 0
    first_hit = True

    for line in file:
        for el in line.split(', '):
            if el == var:
                if first_hit:
                    print(f"\nРезультаты поиска:")
                    first_hit = False
                print(line)
                counter += 1
    if counter == 0:
        return print(f"\nСовпадений не найдено")
    else:
        return




work_on = True
file_created = True
mistake = False

if not os.path.isfile('tel_directory.txt'):
    file_created = False

while work_on:
    if not file_created:
        ToCreate()
        file_created = True
        continue

    if mistake:
        os.system('cls')
        print("Возможные варианты ответа \033[4m{}\033[0m: \033[1m\033[31m{}\033[0m, \033[1m\033[35m{}\033[0m и \033[1m\033[34m{}\033[0m!".format('только', '1', '2', '3'))
        print("Для выхода введите: exit")
        mistake = False

    user_input = input("\nВыбери действие : \033[1m\033[31m{}\033[0m - Вывести все данные ; \033[1m\033[35m{}\033[0m - Добавить запись ; \033[1m\033[34m{}\033[0m - Поиск записи с выводом\n".format('1', '2', '3'))
    if user_input == '1':
        ToPrint()
    elif user_input == '2':
        ToAdd()
    elif user_input == '3':
        ToFind()
    elif user_input == 'exit':
        work_on = False
    else:
        mistake = True























