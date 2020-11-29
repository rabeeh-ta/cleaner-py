# Cleaner-Py

Cleaner-Py is a bot that will traverse through every sub-directory from the root directory and will clean the modules,compilation-files or any other unwanted files found.

The deleted files can be recovered from the trash or recycle-bin is needed.

## Installation

Make sure you are having `python-3`

This script only uses one external library that you should install manually [send2trash](https://pypi.org/project/Send2Trash/). ( if you have anaconda installed send2trash comes default )

```bash
pip install send2trash
```

## Usage

Copy and paste the main.py file to the root directory of Where you store all your projects.

Then run the file with the flag. The script will find all the junk files that you code has created and will delete them.

```bash
python main.py --flag
```

There are two flags

`--flutter` will delete all the build directories found.

`--node` will delete all the node-modules directories found.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
