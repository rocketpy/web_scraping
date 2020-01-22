#  get text of web_page
import requests

response = requests.get("https://en.wikipedia.org/robots.txt")
test = response.text

print(test)


#  extract h1 tag from example
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.example.com/')
h_1 = BeautifulSoup(html.read(), 'html.parser')
print(h_1.h1)


#  extract and display all the header tags
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('https://.com')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# get the number of datasets currently listed on data.gov
import requests
from lxml import html

resp = requests.get('http://www.data.gov/')
doc = html.fromstring(resp.text)
link = doc.cssselect('small a')[0]
print("Number is : ")
print(link.text)



#  test for a given page is found or not on the server
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


try:
    html = urlopen("https://.com")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found !")
else:
    print(html.read())
    
try:
    html = urlopen("http://www. .com")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print("HTML Details")    
    print(html.read())  
