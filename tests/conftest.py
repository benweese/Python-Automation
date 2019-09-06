#!/usr/bin/env python

"""
conftest.py: Configures the chrome browser for use.
"""

import os

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

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
	chrome_options = Options()
	chrome_options.add_argument("--no-sandbox")
	chrome_options.add_argument("--disable-gpu")
	chrome_options.add_argument("--window-size=1400x1200")
	chrome_options.add_argument("--disable-extensions")

	path = os.getcwd()
	if path == "/root/project":
		chrome_options.add_argument("--headless")
		driver = Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
 	else:
 		driver = Chrome(executable_path=path + '/chromedriver', chrome_options=chrome_options)
 	driver.implicitly_wait(10)
 	yield driver
	driver.quit()
