import os

from drive_catalog import driveinfo


def test_driveinfo_succeeds():
    path = os.path.join(os.getcwd(), 'testdrive')
    result = driveinfo.get_drive_info(path)
    assert result['name'] == 'testdrive'
