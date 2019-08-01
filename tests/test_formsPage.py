import os
import pytest
import time

from POMS.FormsPOM import formsPOM
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    message = 'I am Batman'
    forms_page.ContactMessage1(message)
    contact_message = browser.find_element(formsPOM.ContactMessage1)
    assert contact_message.getAttribute('value') == message

    forms_page.submit1()

    success_message = 'Form filled out successfully'

    try:
        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(
            formsPOM.ContactForm1, success_message))
    finally:
        form_text = browser.find_element(formsPOM.ContactForm1)
        assert form_text.getText() == success_message
        browser.quit()


def test_form2(browser):
    name = 'John Doe'

    forms_page = formsPOM(browser)
    forms_page.load()
    forms_page.name_2(name)
    contact_name = browser.find_element(formsPOM.ContactName2)
    assert contact_name.getAttribute('value') == name

    message = 'I am Batman'
    forms_page.ContactMessage2(message)
    contact_message = browser.find_element(formsPOM.ContactMessage2)
    assert contact_message.getAttribute('value') == message

    forms_page.Captcha()
    forms_page.submit2()

    success_message = 'Success'

    try:
        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(
            formsPOM.ContactForm1, success_message))
    finally:
        form_text = browser.find_element(formsPOM.ContactForm2)
        assert form_text.getText() == success_message
        browser.quit()


def share_tweet(browser):
    browser.implicitly_wait(10)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(10)

    tw_url = "https://twitter.com/intent/tweet?text=Complicated+Page&url=https%3A%2F%2Fwww.ultimateqa.com%2Fcomplicated-page%2F&via=Nikolay_A00";
    assert browser.current_url == tw_url
    browser.quit()


# def share_facebook(browser):
# Place Holder


# def share_pocket(browser):
# Place Holder


# def share_linkedin(browser):
# Place Holder


# def share_tumblr(browser):
# Place Holder


# def twitter_link(browser):
# Place Holder


# def linkedin_link(browser):
# Place Holder


# def email_link(browser):
# Place Holder


# def tumblr_link(browser):
# Place Holder


# def facebook_link(browser):
# Place Holder