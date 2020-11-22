import csv
from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup as bs


# here is example of scraping heavy AJAX driven website !!!

# PATH = "C:\Program Files\chromedriver.exe" 
# driver = webdriver.Chrome(PATH) 
PATH = str(Path('geckodriver').resolve())

# headers = {'accept':'*/*',    # accept using on web-page , where we using search 
#            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}      
# base_url = 'https://'
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
    driver = webdriver.Firefox(executable_path=PATH)
    driver.get('https://')
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
    url = 'https://'  # base_url = 'https://'
    html = get_html(url)
    soup = bs(html, 'lxml')
    cards = soup.find_all('div')  # return a list 
    ad_data = []
    
    for card in cards:
        data = get_data(card)
        ad_data.append(data)
        
    write_data(ad_data)
    
if __name__ == '__main__':
    main()
