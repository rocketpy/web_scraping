import csv
import requests
from bs4 import BeautifulSoup



URL = "https://"
CSV = "file_name.csv"

# need take Accept and User-agent from Networkfrom Inspector (Chrome Dev tools)
headers = {"Accept": "..."
           "User=Agent": "..."
          }

def get_html(url, params=''):
    req = requests.get(url=url, headers=headers, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product_item')

    elems = []
    for item in items:
        elems.append({'title': item.find('div', class_='title').get_text(strip=True),
                      'product_link': URL + item.find('div', class_='title').find('a').get('href'),
                      'img': URL + item.find('div', class_='image').find('img').get('src')})
           
    return elems


def save_data(items, path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f, delimeter=';')
        writer.writerow(['Title', 'Product_Link', 'Image'])
        for item in items:
            writer.writerow([item['title'], item['product_link'], item['img']])


if __name__ == '__main__':
    get_html(get_data(save_data()))

