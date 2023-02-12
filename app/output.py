from abc import abstractmethod, ABCMeta
from datetime import datetime
from prettytable import PrettyTable


class Output(metaclass=ABCMeta):
    @abstractmethod
    def show_all(self):
        pass

    @abstractmethod
    def next_birthdays(self):
        pass


class AddressBookOutput(Output):

    def show_all(*args, **kwargs):
        """Displaying the contents of the contact book"""

        x = PrettyTable()
        ab = kwargs.get('ab')
        count = 0
        print(f"\nContacts list:{chr(128214)}")
        for i in ab.values():
            x.field_names = ['№', "name", "phone", "email", "address", "birthday"]
            count += 1
            x.add_row([count, i.name, ", ".join(i.phones), i.email, i.address, i.birthday])
        return x

    def next_birthdays(*args, **kwargs):
        """Displays a list of contacts whose birthday is between the current date and the specified number of days"""

        ab = kwargs.get('ab')
        days = int(args[0])
        x = PrettyTable()
        for i in ab.values():
            if i.days_to_birthday(i.birthday) <= days:
                years = datetime.now().year - i.birthday.year
                x.field_names = ["name", "birthday", "years", "phone", "email", "address"]
                x.add_row([i.name, i.birthday, years, ", ".join(i.phones), i.email, i.address])
        if x:
            print(x)
        else:
            return f"{chr(10062)} No birthdays for the next {days} days"
        return f"\nTo congratulate on his {chr(127873)}birthday!!!"


class NoteBookOutput(Output):
    def show_all(*args, **kwargs):
        """Display the contents of a NoteBook"""

        nb = kwargs.get('nb')
        count = 0
        x = PrettyTable()
        x.align = 'l'
        print(f"NoteBook:")
        for i in nb.values():
            x.field_names = ['№', 'Names', 'Notes', 'Tags']
            count += 1
            x.add_row([count, i.name, " ".join(i.notes), " ".join(i.tags)])
        return x

    def next_birthdays(self):
        pass
