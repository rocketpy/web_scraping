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

