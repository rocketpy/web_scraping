# phantomjs - Python wrapper for PhantomJS

# PyPi: https://pypi.org/project/phantomjs/ 

# pip install phantomjs

# Usage

from phantomjs import Phantom


phantom = Phantom()

conf = {'url': 'http://example.com/',   # Mandatory field
       }
output = phantom.download_page(conf, js_path='/my/phantomjs/script/path')

# In phantomjs script, you can take the url as:
"""
var system = require('system');
var json = JSON.parse(system.args[1]);
var url = json.url;
"""

# Using the default phantomjs script provided with this package:
"""
from phantomjs import Phantom


phantom = Phantom()

conf = {
    'url': 'http://example.com/',   # Mandatory field
    'output_type': 'html',          # json for json
    'min_wait': 1000,               # 1 second
    'max_wait': 30000,              # 30 seconds
    'selector': '',                 # CSS selector if there's any
    'resource_timeout': 3000,       # 3 seconds
    'headers': {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.72 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Sec-Fetch-Mode": "navigate",
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
    },
    'cookies': [
        {'name': '_Country', 'value': 'US', 'domain': '.google.com',},
        {'name': '_Currency', 'value': 'USD', 'domain': '.google.com',},
    ],
    'functions': [
        'function(){window.location.replace("http://icanhazip.com/");}',
    ],
}


output = phantom.download_page(conf)
"""


#  Executing Javascript

# wait for the element
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "list")))

# pass the found element into the script
result = driver.execute_script('return arguments[0].DataTable().data();', element)
# print(result)

