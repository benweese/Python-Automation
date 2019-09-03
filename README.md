# BenWeese.Dev
- [Home](https://benweese.dev)
- [Java Automation](https://benweese.dev/Java_Automation/)
- [Postman](https://benweese.dev/Postman/)
- [BenWeese.com](https://benweese.com)

# Python Automation
This project is for practicing Python, Selenium, and Pytest. You can find the link for the template above for creating your own automation. To learn more you can check out the [Wiki](https://github.com/benweese/Python-Automation/wiki) for this repo where I document what I have learned. 

## Badges
[![CircleCI](https://circleci.com/gh/benweese/Python-Automation/tree/master.svg?style=shield)](https://circleci.com/gh/benweese/Python-Automation/tree/master) ![Actions](https://github.com/benweese/Python-Automation/workflows/Python%20package/badge.svg) ![GitHub](https://img.shields.io/github/license/benweese/Python-Automation.svg) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=benweese_Python-Automation&metric=alert_status)](https://sonarcloud.io/dashboard?id=benweese_Python-Automation)  ![GitHub issues](https://img.shields.io/github/issues-raw/benweese/Python-Automation.svg) [![StackShare](http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/benweese/python-automation)

## Motivation
This is to keep my automation skills sharp.

## Notification
This automation is happy path only and does not test for failures. It is an example and learning on how it can done. If you wish to test more thoroughly then I would suggest adding Pytest-BDD and use a Scenario Outline to test many different scenarios including failures.

## Tools
<b>Built with</b>
- [Pycharm Community](https://www.jetbrains.com/pycharm/)

<b>Testing Language</b>
- [Selenium](https://www.seleniumhq.org/)

<b>Continuous Integration</b>
- [CircleCI](https://circleci.com/)

<b>Dependency Maintenance </b>
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
    ...
    def captcha_calc(self):
        captcha = self.browser.find_element(*self.captcha)
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

    forms_page = FormsPOM(browser)
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

<b>API Test</b>
```
def swapi_films(episode):
	"""
	Gets the films listed in the api.
	:param episode:
	:return: response json
	"""
	response = requests.get(SWAPI_API + 'films/' + str(episode))
	return response


def swapi_film_code(episode):
	"""
	Asserts that a 200 was returned
	:param episode:
	"""
	assert swapi_films(episode).status_code == 200


def swapi_films_episode(name, episode):
	"""
	This checks that all the films are in the response.
	:param name:
	:param episode:
	"""
	assert name.lower() == swapi_films(episode).json()['title'].lower()


def test_episode_1():
	"""
	This runs through episode 1.
	"""
	swapi_film_code(1)
	swapi_films_episode('A New Hope', 1)
```

## Documentation
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/chapter11/)
- [Behavior Driven Python with pytest-bdd](https://testautomationu.applitools.com/behavior-driven-python-with-pytest-bdd/)
- [tau-pytest-bdd github](https://github.com/AndyLPK247/tau-pytest-bdd)
- [Web	Testing Made Easy with Python, Pytest and Selenium WebDriver](https://blog.testproject.io/2019/07/16/open-source-test-automation-python-pytest-selenium-webdriver/)

## Credits
[Ben Weese](https://benweese.dev)
