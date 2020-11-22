from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup


PATH = str(Path('geckodriver').resolve())

headers = {'accept':'*/*',    # accept using on web-page , where we using search 
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
           
base_url = 'https://'

"""
def parse():
    session = requests.Session()
    req = session.get(base_url, headers=headers)
"""

def main():
    driver = webdriver.Firefox(executable_path=PATH)
    driver.get('https://')
    

if __name__ == '__main__':
    main()
