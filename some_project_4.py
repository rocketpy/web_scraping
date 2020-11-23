import csv
# import requests
from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup as bs


# here is example of scraping heavy AJAX driven website !!!

# PATH = "C:\Program Files\chromedriver.exe" 
# driver = webdriver.Chrome(PATH) 
URL = 'https://'
PATH = str(Path('geckodriver').resolve())
driver = webdriver.Firefox(executable_path=PATH)

# accept using on web-page , where we using search !!!
# headers = {'accept':'*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}  
# or
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'} 
"""
resp = requests.get(URL, headers=headers)
soup = bs(resp.content, 'html.parser')

title = soup.find(id='productTitle').get_text()
price = soup.find(id='price').get_text()

# print(soup.prettify())
"""

"""
def parse():
    session = requests.Session()
    req = session.get(base_url, headers=headers)
"""

def write_data(ads):
    with open('result.csv', 'a') as file:
        cols = ['title', 'url', 'price']
        writer = csv.DictWriter(file, fieldsname=cols)
        
        for ad in ads:
            writer.writerow(ad)

            
def get_html(url):
    driver.get(url)
    return driver.page_source
    
    
def get_data(card):
    try:
        name = card.h2
    except:
        title = ''
        url = ''
    else:
        title = name.text.strip()
        url = name.a.get('href')     
        price = card.find('span', class_='').text.strip()
        price = ''.join(price.split(','))
    
        data = {'title': title, 'url': url, 'price': price}
        return data
    
    
def main():
    ad_data = []
    #  adding pagination !!!
    for page in range(1, 10):  # 10 pages , pagination
        url = f'https://www...page={page}/' 
        html = get_html(url)
        soup = bs(html, 'lxml')
        cards = soup.find_all('div', )  # return a list 
    
        for card in cards:
            data = get_data(card)
            ad_data.append(data)
        
    write_data(ad_data)
    
    
if __name__ == '__main__':
    main()
