import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(2)

driver.find_element(By.ID, "submit").click()

time.sleep(2)

driver.quit()
