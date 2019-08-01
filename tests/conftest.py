import os
import pytest

from selenium.webdriver import Chrome

@pytest.fixture
def browser():
    driver = Chrome(executable_path=os.getcwd()+'/chromedriver')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()