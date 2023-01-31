"""Функції виводу інформації"""


def help_info_ab(*args, **kwargs):
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


def help_info_nb(*args, **kwargs):
    """help info for NoteBook"""

    return f"I N F O:" \
           f"\n{'~' * 50}" \
           f"\ncommands:" \
           f"\n{'~' * 50}" \
           f"\n>add<: add new note" \
           f"\n>del<: delete note" \
           f"\n>change<: change note" \
           f"\n>show<: show all NoteBook" \
           f"\n>tag+<: add tag" \
           f"\n>find<: find notes" \
           f"\n>tags<: find and sort by tegs" \
           f"\n>., close, exit<: exit" \
           f"\n{'~' * 50}" \
           f"\nCommand input example:  >command< >note<"


def start_info_ab():
    """start info for AddressBook"""

    return f"\n{'~' * 23}" \
           f"\n A D D R E S S B O O K " \
           f"\n{'~' * 23}" \
           f"\nenter: info"


def start_info_nb():
    """start info for NoteBook"""

    return f"\n{'~' * 17}" \
           f"\n N O T E B O O K " \
           f"\n{'~' * 17}" \
           f"\nenter: info"
