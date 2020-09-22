import itertools
import pandas as pd
import seaborn as sns
from requests import get
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


sns.set()

headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

URL = "https://..."

titles = []
created = []
prices = []
condition = []
descriptions = []
urls = []
thumbnails = []

response = get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
some_containers = html_soup.find_all('div', class_="searchResultProperty")

first = some_containers[0]
first.find_all('span')

# cleaning data
data = first.find_all('span').text
data_cl = data.replace('xxx', '')

num_pages = 0
for page in range(0, 100):
    num_pages += 1
    URL = 'https://...'+str(page)
    r = get(sapo_url, headers=headers)
    page_html = BeautifulSoup(r.text, 'html.parser')
    house_containers = page_html.find_all('div', class_="searchResultProperty")
    if house_containers != []:
        for container in house_containers:
            name_t = container.find_all('span')[0].text
            titles.append(name_t)
            
            # title
            name = container.find_all('span')[0].text
            titles.append(name)
            
            # price            
            price = container.find_all('span')[2].text
            if price == 'Contacte Anunciante':
                price = container.find_all('span')[3].text
            if price.find('/') != -1:
                price = price[0:price.find('/')-1]
            if price.find('/') != -1:
                price = price[0:price.find('/')-1]
            price_ = [int(price[s]) for s in range(0,len(price)) if price[s].isdigit()]
            price = ''
            for x in price_:
                price = price+str(x)
                prices.append(int(price))

#  write data to file
cols = ['Title', 'Price', 'Size', 'Description', 'Date', 'URL', 'Image']
data_to_file = pd.DataFrame({'Title': titles,
                             'Price': prices,
                             'Date': created,
                             'Status': condition,
                             'Description': descriptions,
                             'URL': urls,
                             'Image': thumbnails})[cols]

data_to_file.to_excel('result.xls')
