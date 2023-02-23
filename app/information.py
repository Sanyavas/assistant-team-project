"""Information output functions"""

from prettytable.colortable import ColorTable, Themes
# from prettytable import PrettyTable


def help_info_ab(*args, **kwargs):
    """help info for AddressBook"""

    print(f"I N F O:")
    x = ColorTable(theme=Themes.OCEAN)
    x.field_names = ['commands', 'description', 'example']
    x.align = 'l'
    x.add_row(['>hello<', 'hello', '>command<'])
    x.add_row(['>add<', 'add name and phone, if there is a name add phone', '>command< >name< >phone<'])
    x.add_row(['>change<', 'change phone', '>command< >name< >old_phone< >new_phone<'])
    x.add_row(['>show<', 'show all AddressBook', '>command<'])
    x.add_row(['>phone<', 'show phone', '>command< >name<'])
    x.add_row(['>del<', 'del contact', '>command< >name<'])
    x.add_row(['>birth<', 'add birthday', '>command< >name< >date<'])
    x.add_row(['>email<', 'add email', '>command< >name< >email<'])
    x.add_row(['>address<', 'add address', '>command< >name< >address<'])
    x.add_row(['>find<', 'search by matches', '>command< >target<'])
    x.add_row(['>nextbirth<', 'next birthday for >n< number of days', '>command< >next number days<'])
    x.add_row(['>info<', 'information', '>command<'])
    x.add_row(['>0, ., close, exit<', 'exit', '>command<'])
    return x


def help_info_nb(*args, **kwargs):
    """help info for NoteBook"""

    print(f"I N F O:")
    x = ColorTable(theme=Themes.OCEAN)
    x.field_names = ['commands', 'description', 'example']
    x.align = 'l'
    x.add_row(['>hello<', 'hello', '>command<'])
    x.add_row(['>add<', 'add new name, note and tag', '>command<'])
    x.add_row(['>note<', 'add note', '>command<'])
    x.add_row(['>del<', 'delete note', '>command<'])
    x.add_row(['>show<', 'show all NoteBook', '>command<'])
    x.add_row(['>tag<', 'add tags', '>command<'])
    x.add_row(['>find<', 'find notes', '>command<'])
    x.add_row(['>info<', 'information', '>command<'])
    x.add_row(['>0, ., close, exit<', 'exit', '>command<'])
    return x


def start_info_ab():
    """start info for AddressBook"""

    x = ColorTable(theme=Themes.OCEAN)
    x.field_names = [" A D D R E S S B O O K "]
    x.align = 'l'
    x.add_row([f"enter: info{chr(128227)}"])
    return x


def start_info_nb():
    """start info for NoteBook"""

    x = ColorTable(theme=Themes.OCEAN)
    x.field_names = [" N O T E B O O K "]
    x.align = 'l'
    x.add_row([f"enter: info{chr(128227)}"])
    return x


def start_info_sf():

    x = ColorTable(theme=Themes.OCEAN)
    x.field_names = [" S O R T I N G   F I L E S "]
    x.align = 'l'
    x.add_row([f"Exit: 0"])
    return x


def start_info_menu():

    x = ColorTable(theme=Themes.OCEAN)
    x.field_names = ['C H A T B O T']
    x.align = 'l'
    x.add_row(['0: Exit'])
    x.add_row(['1: AddressBook'])
    x.add_row(['2: NoteBook'])
    x.add_row(['3: Sort files'])
    x.add_row(['4: Games'])
    return x


def start_info_games():
    x = ColorTable(theme=Themes.OCEAN)
    x.field_names = ['G A M E S']
    x.align = 'l'
    x.add_row(['0: Exit'])
    x.add_row(['1: Magic layer'])
    x.add_row(['2: Hangman'])
    return x
