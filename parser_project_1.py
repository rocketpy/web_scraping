import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    r = s.split(' ')[0]
    return r.replace('.00', '')

  
