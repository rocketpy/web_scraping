import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    r = s.split(' ')[0]
    return r.replace('.00', '')

  
def write_csv(data):
    with open('file_name.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow((data['name'],
                         data['url'],
                         data['reviews']))
        

def get_data(html):
    parse = BeautifulSoup(html , 'lxml')
    popular = parse.find_all('section')[1]
    plagins = popular.find_all('article')

    for i in plagins:
        name = i.find('h2').text
        url = i.find('h2').find('a').get('href')
        r = i.find('span', class_='rating-count').find('a').text
        rating = refined(r)

        data = {'name': name,
                'url': url,
                'reviews': rating}

        write_csv(data)


def main():
    url = 'https://www...'
    get_data(get_html(url))


if __name__ == '__main__':
    main()

    
