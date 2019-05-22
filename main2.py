import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    r = s.split()[0]
    return r.replace(',', '')


def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)
# Metod writerow accept only one argument
        writer.writerow((data['name'],
                         data['url'],
                         data['reviews']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[1]
    plugins = popular.find_all('article')

    for plugin in plugins:
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')
        r = plugin.find('span', class_='rating_count').find('a').text
        rating = refined(r)

        data = {'name': name,
                'url': url,
                'reviews': rating
                }

        write_csv(data)
        # print(data)


def main():
    url = 'https:// ... '
    get_data(get_html(url))

# for print html-doc need : print(get_html(url))


if __name__ == '__main__':
    main()
