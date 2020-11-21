from pathlib import Path
from selenium import webdriver


PATH = str(Path('geckodriver').resolve())

def main():
    driver = webdriver.Firefox(executable_path=PATH)
    driver.get('https://')
    

if __name__ == '__main__':
    main()
