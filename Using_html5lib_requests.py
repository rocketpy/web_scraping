#  https://pypi.org/project/html5lib/

# pip install requests
# pip install html5lib
# pip install bs4

import requests
from bs4 import BeautifulSoup


URL = "http://www..."
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib')

print(soup.prettify())

