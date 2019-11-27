from selenium import webdriver


class OnlineBankingPage(object):

    __transferFundsLink = "transfer_funds_link"
    __accountSummaryLink = "account_summary_link"

    def __init__(self, driver):
        print("Initialising Online banking page object")
        self.driver = driver

    def getPageHeading(self):
        return self.driver.find_element_by_tag_name("h1").text

    def navigateToTransferFundsPage(self):
        self.driver.find_element_by_id(self.__transferFundsLink).click()

    def verifyTransferFundsLink(self):
        return self.driver.find_element_by_id(self.__transferFundsLink).is_displayed()

    def verifyAccountSummaryLink(self):
        return self.driver.find_element_by_id(self.__accountSummaryLink).is_displayed()
