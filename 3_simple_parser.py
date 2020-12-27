import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    resp = requests.get(url)
    return resp.text


def refined_data(data):
    r = data.split(' ')[0]
    return r.replace('u\xa0', '')


def write_csv(data):
    with open('result.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')

        writer.writerow((data['name'],
                         data['url'],
                         data['reviews'])
                       )
        
        
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


def main():
    url = 'https://www...'
    get_data(get_html(url))


if __name__ == '__main__':
    main()        
