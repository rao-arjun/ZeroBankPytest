import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope='module')
def setup():
    print("Opening application")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    print("Closing application")
    driver.quit()


@pytest.mark.run('first')
def test_login(setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
    driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
    driver.find_element_by_xpath("//*[@id='btnLogin']").click()
    wait = WebDriverWait(driver, 20)
    wait.until(ec.visibility_of(driver.find_element_by_tag_name("h1")))
    print(driver.find_element_by_tag_name("h1").text)
    assert driver.find_element_by_tag_name("h1").text == "Dashboard"


@pytest.mark.run('last')
def test_navigate_user_page(setup):
    print("Navigate to user search page")
    admin = driver.find_element_by_id("menu_admin_viewAdminModule")
    usermanagement = driver.find_element_by_id("menu_admin_UserManagement")
    users = driver.find_element_by_id("menu_admin_viewSystemUsers")

    wait = WebDriverWait(driver, 20)

    actions = ActionChains(driver)
    actions.move_to_element(admin).move_to_element(usermanagement).move_to_element(users).click().perform()

    wait.until(ec.visibility_of_element_located((By.TAG_NAME, "h1")))
    assert driver.find_element_by_tag_name("h1").text == "System Users"


testData = [("robert", "First"), ("hannah", "Second")]


@pytest.mark.parametrize("emp, expected", testData)
def test_search_user(emp, expected, setup):
    pim = driver.find_element_by_id("menu_pim_viewPimModule")
    employeelist = driver.find_element_by_id("menu_pim_viewEmployeeList")

    actions = ActionChains(driver)
    actions.move_to_element(pim).move_to_element(employeelist).click().perform()
    wait = WebDriverWait(driver, 20)

    if driver.find_element_by_css_selector("table[id='resultTable']").is_displayed():
        driver.find_element_by_id("empsearch_employee_name_empName").clear()
        driver.find_element_by_id("empsearch_employee_name_empName").send_keys(emp)
        driver.find_element_by_id("searchBtn").click()
        wait.until(ec.visibility_of(driver.find_element_by_xpath("//*[@id='resultTable']/tbody")))

    assert len(driver.find_element_by_xpath("//*[@id='resultTable']/tbody").find_elements_by_tag_name("tr")) >= 1
