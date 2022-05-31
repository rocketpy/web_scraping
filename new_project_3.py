import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait


# driver = webdriver.Chrome(PATH) 
firefoxdriver = webdriver.Firefox(executable_path="Path to Firefox driver")
useragent = UserAgent()
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent.random)
driver = webdriver.Firefox(firefox_profile=profile, executable_path="C:\\BrowserDrivers\\geckodriver.exe")

options = Options()
options.add_argument("--start-maximized")
options.add_argument("window-size=1400,600")


# proxy = "12.345.678.910:8080"
# options = Options()
# options.add_argument("--incognito")
# options.add_argument("--start-maximized")
# options.add_argument("--headless")
# options.add_argument('--proxy-server=%s' % proxy)
# driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")


print(driver.get("http://www.whatsmyua.info/"))

