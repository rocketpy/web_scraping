import requests
from bs4 import BeautifulSoup


# lxml -  parser
# beautifulsoup take html to python objects

# create func for requests
# r - response
def get_html(url):
    r = requests.get(url)
    return r.text
# r.text - returning HTML code of web-page


# convert html to python objects
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
# Finding first div with 'id'
    h1 = soup.find('div', id='home-welcome').find('header').find('h1').text
    return h1


def main():
    url = 'https://... .org/'
    print(get_data(get_html(url)))
# for print html-doc need :  print(get_html(url))

if __name__ == '__main__':
    main()
