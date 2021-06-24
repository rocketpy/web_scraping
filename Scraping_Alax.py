import csv
import requests
from bs4 import BeautifulSoup


# headrs = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}

headrs = {'Host': 'www...de',
          'If-None-Match': 'W/"2a07a-cNkp0k044NvAQTMhYpgDt4ar+KU"',
          'Referer': 'https://www..../results?animal_99=true',
          'TE': 'Trailers',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
          'X-API-Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjQ0Nzg1OTMsImlhdCI6MTYyNDQ3NzY5M30.1c_2SSqHH6URAOQig4Fzs-EbUrzD6o93LKdI4IXu9f8'
          'X-Site-ID': '1'
          }

# Take from: Inspector> Network> Headers> query string parameters
data = {
        }


def get_html(url, params=data):
    r = requests.get(url, headers=headrs, params=params)
    return r


def get_data(html):
    soup = BeautifulSoup(html , 'lxml')
    popular = soup.find_all('section')[1]
    plags = popular.find_all('article')

    for plag in plags:
        name = plag.find('h2').text
        url = plag.find('h2').find('a').get('href')

        r = plag.find('span', class_='rating-count').find('a').text
        rating = refined_data(r)

        data = {'name': name,
                'url': url,
                'reviews': rating
               }

        write_csv(data)


def save_data(items, path):
    with open(path, 'w',  encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Name', 'Surname', 'Age'])
        for item in items:
            writer.writerow([item['name'], item['surname'], item['age']])
"""
def write_csv(data):
    with open('result.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')

        writer.writerow((data['name'],
                         data['url'],
                         data['reviews'])
                       )
"""

if __name__ == '__main__':
    get_data(get_html(url))
    
    
