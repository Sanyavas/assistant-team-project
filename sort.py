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

symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяґіїАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯҐІЇ",
           u"abvgdeejzijklmnoprstufhzcss_y_euagiiABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUAGII")
tr = {ord(a): ord(b) for a, b in zip(*symbols)}


def normalize(name):
    filename, file_extension = os.path.splitext(name)
    return re.sub(r'\W', '_',
                  filename.translate(tr)) + file_extension


def sort_dir(root_path, current_path, level=0):
    names = os.listdir(current_path)
    for file in names:

        if level == 0 and file in folder_name:
            continue

        if os.path.isdir(current_path+file):
            sort_dir(root_path, current_path+file+'/', level+1)
            os.rmdir(current_path+file)
            continue

        if sort_extentions(extentions_img, file, root_path + 'image/', current_path):
            continue

        if sort_extentions(extentions_doc, file, root_path + 'text/', current_path):
            continue

        if sort_extentions(extentions_video, file, root_path + 'video/', current_path):
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
                os.remove(location_dir + file)
            except:
                shutil.move(location_dir + file,
                            destination_dir + normalize(file))
            return True


def main():
    try:
        root_path = sys.argv[1]
        if root_path[-1] != '/':
            root_path += '/'
        sort_dir(root_path, root_path)
        print('Все відсортовано, гг вп')
    except:
        print('Введіть шлях до теки для сортування')


if __name__ == "__main__":
    main()
