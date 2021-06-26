#  https://pypi.org/project/html5lib/

# pip install requests
# pip install html5lib
# pip install bs4

import requests
import fake_useragent
from bs4 import BeautifulSoup


user = fake_useragent.UserAgent().random
headers = {'User-Agent': f'{user}', 'accept': '*/*'}
url = "http://www..."
r = requests.get(url, headers=headers)
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

# or 
import html5lib

with open("mydocument.html", "rb") as f:
    lxml_etree_document = html5lib.parse(f, treebuilder="lxml")
    

# When using with urllib.request (Python 3), the charset from HTTP should be pass into html5lib as follows:

from urllib.request import urlopen
import html5lib

with urlopen("http://example.com/") as f:
    document = html5lib.parse(f, transport_encoding=f.info().get_content_charset())
 
"""

