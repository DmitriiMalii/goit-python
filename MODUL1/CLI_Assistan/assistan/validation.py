import re


def check_name(address_book, name):
    for key in address_book:
        if key == name:
            print(f'CONTACT ALREADY EXISTS. ENTER ANOTHER NAME')
            return None
    return name


def check_note(note, keyword):
    keyword = f'\\b{keyword}\\b'
    result = re.search(keyword, note)
    return result


def check_phone(phone):
    pattern = r'^\+?3?8?(0\d{9})$'
    reg_obj = re.compile(pattern)
    result = reg_obj.match(phone)
    return result


def check_email(email):
    pattern = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    reg_obj = re.compile(pattern)
    result = reg_obj.match(email)
    return result


def check_birthday(birthday):
    pattern = r'(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|((29|30)[\/]' \
              r'(0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])(00|04|08|12|16|20|24|28|' \
              r'32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)'
    reg_obj = re.compile(pattern)
    result = reg_obj.match(birthday)
    return result
