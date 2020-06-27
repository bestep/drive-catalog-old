"""fileinfo returns file and directory information.

:param path: The path of a folder or drive
:type path: os.path

:return: Returns a list of dictionaries of file information s:

.. code-block:: python

    {'name': str, # file name
    'size': str, # file size in bytes
    'path': str, # the path of the file
    'create_date': datetime # the reported create date of the file
    'is_directory': bool # True if the current item is a directory or folder
    }

"""

from datetime import datetime
from pathlib import Path


def sizeof_fmt(num, suffix='B'):
    """Format file size info in a readable form."""
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


# set the extensions to search for
images_set = set(['.jpg', '.JPG', '.jpx', '.png', '.gif',
                  '.tif', '.bmp', '.psd', 'heic', '.eps'])
videos_set = set(['.MP4', '.mp4', '.m4v', '.mkv', '.webm',
                  '.mov', '.avi', '.wmv', '.mpg', '.flv', '.MOV'])
audio_set = set(['mp3', '.m4a', '.ogg', '.falc', '.wav'])


def get_file_info(path):
    """Function recurssivly walks a path and returns file and
    directory information.

    :param path: The path to look for files.
    """
    p = Path(path)
    files = []
    # Recursive walk
    for child in p.glob("**/*"):
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
            if child.suffix in images_set:
                fileType = 'Image'
            elif child.suffix in videos_set:
                fileType = 'Video'
            elif child.suffix in audio_set:
                fileType = 'Audio'
            else:
                fileType = ''

            child_size = ''

            create_date = ''
            if (child_info != ''):
                # mod_timestamp = datetime.\
                #        fromtimestamp(child_info.st_mtime)
                create_date = datetime.fromtimestamp(child_info.st_atime)
                child_size = sizeof_fmt(child_info.st_size)
            fileName = child.name
            fileSize = child_size
            filepath = str(child)
            thumbnail = ''

            currentfile = {'name': fileName,
                           'size': fileSize,
                           'type': fileType,
                           'path': filepath,
                           'thumbnail': thumbnail,
                           'create_date': create_date,
                           'is_directory': is_directory,
                           }
            files.append(currentfile)
    return files
