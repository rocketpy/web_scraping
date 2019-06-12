# http://httpbin.org/  -  A simple HTTP Request & Response Service
# http://docs.python-requests.org/en/master/
# https://pypi.org/project/fake-useragent/ - use fake_useragent

import json
import requests
from bs4 import BeautifulSoup
from random import choice


# customize user_agent
example_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
r = requests.get('https:// ... .com',headers=example_headers)

# for more information about response , use this :
# print(dir(r))
# print(help(r))


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
proxies = {
  'http': 'http:// ... ',
  'https': 'http:// ... ',
}

requests.get('http://example.org', proxies=proxies)

r = requests.get('https:// ... ', auth=('user', 'pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()

# custom headers
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
# or
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

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
print resp.status_code, resp.text, resp.headers

# base of r
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()

# forms of request
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')

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

# download and safe image
"""
import requests

r = requests.get('https://  .png')
with open('file_name.png', 'wb') as f:
    f.write(r.content)
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
bs = BeautifulSoup(html, 'html.parser')
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
    soup = BeautifulSoup(html, 'lxml')
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


# lxml -  parser
# beautifulsoup take html to python objects
# create func for requests
# r - response
def get_html(url):
    r = requests.get(url)
    return r.text  # or r.content
# r.text - returning HTML code of web-page
# r.content - return text

# look HTML at page
soup = BeautifulSoup(r.content)
print(soup.prettify)

# convert html to python objects
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
# Finding first div with 'id'
    h1 = soup.find('div', id='home-welcome').find('header').find('h1').text
    return h1


def main():
    url = 'https://... .org/'
    print(get_data(get_html(url)))
# for print html-docum. :  
# print(get_html(url))

if __name__ == '__main__':
    main()
