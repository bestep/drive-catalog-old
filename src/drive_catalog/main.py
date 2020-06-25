import sys
import os
import argparse
from datetime import datetime
from pathlib import Path
from shutil import disk_usage

sys.path.append('src')
from drive_catalog import __version__


def sizeof_fmt(num, suffix='B'):
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

def getFileInfo(path):
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
                           'create_date': create_date,
                           'is_directory': is_directory,
                          }
            files.append(currentfile)
    return files

def getDriveInfo(path):
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


#    st_size=131072, st_atime=315547200, st_mtime=315547200, st_ctime=315547200)


def main():
    # create parser
    my_parser = argparse.ArgumentParser(
        description='Return formatted file information')

    # Add arguments
    my_parser.add_argument('path',
                           metavar = 'path',
                           nargs = '+',
                           help = (
                               'The path of the drive or folder to process.')
                          )
    my_parser.add_argument('--version', action='version',
                           version='{}'.format(__version__),
                           help='Show the version number and exit.')
    
    # Execute the parser_args method
    args = my_parser.parse_args()

    #parse paths
    full_paths = [os.path.join(os.getcwd(), path) for path in args.path]
    files = set()
    for path in full_paths:
        print('Path: {}'.format(path))
        drive_info = getDriveInfo(path)
        print('Drive Info: {}'.format(drive_info))
        file_info = getFileInfo(path)
        print('File Info: {}'.format(file_info))

if __name__ == '__main__':
    main()
