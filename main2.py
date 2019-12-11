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

    
"""
from time import sleep
from bs4 import BeautifulSoup
import requests

head = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; AOL 9.0; Windows NT 5.1)'}
proxi = {
        'http': 'http://195.9.149.198:8081',
        }

time_to_sleep_when_captcha = 5
query = input('What are you searching for?:  ')
number = input('How many pages:  ')
url = 'http://www.google.com/search?q='
page = requests.get(url + query, headers=head, proxies=proxi)
for index in range(int(number)):
    try:
        soup = BeautifulSoup(page.text, "html.parser")
        next_page = soup.find("a", class_="fl")
        next_link = ("https://www.google.com" + next_page["href"])
        h3 = soup.find_all("h3", class_="r")
        for elem in h3:
            elem = elem.contents[0]
            link = ("https://www.google.com" + elem["href"])
            print(link)
        page = requests.get(next_link)
    except:
        sleep(time_to_sleep_when_captcha)
        time_to_sleep_when_captcha += 1
"""
