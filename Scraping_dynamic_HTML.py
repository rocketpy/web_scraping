from selenium import WebDriver


driver = WebDriver.Chrome('./chromedriver')

# Use Inspector
# Inspect the web page, under Network tab !!!!!
# Headers -> General , need find a Request URL: https:// ... 
"""
By copying and pasting the urls into a browser or making HTTP requests using Python Requests library,
we retrieve records in JSON.
"""
"""
The returned JSON data indicates there are some records in total.
A closer look at the Ajax url reveals that the number of records to be retrieved is specified under the parameter “length” in the url.
Length is a quantity an objects.
"""

#  Search for Ajax request urls in WebDriver logs
from selenium.WebDriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = WebDriver.Chrome('./chromedriver', desired_capabilities=caps)
driver.get('https://www...html')
log = driver.get_log('performance')


#   Need use regular expression to find these urls. !!!
import json
import re


pattern = r'https\:\/\/www\.u\-optic\.com\/api\/diy\/get\_product\_by\_type.+'
urls = list() # a list to store Ajax urls
for entry in log:
    message = json.loads(entry['message'])
    if message['message']['method'] == 'Network.requestWillBeSent':
        if re.search(pattern, message['message']['params']['request']['url']):
            
            urls.append(message['message']['params']['request']['url'])


#  When the WebDriver loads the web page, it may take a few seconds for the WebDriver to make Ajax requests
#  and then generate the page content.

from selenium.WebDriver.support.ui import WebDriverWait
from selenium.WebDriver.support import expected_conditions as EC
from selenium.WebDriver.common.by import By


wait_elementid = "//a[@class='text-bold']"
wait_time = 5
WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located((By.XPATH, wait_elementid)))

