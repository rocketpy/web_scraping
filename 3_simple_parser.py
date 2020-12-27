import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text

def refined(s):
    r = s.split(' ')[0]
    return r.replace(u'\xa0', '')


def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')

        writer.writerow((data['name'],
                         data['url'],
                         data['reviews']))
