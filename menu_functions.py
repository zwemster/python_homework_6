import names_base


def print_whole_base():                     # выводит на экран все записи телефонного справочника
    with open('phonebook.csv', 'r') as file:
        whole_file_line = file.readlines()
        for i in range(len(whole_file_line)):
            print(whole_file_line[i])


def search_by_surname(input_surname):       # поиск номера телефона по фамилии абонента
    with open('phonebook.csv', 'r') as file:
        if input_surname in names_base.surnames or input_surname[:-1] in names_base.surnames:
            whole_file_line = file.readlines()
            for i in range(len(whole_file_line)):
                desired_surname = (whole_file_line[i]).split("; ")
                if input_surname in desired_surname:
                    print(desired_surname)
        else:
            print('Человек с такой фамилией в базе не числится')


def search_by_name(input_name):             # поиск номера телефона по имени абонента
    with open('phonebook.csv', 'r') as file:
        if input_name in names_base.male_names or input_name in names_base.female_names:
            whole_file_line = file.readlines()
            for i in range(len(whole_file_line)):
                desired_name = (whole_file_line[i]).split("; ")
                if input_name in desired_name:
                    print(desired_name)
        else:
            print('Человек с таким именем в базе не числится')


def search_by_phone_number(input_number):   # поиск имени абонента по номеру телефона
    with open('phonebook.csv', 'r') as file:
        switch = 0
        whole_file_line = file.readlines()
        for i in range(len(whole_file_line)):
            desired_name = (whole_file_line[i]).split("; ")
            if input_number in desired_name:
                switch = 1
                print(desired_name)
        if switch == 0:
            print('Данный номер телефона отсутствует в базе.')


def add_new_note():                         # добавляет новую запись в телефонный справочник
    person_surname = input('Введите фамилию: ')
    if person_surname not in names_base.surnames or person_surname[:-1] not in names_base.surnames:
        names_base.surnames.append(person_surname)
    person_name = input('Введите имя: ')
    if person_name not in names_base.female_names and person_surname[len(person_name) - 1] not in ['а', 'я']:
        names_base.female_names.append(person_name)
    else:
        names_base.male_names.append(person_name)
    phone_number = input('Введите номер телефона (11 цифр начиная с цифры 8): ')
    try:
        while int(phone_number) < 89000000000 or int(phone_number) > 90000000000:
            print('Некорректный номер телефона. Повторите ввод: ')
            phone_number = input()
    except ValueError:
        print('Некорректный номер телефона. Повторите ввод: ')
        phone_number = input()
        while int(phone_number) < 89000000000 or int(phone_number) > 90000000000:
            print('Некорректный номер телефона. Повторите ввод: ')
            phone_number = input()
    email_address = input('Введите адрес электронной почты: ')
    with open('phonebook.csv', 'r') as file:
        whole_file_line = file.readlines()
        index = len(whole_file_line)
    with open('phonebook.csv', 'a') as file:
        file.write(('{}; {}; {}; {}; {}\n'
                    .format(index, person_surname, person_name, phone_number, email_address)))
