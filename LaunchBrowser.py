import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\PythonBrowserDrivers\chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.maximize_window()
print(driver.title)
time.sleep(3)
driver.find_element(By.XPATH, "//a[text()='Amazon Fresh']").click()
driver.close()
