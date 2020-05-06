import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


path = "C:\Program Files\chromedriver.exe"  # or any other path

driver = webdriver.Chrome(path)
driver.get("https:// ... ")
# print(driver.title)  using this for test !

# search data with input on web_page ( search field )
search = driver.find_element_by_name("some_name")  # tag name
search.send_keys("test")
search.send_keys(Keys.RETURN)

#  need a few seconds for waiting a result
time.sleep(5)

driver.quit()  # or driver.close()
