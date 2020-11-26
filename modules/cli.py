import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--flutter", help="Deletes the Build folders on every flutter project found", action='store_true')
parser.add_argument(
    "--node", help="Deletes the Node-Modules folder on every project found", action='store_true')

args = parser.parse_args()


if args.flutter and args.node:
    print('both clean flutter and node')
else:
    if args.flutter:
        print('clean flutter files')
    elif args.node:
        print('clean node files')
