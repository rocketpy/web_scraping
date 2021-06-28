import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from random import choice


# driver = webdriver.Chrome(PATH) 

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


def get_auth():
    try:
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

