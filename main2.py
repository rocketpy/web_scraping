# importing modules
import csv
import random
import requests
from random import choice
from bs4 import BeautifulSoup

# get data , using proxy and user-agent
def get_html(url, useragent=None, proxy=None):
    proxy = {'http': 'http://' + proxies}
    useragent = {'User-Agent': choice(useragents)}  # useragents is a list
    r = requests.get(url, headers=useragent, proxies=proxy)
    return r.text

# or use a file useragents.txt or proxies.txt
useragents = open('useragents.txt').read().split('\n')  # return a list

proxies = open('proxies.txt').read().split('\n')

# in file proxie must be like : 124.88.66.22:83  , 83 is a port of proxie

# use random for proxy and user-agent
for i in range(10):
    proxy = {'http': 'http://' + proxies}
    useragent = {'User-Agent': choice(useragents)}  # useragents is a list
    

def refined(s):
    r = s.split()[0]
    return r.replace(',', '')

# writing data to CSV file
def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)
# method writerow accept only one argument
        writer.writerow((data['name'],
                         data['url'],
                         data['reviews']))

# get some data for writing to CSV file
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[1]
    plugins = popular.find_all('article')

    for plugin in plugins:
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')
        r = plugin.find('span', class_='rating_count').find('a').text
        rating = refined(r)

        data = {'name': name,
                'url': url,
                'reviews': rating
                }

        write_csv(data)
        # print(data)

# call main function
def main():
    url = 'https:// ... '
    get_data(get_html(url))

# for print html-doc need : print(get_html(url))

if __name__ == '__main__':
    main()
