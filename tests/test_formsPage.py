from POMS.FormsPOM import formsPOM
import pytest
from selenium import webdriver
import os

@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path=os.getcwd())
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_form1(browser):
    name = 'John Doe'

    forms_page = formsPOM(browser)
    forms_page.load()
    forms_page.name_1(name)
    contact_name = browser.find_element(formsPOM.ContactName1)
    assert contact_name.getAttribute('value') == name

