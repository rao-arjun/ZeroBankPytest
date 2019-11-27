from selenium import webdriver


class SignInPage(object):

    __loginTextField = "user_login"
    __password = "user_password"
    __signInButton = "input[type=''][value='Sign in']"
    __pageHeader = "h3"

    def __init__(self, driver):
        print("Initialising Sign in page object")
        self.driver = driver

    def performLogin(self, username, password):
        self.driver.find_element_by_id(self.__loginTextField).send_keys(username)
        self.driver.find_element_by_id(self.__loginTextField).send_keys(password)
        self.driver.find_element_by_css_selector(self.__signInButton).click()

    def getHeaderTextLoginPage(self):
        return self.driver.find_element_by_tag_name(self.__pageHeader).text
