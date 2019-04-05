import requests
from bs4 import BeautifulSoup


# If you need to use a proxy, you can configure individual requests with the proxies argument to any request method
proxies = {
  'http': 'http:// ... ',
  'https': 'http:// ... ',
}

requests.get('http://example.org', proxies=proxies)


# lxml -  parser
# beautifulsoup take html to python objects
# create func for requests
# r - response
def get_html(url):
    r = requests.get(url)
    return r.text  # or r.content
# r.text - returning HTML code of web-page
# r.content - return text


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
