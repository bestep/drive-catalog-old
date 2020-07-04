![Bitbucket Pipelines](https://img.shields.io/bitbucket/pipelines/bestep/drive-catalog) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/drive-catalog) ![PyPI](https://img.shields.io/pypi/v/drive-catalog) [![codecov](https://codecov.io/gh/bestep/drive-catalog/branch/master/graph/badge.svg)](https://codecov.io/gh/bestep/drive-catalog) 
<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/drive-catalog)-->

# Drive Catalog

Library to recursively read and return file and directory information about drives and folders.


## License

drive-catalog is licensed under the
[GNU Affero General Public License v3.0](https://github.com/bestep/drive-catalog/blob/master/LICENSE)

## Installation

To install using pip:

```bash
> pip install drive-catalog
```

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
Drive Info: {'name': 'testdrive', 'total_files': 47, 'portable_drive': False, 'size': 499963174912, 'free': 60009164800, 'used': 423691579392, 'create_date': '2020-07-01T08:43:48.161025-04:00'}
p /Users/bestep/3_Development/drive-catalog/testdrive
File Info: [{'name': 'coffee_beans_coffee_drink.jpg', 'size': '147.8KiB', 'size_bytes': 151326, 'type': 'Image', 'path': '/Users/bestep/3_Development/drive-catalog/testdrive/coffee_beans_coffee_drink.jpg', 'thumbnail': '', 'create_date': '2020-06-30T23:09:33.792833-04:00', 'is_directory': False}, {'name': 'OTRR_An_Evening_With_Groucho_Singles', 'size': '1.3KiB', 'size_bytes': 1312, 'type': '', 'path': '/Users/bestep/3_Development/drive-catalog/testdrive/OTRR_An_Evening_With_Groucho_Singles', 'thumbnail': '', 'create_date': '2020-06-30T23:09:34.153570-04:00', 'is_directory': True}, {'name': 'new_york_skyline_usa.jpg', 'size': '141.2KiB', 'size_bytes': 144612, 'type': 'Image', 'path': '/Users/bestep/3_Development/drive-catalog/testdrive/new_york_skyline_usa.jpg', 'thumbnail': '', 'create_date': '2020-06-30T23:09:33.793437-04:00', 'is_directory': False},...]
```

Add the individual libraries and call the functions directly to return
drive and file information.

To get drive info for a path:

```bash
from drive_catalog import driveinfo

newDriveInfo = driveinfo.get_drive_info(path)
total_files = newDriveInfo['total_files']
```
Output example

```
>>> newDriveInfo = driveinfo.get_drive_info(path)
>>> total_files = newDriveInfo['total_files']
>>> total_files
43
>>> newDriveInfo
{'name': 'testdrive', 'total_files': 43, 'portable_drive': False, 'size': 499963174912, 'free': 56823353344, 'used': 423656300544, 'create_date': '2020-07-04T11:20:21.414142-04:00'}
```

To get the file information for a path:

```bash
from drive_catalog import fileinfo

files = fileinfo.get_file_info(path)
for file in files:
	print("File Name: {}".format(file['name']))
	print("File Size: {}".format(file['size']))
	print("File Size Bytes: {}".format(file['size_bytes']))
	print("File Path: {}".format(file['path']))
	print("File Type: {}".format(file['type']))
	print("File Create Date: {}".format(file['create_date']))

```

Output:

```bash
File Name: test.mov
File Size: 309.9KiB
File Size Bytes: 317325
File Path: /Users/bestep/3_Development/drive-catalog/testdrive/test.mov
File Type: Video
File Create Date: 2020-07-04T11:20:22.204868-04:00
...
```
