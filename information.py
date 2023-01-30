"""Функції виводу інформації"""


def help_info(*args, **kwargs):
    """help info for AddressBook"""

    return f"I N F O:" \
           f"\n{'~' * 50}" \
           f"\ncommands:" \
           f"\n{'~' * 50}" \
           f"\n>hello<" \
           f"\n>add<: add name and phone, if there is a name add phone" \
           f"\n>change<: change phone" \
           f"\n>show<: show all AddressBook" \
           f"\n>phone<: show phone" \
           f"\n>del<: del contact" \
           f"\n>birth<: add birthday" \
           f"\n>email<: add email" \
           f"\n>address<: add address" \
           f"\n>search<: search by matches" \
           f"\n>nxbirt<: next birthday for >n< number of days" \
           f"\n>info<: information" \
           f"\n>., close, exit<: exit" \
           f"\n{'~' * 50}" \
           f"\nContact is created with the phone!" \
           f"\nCommand input example:  >command< >name< >info<"


def start_info():
    """start info for AddressBook"""

    return f"\n{'~' * 23}" \
           f"\n A D D R E S S B O O K " \
           f"\n{'~' * 23}" \
           f"\nenter: info"
