import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https:// ... ")

# print(driver.title)
some_elem = driver.find_element_by_name("some_name")

driver.quit()
