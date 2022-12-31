import shutil
import logger
from menu_functions import *


def phonebook_cover():      # обложка телефонного справочника
    phonebook_info = ['=' * 41, 'Т Е Л Е Ф О Н Н Ы Й   С П Р А В О Ч Н И К', '=' * 41]
    width = shutil.get_terminal_size().columns
    position = (width - max(map(len, phonebook_info))) // 2
    for info in phonebook_info:
        print(info.center(width))


def phonebook_menu():       # меню телфонного справочника
    print('\tМ Е Н Ю')
    print('\t1. Вывести все записи на экран.')
    print('\t2. Найти номер телефона по фамилии абонента.')
    print('\t3. Найти номер телефона по имени абонента.')
    print('\t4. Узнать имя абонента по номеру телефона.')
    print('\t5. Добавить новую запись.')
    print('\t6. Закрыть телефонный справочник.')


def user_choice():      # взаимодействие пользователя с меню
    phonebook_work = True
    while phonebook_work:
        choice = input('\n\tВыберите пункт меню: ')
        if int(choice) == 1:
            logger.logging.info('User selected item 1')
            print_whole_base()
        elif int(choice) == 2:
            logger.logging.info('User selected item 2')
            search_surname = input('Введите фамилию: ')
            logger.logging.info(f'User entered {search_surname}')
            search_by_surname(search_surname)
        elif int(choice) == 3:
            logger.logging.info('User selected item 3')
            search_name = input('Введите имя: ')
            logger.logging.info(f'User entered {search_name}')
            search_by_name(search_name)
        elif int(choice) == 4:
            logger.logging.info('User selected item 4')
            search_phone_number = input('Введите номер телефона: ')
            logger.logging.info(f'User entered {search_phone_number}')
            search_by_phone_number(search_phone_number)
        elif int(choice) == 5:
            logger.logging.info('User selected item 5')
            add_new_note()
        elif int(choice) == 6:
            logger.logging.info('User selected item 6')
            print('Закрытие телефонной книги...')
            logger.logging.info('Shutdown')
            phonebook_work = False
        else:
            print('Введён некорректный номер пункта меню. Повторите ввод.')
            logger.logging.info('The user entered an invalid value')