import random
from transliterate import slugify
from names_base import *


def phone_base_header():            # создание шапки телефонного справочника
    with open('phonebook.csv', 'w') as file:
        file.write('№ п/п; Фамилия; Имя; Номер телефона; Адрес эл.почты\n')


def names_creator():                # создание случайных комбинаций имён
    sex = random.randint(0, 2)
    if sex == 0:
        name = random.choice(male_names)
        surname = random.choice(surnames)
    else:
        name = random.choice(female_names)
        surname = random.choice(surnames) + 'а'
    # person = name + ' ' + surname
    return name, surname


def phone_numbers_creator():        # создание случайных номеров телефонов
    person_phone_number = random.randint(89000000000, 90000000000)
    return person_phone_number


def email_creator(person_name):     # создание адреса электронной почты с именем, привязанным к имени пользователя
    person_email_address = slugify(person_name) + str(random.randint(1, 9999)) + random.choice(emails)
    return person_email_address


def base_generator():               # генерация файла с телефонной книгой и запись данных пользователей
    for i in range(1, random.randint(100, 500)):
        person_name, person_surname = names_creator()
        phone_number = phone_numbers_creator()
        email_address = email_creator(str(person_name + ' ' + person_surname))
        with open('phonebook.csv', 'a') as file:
            file.write('{}; {}; {}; {}; {}\n'
                       .format(i, person_surname, person_name, phone_number, email_address))
