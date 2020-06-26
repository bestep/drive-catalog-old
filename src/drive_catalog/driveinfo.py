from datetime import datetime
from pathlib import Path
from shutil import disk_usage


def get_drive_info(path):
    """Get the drive info from the supplied path

    Test if it is removable media. If not, return folder information.

    isRemoveableDrive
    

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
