#  pip install splinter
#  docs - https://github.com/cobrateam/splinter

from splinter import Browser
import pandas as pd


browser = Browser('chrome')

browser.driver.set_window_size(640, 480)
browser.visit('https://www.google.com')

# take searhfield xpath
search_bar_xpath = '//*[@id="lst-ib"]

# I recommend using single quotes
search_bar_xpath = '//*[@id="lst-ib"]'

# index 0 to select from the list
search_bar = browser.find_by_xpath(search_bar_xpath)[0]

# Now let's set up code to click the search button!
search_button_xpath = '//*[@id="tsf"]/div[2]/div[3]/center/input[1]' 
search_button = browser.find_by_xpath(search_button_xpath)[0] 
search_button.click()

search_results_xpath = '//h3[@class="r"]/a' # simple, right?

search_results = browser.find_by_xpath(search_results_xpath)
