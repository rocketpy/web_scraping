from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


# driver = webdriver.Chrome(PATH) 

LOGIN = ""
PASSWORD = ""


def get_auth():
    try:
        driver.get("https://www.")
        sleep(5)
        driver.find_element_by_id("email").send_keys(LOGIN_FB)
        sleep(2)
        driver.find_element_by_id("pass").send_keys(PASSWORD_FB)
        sleep(2)
        driver.find_element_by_id("").click()
        
        if driver.find_element_by_id(""):
            print("Authorization not done ! ")
            #vget_auth()
    except NoSuchElementException:
        print("Authorization is done !")

if __name__ == '__main__':
    get_auth()

