class AddressBook(object):
    '''
        Адресная книга представляет собой список, содержащий словари/рекорды с полями/fields
    '''
    def __init__(self):
        self.counter = -1
        self.phonebook = []
        self.phonebook_file = 'AddressBook.bin'

    def __len__(self):
        return len(self.phonebook)

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter < len(self.phonebook):
            return self.phonebook[self.counter]
        raise StopIteration

    def __str__(self):
        result = ''
        for record in self.phonebook:
            result += f'{str(record)}\n'
        return result

    def __setitem__(self, value):
        self.phonebook.append(value)

    def __getitem__(self, index):
        return self.phonebook[index]

    def add_record(self, record):
        self.phonebook.append(record)

    def remove_record(self, index):
        del self.phonebook[index]


class Record:
    def __init__(self):
        self.counter = 0
        self.record = {}

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.record)

    def __next__(self):
        if self.counter >= len(self.record):
            self.counter += 1
            return self.record.values()
        raise StopIteration

    def __setitem__(self, key, value):
        self.record[key] = value

    def __getitem__(self, key):
        return self.record[key]

    def __str__(self):
        result = ""
        for key, value in self.record.items():
            result += f"{key} : {str(value)}\n"
        return result + f'{20 * "="}'

    def create_record(self, name, phone, birthday=None):
        if birthday:
            self.record['name'] = name
            self.record['phone'] = phone
            self.record['birthday'] = birthday
        else:
            self.record['name'] = name
            self.record['phone'] = phone


class RecordField(object):
    def __init__(self):
        self.__value = None

    def __str__(self):
        return f"{self.__value}"


class Name(RecordField):
    def __init__(self, name):
        super().__init__()
        self.name = name


class Phone(RecordField):
    def __init__(self, phone):
        super().__init__()
        self.phone = phone

    @property
    def phone(self):
        return self.__value

    @phone.setter
    def phone(self, phone):
        if phone.isdigit():
            self.__value = phone
        else:
            raise Exception('Please, enter a valid phone number')


class Birthday(RecordField):
    def __init__(self, birthday):
        super().__init__()
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__value

    @birthday.setter
    def birthday(self, birthday):
        if birthday.isdigit() and len(birthday) == 8:
            self.__value = birthday
        else:
            raise Exception('Please, enter a valid date birthday')
