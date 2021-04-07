#  download and display the content of robot.txt
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

# write csv file
import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    
# write csf file with Pandas
import pandas as pd

df = pd.DataFrame(data)
df.to_csv('out.csv', index=True, sep='\t', encoding='utf-8')


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

    
#  check whether a page contains a title or not
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
    
    title = get_title(url)
    if title == None:
      return "Title could not be found !"
    else:
      return title

print(get_title("https://www..com/"))
print(get_title("http://www..com/"))  
    
