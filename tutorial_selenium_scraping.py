import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


path = "C:\Program Files\chromedriver.exe"  # or any path

driver = webdriver.Chrome(path)
driver.get("https:// ... ")

# print(driver.title)
some_elem = driver.find_element_by_name("some_name")
some_elem.send_keys("test")
some_elem.send_keys(Keys.RETURN)

driver.quit()
