import sys
import os
import argparse
from datetime import datetime
from pathlib import Path


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def addFilesToDatabase(self, path, scope, newDrive, progress_callback):
    # create session and connection for this thread.
    temp_session = Session()
    # set the extensions to search for
    images_set = set(['.jpg', '.JPG', '.jpx', '.png', '.gif',
                      '.tif', '.bmp', '.psd', 'heic', '.eps'])
    videos_set = set(['.MP4', '.mp4', '.m4v', '.mkv', '.webm',
                      '.mov', '.avi', '.wmv', '.mpg', '.flv', '.MOV'])
    audio_set = set(['mp3', '.m4a', '.ogg', '.falc', '.wav'])
    # Set variables then write new file to database
    p = Path(path)

    # Recursive walk
    n = 0
    # find out the number of files for progress bar
    total_files = len(list(p.glob("**/*")))
    print('total_files: {}'.format(total_files))
    for child in p.glob("**/*"):
        n = n + 1
        progress_callback.emit(n*100/total_files)
        if child.is_dir():
            continue
        elif child.exists():
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
            if (scope == "Media Files" and fileType == ""):
                continue
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
            drive_id = newDrive.id

            currentfile = File(fileName,
                               fileSize,
                               fileType,
                               filepath,
                               thumbnail,
                               create_date,
                               drive_id)
            temp_session.add(currentfile)
            temp_session.commit()
            # print('{} added to database.'.format(fileName))
    return "Done."

def main():
    print('Running Main!')
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
    
    # Execute the parser_args method
    args = my_parser.parse_args()

    #parse paths
    full_paths = [os.path.join(os.getcwd(), path) for path in args.path]
    files = set()
    for path in full_paths:
        print('Path: {}'.format(path))


if __name__ == '__main__':
    main()
