import sys
from phone_base_generator import *
from user_interface import *


def interaction_method():
    phonebook_wk = True
    while phonebook_wk:
        print('Сгенерировать новый телефонный справочник и работать с ним? (y/n)')
        working_with_new_book = input()
        if str(working_with_new_book) == 'y':
            logger.logging.info('The user chose to generate a new phone book')
            phone_base_header()
            base_generator()

            phonebook_cover()
            phonebook_menu()
            user_choice()
            sys.exit('Благодарю за использование.')
        elif str(working_with_new_book) == 'n':
            logger.logging.info('The user chose not to generate a new phone book')
            print('Использовать уже имеющийся телефонный справочник? (y/n)')
            working_with_actual_book = input()
            if str(working_with_actual_book) == 'y':
                logger.logging.info('The user chose to use an existing phone book')
                phonebook_cover()
                phonebook_menu()
                user_choice()
                sys.exit('Благодарю за использование.')
            elif str(working_with_actual_book) == 'n':
                logger.logging.info('The user chose not work with phone book')
                print('Что ж...до свидания.')
                logger.logging.info('Shutdown')
                phonebook_wk = False
        else:
            print('Ошибка! Введите латинскую букву "y" или "n": ')
            logger.logging.info('The user entered an invalid value')
            input()
