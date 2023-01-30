"""Створення нотаток з текстовою інформацією"""

from collections import UserDict, UserString
import pickle


class Teg(UserString):
    MAX_LEN = 13

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]


class Note:
    def __init__(self, note: str, *tags):
        self.note = note
        self.tags = list(tags)

    def __str__(self):
        if self.value == None:
            self.value = ''
        return self.value


class NoteBook(UserDict):
    def add_note(self, note: Note):
        self.data[id(note)] = note

    def note_iterator(self, n = 2):
        """Пагінація (посторінкове виведення) для NoteBook"""
        block = ''
        string_counter = 0
        for note in self.data.values():
            string_counter += 1
            block += str(note) + '\n'
            if string_counter == n:
                block += '-' * 40
                yield block
                string_counter = 0
                block = ''
        yield block

    def del_note(self, note: Note):
        if id(note) in self.data:
            self.data.pop(id(note))

    def change_note(self, note_old: Note, note_new: Note):
        if id(note_old) in self.data:
            self.data.pop(id(note_old))
            self.data[id(note_new)] = note_new

    def find(self, find_str: str):
        str_ret = find_str + '\n' + '_' * 40 + '\n'
        for value in self.data.values():
            if find_str in str(value):
                str_ret += str(value) + '\n'
        return str_ret

    def find_sort_tags(self, tags):
        dict_ret = dict.fromkeys(tags, [])
        for tag in tags:
            for value in self.data.values():
                if tag in value.tags:
                    dict_ret[tag].append(value)
        return dict_ret

    def save_to_file(self):
        """Функція збереження нотатків до файлу"""

        with open("notes_list.bin", "wb") as fh:
            pickle.dump(self, fh)
            print("Notes saved in file")


def read_from_file() -> NoteBook:
    """Функція завантаження даних із файлу в об'єкт класу"""

    try:
        with open("notes_list.bin", "rb") as fh:
            result = pickle.load(fh)
            return result
    except FileNotFoundError:
        return NoteBook()
