from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://opensource-demo.orangehrmlive.com")

driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

wait = WebDriverWait(driver,20)

wait.until(ec.visibility_of_element_located((By.TAG_NAME, "h1")))
print(driver.find_element_by_tag_name("h1").text)

# mouse hover
admin = driver.find_element_by_id("menu_admin_viewAdminModule")
userManagement = driver.find_element_by_id("menu_admin_UserManagement")
users = driver.find_element_by_id("menu_admin_viewSystemUsers")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(userManagement).move_to_element(users).click().perform()

print(driver.find_element_by_tag_name("h1").is_displayed())

driver.get("http://testautomationpractice.blogspot.com/")
#double click
driver.find_element_by_id("field1").send_keys("Tester")
actions = ActionChains(driver)
print(driver.find_element_by_xpath("//button[text()='Copy Text']").is_displayed())
actions.double_click(driver.find_element_by_xpath("//button[text()='Copy Text']")).perform()

draggable = driver.find_element_by_id("draggable")
droppable = driver.find_element_by_id("droppable")
actions.drag_and_drop(draggable, droppable).perform()

#file upload
driver.execute_script("arguments[0].scrollIntoView()", driver.find_element_by_name("RESULT_FileUpload-11"))
driver.find_element_by_name("RESULT_FileUpload-11").send_keys("C://Users//arjunrao//Desktop//Untitled Document.pdf")
driver.quit()
