# http://docs.python-requests.org/en/master/
import requests
from bs4 import BeautifulSoup


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
