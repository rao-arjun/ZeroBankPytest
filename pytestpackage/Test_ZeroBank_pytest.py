import pytest

from pages.HomePageObject import HomePage
from pages.SignInPageObject import SignInPage
from pages.OnlineBankingPageObject import OnlineBankingPage
from pages.SearchResultsPageObject import SearchResultsPage

from pytestpackage.ZeroBankAppEnvironmentConfig import AppSetUpTearDown


@pytest.fixture(scope='module')
def setup():
    print("Opening application")
    global moduledriver
    global homepage
    app = AppSetUpTearDown()
    moduledriver = app.getWebDriver()
    homepage = HomePage(moduledriver)
    yield
    app.tearDownDriver()


@pytest.mark.skip
def test_skipTest(setup):
    print("Skipped test")


def test_homepage(setup):
    # homepage = HomePage(moduledriver)
    homepage.clickZeroBankHomeButton()
    assert homepage.verifyHomePage()


def test_navigate_to_online_banking_section(setup):
    # homepage = HomePage(moduledriver)
    homepage.clickZeroBankHomeButton()
    homepage.goToOnlineBankingPage()
    onlinebankingpage = OnlineBankingPage(moduledriver)
    assert onlinebankingpage.getPageHeading() == "Online Banking"


def test_validate_links_in_online_banking_page(setup):
    # homepage = HomePage(moduledriver)
    homepage.clickZeroBankHomeButton()
    onlinebankingpage = OnlineBankingPage(moduledriver)
    assert onlinebankingpage.verifyTransferFundsLink()


def test_navigate_to_login_page(setup):
    homepage = HomePage(moduledriver)
    homepage.clickZeroBankHomeButton()
    homepage.goToLoginPage()
    signinpage = SignInPage(moduledriver)
    assert signinpage.getHeaderTextLoginPage() == "Log in to ZeroBank"


@pytest.mark.parametrize("search_section", ["pay bills", "transfer funds"])
def test_search_feature(search_section, setup):
    # homepage = HomePage(moduledriver)
    homepage.clickZeroBankHomeButton()
    homepage.enterSearch(search_section)
    searchresultspage = SearchResultsPage(moduledriver)
    if searchresultspage.verifySearchResultsPageDisplayed():
        assert searchresultspage.returnSearchResultText().lower().find(search_section) > 0
