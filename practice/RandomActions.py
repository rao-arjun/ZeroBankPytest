from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://agoda.com")

print(driver.title)

print(driver.find_element_by_css_selector("#SearchBoxContainer > div > div > button").is_displayed())

driver.find_element_by_link_text("Today’s deals").click()

wait = WebDriverWait(driver, 30)
wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, "div[class='promotions-section-header']"), "Explorer Deals"))

driver.find_element_by_xpath("//*[@id='header-logo']/a/img[@title='Agoda']").click()

print(len(driver.find_elements_by_tag_name("a")))
links = driver.find_elements_by_tag_name("a")
for link in links:
    print(link.text)

driver.find_element_by_xpath("//*[@class='LinkContainer__Link']//*[text()='Flights']").click()
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title =='Book CHEAP FLIGHTS on Agoda >> Compare Deals on Airline Tickets':
        print(driver.find_element_by_tag_name("h1").text + " is the message displayed")

driver.close()
driver.quit()
