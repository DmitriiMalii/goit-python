from datetime import datetime
from pathlib import Path
import pickle
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
    '''
    for i in range(len(book)):
        if book[i].__getitem__('name') == cmd[1]:
            return f'\nThe contact is already in the phone book.'
    record = Record()
    if len(cmd) >= 4:
        record.create_record(cmd[1], cmd[2], cmd[3])
    else:
        record.create_record(cmd[1], cmd[2])
    book.add_record(record)
    return f'\nContact {cmd[1]} has been added.'


def back_to_main(*args, **kwargs):
    return f''


def days_to_birthday(cmd):
    '''
        Выводит кол-во дней до ДР.
    '''
    for i in range(len(book)):
        if book[i].__getitem__('name') == cmd[1]:
            birthday = book[i].__getitem__('birthday')
            if birthday:
                b_day = (datetime(year=int(birthday[4:]), month=int(birthday[2:4]),
                                  day=int(birthday[0:2]))).replace(datetime.now().year)
                if b_day.month >= datetime.now().month:
                    return b_day.date() - datetime.now().date()
                else:
                    b_day = datetime(year=b_day.year + 1, month=b_day.month,
                                     day=b_day.day).date()
                    return b_day - datetime.now().date()
    return f'Record with name: {cmd[1]} not found.'


def bye(*args):
    return f'\nGood bye!'


@input_error
def change_phone(cmd):
    '''
        Проверяю. есть ли запись с заданным именем, меняю номер телефона на новый.
    '''
    for i in range(len(book)):
        if book[i].__getitem__('name') == cmd[1]:
            book[i].__setitem__('phone', cmd[2])
            return f'Phone number has been changed'
    return f'Record with name: {cmd[1]} not found.'


def change_birthday(cmd):
    '''
        Проверяю. есть ли запись с заданным именем, меняю ДР контакта на новый.
    '''
    for i in range(len(book)):
        if book[i].__getitem__('name') == cmd[1]:
            book[i].__setitem__('birthday', cmd[2])
            return f'Birthday has been changed'
    return f'Record with name: {cmd[1]} not found.'


def delete(cmd):
    '''
        Удаляю запись с заданным именем.
    '''
    for i in range(len(book)):
        if book[i].__getitem__('name') == cmd[1]:
            index = i.__index__()
            book.remove_record(index)
            return f'Record with name: {cmd[1]} deleted.'
    return f'Record with name: {cmd[1]} not found.'


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
    '''
        Ищу и вывожу в консоль номер телефона контакта по имени.
    '''
    for i in range(len(book)):
        if book[i].__getitem__('name') == cmd[1]:
            phone = book[i].__getitem__('phone')
            return f'{cmd[1]}: {phone}.'
    return f'Record with name: {cmd[1]} not found.'


def show_all(cmd):
    '''
        Вывод с пагинацией. Кол-во выводимых за один раз записей задается после комманды show_all
        Если кол-во не задано, то выводится вся книга.
    '''
    if len(cmd) >= 2:
        step = int(cmd[1])
        count = 0
        while count < len(book):
            new_book = book[count:]
            for i in range(len(new_book[0:step])):
                print(new_book[i])
            count += step
            input()
    else:
        return book
    return f'Finish'


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


COMMANDS = {
    'hello': hello,
    'add': add,
    'delete': delete,
    'change_phone': change_phone,
    'change_birthday': change_birthday,
    'phone': phone,
    'birthday': days_to_birthday,
    'show_all': show_all

}

EXIT_COMMANDS = {
    'exit': '',
    'close': '',
    'good': ''
}


def main():
    while True:
        string = input(
            '\nEnter your command (hello, add, delete, change_phone, change_birthday, phone, show_all or exit):\n')
        cmd = parser(string)
        if cmd[0].lower() in EXIT_COMMANDS:
            # сохраняю текущее состояние книги на диск
            save_data(book)
            print(bye())
            break
        else:
            print(get_handler(cmd[0].lower())(cmd))


phonebook_file = 'AddressBook.bin'
book = check_addressbook_data()


if __name__ == "__main__":
    main()
