#!/usr/bin/env python

"""
conftest.py: Configures the chrome browser for use.
"""

import os

import pytest
from selenium.webdriver import Chrome

__author__ = "Ben Weese"
__copyright__ = "Copyright 2019, Python Automation"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ben Weese"
__email__ = "ben@benweese.dev"
__status__ = "refactor"


@pytest.fixture
def browser():
    """
     Configures the chrome browser for use.
    """
    driver = Chrome(executable_path=os.getcwd() + '/chromedriver')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
