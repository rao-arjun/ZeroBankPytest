from selenium import webdriver
import unittest

from selenium.webdriver.chrome.webdriver import WebDriver


class AppSetUpTearDown(unittest.TestCase):

    __SITE_URL = "http://zero.webappsecurity.com/index.html"

    @classmethod
    def setUpClass(cls):
        # self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        # self.driver.get(self.__SITE_URL)
        cls.driver = webdriver.Chrome()
        print('Initiating web driver session in Chrome')
        cls.driver.maximize_window()
        cls.driver.get(cls.__SITE_URL)

    @classmethod
    def tearDownClass(cls):
        print('Tearing down web driver')
        cls.driver.close()
        cls.driver.quit()
