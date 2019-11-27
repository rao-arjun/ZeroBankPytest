import unittest

import HtmlTestRunner

from pythonunittests.ZeroBankAppEnvironmentConfig import AppSetUpTearDown
from pages.HomePageObject import HomePage
from pages.OnlineBankingPageObject import OnlineBankingPage
from pages.SignInPageObject import SignInPage
from pages.SearchResultsPageObject import SearchResultsPage
from parameterized import parameterized


class ZeroBankTestCases(AppSetUpTearDown):

    homepage = None
    onlinebankingpage = None
    signinpage = None
    searchresultspage = None

    def setUp(self):
        self.homepage = HomePage(self.driver)
        self.homepage.clickZeroBankHomeButton()

    def test_homePage(self):
        self.assertTrue(self.homepage.verifyHomePage(), "Verify home page is displayed")

    def test_navigate_to_online_banking_section(self):
        # self.homepage.clickZeroBankHomeButton()
        self.homepage.goToOnlineBankingPage()
        self.onlinebankingpage = OnlineBankingPage(self.driver)
        self.assertEqual(self.onlinebankingpage.getPageHeading(), "Online Banking", "Verify Online Banking displayed")

    def test_validate_links_in_online_banking_page(self):
        # self.homepage.clickZeroBankHomeButton()
        self.homepage.goToOnlineBankingPage()
        self.onlinebankingpage = OnlineBankingPage(self.driver)
        self.assertTrue(self.onlinebankingpage.verifyTransferFundsLink(), "Verify transfer funds link displayed")
        self.assertTrue(self.onlinebankingpage.verifyAccountSummaryLink(), "Verify account summary link displayed")

    def test_navigate_to_login_page(self):
        # self.homepage.clickZeroBankHomeButton()
        self.homepage.goToLoginPage()
        self.signinpage = SignInPage(self.driver)
        self.assertEqual(self.signinpage.getHeaderTextLoginPage(), "Log in to ZeroBank", "Verify Login Page displayed")

    @parameterized.expand(["pay bills", "transfer funds"])
    def test_search_feature(self, searchCriterion):
        # self.homepage.clickZeroBankHomeButton()
        self.homepage.enterSearch(searchCriterion)
        self.searchresultspage = SearchResultsPage(self.driver)
        if self.searchresultspage.verifySearchResultsPageDisplayed():
            self.assertTrue(self.searchresultspage.returnSearchResultText().lower().find(searchCriterion) > 0, "Search outcome")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports/'))
