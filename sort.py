import os
import sys
import shutil
import re

extentions_img = ['.jpeg', '.png', '.jpg', '.svg']
extentions_doc = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
extentions_video = ['.avi', '.mp4', '.mov', '.mkv']
extentions_music = ['.mp3', '.ogg', '.wav', '.amr']
extentions_archives = ['.zip', '.gz', '.tar']
folder_name = ['image', 'text', 'video', 'archives', 'other']


def translit(name):
    cyrillic_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    translation = (
        "a", "b", "v", "h", "d", "e", "e", "zh", "z", "y", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
        "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    trans = {}

    for c, l in zip(cyrillic_symbols, translation):
        trans[ord(c)] = l
        trans[ord(c.upper())] = l.upper()

    return name.translate(trans)


def normalize(name):
    filename, file_extension = os.path.splitext(name)
    return re.sub(r'\W', '_',
                  translit(filename)) + file_extension


# def rename_files_from_arch(extract_dir, file):
#     extract_dir = extract_dir + file + '/'
#     names = os.listdir(extract_dir)
#     print(names)
#     for name in names:
#         new_name = name.encode('cp437').decode('cp866')
#         os.rename(extract_dir + name,
#                   extract_dir + new_name)


def sort_dir(root_path, current_path, level=0):
    names = os.listdir(current_path)
    for file in names:

        if level == 0 and file in folder_name:
            continue

        if os.path.isdir(current_path+file):
            sort_dir(root_path, current_path+file+'/', level+1)
            shutil.rmtree(current_path+file)
            continue

        if sort_extentions(extentions_img, file, root_path + 'image/', current_path):
            continue

        if sort_extentions(extentions_doc, file, root_path + 'text/', current_path):
            continue

        if sort_extentions(extentions_video, file, root_path + 'video/', current_path):
            continue

        if sort_extentions(extentions_music, file, root_path + 'music/', current_path):
            continue

        if sort_archive(extentions_archives, file, root_path + 'archives/', current_path):
            continue

        if not os.path.exists(root_path + 'other/' + file):
            if not os.path.exists(root_path + 'other/'):
                os.makedirs(root_path + 'other/')
            shutil.move(current_path + file, root_path + 'other/' + file)


def sort_extentions(extentions, file, destination_dir, location_dir):
    for extention in extentions:
        if extention in file.lower():
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            shutil.move(location_dir + file,
                        destination_dir + normalize(file))
            return True


def sort_archive(extentions, file, destination_dir, location_dir):
    for extention in extentions:
        if extention in file.lower():
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            try:
                shutil.unpack_archive(
                    location_dir + file, destination_dir + file.removesuffix(extention))
#                 rename_files_from_arch(
#                     destination_dir, file.removesuffix(extention))
                os.remove(location_dir + file)
            except:
                shutil.move(location_dir + file,
                            destination_dir + normalize(file))
            return True


def main():
    print('\nSorting files\n')
    try:
        #root_path = sys.argv[1]
        root_path = input('Enter the path to the folder to sort: ')
        if root_path[-1] != '/':
            root_path += '/'
        sort_dir(root_path, root_path)
        print('Everything is sorted')
    except:
        print('Error')


if __name__ == "__main__":
    main()
