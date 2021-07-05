from time import sleep
from random import choice
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


# driver = webdriver.Chrome(PATH) 
# firefoxdriver = webdriver.Firefox(executable_path="Path to Firefox driver")

# options = Options()
# options.add_argument("--start-maximized")
# options.add_argument("window-size=1400,600")


# proxy = "12.345.678.910:8080"
options = Options()
options.add_argument("--incognito", "--start-maximized", "--headless")
options.add_argument('--proxy-server=%s' % proxy)
driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")

"""
# create a random user agent for Firefox
useragent = UserAgent()
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent.random)
driver = webdriver.Firefox(firefox_profile=profile, executable_path="C:\\BrowserDrivers\\geckodriver.exe")
driver.get("http://www.whatsmyua.info/")
"""

# create a random user agent for Chrome
"""
options = Options()
options.add_argument("window-size=1400,600")
ua = UserAgent()
a = ua.random
user_agent = ua.random
print(user_agent)
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://whoer.net/')
driver.quit()
"""

LOGIN = ""
PASSWORD = ""
comments = ['Please more video, like this !', 'Perfection! Absolutely love this ...', 
                    'This is such a wonderful !', 'Perfect starter video for a total amateur like me ))!', 
                    'Hi! Thanks for this amazing video.', 'Wow, thank you for the video. Please more ))!'
                   ]


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
        # proxy = {'schema': shape, 'address: ip + ':' + port}
        proxy = f"{ip} + ':' + {port}"
        proxies.append(proxy)
        return choice(proxies)

                 
def make_preview_without_auth():
    try:
        proxy = get_proxy()
        options = Options()
        options.add_argument("--incognito", "--start-maximized", "--headless")
        options.add_argument('--proxy-server=%s' % proxy)
        driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")
        driver.get("https://www.")
        sleep(5)
        driver.find_element_by_class_name('ytp-play-button ytp-button').click() 
        sleep(20)
    except:
        print("Oooops, Some Error !")     
                 
                 
def create_comment():
    try:
        driver.find_element_by_id("contenteditable-root").send_keys(choice(comments))
        sleep(5)
        driver.find_element_by_id('submit-button').click()
        sleep(5)
    except:
        print("Oooops, Some Error !")      
                 
                 
def make_like():
    try:
        driver.find_element_by_id('button').click()
        sleep(5)
    except:
        print("Oooops, Some Error !")    
                 

def get_auth():
    try:
        proxy = get_proxy()
        # proxy = "12.345.678.910:8080"
        options = Options()
        options.add_argument("--incognito", "--start-maximized", "--headless")
        options.add_argument('--proxy-server=%s' % proxy)
        driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")
        driver.get("https://www.")
        sleep(5)
        driver.find_element_by_id("email").send_keys(LOGIN)
        sleep(2)
        driver.find_element_by_id("pass").send_keys(PASSWORD)
        sleep(2)
        driver.find_element_by_id("").click()
        
        if driver.find_element_by_id(""):
            print("Authorization not done ! ")
            # get_auth()
    except Exception:
        print("Authorization is done !")

        
if __name__ == '__main__':
    get_proxy()
    get_auth()
    make_preview_without_auth()
    # make_comment()
    # make_like()
    driver.quit()  
    # driver.close()

