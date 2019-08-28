import csv
import time
import random
import requests
from bs4 import BeautifulSoup


def get_html(url):
    time.sleep(3)
    r = requests.get(url, headers=headers, timeout=3)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('div', id='home-welcome').find('header').find('h1').text
    return h1

def main():
    url = 'https://... .org/'
    print(get_data(get_html(url)))

if __name__ == '__main__':
    main()
