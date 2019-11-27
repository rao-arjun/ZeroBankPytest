from selenium import webdriver


class SearchResultsPage:

    __searchresultsheader = "h2"
    __searchresultlinktext = "//ul/li/a"

    def __init__(self, driver):
        print("Initialising Search Results page object")
        self.driver = driver

    def verifySearchResultsPageDisplayed(self):
        return self.driver.find_element_by_tag_name(self.__searchresultsheader).is_displayed()

    def returnSearchResultText(self):
        return self.driver.find_element_by_xpath(self.__searchresultlinktext).text
