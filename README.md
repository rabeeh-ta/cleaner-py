# Cleaner-Py

Cleaner-Py is a bot that will traverse through every sub-directory and will clean the modules,compilation files found.

## Installation

This script only uses one external library that you should install manually [send2trash](https://pip.pypa.io/en/stable/).

Make sure you are having `python-3`

```bash
pip install send2trash
```

## Usage

```bash
python main.py --flag
```

For now you can pass two flags

`--flutter` => will delete all the build directories found.

`--node` => will delete all the node-modules directories found.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
