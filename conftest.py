#!/usr/bin/env python
# -*- coding: utf8 -*-

import pytest
import os
import requests
import config
from selenium import webdriver
from file_helper import FileHelper


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def get_user():
    r = requests.get(config.users_data_link).json()
    user = {'email': r[1]['email'],
            'phone': r[1]['phone'],
            'password': r[1]['website']}
    return user


@pytest.hookimpl
def pytest_sessionstart(session):
    """Удаление старого отчёта при запуске тестов"""
    if os.path.exists(config.report_file):
        os.remove(config.report_file)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """ Создание отчёта по упавшим тестам"""
    # PS. Такую хрень я бы использовать не стал,
    # но по уловиям задачи использовать готовые решения, например allure, нельзя
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        report_text = rep.nodeid + '\n' * 2 + rep.longreprtext + "\n" + '===' * 20 + '\n'
        FileHelper.write_file(config.report_file, report_text)




