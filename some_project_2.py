import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


# driver = webdriver.Chrome(path)

EMAIL = ""
PASSWORD = ""

driver.get('https://www.')

search = driver.find_element_by_xpath('//*[@id="sbxJxRegEmail"]')
time.sleep(1)
search.send_keys(EMAIL) 

search = driver.find_element_by_xpath('//*[@id="sbxJxRegPswd"]')
time.sleep(1)
search.send_keys(PASSWORD) 

login_button = driver.find_element_by_xpath('//*[@id="loginBtn"]')
login_button.click() 

answer = driver.find_element_by_xpath('//*[@id="sbMainNavSectionListItemAnswer"]/a')
answer.click() 

choose = driver.find_element_by_xpath()
choose.click() 

rand_int = random.randint(1, 2)

def cycle(rand):
    if rand == 1:
        first = driver.find_element_by_xpath('//*[@id="middleInner"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/span[1]/span')
        first.click() 
        time.sleep(1)
        answer = driver.find_element_by_xpath('//*[@id="middleInner"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/button')
        answer.click()
        time.sleep(3)
    else:
        second = driver.find_element_by_xpath('//*[@id="middleInner"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/span[2]/span')
        second.click()
        time.sleep(1)
        answer = driver.find_element_by_xpath('//*[@id="middleInner"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/button')
        answer.click()
        time.sleep(3)
    
while choose.is_displayed():
    cycle(rand_int)
