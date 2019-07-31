from selenium.webdriver.common.by import By

class formsPOM:
    URL = 'https://www.ultimateqa.com/filling-out-forms/'

    ContactForm1 = (By.ID, 'et_pb_contact_form_0')
    ContactForm2 = (By.ID, 'et_pb_contact_form_1')

    ContactName1 = (By.ID, 'et_pb_contact_name_0')
    ContactName2 = (By.ID, 'et_pb_contact_name_1')

    ContactMessage1 = (By.ID, 'et_pb_contact_message_0')
    ContactMessage2 = (By.ID, 'et_pb_contact_message_1')

    Submit1 = (By.CSS_SELECTOR, '#et_pb_contact_name_0 .et_pb_contact_submit')
    Submit2 = (By.CSS_SELECTOR, '#et_pb_contact_name_1 .et_pb_contact_submit')

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

    def name_2(self, name):
        name_input = self.browser.find_element(*self.ContactName2)
        name_input.send_keys(name)

    def message_1(self, message):
        message_input = self.browser.find_element(*self.ContactMessage1)
        message_input.send_keys(message)

    def message_2(self, message):
        message_input = self.browser.find_element(*self.ContactMessage2)
        message_input.send_keys(message)

    def submit1(self):
        self.browser.find_element(*self.Submit1).click()

    def submit2(self):
        self.browser.find_element(*self.Submit2).click()

    def captcha_calc(self):
        captcha = self.browser.find_element(*self.Captcha)
        cap1 = captcha.getAttribute('data-first_digit')
        cap2 = captcha.getAttribute('data-second_digit')

        answer = int(cap1) + int(cap2)

        captcha.send_keys(str(answer))

