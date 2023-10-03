from config import auth_link
from authorization_page import AuthPage


class TestAuthorization:

    def test_successful_enter_by_email(self, driver, get_user):
        driver.get(auth_link)
        AuthPage(driver).enter_by_email(get_user['email'])
        AuthPage(driver).check_correct_email()
        AuthPage(driver).enter_password(get_user['password'])
        AuthPage(driver).check_successful_login()

    def test_enter_by_email_with_wrong_password(self, driver, get_user):
        driver.get(auth_link)
        AuthPage(driver).enter_by_email(get_user['email'])
        AuthPage(driver).check_correct_email()
        AuthPage(driver).enter_wrong_password(get_user['password'])
        AuthPage(driver).check_password_error()

    def test_successful_enter_by_phone(self, driver, get_user):
        driver.get(auth_link)
        AuthPage(driver).enter_by_phone(get_user['phone'])
        AuthPage(driver).check_correct_phone()
        AuthPage(driver).enter_sms_code(get_user)
        AuthPage(driver).check_successful_login()

    def test_enter_by_phone_with_wrong_sms_code(self, driver, get_user):
        driver.get(auth_link)
        AuthPage(driver).enter_by_phone(get_user['phone'])
        AuthPage(driver).check_correct_phone()
        AuthPage(driver).enter_wrong_sms_code(get_user)
        AuthPage(driver).check_sms_error()

    def test_successful_enter_by_social_site_google(self, driver, get_user):
        driver.get(auth_link)
        AuthPage(driver).enter_by_social_site(get_user, 'google')
        AuthPage(driver).check_successful_login()
