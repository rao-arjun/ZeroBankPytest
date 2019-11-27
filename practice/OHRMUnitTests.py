import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from parameterized import parameterized

import HtmlTestRunner


def setUpModule():
    print("Executing begin of module")


def tearDownModule():
    print("Executing end of module")


class TestOrhmUnitTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Opening application")
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
        cls.driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
        cls.driver.find_element_by_xpath("//*[@id='btnLogin']").click()

    @classmethod
    def tearDownClass(cls):
        print("Closing application and webdriver")
        cls.driver.quit()

    def setUp(self):
        print("Main page of the application")
        self.driver.find_element_by_id("menu_dashboard_index").click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(ec.visibility_of_element_located((By.TAG_NAME, "h1")))

    def test_navigate_user_page(self):
        print("Navigate to user search page")
        admin = self.driver.find_element_by_id("menu_admin_viewAdminModule")
        usermanagement = self.driver.find_element_by_id("menu_admin_UserManagement")
        users = self.driver.find_element_by_id("menu_admin_viewSystemUsers")

        wait = WebDriverWait(self.driver, 20)

        actions = ActionChains(self.driver)
        actions.move_to_element(admin).move_to_element(usermanagement).move_to_element(users).click().perform()

        wait.until(ec.visibility_of_element_located((By.TAG_NAME, "h1")))
        self.assertEqual(self.driver.find_element_by_tag_name("h1").text, "System Users", "Verifying navigation to users page")

    @parameterized.expand([("robert"), ("hannah"), ("steven")])
    def test_search_employee(self, searchQuery):
        pim = self.driver.find_element_by_id("menu_pim_viewPimModule")
        employeelist = self.driver.find_element_by_id("menu_pim_viewEmployeeList")

        actions = ActionChains(self.driver)
        actions.move_to_element(pim).move_to_element(employeelist).click().perform()
        wait = WebDriverWait(self.driver, 20)

        if self.driver.find_element_by_css_selector("table[id='resultTable']").is_displayed():
            self.driver.find_element_by_id("empsearch_employee_name_empName").click()
            self.driver.find_element_by_id("empsearch_employee_name_empName").clear()
            self.driver.find_element_by_id("empsearch_employee_name_empName").send_keys(searchQuery)
            self.driver.find_element_by_id("searchBtn").click()
            wait.until(ec.visibility_of(self.driver.find_element_by_xpath("//*[@id='resultTable']/tbody")))

        self.assertGreaterEqual(len(self.driver.find_element_by_xpath("//*[@id='resultTable']/tbody").find_elements_by_tag_name("tr")), 1, "Count of search results")

    @unittest.SkipTest
    def test_future_case(self):
        print("Skipped test ")

    @unittest.skip("Skipping test")
    def test_future_case1(self):
        print("Skipped test ")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports/'))

'''
suite = unittest.TestLoader().loadTestsFromTestCase(TestOrhmUnitTests)
unittest.TextTestRunner(verbosity=2).run(suite)
'''