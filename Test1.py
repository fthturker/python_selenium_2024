from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
# http://172.30.10.221:8085/datacat/login

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(4)

driver.close()
driver.quit()

print("Done")