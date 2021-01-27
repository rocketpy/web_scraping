import requests
from bs4 import BeautifulSoup


def get_html(url):
    result = requests.get(url)
    return result.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    section = soup.find_all('section', {'class': 'class_name'})[1]  # taking a second elem.
    arts = section.find_all('article')  # return a list
    for art in arts:
        h2 = art.find('h2')
        rate = art.find('span', {'class': 'class_name'})
        print(h2.text, rate.text)


def main():
    html = get_html('https://www...')
    data = get_data(html)


if __name__ == '__main__':
    main()
 
