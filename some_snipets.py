#  get text of web_page
import requests

response = requests.get("https://en.wikipedia.org/robots.txt")
test = response.text

print(test)


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
