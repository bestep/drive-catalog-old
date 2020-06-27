import os
import click

from drive_catalog import __version__
from drive_catalog import driveinfo
from drive_catalog import fileinfo


@click.command()
@click.version_option(version=__version__)
@click.argument('path')
def main(path):

    # parse paths
    full_path = os.path.join(os.getcwd(), path)
    if os.path.exists(full_path):
        print('Path: {}'.format(full_path))
        drive_info = driveinfo.get_drive_info(full_path)
        print('Drive Info: {}'.format(drive_info))
        file_info = fileinfo.get_file_info(full_path)
        print('File Info: {}'.format(file_info))
    else:
        print("Path does not exist.")


if __name__ == '__main__':
    main()
