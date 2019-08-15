# BenWeese.Dev
- [Home](https://benweese.dev)
- [Java Automation](https://benweese.dev/Java_Automation/)
- [Postman](https://benweese.dev/Postman/)
- [BenWeese.com](https://benweese.com)

# Python Automation
This project is for practiceing Python, Selenuim, and Pytest. You can find the link for the template above for creating your own automation. To learn more you can check out the [Wiki](https://github.com/benweese/Python-Automation/wiki) for this repo where I document what I have learned. 

## Motivation
This is to keep my automations skills sharp.

# Badges
[![CircleCI](https://circleci.com/gh/benweese/Python-Automation/tree/master.svg?style=shield)](https://circleci.com/gh/benweese/Python-Automation/tree/master) ![GitHub](https://img.shields.io/github/license/benweese/Python-Automation.svg)  ![GitHub issues](https://img.shields.io/github/issues-raw/benweese/Python-Automation.svg) [![StackShare](http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/benweese/python-automation)

## Tools
<b>Built with</b>
- [Pycharm Community](https://www.jetbrains.com/pycharm/)

<b>Testing Language</b>
- [Selenium](https://www.seleniumhq.org/)

<b>Continuous Intergration</b>
- [CircleCI](https://circleci.com/)

<b>Depandacy Maintenance </b>
- [Dependabot by Github](https://dependabot.com/)

<b>Security</b>
- [Sonatype Depshield](https://www.sonatype.com/depshield)

<b>Downloads</b>
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [pip3](https://pip.pypa.io/en/stable/)
- [pipenv](https://docs.pipenv.org/en/latest/)
- [Python3](https://www.python.org/download/releases/3.0/)


## Features
With testing our Circle-CI runner will use maven to run our automation scripts in Command line.

## Page Being Automated
- [Ultimate QA: Automation Exercises: Filling out Forms](https://www.ultimateqa.com/filling-out-forms/)

## Code Example

<b>conftest.py</b>
```
import os
import pytest

from selenium.webdriver import Chrome

@pytest.fixture
def browser():
    driver = Chrome(executable_path=os.getcwd()+'/chromedriver')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
```

<b>Page Object</b>
```
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class formsPOM:
    URL = 'https://www.ultimateqa.com/filling-out-forms/'

    ContactForm1 = (By.ID, 'et_pb_contact_form_0')
    ContactForm2 = (By.ID, 'et_pb_contact_form_1')

    ContactName1 = (By.ID, 'et_pb_contact_name_0')
    ContactName2 = (By.ID, 'et_pb_contact_name_1')
    ...
    Twitter = (By.CLASS_NAME, 'swp_share_link')
    LinkedIn = (By.CLASS_NAME, 'swp_linkedin')
    Email = (By.CLASS_NAME, 'swp_email')
    Tumblr = (By.CLASS_NAME, 'swp_tumblr')
    Facebook = (By.CLASS_NAME, 'swp_facebook')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def name_1(self, name):
        name_input = self.browser.find_element(*self.ContactName1)
        name_input.send_keys(name)

    def get_name_1(self):
        return self.browser.find_element(*self.ContactName1).get_attribute('value')
    ...
    def captcha_calc(self):
        captcha = self.browser.find_element(*self.Captcha)
        cap1 = captcha.get_attribute('data-first_digit')
        cap2 = captcha.get_attribute('data-second_digit')

        answer = int(cap1) + int(cap2)

        captcha.send_keys(str(answer))
```
  
<b>Test</b>
```
import time

from POMS.FormsPOM import formsPOM



def test_form1(browser):
    name = 'John Doe'

    forms_page = formsPOM(browser)
    forms_page.load()
    forms_page.name_1(name)
    assert forms_page.get_name_1() == name

    message = 'I am Batman'
    forms_page.message_1(message)
    assert forms_page.get_message_1() == message

    forms_page.submit1()

    success_message = 'Form filled out successfully'

    try:
        forms_page.wait_form1(success_message)
    finally:
        assert forms_page.get_form_text1() == success_message
        browser.quit()
```

## Documentation
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/chapter11/)
- [Behavior Driven Python with pytest-bdd](https://testautomationu.applitools.com/behavior-driven-python-with-pytest-bdd/)
- [tau-pytest-bdd github](https://github.com/AndyLPK247/tau-pytest-bdd)
- [Web	Testing Made Easy with Python, Pytest and Selenium WebDriver](https://blog.testproject.io/2019/07/16/open-source-test-automation-python-pytest-selenium-webdriver/)

## Credits
[Ben Weese](https://benweese.dev)
