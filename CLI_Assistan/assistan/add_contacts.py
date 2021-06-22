from validation import *


"""Addressbook has a structure in the form: dict{name contact: values},
   values = list[phones], list[e-mails], string 'birthday' and dict{tag: note}"""


def add_contact(address_book):
    while True:
        name = add_name()
        if check_name(address_book, name):
            address_book[name] = [add_phone(), add_email(), add_birthday(), add_note()]
            break
        else:
            continue
    return 'CONTACT HAS BEEN ADDED'


def add_name():
    name = input('INPUT YOUR CONTACT NAME >> ')
    return name


def add_phone():
    phone = []
    while True:
        contact_phone = input('INPUT YOUR CONTACT PHONE IN FORMAT +380 >> ')
        if not check_phone(contact_phone):
            print('YOU ENTERED WRONG NUMBER! RE-ENTER, PLEASE')
            continue
        else:
            phone.append(contact_phone)
            print('DO YOU WANT TO ADD ANOTHER NUMBER? Y/n >> ')
            answer = input()
            if answer.lower() == 'y':
                continue
            else:
                break
    return phone


def add_email():
    email = []
    while True:
        contact_email = input('INPUT YOUR CONTACT EMAIL >> ')
        if not check_email(contact_email):
            print('YOU ENTERED WRONG EMAIL! RE-ENTER, PLEASE')
            continue
        else:
            email.append(contact_email)
            print('DO YOU WANT TO ADD ANOTHER EMAIL? Y/n >> ')
            answer = input()
            if answer.lower() == 'y':
                continue
            else:
                break
    return email


def add_birthday():
    while True:
        birthday = input('INPUT YOUR CONTACT BIRTHDAY (DD/MM/YYYY) >> ')
        if not check_birthday(birthday):
            print('YOU ENTERED WRONG BIRTHDAY DATE! RE-ENTER, PLEASE')
            continue
        else:
            break
    return birthday


def add_note():
    tag = input('INPUT TAG FOR YOUR CONTACT NOTE >> ')
    note = input('INPUT YOUR CONTACT NOTE >> ')
    return {tag: note}
