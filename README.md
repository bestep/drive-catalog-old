![build](https://github.com/bestep/drive-catalog/workflows/Python%20package/badge.svg) [![codecov](https://codecov.io/gh/bestep/drive-catalog/branch/master/graph/badge.svg)](https://codecov.io/gh/bestep/drive-catalog)

# Drive Catalog

Library to recursively read and return file and directory information about drives and folders.

## License

drive-catalog is licensed under the
[GNU Affero General Public License v3.0](https://github.com/bestep/drive-catalog/blob/master/LICENSE)

## Installation

## Usage Example

Call the application from the command-line without parameters returns:

``` bash
> python drive_catalog

usage: main.py [-h] [--version] path [path ...]
main.py: error: the following arguments are required: path

```

Command-line help is provided by using the help directive:

```bash
> python drive_catalog --help

usage: main.py [-h] [--version] path [path ...]

Return formatted file information

positional arguments:
  path        The path of the drive or folder to process.

optional arguments:
  -h, --help  show this help message and exit
  --version   Show the version number and exit.
```

Call the application from the command-line with path. Note the testdrive folder
contains public domain images, audio and video.

```bash
> python drive-catalog testdrive/

Path: /Users/bestep/3_Development/drive-catalog/testdrive
Drive Info: {'name': 'testdrive', 'total_files': 28, 'portable_drive': False,
'size': 499963174912, 'free': 62603624448, 'used': 422170857472, 
'create_date': datetime.datetime(2020, 6, 25, 16, 39, 43, 436211)}
File Info: [{'name': 'Another Folder', 'size': '224.0B', 'type': '', 
'path': '/Users/bestep/3_Development/drive-catalog/testdrive/Another Folder', 
'create_date': datetime.datetime(2020, 6, 25, 16, 40, 12, 968011), 
'is_directory': True}, {'name': 'Video Files', 'size': '96.0B', 'type': '', 
'path': '/Users/bestep/3_Development/drive-catalog/testdrive/Video Files', 
'create_date': datetime.datetime(2020, 6, 25, 16, 40, 13, 207838), 
'is_directory': True}, {'name': '133-122010-Schnitt_original.pdf', 
'size': '1.1MiB', 'type': '', 'path': '/Users/bestep/3_Development/
drive-catalog/testdrive/133-122010-Schnitt_original.pdf', 
'create_date': datetime.datetime(2020, 6, 25, 16, 39, 5, 591855), 
'is_directory': False}, ...]
```

