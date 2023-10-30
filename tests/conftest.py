import pytest
import sys

from pathlib import Path

pytest_plugins = 'sphinx.testing.fixtures'

# Exclude 'roots' dirs for pytest test collector
collect_ignore = ['roots']
# Add the parent directory to the Python system path so we can load from extensions
repo_root_path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, repo_root_path)


@pytest.fixture(scope='session')
def rootdir():
    return Path(__file__).parent.absolute() / 'roots'
