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
	path = os.getcwd()
	if path == "/home/circleci/project":
		driver = Chrome(executable_path=path + '/chromedriver_linux')
	else:
		driver = Chrome(executable_path=path + '/chromedriver')
	driver.implicitly_wait(10)
	yield driver
	driver.quit()
