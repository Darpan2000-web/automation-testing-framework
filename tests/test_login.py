from pages.login_page import LoginPage
from data.login_data import *

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login(valid_user, valid_pass)

    assert "You logged into a secure area!" in login.get_message()


def test_invalid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login(invalid_user, invalid_pass)

    assert "Your username is invalid!" in login.get_message()