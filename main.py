import os
import argparse

# getting the root file path
cwd = os.getcwd()

# takking input from the user
parser = argparse.ArgumentParser()
parser.add_argument(
    "--flutter", help="Deletes the Build folders on every flutter project found", action='store_true')
parser.add_argument(
    "--node", help="Deletes the Node-Modules folder on every project found", action='store_true')

args = parser.parse_args()

# search function to find the things to delete


def search_func(path, item):
    for folders, sub_folders, files in os.walk(path):
        if item in sub_folders:
            print(folders)


    # checking the passed argument by the user
if args.flutter and args.node:
    print('both clean flutter and node')
    search_func(cwd, 'build')
    search_func(cwd, 'node_modules')
else:
    if args.flutter:
        print('clean flutter files')
        search_func(cwd, 'build')
    elif args.node:
        print('clean node files')
        search_func(cwd, 'node_modules')
