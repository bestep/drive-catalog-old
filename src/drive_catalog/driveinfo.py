"""driveinfo returns drive info

:param path: The path of a folder or drive
:type path: os.path

:return: Returns a dictionary of drive information as:

.. code-block:: python

    {'name': str, # drive name
    'total_files;: int, # total number of files in drive
    'portable_drive': bool, # Is the drive a mounted drive
    'size': int, # size of drive in bytes
    'free': int, # free space of drive in bytes
    'used': int, # used space of drive in bytes
    'create_date': datetime, # the reported create date of the drive}

"""
from datetime import datetime
from pathlib import Path
from shutil import disk_usage


def get_drive_info(path):
    """Get the drive info from the supplied path

    :param path: The path of the folder or drive
    :type path: os.path

    :return: Returns a dictionary of drive information.
    """
    p = Path(path)
    total_files = len(list(p.glob("**/*")))
    drive_info = p.stat()
    drive_is_mount = p.is_mount()
    drive_shutilstats = disk_usage(p)
    drive_size_in_bytes = drive_shutilstats.total
    drive_free_space_in_bytes = drive_shutilstats.free
    drive_used_space_in_bytes = drive_shutilstats.used
    drive_name = p.stem
    drive_create_date = datetime.fromtimestamp(drive_info.st_ctime)
    drive = {'name': drive_name,
             'total_files': total_files,
             'portable_drive': drive_is_mount,
             'size': drive_size_in_bytes,
             'free': drive_free_space_in_bytes,
             'used': drive_used_space_in_bytes,
             'create_date': drive_create_date,
             }
    return drive
