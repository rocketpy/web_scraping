"""
import requests
from bs4 import BeautifulSoup
from lxml import html


user_id = 12345
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

url = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/2/#list' % (user_id) # url для второй страницы
r = requests.get(url, headers=headers)

with open('test.html', 'w') as output_file:
  output_file.write(r.text.encode('cp1251'))
"""

"""
import requests
from bs4 import BeautifulSoup
from lxml import html

soup = BeautifulSoup(text)
film_list = soup.find('div', {'class': 'profileFilmsList'})

tree = html.fromstring(text)
film_list_lxml = tree.xpath('//div[@class = "profileFilmsList"]')[0]
"""

#  full  code
"""
import requests
from bs4 import BeautifulSoup
from lxml import html


s = requests.Session() 
s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    })


def load_user_data(user_id, page, session):
    url = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/%d/#list' % (user_id, page)
    request = session.get(url)
    return request.text

def contain_movies_data(text):
    soup = BeautifulSoup(text)
    film_list = soup.find('div', {'class': 'profileFilmsList'})
    return film_list is not None


page = 1
while True:
    data = load_user_data(user_id, page, s)
    if contain_movies_data(data):
        with open('./page_%d.html' % (page), 'w') as output_file:
            output_file.write(data.encode('cp1251'))
            page += 1
    else:
            break
"""
