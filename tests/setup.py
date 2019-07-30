import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser = webdriver.Chrome(executable_path=os.getcwd())

Automation_form = 'https://www.ultimateqa.com/filling-out-forms/'

def go_home(browser):
    browser.get(Automation_form)
