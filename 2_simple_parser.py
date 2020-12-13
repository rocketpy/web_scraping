import requests
from bs4 import BeautifulSoup


def get_html(url):
    result = requests.get(url)
    return result.text
