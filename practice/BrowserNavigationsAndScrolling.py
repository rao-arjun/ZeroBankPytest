from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://agoda.com")
print(driver.title)
driver.get("http://newtours.demouat.com")
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
driver.back()
# driver.execute_script("window.scrollBy(0,1000)", "")

careers = driver.find_element_by_link_text("Careers")
driver.execute_script("arguments[0].scrollIntoView()", careers)


driver.quit()
