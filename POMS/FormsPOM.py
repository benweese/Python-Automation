#!/usr/bin/env python

"""
forms_POM.py: .
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

__author__ = "Ben Weese"
__copyright__ = "Copyright 2019, Python Automation"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ben Weese"
__email__ = "ben@benweese.dev"
__status__ = "refactor"


class FormsPOM(object):
    """
    This is the Page Object Model used in test_forms_Page.py for the filling out forms section
    of Ultimate QA's Automation Exercises.
    """
    URL = 'https://www.ultimateqa.com/filling-out-forms/'

    contact_form_1 = (By.ID, 'et_pb_contact_form_0')
    contact_form_2 = (By.ID, 'et_pb_contact_form_1')

    contact_name_1 = (By.ID, 'et_pb_contact_name_0')
    contact_name_2 = (By.ID, 'et_pb_contact_name_1')

    contact_message_1 = (By.ID, 'et_pb_contact_message_0')
    contact_message_2 = (By.ID, 'et_pb_contact_message_1')

    submit_1 = (By.CSS_SELECTOR, "#et_pb_contact_form_0 button.et_pb_contact_submit")
    submit_2 = (By.CSS_SELECTOR, "#et_pb_contact_form_1 button.et_pb_contact_submit")

    captcha = (By.NAME, 'et_pb_contact_captcha_1')

    sh_tweet = (By.CLASS_NAME, 'share-twitter')
    sh_facebook = (By.CLASS_NAME, 'share-facebook')
    sh_pocket = (By.CLASS_NAME, 'share-pocket')
    sh_linkedin = (By.CLASS_NAME, 'share-linkedin')
    sh_tumblr = (By.CLASS_NAME, 'share-tumblr')

    twitter = (By.CLASS_NAME, 'swp_share_link')
    linkedin = (By.CLASS_NAME, 'swp_linkedin')
    email = (By.CLASS_NAME, 'swp_email')
    tumblr = (By.CLASS_NAME, 'swp_tumblr')
    facebook = (By.CLASS_NAME, 'swp_facebook')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def name_1(self, name):
        name_input = self.browser.find_element(*self.contact_name_1)
        name_input.send_keys(name)

    def get_name_1(self):
        return self.browser.find_element(*self.contact_name_1).get_attribute('value')

    def name_2(self, name):
        name_input = self.browser.find_element(*self.contact_name_2)
        name_input.send_keys(name)

    def get_name_2(self):
        return self.browser.find_element(*self.contact_name_2).get_attribute('value')

    def message_1(self, message):
        message_input = self.browser.find_element(*self.contact_message_1)
        message_input.send_keys(message)

    def get_message_1(self):
        message = self.browser.find_element(*self.contact_message_1)
        return message.get_attribute('value')

    def message_2(self, message):
        message_input = self.browser.find_element(*self.contact_message_2)
        message_input.send_keys(message)

    def get_message_2(self):
        message = self.browser.find_element(*self.contact_message_2)
        return message.get_attribute('value')

    def submit1(self):
        submit = self.browser.find_element(*self.submit_1)
        submit.click()

    def submit2(self):
        submit = self.browser.find_element(*self.submit_2)
        submit.click()

    def captcha_calc(self):
        captcha = self.browser.find_element(*self.captcha)
        cap1 = captcha.get_attribute('data-first_digit')
        cap2 = captcha.get_attribute('data-second_digit')

        answer = int(cap1) + int(cap2)

        captcha.send_keys(str(answer))

    def wait_form1(self, success_message):
        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element(self.contact_form_1, success_message))

    def wait_form2(self, success_message):
        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element(self.contact_form_2, success_message))

    def get_form_text1(self):
        text = self.browser.find_element(*self.contact_form_1)
        return text.text

    def get_form_text2(self):
        text = self.browser.find_element(*self.contact_form_2)
        return text.text

    def share_tweet(self):
        element = self.browser.find_element(*self.sh_tweet)
        element.click()

    def share_facebook(self):
        element = self.browser.find_element(*self.sh_facebook)
        element.click()

    def share_pocket(self):
        self.browser.find_element(*self.sh_pocket).click()

    def share_linkedin(self):
        element = self.browser.find_element(*self.sh_linkedin)
        element.click()

    def share_tumblr(self):
        element = self.browser.find_element(*self.sh_tumblr)
        element.click()

    def link_tweet(self):
        element = self.browser.find_element(*self.twitter)
        element.click()

    def link_linked_in(self):
        element = self.browser.find_element(*self.linkedin)
        element.click()

    def link_email(self):
        element = self.browser.find_element(*self.email)
        element.click()

    def link_tumblr(self):
        element = self.browser.find_element(*self.tumblr)
        element.click()

    def link_facebook(self):
        element = self.browser.find_element(*self.facebook)
        element.click()
