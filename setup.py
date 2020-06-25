import re
import sys

from setuptools import setup, find_packages

import src.drive_catalog as drive_catalog

with open('README.RST') as f:
    long_desc = f.read()

setup(
    name = "Drive Catalog",
    version = drive_catalog.__version__,
    author = "William Estep",
    description = "Return formatted file and directory information.",
    long_description = long_desc,
    long_description_content_type='text/x-rst',
    package_dir = {"": "src"},
    packages = find_packages(where="src", exclude=['tests']),
    entry_points = {
        'console_scripts': [
            'drive-catalog = drive_catalog.main:main',
        ]
    },
    python_requires = ">=3.7",
    install_requires = [
        'setuptools',
    ],
    extras_require = {
        'lint': [
            'flake8 >= 3.5.0',
        ],
        'test': [
            'pytest',
            'pytest-cov',
        ],
    },
)
