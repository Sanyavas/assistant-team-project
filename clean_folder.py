# homework_6
# скрипт має сортувати файли по розширенню та перекладає з кирилиці на латиницю переміщаючи у теки


import os
import re
from pathlib import Path
import sys
import shutil

""" Словник з розширеннями, при додаванні нового розширення
 - будуть створюватись нові теки під файли з новими розширеннями """

file_extension = {"images": ['.jpeg', '.png', '.jpg', '.svg'],
                  "documents": ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
                  "archives": ['.zip', '.gz', '.tar'],
                  "audio": ['.mp3', '.ogg', '.wav', '.amr'],
                  "video": ['.avi', '.mp4', '.mov', '.mkv'],
                  "different": None
                  }

""" Функція змінює транлітерацію файлів з керилиці на латиницю 
та замінює символи на символ "_" """


def normalize(name):
    cyrillic_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    translation = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "y", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
        "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    trans = {}

    for c, l in zip(cyrillic_symbols, translation):
        trans[ord(c)] = l
        trans[ord(c.upper())] = l.upper()
    trans_name = name.translate(trans)
    trans_name = re.sub(r'\W', '_', trans_name)

    return trans_name


"""" Функція сортування файлів згідно їх розширень, повертає словник:
     ключ - тип файлу, значення - це список файлів """


def sorter(files):
    chars = {
        "images": [],
        "documents": [],
        "archives": [],
        "audio": [],
        "video": [],
        "different": [],
    }
    for file in files:
        suff_name = file[file.rfind("."):]
        if suff_name in file_extension["images"]:
            chars["images"].append(file)
        elif suff_name in file_extension["documents"]:
            chars["documents"].append(file)
        elif suff_name in file_extension["archives"]:
            chars["archives"].append(file)
        elif suff_name in file_extension["audio"]:
            chars["audio"].append(file)
        elif suff_name in file_extension["video"]:
            chars["video"].append(file)
        else:
            chars["different"].append(file)

    return chars


""" Функція видалення порожніх папок """


def remove_folders(path):
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            remove_folders(a)
            if not os.listdir(a):
                os.rmdir(a)


""" Головна Функція"""


def main(path_dir):
    path_to_file = path_dir
    norm_names_list = []
    all_suff_names = []
    count_files = 0
    for root, dirs, files in os.walk(path_dir):

        for file in files:
            suff_name = file[file.rfind("."):]
            if suff_name not in all_suff_names:
                all_suff_names.append(suff_name)

            os.replace(Path(root) / file, Path(path_to_file, file))
            norm_name = normalize(file[:file.rfind(".")]) + file[file.rfind("."):]
            os.replace(Path(path_to_file, file), Path(path_to_file, norm_name))

            if norm_name not in norm_names_list:
                norm_names_list.append(norm_name)
                count_files += 1

    dict_files = sorter(norm_names_list)
    list_new_folders = []

    for file_types, files in dict_files.items():
        list_new_folders.append(file_types)

        for file in files:
            if not Path(path_to_file, file_types).exists():
                Path(path_to_file, file_types).mkdir()
            if not Path(path_to_file, file_types, file_types).exists():
                Path(path_to_file, file_types, file_types).mkdir()
            if file_types == "archives":
                shutil.unpack_archive(Path(path_to_file, file), Path(path_to_file, file_types, file_types, file))
                os.replace(Path(path_to_file, file), Path(path_to_file, file_types, file))
            else:
                os.replace(Path(path_to_file, file), Path(path_to_file, file_types, file))

    remove_folders(path_to_file)

    print("All folders: ", list_new_folders)
    print("All extension files: ", all_suff_names)
    print("Names all files in folder: ", dict_files)
    print("Count files: ", count_files)


""" Function for <<<RUN>>> """


def run():
    p_dir = None
    try:
        p_dir = sys.argv[1]
    except IndexError:
        p_dir = input("Enter the path sort: ")
        if not Path(p_dir).exists():
            print(f"Not found the path: {p_dir}")
        else:
            main(p_dir)
            print()

            print("Sorted!")


if __name__ == "__main__":
    run()
