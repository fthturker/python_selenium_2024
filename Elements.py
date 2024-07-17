from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
# http://172.30.10.221:8085/datacat/login

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://www.google.com")
# driver.maximize_window()
# time.sleep(3)
# googleSearchBox=driver.find_element(By.ID,"APjFqb")
# googleSearchBox.send_keys("Automation")
#
# googleSearchBox.send_keys(Keys.RETURN)
# #driver.find_element(By.NAME,"btnK").click()
# time.sleep(3)

driver.get("https://trytestingthis.netlify.app/")
driver.find_element(By.ID,"fname").send_keys("Fatih")
driver.find_element(By.ID,"lname").send_keys("Turker")

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
time.sleep(3)

