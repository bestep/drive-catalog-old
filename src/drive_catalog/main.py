import sys
import os
import argparse
from datetime import datetime
from pathlib import Path
from shutil import disk_usage

sys.path.append('src')
from drive_catalog import __version__
from drive_catalog import driveinfo
from drive_catalog import fileinfo

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
        drive_info = driveinfo.get_drive_info(path)
        print('Drive Info: {}'.format(drive_info))
        file_info = fileinfo.get_file_info(path)
        print('File Info: {}'.format(file_info))

if __name__ == '__main__':
    main()
