import requests
import urllib.request
from bs4 import BeautifulSoup


URL = ""

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")
imgs = soup.find_all("img", attrs={"class": "name_class"})
numb = 0

for im in imags:
    img_src = im["src"]
    urllib.request.urlretrieve(img_src, str(nummb))
    numb += 1


#  or

#...same imports
import random

# same

for link in soup.find_all("img", attrs={"class": "name_class"}):
    img_href = link.get("href")
    img_name = str(random.randrange(1, 1000000)) + ".jpg"
    urllib.request.urlretrieve(img_href, img_name)

    
    
