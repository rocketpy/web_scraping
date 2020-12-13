import requests
from bs4 import BeautifulSoup


def get_html(url):
    result = requests.get(url)
    return result.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('h1', {'class': 'class_name'})
    a = soup.find('a', {'href': 'https://www...'})
    navbar = soup.find('ul', {'id': 'id_name'})
    li = navbar.find('li').find('a').text


def main():
    html = get_html('https://www...')
    get_data(html)


if __name__ == '__main__':
    main()
