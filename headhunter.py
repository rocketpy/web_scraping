import requests 
from bs4 import BeautifulSoup as bs


headers = {'accept':'*/*',    # accept using on web-page , where we using search 
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
           
base_url = 'https://hh.ua'  # https://hh.ua/search/vacancy?area=5&st=searchVacancy&text=Intern+data+analyst&from=suggest_post

def hh_parse():
    session = requests.Session()   # when we using session , website understanding what all requests from only one browser
    req = session.get(base_url, headers=headers)
    if req.status_code == 200:
        print('Succes')
        soup = bs(req.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data': 'vacancy'})
        for div in divs:
            title = div.find('a', attrs={'data_1': 'vacancy_1'}).text
            href = div.find('a', attrs={'data_2': 'vacancy_2'})['href']
            company = div.find('a', attrs={'data_3': 'vacancy_3'}).text
        print()
    else:
        print('Error')
  
hh_parse(base_url, headers)
