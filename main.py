import os
import argparse
import send2trash

# getting the root file path
cwd = os.getcwd()

# takking input from the user
parser = argparse.ArgumentParser()
parser.add_argument(
    "--flutter", help="Deletes the Build folders on every flutter project found", action='store_true')
parser.add_argument(
    "--node", help="Deletes the Node-Modules folder on every project found", action='store_true')

args = parser.parse_args()

total_found = 0  # calculate the folders found


# search function to find the things to delete
def search_func_root(path, item):
    global total_found
    for folders, sub_folders, files in os.walk(path):
        if item in sub_folders:  # checks if the flag specific is found in the current folder
            print(f"Found and deleted a {item} directory in {folders}")
            send2trash.send2trash(folders+"\\"+item)  # delete the folder
            total_found += 1

    # checking the passed argument by the user
if args.flutter and args.node:  # clean both
    # '\x1b[1;31;40m' coloring thing for cli output
    print('\x1b[1;31;40m' + ' Cleaning both flutter and node ' + '\x1b[0m')
    search_func_root(cwd, 'build')
    search_func_root(cwd, 'node_modules')
else:
    if args.flutter:  # clean flutter- build directorys
        print('\x1b[1;31;40m' + ' Cleaning Flutter files ' + '\x1b[0m')
        search_func_root(cwd, 'build')
    elif args.node:  # clean node-modules
        print('\x1b[1;31;40m' + ' Cleaning Node files ' + '\x1b[0m')
        search_func_root(cwd, 'node_modules')


print('\n' + '\x1b[1;32;40m' +
      f' Total files found and cleaned: {total_found} ' + '\x1b[0m')  # print total number of files deleted
