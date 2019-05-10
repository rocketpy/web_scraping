# http://docs.python-requests.org/en/master/
# https://pypi.org/project/fake-useragent/ - use fake_useragent

import json
import requests
from bs4 import BeautifulSoup
from random import choice


# customize user_agent
example_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
r = requests.get('https:// ... .com',headers=example_headers)

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
