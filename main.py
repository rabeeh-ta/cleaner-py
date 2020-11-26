import os

cwd = os.getcwd()


def search_func(path, item):
    for folders, sub_folders, files in os.walk(path):
        if item in sub_folders:
            print(folders)


search_func(cwd, 'build')
