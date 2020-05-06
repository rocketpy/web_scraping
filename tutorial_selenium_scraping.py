import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


path = "C:\Program Files\chromedriver.exe"  # or any other path

driver = webdriver.Chrome(path)
#  driver = webdriver.Firefox()
driver.get("https:// ... ")
# print(driver.title)  using this for test !

# search data with input on web_page ( search field )
search = driver.find_element_by_name("some_name")  # tag name
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()

# find elem by id
some_elem = driver.find_element_by_id("some_name")
print(some_elem.text)

#  need a few seconds for waiting a result
time.sleep(5)

driver.quit()  # or driver.close()
