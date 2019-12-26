import sys
import requests
import pyperclip
import webbrowser
from bs4 import BeautifulSoup


# searching by keyword
def main():
    if len(sys.argv) > 1:
        keyword = ' '.join(sys.argv[1:])
    else:
        keyword = pyperclip.paste()

    resp = requests.get('http://google.com/search?q=' + keyword)
    resp.raise_for_status()
    soup = bs4.BeautifulSoup(resp.text)
    link_elems = soup.select('.r a')
    num_open = min(5, len(linkElems))

    for i in range(numOpen):
        webbrowser.open('http://google.com' + link_elems[i].get('href'))

if __name__ == '__main__':
    main()
