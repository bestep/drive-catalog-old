import sys
import click.testing
import pytest

sys.path.append('src')

from drive_catalog import console 
from drive_catalog import __version__

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_console_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 2

def test_console_returns_version(runner):
    result = runner.invoke(console.main, '--version')
    assert result.exit_code == 0
    assert result.output == 'main, version ' + __version__ + '\n'

def test_console_return_path(runner):
    result = runner.invoke(console.main, 'testdrive')
    assert result.exit_code == 0
    assert "Path:" in result.output 

def test_console_return_drive(runner):
    result = runner.invoke(console.main, 'testdrive')
    assert result.exit_code == 0
    assert "Drive Info:" in result.output

def test_console_return_badpath(runner):
    result = runner.invoke(console.main, 'abcdefg')
    assert result.exit_code == 0
    assert "Path does not exist" in result.output

