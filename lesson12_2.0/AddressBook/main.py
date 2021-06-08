from phone_book_new import *


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print(f'\nInvalid command. Try again...')
            return back_to_main
        except IndexError:
            print('\nGive me name and phone, please.')
            return back_to_main(*args, **kwargs)
    return inner


@input_error
def add(cmd):
    for item in book:
        if cmd[1] in item:
            return f'\nThe contact is already in the phone book.'
        else:
            record = Record()
            record.create_record(cmd[1], cmd[2], cmd[3])
            book.add_record(record)
    return f'\nContact {cmd[1]} has been added.'


def back_to_main(*args, **kwargs):
    return f''


def bye(*args):
    return f'\nGood bye!'


@input_error
def change(cmd):
    for item in book:
        if cmd[1] in item:
            item.update({'phone': cmd[2]})
    return f'\nContact {cmd[1]} has been updated.'


def delete(cmd):
    for item in book:
        if cmd[1] in item:
            index = item.__index__()
            book.remove_record(index)
            print(f'Record with name: {cmd[1]} deleted.')
            break
        else:
            print(f'Record with name: {cmd[1]} not found.')


@input_error
def get_handler(command):
    return COMMANDS[command]


def hello(*args):
    return f'\nHow can I help you?'


def parser(string):
    return string.split(' ')


@input_error
def phone(cmd):
    for item in book:
        if cmd[1] in item:
            return item
        else:
            print(f'Record with name: {cmd[1]} not found.')


def show_all(*args):
    return book


COMMANDS = {
            'hello': hello,
            'add': add,
            'delete': delete,
            'change': change,
            'phone': phone,
            'show_all': show_all

}

EXIT_COMMANDS = {
                'exit': '',
                'close': '',
                'good': ''
}

book = AddressBook()


def main():
    book.load_data()
    while True:
        string = input('\nEnter your command (hello, add, delete, change, phone, show_all or exit):\n')
        cmd = parser(string)
        if cmd[0].lower() in EXIT_COMMANDS:
            book.save_data()
            print(bye())
            break
        else:
            print(get_handler(cmd[0].lower())(cmd))


if __name__ == "__main__":
    main()
