"""CHATBOT"""

from addressbook import main as ab_main

"""
Головна функція
"""


def main():
    print(f"COMANDS:\n{'-' * 50}\nMain menu\n1: AddressBook")
    user_input = input("Enter command >>>")
    if user_input == "1":
        ab_main()
    else:
        print(f"I don't understand you!!")


if __name__ == "__main__":
    main()
