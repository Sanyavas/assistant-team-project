"""CHATBOT"""

from addressbook import main as ab_main

"""
Головна функція
"""


def main():
    user_input = input("Main menu. Enter command >>>")
    if user_input == "ab":
        ab_main()
    else:
        print(f"I don't understand you!!")


if __name__ == "__main__":
    main()
