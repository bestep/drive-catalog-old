"""fileinfo returns file and directory information.

:param path: The path of a file, folder or drive
:type path: os.path

:return: Returns a list of dictionaries of file information s:

.. code-block:: python

    {'name': str, # file name
    'size': str, # file size as string
    'size_bytes: int, # file size in bytes
    'type: str,  # Set to Image, Video or Audio if ext matches
    'path': str, # the path of the file
    'create_date': datetime # the reported create date of the file
    'is_directory': bool # True if the current item is a directory or folder
    }

"""

from datetime import datetime
from pathlib import Path
from dateutil import tz


def sizeof_fmt(num, suffix='B'):
    """Format file size info in a readable form."""
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


# set the extensions to search for
images_set = set(['.jpg', '.jpx', '.png', '.gif', '.jpeg',
                  '.tif', '.bmp', '.psd', '.heic', '.eps',
                  '.svg', '.tiff', '.webp'])
videos_set = set(['.mp4', '.m4v', '.mkv', '.webm', '.mpeg',
                  '.mov', '.avi', '.wmv', '.mpg', '.flv',
                  '.mts', '.ogv'])
audio_set = set(['.mp3', '.m4a', '.ogg', '.flac', '.wav',
                 '.aac', '.mid', '.midi', '.oga', '.opus',
                 '.weba', ])


def get_child_info(child):
    localtz = tz.gettz()
    if child.is_dir():
        is_directory = True
    else:
        is_directory = False
    if child.exists():
        child_info = ''
        try:
            child_info = child.stat()
        except FileNotFoundError as e:
            print(e)
        fileType = ''
        if child.suffix.lower() in images_set:
            fileType = 'Image'
        elif child.suffix.lower() in videos_set:
            fileType = 'Video'
        elif child.suffix.lower() in audio_set:
            fileType = 'Audio'
        else:
            fileType = ''

        child_size = ''
        child_size_bytes = 0
        create_date = ''
        if (child_info != ''):
            # mod_timestamp = datetime.\
            #        fromtimestamp(child_info.st_mtime)
            create_date = datetime.fromtimestamp(child_info.st_atime,
                                                 localtz).isoformat()
            child_size = sizeof_fmt(child_info.st_size)
            child_size_bytes = child_info.st_size
        fileName = child.name
        fileSize = child_size
        fileSizeBytes = child_size_bytes
        filepath = str(child)
        thumbnail = ''

        currentfile = {'name': fileName,
                       'size': fileSize,
                       'size_bytes': fileSizeBytes,
                       'type': fileType,
                       'path': filepath,
                       'thumbnail': thumbnail,
                       'create_date': create_date,
                       'is_directory': is_directory,
                       }
    return currentfile


def get_file_info(path):
    """Function recurssivly walks a path and returns file and
    directory information.

    :param path: The path to look for files.
    """
    p = Path(path)
    print("p {}".format(p))
    files = []
    # Recursive walk
    if p.is_file():
        # Get the file info and return
        currentfile = get_child_info(p)
        files.append(currentfile)
    elif p.is_dir():
        # Get the info for all the files below directory
        for child in p.glob("**/*"):
            currentfile = get_child_info(child)
            files.append(currentfile)
    return files
