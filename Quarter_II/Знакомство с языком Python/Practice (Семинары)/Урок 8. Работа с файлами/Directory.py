import os.path

os.system('cls')

fields = ['Номер', 'Имя', 'Фамилия', 'Отчество']

def ToCreate(filename):                                     # Создание нового файла(справочника) 
    with open(filename, 'w', encoding='utf-8') as data:
        data.writelines("Directory:\n")

def get_file(filename):                                     # Возвращает список словарей 
    all_lines = []

    with open(filename, 'r', encoding= 'utf-8') as phonebook:
        for line in phonebook:
            one_line = dict(zip(fields, line.replace(';\n', '').replace(':\n','').split(', ')))
            all_lines.append(one_line)
    return all_lines

def write_file(filename, file):                             # Записывает 'file' в файл 'filename' 
    with open(filename, 'w', encoding= "utf-8") as phonebook:
        phonebook.write("Directory:\n")
        for i in range(len(file)):
            line = ''
            for key in fields:
                line += f"{file[i][key]}, "
            phonebook.write(line[:-2] + ";\n")

def add_note(filename, file):                               # Добавление записи в all_file 
    
    print(f"\033[1mНовая запись\033[0m\n")
    tel = input(f"Введи номер телефона: ")
    name = input(f"Введи имя владельца: ")
    s_name = input(f"Введи фамилию владельца: ")
    t_name = input(f"Введи отчество владельца: ")
    user = f"{tel}, {name}, {s_name}, {t_name};\n"
    if is_in_directory(filename, user):
        return file
    else:
        file.append(dict(zip(fields, user.replace(';\n', '').split(', '))))
        print_file([file[-1]])
        return file

def is_in_directory(filename, word_to_check):               # Проверка на наличие данной записи 
    with open(filename, 'r', encoding='utf-8') as phonebook:
        counter = 0
        for i in phonebook:
            if word_to_check == i:
                hit = i
                counter += 1
        if counter == 0:
            os.system('cls')
            print(f"\n\033[1mНовая запись успешно создана\033[0m")
            return False
        else:
            os.system('cls')
            print(f"\n\033[1mДанная запись уже имеется\033[0m")
            print(f"{hit}")
            return True

def print_file(file):                                       # Печать файла в терминал 
    # os.system('cls')
    
    res = list()
    for i in range(len(file)):
        temp = ''
        for key in fields:
            temp += f"{file[i][key]}, "
        res.append(temp[:-2])

    if len(res) > 1:
        print(f"\033[1mDirectory:\033[0m\n")
        for i in range(len(res)):
            print(f"{i+1} - {res[i]}")
    elif len(res) == 1:
        for i in range(len(res)):
            print(f"{res[i]}")
    else:
        for i in range(len(res)):
            print(f"{i+1} - {res[i]}")
        
def find_note(file, user_inp):                              # Поиск записи по одной из характеристик 
    word = input(f"Введи одну из характеристик для поиска записи(ей): ")
    print()
    found_index = [i for i in range(len(file)) if word in file[i].values()]
    found = [file[i] for i in found_index]
    found_index = dict(zip([x for x in range(1, len(found_index) + 1)], found_index))
    if user_inp == '4' or user_inp == '5':
        return found + [found_index]
    elif len(found) == 1:
        return found + [0]
    elif len(found) == 0:
        print(f"\033[4mЗапись не найдена!\033[0m")
        return found
    else:
        return found
            
def change_number(main_file, choice_file):                  # Логика замены номера в выбранной записи 
    the_file = choice_file[:-1]
    ids = choice_file[-1]
    if len(the_file) > 1:
        print_file(the_file)
        user_inp = int(input(f"\nВыбери какую запись хочешь изменить (1 - {len(the_file)}): "))
        print()
        if 0 < user_inp < len(the_file) + 1:
            print(len(the_file))
            return change(main_file, choice_file, ids, user_inp)
        else:
            print(f"Введи число от 1 до {len(the_file)}")
            return main_file
    else:
        return change(main_file, the_file, ids)
  
def change(main_file, the_file, ids, user_inp = 1):         # Замена номера 
    os.system('cls')
    print("\033[1mРедактирование записи\033[0m\n")
    if len(the_file) == 0:
        print(f'\033[4mЗапись не найдена!\033[0m')
        return main_file
    else:
        print_file([the_file[user_inp - 1]])
    print()
    new_tel = input(f"Введи новый номер телфона: ")
    main_file[ids[user_inp]][fields[0]] = new_tel 

    os.system('cls')
    print(f"\033[1mЗапись успешно изменена!\033[0m\n")
    print_file([the_file[user_inp - 1]])
    return main_file

def delete_note(main_file, choice_file):                    # Удаление записи 
    the_file = choice_file[:-1]
    ids = choice_file[-1]
    if len(the_file) > 1:
        print_file(the_file)
        user_inp = int(input(f"\nВыбери какую запись хочешь удалить (1 - {len(the_file)}): "))
        print()
        x = main_file.pop(ids[user_inp])
        os.system('cls')
        print("\033[1mЗапись успешно удалена!\033[0m\n")
        print_file([x])
        return main_file
    elif len(the_file) == 1:
        index = 0
        for i in range(len(main_file)):
            if the_file == [main_file[i]]:
                index = i
            # else:
            #     print("\033[1mЗапись не была найдена!\033[0m\n")
            #     return main_file
        os.system('cls')
        print("\033[1mЗапись успешно удалена!\033[0m\n")
        x = main_file.pop(index)
        print_file([x])
        return main_file
    else:
        print(f"\033[4mЗапись не найдена!\033[0m")
        return main_file

        
    


is_on = True

file_created = True
mistake = False

if not os.path.isfile('tel_directory.txt'):
    file_created = False

while is_on:
    file_name = 'tel_directory.txt'

    if not file_created:
        ToCreate(file_name)
        file_created = True
        continue

    all_file = get_file(file_name)
    all_file.pop(0)

    if mistake:
        os.system('cls')
        print("Возможные варианты ответа \033[4m{}\033[0m: \033[1m\033[31m{}\033[0m, \033[1m\033[35m{}\033[0m, \033[1m\033[34m{}\033[0m, \033[1m\033[32m{}\033[0m и \033[1m\033[33m{}\033[0m!".format('только', '1', '2', '3', '4', '5'))
        print("Для выхода введите: exit")
        mistake = False

    user_input = input("\nВыбери действие : \033[1m\033[31m{}\033[0m - Вывести все данные ; \033[1m\033[35m{}\033[0m - Добавить запись ; \033[1m\033[34m{}\033[0m - Поиск записи с выводом ; \033[1m\033[32m{}\033[0m - Изменить номер телефона ; \033[1m\033[33m{}\033[0m - Удалить запись\n".format('1', '2', '3', '4', '5'))
    
    if user_input == '1':
        os.system('cls')
        if len(all_file) > 0:
            print_file(all_file)
        else:
            print(f"\033[4mСправочник пуст, добавь запись!\033[0m")

    elif user_input == '2':
        os.system('cls')
        write_file(file_name, add_note(file_name, all_file))

    elif user_input == '3':
        os.system('cls')
        print_file(find_note(all_file, user_input))

    elif user_input == '4':
        os.system('cls')
        write_file(file_name, change_number(all_file, find_note(all_file, user_input)))

    elif user_input == '5':
        os.system('cls')
        write_file(file_name, delete_note(all_file, find_note(all_file, user_input)))

    elif user_input == 'exit':
        work_on = False

    else:
        mistake = True