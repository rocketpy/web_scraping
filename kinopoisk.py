import requests

"""
user_id = 12345
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

url = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/2/#list' % (user_id) # url для второй страницы
r = requests.get(url, headers=headers)

with open('test.html', 'w') as output_file:
  output_file.write(r.text.encode('cp1251'))
"""

