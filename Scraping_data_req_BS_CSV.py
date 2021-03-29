import csv
import requests
from bs4 import BeautifulSoup



URL = "https://"
CSV = "file_name.csv"
headers = {"Accept": "..."
           "User=Agent": "..."
          }

def get_html(url, params=''):
    req = requests.get(url=url, headers=headers, params=params)
    return req
