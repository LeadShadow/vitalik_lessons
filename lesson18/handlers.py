import re
from decorator import input_error


def hello(*args):
    return 'Hello! How can I help you?'


# ('Oleksandr', '+380937316049')
def verify_phone(phone):
    new_phone = re.sub(r'\+|\(|\)|-| | [a-zA-ZА-Яа-я]', '', phone)
    return new_phone


@input_error
def add_contact(contacts, *args):
    name, phone = args[0], args[1]
    phone = verify_phone(phone)
    contacts[name] = phone
    return f'Added user {name}'


@input_error
def change_contact(contacts, *args):
    name, phone = args[0], args[1]
    contacts[name] = verify_phone(phone)
    return f'Change user {name}'


@input_error
def show_phone(contacts, *args):
    name = args[0]
    return f'User - {name}, phone - {contacts[name]}'


@input_error
def show_all(contacts, *args):
    result = 'List of all users: '
    for name, phone in contacts.items():
        result += '\n|User - {:^10}|phone - {:^15}'.format(name, phone)
    return result


def goodbye(*args):
    return None


def help_me(*args):
    return """Command format:
help or ? - help
hello - func of greeting
add <name> <phone> - add user to addressbook
change <name> <phone> - change the user's phone number
phone <name> - show the user's phone number
show all - show all contacts
close or . or exit or stop - exit the program"""
