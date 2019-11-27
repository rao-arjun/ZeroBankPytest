from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import FirefoxProfile

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": r"D:\git"})

driver = webdriver.Chrome(options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element_by_css_selector("textarea[id='pdfbox'][class='form-control']").send_keys("test_pdf_chrome")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

driver.quit()

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", r"D:\git")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element_by_css_selector("textarea[id='pdfbox'][class='form-control']").send_keys("test_pdf_firefox")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()