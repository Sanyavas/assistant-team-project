"""CHATBOT"""

from addressbook import *

"""
Головна функція
"""


def main():
    user_input = input("Main menu. Enter command >>>")
    if user_input == "addressbook":
        main_addressbook()
    else:
        print(f"I don't understand you!!")


if __name__ == "__main__":
    main()
