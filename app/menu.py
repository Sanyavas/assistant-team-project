"""C H A T B O T"""

from addressbook import main as ab_main
from notes import main as nb_main
from sort import main as sr_main
from prettytable import PrettyTable


def main():
    """Main function"""

    while True:
        x = PrettyTable()
        x.field_names = ['C H A T B O T']
        x.align = 'l'
        x.add_row(['0: Exit'])
        x.add_row(['1: AddressBook'])
        x.add_row(['2: NoteBook'])
        x.add_row(['3: Sort files'])
        print(x)
        user_input = input(f"\nEnter command {chr(10151)*3} ")
        if user_input == "1":
            ab_main()
        elif user_input == "2":
            nb_main()
        elif user_input == "3":
            sr_main()
        elif user_input == "0":
            print(f"\n{chr(128075)} Good bay!")
            break
        else:
            print(f"\n{chr(129400)}I don't understand you!")


if __name__ == "__main__":
    main()
