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

def get_html(url):
    driver = webdriver.Firefox(executable_path=PATH)
    driver.get('https://')
    return driver.page_source
    

def main():
    url = 'https://'  # base_url = 'https://'
    html = get_html(url)
    soup = bs(html, 'lxml')
    cards = soup.find_all('div')  # return a list 
    for card in cards:
        name = card.h2
        title = name.text.strip()
        url = name.a.get('href')
        
        price

    
if __name__ == '__main__':
    main()
