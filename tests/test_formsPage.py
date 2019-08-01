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


def test_form2(browser):
    name = 'John Doe'

    forms_page = formsPOM(browser)
    forms_page.load()
    forms_page.name_2(name)
    assert forms_page.get_name_2() == name

    message = 'I am Batman'
    forms_page.message_2(message)
    assert forms_page.get_message_2() == message

    forms_page.captcha_calc()
    forms_page.submit2()

    success_message = 'Success'

    try:
        forms_page.wait_form2(success_message)
    finally:
        assert forms_page.get_form_text2() == success_message
        browser.quit()


def test_share_tweet(browser):
    forms_page = formsPOM(browser)
    forms_page.load()

    forms_page.sh_tweet()
    browser.implicitly_wait(10)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(10)

    nw_url = 'https://twitter.com/intent/tweet?text=Filling%20Out%20Forms&url=https%3A%2F%2Fwww.ultimateqa.com%2Ffilling-out-forms%2F'
    assert browser.current_url == nw_url
    browser.quit()


def test_share_facebook(browser):
    forms_page = formsPOM(browser)
    forms_page.load()
    forms_page.sh_facebook()
    browser.implicitly_wait(10)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(10)

    nw_url = 'https://www.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fwww.ultimateqa.com%252Ffilling-out-forms%252F%26t%3DFilling%2BOut%2BForms&cancel_url=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=popup&locale=en_US'
    assert browser.current_url == nw_url
    browser.quit()


def test_share_pocket(browser):
    forms_page = formsPOM(browser)
    forms_page.load()
    forms_page.sh_pocket()
    browser.implicitly_wait(10)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(10)

    nw_url = 'https://getpocket.com/login?e=2&route=%2Fedit.php%3Furl%3Dhttps%253A%252F%252Fwww.ultimateqa.com%252Ffilling-out-forms%252F%26url%3Dhttps%253A%252F%252Fwww.ultimateqa.com%252Ffilling-out-forms%252F%26title%3DFilling%2520Out%2520Forms'
    assert browser.current_url == nw_url
    browser.quit()


def test_share_linkedin(browser):
    forms_page = formsPOM(browser)
    forms_page.load()
    forms_page.sh_linkedin()

    browser.implicitly_wait(10)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(10)

    nw_url = 'https://www.linkedin.com/m/login/'
    assert browser.current_url == nw_url
    browser.quit()


def test_share_tumblr(browser):
    forms_page = formsPOM(browser)
    forms_page.load()
    forms_page.sh_tumblr()

    browser.implicitly_wait(10)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(10)

    nw_url = 'https://www.tumblr.com/login?redirect_to=https%3A%2F%2Fwww.tumblr.com%2Fwidgets%2Fshare%2Ftool%3FshareSource%3Dlegacy%26canonicalUrl%3D%26url%3Dhttps%253A%252F%252Fwww.ultimateqa.com%252Ffilling-out-forms%252F%26title%3DFilling%2BOut%2BForms'
    assert browser.current_url == nw_url
    browser.quit()


def test_twitter_link(browser):
    forms_page = formsPOM(browser)
    forms_page.load()
    forms_page.tweet()
    browser.implicitly_wait(10)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(10)

    nw_url = 'https://twitter.com/intent/tweet?text=Filling+Out+Forms&url=https%3A%2F%2Fwww.ultimateqa.com%2Ffilling-out-forms%2F&via=Nikolay_A00'
    assert browser.current_url == nw_url
    browser.quit()


def test_linkedin_link(browser):
    forms_page = formsPOM(browser)
    forms_page.load()
    forms_page.linkedin()

    browser.implicitly_wait(10)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(10)

    nw_url = 'https://www.linkedin.com/m/login/'
    assert browser.current_url == nw_url
    browser.quit()


# def test_email_link(browser):
#     forms_page = formsPOM(browser)
#     forms_page.load()
#     forms_page.email()
#
#     browser.implicitly_wait(10)
#
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#     time.sleep(10)


def test_tumblr_link(browser):
    forms_page = formsPOM(browser)
    forms_page.load()
    forms_page.tumblr()

    browser.implicitly_wait(10)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(10)

    nw_url = 'https://www.tumblr.com/login?redirect_to=https%3A%2F%2Fwww.tumblr.com%2Fwidgets%2Fshare%2Ftool%3FshareSource%3Dlegacy%26canonicalUrl%3D%26url%3Dhttps%253A%252F%252Fwww.ultimateqa.com%252Ffilling-out-forms%252F%26title%3DFilling%2BOut%2BForms'
    assert browser.current_url == nw_url
    browser.quit()


def test_facebook_link(browser):
    forms_page = formsPOM(browser)
    forms_page.load()
    forms_page.facebook()
    browser.implicitly_wait(10)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(10)

    nw_url = 'https://www.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fshare.php%3Fu%3Dhttps%253A%252F%252Fwww.ultimateqa.com%252Ffilling-out-forms%252F&cancel_url=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=popup&locale=en_US'
    assert browser.current_url == nw_url
    browser.quit()