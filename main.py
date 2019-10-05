# http://httpbin.org/  -  A simple HTTP Request & Response Service
# http://docs.python-requests.org/en/master/
# https://pypi.org/project/fake-useragent/ - use fake_useragent
# pip install haul - find thumbnails and original images from URL or HTML file
# https://github.com/detailyang/awesome-cheatsheet  
# http://docs.pyspider.org/en/latest/ - a powerful Spider(Web Crawler) system in Python !
# https://pypi.org/project/proxy-requests/  -  Python Proxy Requests -  https://github.com/rootVIII/proxy_requests
# https://github.com/bulkan/robotframework-requests  - Robot Framework keyword library wrapper for requests 
# https://github.com/SpiderClub/weibospider  - A distributed crawler for weibo, building with celery and requests.
# https://github.com/encode/requests-async  - async-await support for `requests` !
# https://github.com/scrapinghub/dateparser  - dateparser -- python parser
# https://github.com/liamks/libpytunes  - parse iTunes

import csv
import time
import json
import requests
from bs4 import BeautifulSoup
from random import choice


# some simple example , if HTML is saved in the file .html , without requests !
"""
from bs4 import BeautifulSoup

raw_html = open('contrived.html').read()
html = BeautifulSoup(raw_html, 'html.parser')
for p in html.select('p'):
  if p['id'] == 'name_id':
    print(p.text)
"""

"""
#  snippet for naming of imgs
import random
import requests

names = []

def name_img(url):
  new_img_name = random.randrange(1, 1000000)
  new_name = str(new_img_name) + ".jpg"
  r = requests.get(url, name)
  return names.append(new_name)
"""


# VERY  important , use Timeouts for prevent failure of programm  !!!
#  if no timeout is specified explicitly, requests do not time out !!!
requests.get('https://github.com/', timeout=1)  # 1 sec

# checking status of response
"""
response = requests.get('https:// ... ')
 
if response.status_code == 200:
    print('Success !')
 
elif response.status_code == 404:
    print('Not Found !')
    
or 

if response:
    print('Success !')
else:
    print('An error has occurred !')
    
"""
# in Python 3.6+
import requests
from requests.exceptions import HTTPError


for url in ['https://...', 'https://...']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}') 
    else:
        print('Success !')

# with headers and timeout example
"""
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko)
          Chrome/53.0.2785.143 Safari/537.36'}
r = requests.get(url, headers=headers, timeout=5)
"""

# customize user_agent
example_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
r = requests.get('https:// ... .com',headers=example_headers)

# for more information about response , use this :
print(dir(r))
print(help(r))


# random user_agent
desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']
 
def random_headers():
    return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
 
r = requests.get('https://edmundmartin.com',headers=random_headers())



# If you need to use a proxy, you can configure individual requests with the proxies argument to any request method
proxies = {'http': 'http:// ... ',
           'https': 'http:// ... '}

requests.get('http://example.org', proxies=proxies)

r = requests.get('https:// ... ', auth=('user', 'pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()
r.history

# custom headers
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)

# or
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
r.headers.get('content-type')

# working with headers
r.headers
{
    'status': '200 OK',
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json; charset=utf-8'
}
 
r.headers['Content-Type']
# 'application/json; charset=utf-8'
 
r.headers.get('content-type')
# 'application/json; charset=utf-8'
 
r.headers['X-Random']
# None
 
# Get the headers of a given URL
resp = requests.head("http://www.google.com")
print(resp.status_code, resp.text, resp.headers)

# base of r
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()

# FORMS of requests  !!!
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')


# WORKING WITH COOKIES !

#  if a response contains some Cookies
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
r.cookies['example_cookie_name']

#  to send your own cookies to the server
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text


#  a Session object has all the methods of the main Requests API 
s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')
print(r.text)   # '{"cookies": {"sessioncookie": "123456789"}}'

#  provide default data to the request methods
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})

"""

import requests

# using GET
payload = {'page': 2, 'count': 25}  # 'https:// ... .org/get?page=2&count=25'
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)
print(r.url)
print(r.headers)
"""

"""
import requests

# using POST
payload = {'username': 'John', 'password': 'testing'}  # 'https:// ... .org/get?page=2&count=25'
r = requests.post('https://httpbin.org/post', data=payload)
print(r.json())
print(r.text)
print(r.url)
print(r.headers)

or

import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))

or

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
"""

"""
import requests

# using AUTHorization

r = requests.get('https://httpbin.org/basic-auth/John/testing', auth=('John', 'testing'))
print(r.text)
"""
"""
import requests

# using DELAY

r = requests.get('https://httpbin.org/delay/1', timeout=3)  # 1 - 1 second
print(r)
print(r.text)
"""

# some tricks or traps
"""
import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'\
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'\
           'q=0.9,image/webp,*/*;q=0.8'}
url = 'https://www.whatismybrowser.com/'\
'developers/what-http-headers-is-my-browser-sending'
req = session.get(url, headers=headers)

bs = BeautifulSoup(req.text, 'html.parser')
print(bs.find('table',{'class':'table-striped'}).get_text)
"""

# web-crawler 
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup 

html = urlopen('https://')
bs = BeautifulSoup(html, 'html.parser')   # soup = BeautifulSoup(page.text, 'html.parser')
for link in bs.find_all('a'):           
    if 'href' in link.attrs:             
        print(link.attrs['href'])
"""

# if no valid object(soup-object) or no valid href for video  !!!
"""
# for VK API
# https://www.youtube.com/watch?v=q3UXjbkX8s8
def download_file(url):
    try:
        r = requests.get(url, stream=True)
    except:
        print(url)
    else:
        filename = url.split('/')[-1]
        with open(filename, 'wb') as file:
            for chunk in r.iter_content(1024000):
                file.write(chunk)


def get_file(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')  #  # soup = BeautifulSoup(page.text, 'html.parser')
    try:
        video_url = soup.find('div', id='page_wrap').find('source').get('src').split('?')[0]
    except:
        print(soup)
    else:
        download_file(video_url)
"""

# crawling through Forms and Logins
"""
import requests

params = {'firstname': 'John', 'lastname': 'Doe'}
r = requests.post("http:// ... ", data=params)
print(r.text)

# or

import requests

params = {'email_addr': ' ... @gmail.com'}
r = requests.post("http:// ... ", data=params)
print(r.text)

# or

import requests

files = {'uploadFile': open('files/Python-logo.png', 'rb')}
r = requests.post('http:// ... ', files=files)
print(r.text)

# or

import requests

params = {'username': 'Ryan', 'password': 'password'}
r = requests.post('http:// ... ', params)

print('Cookie is set to:')
print(r.cookies.get_dict())
print('Going to profile page...')
r = requests.get('http:// ... ', cookies=r.cookies)
print(r.text)

# or

import requests

session = requests.Session()

params = {'username': 'username', 'password': 'password'}
s = session.post('http:// ... ', params)
print("Cookie is set to:")
print(s.cookies.get_dict())
print('Going to profile page...')
s = session.get('http:// ... ')
print(s.text)

# or

import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('ryan', 'password')
r = requests.post(url='http:// ... ', auth=auth)
print(r.text)
"""


# for download img from url
"""
from requests import get 

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)
"""

# find images from img src, a href and even background-image
import haul

url = 'http://gibuloto.tumblr.com/post/62525699435/fuck-yeah'
result = haul.find_images(url)

print(result.image_urls)

# or 

# find original (or bigger size) images with extend=True

import haul

url = 'http://gibuloto.tumblr.com/post/62525699435/fuck-yeah'
result = haul.find_images(url, extend=True)

print(result.image_urls)


# storing data to CSV
"""
import csv

csvFile = open('test.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow( (i, i+2, i*2))
finally:
    csvFile.close()
"""


# lxml -  parser
# beautifulsoup take html to python objects
# create func for requests
# r - response
def get_html(url):
    time.sleep(3)  # before make request , wait 3 seconds
    r = requests.get(url)
    return r.text  # or r.content
# r.text - returning HTML code of web-page
# r.content - return text

# look HTML at page
soup = BeautifulSoup(r.content)
print(soup.prettify)

# convert html to python objects
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')  # # soup = BeautifulSoup(page.text, 'html.parser')
# Finding first div with 'id'
    h1 = soup.find('div', id='home-welcome').find('header').find('h1').text
    return h1

  #  soup.find_all('p')[2].get_text()
  #  soup.find_all(class_='some_name')

  
def main():
    url = 'https://... .org/'
    print(get_data(get_html(url)))
# for print html-docum. :  
# print(get_html(url))

if __name__ == '__main__':
    main()
    

# big list with useragents !!! 
    
"""
Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)
Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)
Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)
Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US)
Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)
Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)
Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))
Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)
"""
