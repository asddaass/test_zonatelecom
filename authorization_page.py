from base_page import BasePage
from locators import AuthLocators as AuthL
import selenium.common.exceptions as ex


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_by_email(self, login):
        self.find(AuthL.email_switcher).click()
        self.find(AuthL.login_field).send_keys(login)
        self.find(AuthL.enter_button).click()

    def enter_by_phone(self, phone):
        self.find(AuthL.phone_switcher).click()
        self.find(AuthL.phone_field).send_keys(phone)
        self.find(AuthL.enter_button).click()

    def enter_password(self, password):
        self.find(AuthL.password_field).send_keys(password)
        self.find(AuthL.enter_button).click()

    def enter_wrong_password(self, password):
        self.find(AuthL.password_field).send_keys(password + '11')
        self.find(AuthL.enter_button).click()

    def enter_sms_code(self, user):
        sms = self.get_sms_code(user)
        self.find(AuthL.sms_code_field).send_keys(sms)

    def enter_wrong_sms_code(self, user):
        wrong_sms = self.get_wrong_sms_code(user)
        self.find(AuthL.sms_code_field).send_keys(wrong_sms)

    def enter_by_social_site(self, user, soc_type):
        if soc_type == 'google':
            self.find(AuthL.social_google_button).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.find(AuthL.social_google_login_field).send_keys(user['email'])
            self.find(AuthL.social_google_next_button).click()
            assert self.find(AuthL.social_google_password_field, True), 'Не корректный эмейл, поле для пароля не появилось'
            self.find(AuthL.social_google_password_field).send_keys(user['password'])
            self.find(AuthL.social_google_next_button).click()
            assert isinstance(self.find(AuthL.social_google_password_error, True), ex.NoSuchElementException), 'Неверный пароль'
            self.driver.switch_to.window(self.driver.window_handles[0])

    def check_correct_email(self):
        assert self.find(AuthL.password_field, True), 'Не корректный эмейл, поле для пароля не появилось'

    def check_correct_phone(self):
        assert self.find(AuthL.sms_code_field, True), 'Не корректный номер, поле для смс не появилось'

    def check_successful_login(self):
        assert self.wait_present(AuthL.lk_home_locator, True), 'Вход не выполнен'

    def check_password_error(self):
        assert self.wait_present(AuthL.password_error_text, True), 'Ошибка неверного пароля не появилась'

    def check_sms_error(self):
        """В текущей реализации на фронте ошибок нет, просто стирается код и поле ввода становится пустым"""
        value = self.find(AuthL.sms_code_field).get_attribute('value')
        assert value == '', 'Поле ввода смс кода не очистилось'
