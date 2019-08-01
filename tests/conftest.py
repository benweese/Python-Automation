import os
import pytest

from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path=os.getcwd())
    driver.implicitly_wait(10)
    yield driver
    driver.quit()