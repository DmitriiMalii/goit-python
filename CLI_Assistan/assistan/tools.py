from datetime import datetime, timedelta
import json
from pathlib import Path
from assistan.add_contacts import add_phone, add_email, add_birthday, add_note
from assistan.validation import check_note


def find_contact(address_book):
    user_input = input('ENTER SEARCH NAME >> ')
    for key in address_book:
        if check_note(key, user_input):
            return address_book.get(key)
    return 'CONTACT NOT FOUND'


def find_note_by_tag(address_book):
    """Scan note by tag"""
    user_input = input('ENTER SEARCH TAG >> ')
    result = {}
    for key in address_book:
        val = address_book.get(key)
        note = str([k for k in val[3]])
        if user_input in note:
            result.update({key: list(val[3].values())[0]})
    return f'FOR TAG "{user_input}" FOUND {result}'


def find_note_by_keyword(address_book):
    """Scan note by keyword"""
    user_input = input('ENTER KEYWORD FOR SEARCH >> ')
    result = {}
    for key in address_book:
        val = address_book.get(key)
        note = list(val[3].values())[0]
        if check_note(note, user_input):
            result.update({key: note})
    return result if result else f'NO MATCHES FOUND!'


def change_contact(address_book):
    """Replace one of the following value: 'phone', 'email', 'birthday', 'note'"""
    user_input = input('ENTER THE NAME OF THE CONTACT TO CHANGE >> ')
    for key in address_book:
        if key == user_input:
            while True:
                value_input = input('ENTER THE VALUE YOU WANT TO REPLACE PHONE/E-MAIL/BIRTHDAY/NOTE >> ')
                if value_input.lower() in ('phone', 'email', 'birthday', 'note'):
                    if value_input.lower() == 'phone':
                        val = address_book.get(key)
                        val[0].clear()
                        val[0].extend(add_phone())
                        return f'PHONE FOR {key} CHANGED'
                    elif value_input.lower() == 'email':
                        val = address_book.get(key)
                        val[1].clear()
                        val[1].extend(add_email())
                        return f'E-MAIL FOR {key} CHANGED'
                    elif value_input.lower() == 'birthday':
                        val = address_book.get(key)
                        val[2].replace(val[2], add_birthday())
                        return f'BIRTHDAY FOR {key} CHANGED'
                    else:
                        val = address_book.get(key)
                        val[3].clear()
                        val[3].update(add_note())
                        return f'NOTE FOR {key} CHANGED'
                else:
                    print('YOU ENTERED WRONG VALUE!')
                    continue
    return 'CONTACT NOT FOUND'


def del_contact(address_book):
    user_input = input('INPUT NAME TO REMOVE >> ')
    for key in address_book:
        if key == user_input:
            del address_book[key]
            return 'CONTACT HAS BEEN REMOVED'
    return 'CONTACT NOT FOUND'


def check_addressbook_data():
    for file in Path.cwd().iterdir():
        if file.name == 'AddressBook.json':
            return load_data()
        else:
            continue
    return {}


def convert_in_datetime(date):
    """Convert string with birthday from dd/mm/yyyy to datetime object"""
    convert_date = datetime(year=int(date[6:]), month=int(date[3:5]), day=int(date[0:2]))
    return convert_date


def check_birthday_day(address_book):
    """Return contact's birthday through N days"""
    n = int(input('ENTER NUMBER OF DAYS TO SEARCH >> '))
    delta = timedelta(days=n)
    d1 = datetime.now().date()
    d2 = d1 + delta
    result = {}
    for key in address_book:
        val = address_book.get(key)
        if convert_in_datetime(val[2]).day == d2.day:
            result.update({key: val[2]})
    return result


def save_data(save_book):
    with open('AddressBook.json', 'w') as fh:
        json.dump(save_book, fh)


def load_data():
    with open('AddressBook.json', 'r') as fh:
        return json.load(fh)
