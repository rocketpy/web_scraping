#  pip install splinter
#  docs - https://github.com/cobrateam/splinter

from splinter import Browser
import pandas as pd


browser = Browser('chrome')

browser.driver.set_window_size(640, 480)
browser.visit('https://www.google.com')

# take searchfield xpath
search_bar_xpath = ''
search_bar = browser.find_by_xpath(search_bar_xpath)[0]  # from list take idex 0

# find_by_tag(), find_by_name(), find_by_text() 

# xext step , click the search button
search_button_xpath = '' 
search_button = browser.find_by_xpath(search_button_xpath)[0] 
search_button.click()

search_results_xpath = '//h3[@class="r"]/a'  # all classes r with a tags
search_results = browser.find_by_xpath(search_results_xpath)

# for navigation auth pages use : fill() and click() !!!

data = []

for i in search_results:
     title = search_result.text.encode('utf8')
     link = search_result["href"]
     scraped_data.append((title, link))
    
#  need add export scrapped data to CSV file with pandas    

browser.quit()
