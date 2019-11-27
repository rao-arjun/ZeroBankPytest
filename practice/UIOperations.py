from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://testautomationpractice.blogspot.com/")

# Search results box
driver.find_element_by_id("Wikipedia1_wikipedia-search-input").clear()
driver.find_element_by_id("Wikipedia1_wikipedia-search-input").send_keys("Metallica")
driver.find_element_by_class_name("wikipedia-search-button").click()

wait = WebDriverWait(driver, 10)

element = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "wikipedia-search-results")))
if element.is_displayed():
    print(len(element.find_elements(By.CSS_SELECTOR, "#wikipedia-search-result-link > a")))
    # Print the primary search results
    for searchresult in element.find_elements(By.CSS_SELECTOR, "#wikipedia-search-result-link > a"):
        print(searchresult.text)

# count of text boxes

print(len(driver.find_elements(By.CLASS_NAME, "text_field")))

# selecting drop down value

dropdownelement = Select(driver.find_element_by_id("products"))
dropdownelement.select_by_value("Yahoo")
dropdownelement.select_by_index(3)

for option in dropdownelement.options:
    print(option.text)

# radio button
radioButtons = driver.find_elements_by_css_selector("input[type='radio']")
print(len(radioButtons))
for button in radioButtons:
    if not(button.is_selected()):
        button.click()

# check boxes
checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    checkbox.click()
# /preceding-sibling::input[@type='radio']")
# print(radioButtonMale.is_selected())
# //*[@id="q26"]/table/tbody/tr[1]/td/label

# #q26 > table > tbody > tr:nth-child(1) > td > label

driver.find_element_by_xpath("//button[text()='Click Me']").click()
driver.switch_to_alert().accept()

# tables
tableElement = driver.find_element_by_name("BookTable")
# no of rows in table
print(len(tableElement.find_elements_by_tag_name("tr")))

# printing all contents of table

for row in tableElement.find_elements_by_tag_name("tr"):
    for column in row.find_elements_by_tag_name("td"):
        print(column.text + "     ")
    print("\n")
'''
driver.get("https://selenium.dev/selenium/docs/api/java/index.html")


driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium.firefox").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("FirefoxProfile")
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element_by_link_text("OVERVIEW")

driver.quit()
'''
