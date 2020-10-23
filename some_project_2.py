import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


# driver = webdriver.Chrome(path)

EMAIL = ""
PASSWORD = ""

driver.get('https://www.swagbucks.com/')

search = driver.find_element_by_xpath('//*[@id="sbxJxRegEmail"]')
time.sleep(1)
search.send_keys(EMAIL) 

search = driver.find_element_by_xpath('//*[@id="sbxJxRegPswd"]')
time.sleep(1)
search.send_keys(PASSWORD) 

login_button = driver.find_element_by_xpath('//*[@id="loginBtn"]')
login_button.click() 

