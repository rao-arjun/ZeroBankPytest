from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common import keys

class HomePage(object):

    __homeLink = "#nav > #pages-nav > #homeMenu"
    __searchBox = "input[type='text'][id='searchTerm']"
    __signInButton = "signin_button"
    __onlineBankingMenu = "#nav > #pages-nav > #onlineBankingMenu"
    __zeroBankHomeButton = "//a[text()='Zero Bank']"

    def __init__(self, driver):
        print('Initializing home page object')
        self.driver = driver

    def goToOnlineBankingPage(self):
        self.driver.find_element_by_css_selector(self.__onlineBankingMenu).click()

    def verifyHomePage(self):
        return self.driver.find_element_by_css_selector(self.__homeLink).is_displayed()

    def goToLoginPage(self):
        self.driver.find_element_by_id(self.__signInButton).click()

    def enterSearch(self, searchItem):
        self.driver.find_element_by_css_selector(self.__searchBox).clear()
        self.driver.find_element_by_css_selector(self.__searchBox).send_keys(searchItem)
        actions = ActionChains(self.driver)
        actions.key_down(keys.Keys.ENTER).key_up(keys.Keys.ENTER).perform()

    def clickZeroBankHomeButton(self):
        self.driver.find_element_by_xpath(self.__zeroBankHomeButton).click()