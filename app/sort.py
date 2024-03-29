"""S O R T   F I L E"""

import os
import shutil
import re
import rarfile
from .information import start_info_sf
from .logger import get_logger

logger = get_logger(__name__)


extensions_img = ['.jpeg', '.png', '.jpg', '.svg']
extensions_doc = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
extensions_video = ['.avi', '.mp4', '.mov', '.mkv']
extensions_music = ['.mp3', '.ogg', '.wav', '.amr']
extensions_archives = ['.zip', '.gz', '.tar', '.rar']
folder_name = ['image', 'text', 'video', 'music', 'archives', 'other']


def normalize(name):
    """Transliteration of files from Cyrillic to Latin"""

    cyrillic_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    translation = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "y", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
        "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    trans = {}

    for c, l in zip(cyrillic_symbols, translation):
        trans[ord(c)] = l
        trans[ord(c.upper())] = l.upper()
        
    filename, file_extension = os.path.splitext(name)
    return re.sub(r'\W', '_',
                  filename.translate(trans)) + file_extension


def sort_dir(root_path, current_path, level=0):
    """Recursion through directories"""

    names = os.listdir(current_path)
    for file in names:

        if level == 0 and file in folder_name:
            continue

        if os.path.isdir(current_path+file):
            sort_dir(root_path, current_path+file+'/', level+1)
            shutil.rmtree(current_path+file)
            continue

        if sort_extensions(extensions_img, file, root_path + 'image/', current_path):
            continue
        if sort_extensions(extensions_doc, file, root_path + 'text/', current_path):
            continue
        if sort_extensions(extensions_video, file, root_path + 'video/', current_path):
            continue
        if sort_extensions(extensions_music, file, root_path + 'music/', current_path):
            continue
        if sort_archive(extensions_archives, file, root_path + 'archives/', current_path):
            continue

        if not os.path.exists(root_path + 'other/' + file):
            if not os.path.exists(root_path + 'other/'):
                os.makedirs(root_path + 'other/')
            shutil.move(current_path + file, root_path + 'other/' + file)


def sort_extensions(extensions, file, destination_dir, location_dir):
    """Sorting files by extension"""

    for extension in extensions:
        if extension in file.lower():
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            shutil.move(location_dir + file,
                        destination_dir + normalize(file))
            return True


def sort_archive(extensions, file, destination_dir, location_dir):
    """Unzipping and sorting archives"""

    for extension in extensions:
        if extension in file.lower():
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            try:
                if extension == '.rar':
                    r = rarfile.RarFile(location_dir + file)
                    r.extractall(destination_dir +
                                 file.removesuffix(extension))
                    r.close()
                else:
                    shutil.unpack_archive(
                        location_dir + file, destination_dir + file.removesuffix(extension))
                os.remove(location_dir + file)
            except:
                shutil.move(location_dir + file,
                            destination_dir + normalize(file))
            return True


def count_files(dir_path):
    """File counter"""

    count = 0
    for root_dir, cur_dir, files in os.walk(dir_path):
        if files != ['.DS_Store']:
            print(files)
            count += len(files)
    return f'In folder: {count} files'


def sort_again():
    while True:
        user_input = input(f"{chr(128221)}You have files to sort? y/n: ")
        if user_input == "y":
            main()
            break
        elif user_input == "n":
            break
        else:
            print(f"enter y/n")

    print(f"{chr(128075)} Good bye!")


def main():
    """Main function, which makes a request to enter the path to the directory for sorting"""

    logger.info("Start Sort file")
    print(start_info_sf())
    while True:
        try:
            root_path = input(f'\nEnter path to folder{chr(10151)*3} ')
            logger.info(f'path to folder {root_path}')
            if root_path == "0":
                break
            if root_path[-1] != '/':
                root_path += '/'
                sort_dir(root_path, root_path)
                print(f'Everything is sorted  {chr(9989)}')
                print(count_files(root_path))
                sort_again()
                break
            else:
                print(f"{chr(128679)} error, try again")

        except:
            print(f'{chr(128679)} error')


if __name__ == "__main__":
    main()
