import os
from selenium import webdriver


path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https:// ... ")

# print(driver.title)
some_elem = driver.find_element_by_name("some_name")

driver.quit()
