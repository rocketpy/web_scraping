import itertools
import pandas as pd
import seaborn as sns
from requests import get
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


sns.set()

headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

URL = "https://..."

response = get(URL, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

some_containers = html_soup.find_all('div', class_="searchResultProperty")
