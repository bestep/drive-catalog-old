import sys

sys.path.append('src')

import drive_catalog

def test_version():
    assert drive_catalog.__version__ == '0.1.0'
