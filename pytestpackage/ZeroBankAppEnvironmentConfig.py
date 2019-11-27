import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox


class AppSetUpTearDown(object):

    __SITE_URL = "http://zero.webappsecurity.com/index.html"

    def __init__(self):
        # self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        # self.driver.get(self.__SITE_URL)
        self.driver = webdriver.Chrome()
        print('Initiating web driver session in Chrome')
        self.driver.maximize_window()

    def getWebDriver(self):
        self.driver.get(self.__SITE_URL)
        return self.driver

    def tearDownDriver(self):
        print('Tearing down web driver')
        self.driver.close()
        self.driver.quit()
