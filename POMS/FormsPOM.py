from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class formsPOM:
    URL = 'https://www.ultimateqa.com/filling-out-forms/'

    ContactForm1 = (By.ID, 'et_pb_contact_form_0')
    ContactForm2 = (By.ID, 'et_pb_contact_form_1')

    ContactName1 = (By.ID, 'et_pb_contact_name_0')
    ContactName2 = (By.ID, 'et_pb_contact_name_1')

    ContactMessage1 = (By.ID, 'et_pb_contact_message_0')
    ContactMessage2 = (By.ID, 'et_pb_contact_message_1')

    Submit1 = (By.CSS_SELECTOR, "#et_pb_contact_form_0 button.et_pb_contact_submit")
    Submit2 = (By.CSS_SELECTOR, "#et_pb_contact_form_1 button.et_pb_contact_submit")

    Captcha = (By.NAME, 'et_pb_contact_captcha_1')

    ShTweet = (By.CLASS_NAME, 'share-twitter')
    ShFacebook = (By.CLASS_NAME, 'share-facebook')
    ShPocket = (By.CLASS_NAME, 'share-pocket')
    ShLinkedIn = (By.CLASS_NAME, 'share-linkedin')
    ShTumblr = (By.CLASS_NAME, 'share-tumblr')

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

    def name_2(self, name):
        name_input = self.browser.find_element(*self.ContactName2)
        name_input.send_keys(name)

    def get_name_2(self):
        return self.browser.find_element(*self.ContactName2).get_attribute('value')

    def message_1(self, message):
        message_input = self.browser.find_element(*self.ContactMessage1)
        message_input.send_keys(message)

    def get_message_1(self):
        message = self.browser.find_element(*self.ContactMessage1)
        return message.get_attribute('value')

    def message_2(self, message):
        message_input = self.browser.find_element(*self.ContactMessage2)
        message_input.send_keys(message)

    def get_message_2(self):
        message = self.browser.find_element(*self.ContactMessage2)
        return message.get_attribute('value')

    def submit1(self):
        submit = self.browser.find_element(*self.Submit1)
        submit.click()

    def submit2(self):
        submit = self.browser.find_element(*self.Submit2)
        submit.click()

    def captcha_calc(self):
        captcha = self.browser.find_element(*self.Captcha)
        cap1 = captcha.get_attribute('data-first_digit')
        cap2 = captcha.get_attribute('data-second_digit')

        answer = int(cap1) + int(cap2)

        captcha.send_keys(str(answer))

    def wait_form1(self, success_message):
        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element(*self.ContactForm1, success_message))

    def wait_form2(self, success_message):
        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element(*self.ContactForm1, success_message))

    def get_form_text1(self):
        text = self.browser.find_element(*self.ContactForm1)
        return text.text

    def get_form_text2(self):
        text = self.browser.find_element(*self.ContactForm2)
        return text.text

    def sh_tweet(self):
        element = self.browser.find_element(*self.ShTweet)
        element.click()

    def sh_facebook(self):
        element = self.browser.find_element(*self.ShFacebook)
        element.click()

    def sh_pocket(self):
        self.browser.find_element(*self.ShPocket).click()

    def sh_linkedin(self):
        element = self.browser.find_element(*self.ShLinkedIn)
        element.click()

    def sh_tumblr(self):
        element = self.browser.find_element(*self.ShTumblr)
        element.click()

    def tweet(self):
        element = self.browser.find_element(*self.Twitter)
        element.click()

    def linkedin(self):
        element = self.browser.find_element(*self.LinkedIn)
        element.click()

    def email(self):
        element = self.browser.find_element(*self.Email)
        element.click()

    def tumblr(self):
        element = self.browser.find_element(*self.Tumblr)
        element.click()

    def facebook(self):
        element = self.browser.find_element(*self.Facebook)
        element.click()