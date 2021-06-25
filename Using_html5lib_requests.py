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


# Usage
"""
import html5lib

with open("mydocument.html", "rb") as f:
    document = html5lib.parse(f)

# or:

import html5lib

document = html5lib.parse("<p>Hello World!")
"""

