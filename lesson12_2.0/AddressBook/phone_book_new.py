import pickle


class AddressBook(object):
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

    def add_record(self, record):
        self.phonebook.append(record)

    def search(self, string):
        for item in self.phonebook:
            for key in item:
                if key == string:
                    return True
                else:
                    return False

    def remove_record(self, index):
        del self.phonebook[index]

    def save_data(self):
        with open(self.phonebook_file, 'wb') as file:
            pickle.dump(self, file)

    def load_data(self):
        with open(self.phonebook_file, 'rb') as file:
            self.phonebook = pickle.load(file)


class Record(object):
    def __init__(self):
        self.counter = 0
        self.record = {}

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.record)

    def __next__(self):
        if self.counter < len(self.record):
            self.counter += 1
            return self.record.items()
        raise StopIteration

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
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"


class Name(RecordField):
    pass


class Phone(RecordField):
    pass


class Birthday(RecordField):
    pass


# book = AddressBook()
#
# name1 = Name('Alex')
# phone1 = Phone('0951225888')
# birthday1 = Birthday('18/04/2006')
# record1 = Record()
# record1.create_record(name1, phone1, birthday1)
# book.add_record(record1)
#
# name2 = Name('Dima')
# phone2 = Phone('0503270404')
# record2 = Record()
# record2.create_record(name2, phone2)
# book.add_record(record2)
#
# for i in book:
#     print(i)



