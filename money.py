import csv
import requests
from bs4 import BeautifulSoup


url = 'https://minfin.com.ua/currency/'
r = requests.get(url)
response = r.text
soup = BeautifulSoup(response)

#  find first
data = soup.find('table', {'class'_: 'table-auto'})

#  find all
data = soup.findAll('table', {'class'_: 'table-auto'})

tr = data.find('td', {'class'_: 'responsive-hide'}).text

t_r = tr[:7]

