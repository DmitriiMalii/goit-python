from collections import UserDict


class AddressBook(UserDict):

    def add_recored(self, record):
        self.data[record] = record


class Record:

    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, phone):
        pass


class Field:

    pass


class Name(Field):

    def __init__(self, name):
        self.name = name


class Phone(Field):

    def __init__(self, phone):
        self.phone = phone
