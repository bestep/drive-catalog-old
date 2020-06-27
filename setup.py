import os.path
import codecs

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="drive-catalog",
    version=get_version("src/drive_catalog/__init__.py"),
    author="William Estep",
    description="Return formatted file and directory information.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/bestep/drive-catalog",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=['tests']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Affero General "
        "Public License v3 or later (AGPLv3+)",
    ],
    entry_points={
        'console_scripts': [
            'drive-catalog = drive_catalog.main:main',
        ]
    },
    python_requires=">=3.7",
    install_requires=[
        'setuptools',
    ],
    extras_require={
        'lint': [
            'flake8 >= 3.5.0',
        ],
        'test': [
            'pytest',
            'pytest-cov',
        ],
    },
)
