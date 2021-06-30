from time import sleep
from random import choice
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


# driver = webdriver.Chrome(PATH) 
# firefoxdriver = webdriver.Firefox(executable_path="Path to Firefox driver")

# options = Options()
# options.add_argument("--start-maximized")

options = Options()
options.add_argument("--incognito", "--start-maximized", "--headless")
driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")

LOGIN = ""
PASSWORD = ""


def get_proxy():
    # pattern = {'https': 'ipaddress:port'}
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'lxml')
    elems = soup.find('table', id='proxylisttable').find_all('tr')[1:]
    proxies = []
    for el in elems:
        cell = el.find_all('td')
        ip = cell[0]text.strip()
        port = cell[1].text.strip()
        shape = 'https' if 'yes' in cell[6] text.strip() else 'http'
        proxy = {'schema': shape, 'address: ip + ':' + port}
        proxies.append(proxy)
        return choice(proxies)

                 
def make_preview():
    try:
        get_proxy()
        driver.get("https://www.")
        # time.sleep(5)
        driver.find_element_by_class_name('').click() 
        time.sleep(20)
                 
        # driver.find_element_by_class_name('').click()
        # time.sleep(5)
        # driver.find_element_by_id("contenteditable-root").send_keys()
        # time.sleep(5)
        # submit_button = driver.find_element_by_id('submit-button').click()
    except:
        print("Oooops, Some Error !")     
                 
                 
def create_comment():
    try:
        driver.find_element_by_id("contenteditable-root").send_keys()
        # time.sleep(5)
        driver.find_element_by_id('submit-button').click()
    except:
        print("Oooops, Some Error !")      
                 

def get_auth():
    try:
        get_proxy()
        driver.get("https://www.")
        sleep(5)
        driver.find_element_by_id("email").send_keys(LOGIN)
        sleep(2)
        driver.find_element_by_id("pass").send_keys(PASSWORD)
        sleep(2)
        driver.find_element_by_id("").click()
        
        if driver.find_element_by_id(""):
            print("Authorization not done ! ")
            #vget_auth()
    except NoSuchElementException:
        print("Authorization is done !")

if __name__ == '__main__':
    get_auth()
    driver.quit()  # or driver.close()

