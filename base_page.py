#!/usr/bin/env python
# -*- coding: utf8 -*-

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import requests
from config import users_data_link
import selenium.common.exceptions as EX


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, for_asserts=False):
        if for_asserts:
            try:
                return self.driver.find_element(By.XPATH, locator)
            except EX.NoSuchElementException:
                return False
        else:
            return self.driver.find_element(By.XPATH, locator)

    def wait_present(self, locator, for_asserts=False):
        if for_asserts:
            try:
                return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, locator)))
            except EX.NoSuchElementException:
                return False
        else:
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, locator)))


    def get_sms_code(self, user):
        """Заглушка. Здесь я ищу отправленную смс по параметрам пользователя в кокой нибудь системе"""
        sms_code = '111111'
        return sms_code

    def get_wrong_sms_code(self, user):
        """ Заглушка """
        sms_code = self.get_sms_code(user)
        wrong_code = ''
        for i in sms_code:
            if int(i) != 9:
                i = int(i)
                i += 1
                wrong_code += str(i)
            else:
                wrong_code += '0'
        return wrong_code
