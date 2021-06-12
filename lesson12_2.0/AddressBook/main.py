from pathlib import Path
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
    '''
        Добавляю запись (словарь, содержащий имя, телефон и если есть ДР)
        в телефонную книгу.
        ЕСТЬ НЕРЕШЕННАЯ ПРОБЛЕМА С ПРОВЕРКОЙ НА НАЛИЧИИ УЖЕ ВНЕСЕННОГО ИМЕНИ!!!
        как получить доступ к аттрибутам объектов(полей) в объекте(рекорд/словарь)?
    '''
    for item in book:
        for value in item.values():
            if value == cmd[1]:
                return f'\nThe contact is already in the phone book.'
            else:
                record = Record()
                if len(cmd) >= 4:
                    record.create_record(cmd[1], cmd[2], cmd[3])
                else:
                    record.create_record(cmd[1], cmd[2])
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
    '''
        Разбиваю введенные данные на список строк, содержащий комманду и входные аргументы (имя, телефон, ДР)
        Далее доступ к ним по индексу.
    '''
    return string.split(' ')


@input_error
def phone(cmd):
    for item in book:
        if cmd[1] in item:
            return item
        else:
            print(f'Record with name {cmd[1]} not found.')


def show_all(*args):
    '''
        Благодаря магическому методу __str__, выводится простыня адресной книги.
        Нужно доработать вывод с пагинацией.
    '''
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


def save_data(save_book):
    with open(phonebook_file, 'wb') as file:
        print('SAVE')
        pickle.dump(save_book, file)


def load_data():
    with open(phonebook_file, 'rb') as file:
        print('LOADING...')
        return pickle.load(file)


def check_addressbook_data():
    """
        Проверка на наличие файла с адресной книгой.
        Если его нет, то создаю пустой экземпляр класса и присваиваю ему указатель book.
        Если есть такой файл, загружаю содержимое и также помечаю book.
        Далее работаю только с book. При выходе автоматически сохраняю.
    """
    for file in Path.cwd().iterdir():
        if file.name == 'AddressBook.bin':
            print('FILE FOUND')
            return load_data()
        else:
            continue
    print('FILE NOT FOUND. CREATING ADDRESSBOOK...')
    return AddressBook()


def main():
    while True:
        string = input('\nEnter your command (hello, add, delete, change, phone, show_all or exit):\n')
        cmd = parser(string)
        if cmd[0].lower() in EXIT_COMMANDS:
            # сохраняю введенные данные на диск
            save_data(book)
            print(bye())
            break
        else:
            print(get_handler(cmd[0].lower())(cmd))


phonebook_file = 'AddressBook.bin'
book = check_addressbook_data()


if __name__ == "__main__":
    main()
