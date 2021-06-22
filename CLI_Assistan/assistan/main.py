from add_contacts import *
from sort_files import sort_files_in_directory
from tools import *


address_book = check_addressbook_data()

COMMANDS = {
    '1': add_contact,
    '2': find_contact,
    '3': change_contact,
    '4': del_contact,
    '5': check_birthday_day,
    '6': find_note_by_tag,
    '7': find_note_by_keyword,
}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print(f'Invalid command. Try again...')
            return back_to_main
    return inner


def back_to_main(*args):
    return f''


@input_error
def get_handler(command):
    return COMMANDS[command]


def main():
    while True:
        print('\nPlease choose one of the supported commands:\n\
            1 - ADD CONTACT\n\
            2 - FIND CONTACT\n\
            3 - CHANGE CONTACT\n\
            4 - DELETE CONTACT\n\
            5 - CHECK BIRTHDAY DAY\n\
            6 - FIND NOTE BY TAG\n\
            7 - FIND NOTE BY KEYWORD\n\
            8 - SORT FILES IN THE SPECIFIED DIRECTORY\n\
            0 - EXIT')
        user_input = input('\nENTER COMMAND, PLEASE >> ')
        if user_input == '0':
            # сохраняю текущее состояние книги на диск
            save_data(address_book)
            print('BYE!')
            break
        elif user_input == '8':
            sort_files_in_directory()
        else:
            print(get_handler(user_input)(address_book))


if __name__ == '__main__':
    main()
