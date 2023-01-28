"""
CONSOLE BOT 2.2
"""

from collections import UserDict
from datetime import datetime
import re
import pickle


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        print(record)

    def iterator(self, n=1):
        index = 1
        print_block = '-' * 100 + '\n'  # блоки виводу, пагінація
        for record in self.data.values():
            print_block += str(record) + '\n'
            if index < n:
                index += 1
            else:
                yield print_block
                index, print_block = 1, '-' * 100 + '\n'
        yield print_block  # повертаємо що залишилось якщо < n


class Filed:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class Name(Filed):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value.title()


class Phone(Filed):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        new_value = (
            new_value.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        if len(new_value) == 12:
            new_value = "+" + new_value
            self._value = new_value
        elif len(new_value) == 10:
            new_value = "+38" + new_value
            self._value = new_value
        else:
            print(f"!!! Entered wrong phone: {new_value}")


class Birthday(Filed):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, birthday):
        try:
            new_value = datetime.strptime(birthday, "%d.%m.%Y").date()
            self._value = new_value
        except ValueError:
            print("ValueError! Enter correct date %dd.%mm.%yyyy")


class Email(Filed):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, email):
        new_email = re.search(r"[a-zA-Z][\w._]+@\w+\.\w{2,}", email)
        if new_email:
            self._value = email
        else:
            print(f"!!! You entered wrong email! {new_email}")


class Address(Filed):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_address):
        self._value = new_address.title()


class Record:
    def __init__(self, name, *phones):
        self.name = name
        self.phones = list(phones)
        self.birthday = "-"
        self.email = "-"
        self.address = "-"

    def __repr__(self):
        return f"name: {self.name}, phone: {self.phones}, email: {self.email}," \
               f" address: {self.address}, birthday: {self.birthday}"

    def add_phone(self, phones):
        self.phones.append(phones)

    def change_phone(self, phone_old, phone_new):
        self.phones.remove(phone_old)
        self.phones.append(phone_new)

    def remove_contact(self, phones):
        self.phones.remove(phones)

    def add_birthday(self, birthday):
        self.birthday = birthday

    def add_email(self, email):
        self.email = email

    def add_address(self, address):
        self.address = address


"""
Функція-decorator для обробки винятків 
"""


def decor_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "IndexError... Enter name or phone please"
        except KeyError:
            return "KeyError..."
        except ValueError:
            return "ValueError..."
        except AttributeError:
            return "AttributeError..."

    return wrapper


"""
Функції handlers відповідають за безпосереднє виконання команд
"""


@decor_error
def hello(*args, **kwargs):
    return "How can I help you?"


@decor_error
def add_phone(*args, **kwargs):
    ab = kwargs.get('ab')
    name = Name(args[0])
    phone = Phone(args[1])
    rec = ab.get(name.value)
    if rec:
        rec.add_phone(phone.value)
    else:
        rec = Record(name, phone.value)
    ab.add_record(rec)
    return f"Contact {name} was created. Phone: {phone}"


@decor_error
def change(*args, **kwargs):
    ab = kwargs.get('ab')
    name = Name(args[0])
    phone_old = Phone(args[1])
    phone_new = Phone(args[2])
    rec = ab.get(name.value)
    if rec:
        rec.change_phone(phone_old.value, phone_new.value)
        ab.add_record(rec)
        return f"Contact {name} was change -> old phone: {phone_old} new phone: {phone_new}"
    else:
        return f"Name {name} don't in AddressBook"


@decor_error
def phone(*args, **kwargs):
    name = Name(args[0])
    ab = kwargs.get('ab')
    rec = ab.get(name.value)
    if rec:
        return f"{ab.data.get(name.value)}"
    return f"Name {name} don't in AddressBook"


@decor_error
def delete(*args, **kwargs):
    ab = kwargs.get('ab')
    name = Name(args[0])
    rec = ab.get(name.value)
    if rec:
        ab.pop(name.value)
        return f"Contact {name} deleted"
    return f"Name {name} don't in AddressBook"


@decor_error
def add_birthday(*args, **kwargs):
    ab = kwargs.get('ab')
    name = Name(args[0])
    bir_day = Birthday(args[1])
    rec = ab.get(name.value)
    if rec:
        rec.add_birthday(bir_day.value)
        ab.add_record(rec)
        return f"Contact {name} was add birthday {bir_day}"
    return f"Name {name} don't in AddressBook"


@decor_error
def add_email(*args, **kwargs):
    ab = kwargs.get('ab')
    name = Name(args[0])
    email = Email(args[1])
    rec = ab.get(name.value)
    if rec:
        rec.add_email(email.value)
        ab.add_record(rec)
        return f"Contact {name} was add email {email}"
    return f"Name {name} don't in AddressBook"


@decor_error
def add_address(*args, **kwargs):
    ab = kwargs.get('ab')
    name = Name(args[0])
    address = Address(args[1])
    rec = ab.get(name.value)
    if rec:
        rec.add_address(address.value)
        ab.add_record(rec)
        return f"Contact {name} was add address {address}"
    return f"Name {name} don't in AddressBook"


@decor_error
def show_all(*args, **kwargs):
    ab = kwargs.get('ab')
    print(ab)
    result = f'Contacts list:\n'
    print_list = ab.iterator()
    for item in print_list:
        result += f"{item}"
    return result


@decor_error
def search(*args, **kwargs):
    ab = kwargs.get('ab')
    s_search = args[0]
    result = []
    for contact in ab.values():
        contact = str(contact)
        if s_search.lower() in contact.lower():
            result.append(contact)
    return result


def help_info(*args, **kwargs):
    return f"{'~' * 136}\nI know this commands: >hello< >add<, >change<, " \
           f">show<, >phone<, >del<, >birt<, >email<, >address<, >sear<" \
           f" and for Exit:(., close, exit)\n{'~' * 136}"


def start_info():
    return f"\n Hello I'm console bot, I was created to record contacts.\n{'~' * 57}"


def exit_save_change(ab):
    while True:
        user_input_save = input("Save change? y/n: ")
        if user_input_save == "y":
            save_contacts_to_file(ab)
            break
        elif user_input_save == "n":
            break
        else:
            continue
    print("Good bye!")


"""
Функції для збереження у файл та завантаження контактів з файлу у class AddressBook()
"""


def save_contacts_to_file(contacts):
    with open("AddressBook.bin", 'wb') as file:
        pickle.dump(contacts, file)
        print("Changes saved.")


def open_contacts_from_file():
    try:
        with open("AddressBook.bin", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()


"""
Словник з командами (key - функція: value - команда)
"""

COMMANDS = {
    hello: "hello",
    add_phone: "add ",
    change: "change",
    phone: "phone",
    show_all: "show",
    delete: "del",
    add_birthday: "birt",
    add_email: "email",
    add_address: "address",
    search: "sear",
    help_info: "info",
    # exit_save_change: "."
}

"""
Функція парсить строку яку ввів користувач, розділяє на команту та іншу інформація
"""


def parser_command(user_input: str):
    for command, key_word in COMMANDS.items():
        if user_input.lower().startswith(key_word):
            return command, user_input.replace(key_word, "").strip().split(" ")

    return None, None


"""
Головна функція
"""


def main():
    print(start_info())
    ab = open_contacts_from_file()

    while True:
        user_input = input("Enter command>>>")
        if user_input.lower() in ["close", "exit", "."]:
            exit_save_change(ab)
            break
        command, data = parser_command(user_input)
        if not command:
            print("Sorry, I don't understand you!")
        else:
            print(command(*data, ab=ab))


if __name__ == "__main__":
    main()

