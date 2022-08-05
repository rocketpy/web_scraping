# gazpacho is a simple, fast, and modern web scraping library. 

# https://github.com/maxhumber/gazpacho
# https://gazpacho.xyz/

# pip install -U gazpacho

from gazpacho import get, Soup


url = 'https://scrape.world/books'
html = get(url)
soup = Soup(html)
books = soup.find('div', {'class': 'book-'}, partial=True)

def parse(book):
    name = book.find('h4').text
    price = float(book.find('p').text[1:].split(' ')[0])
    return name, price

[parse(book) for book in books]


# Tutorial

from gazpacho import get, Soup

# get
url = 'https://scrape.world/soup'
html = get(url)
print(html[:50])

# Adjust get requests with optional params and headers:
get(
    url='https://httpbin.org/anything',
    params={'foo': 'bar', 'bar': 'baz'},
    headers={'User-Agent': 'gazpacho'}
)


# Soup
# Use the Soup wrapper on raw html to enable parsing:
soup = Soup(html)

# Soup objects can alternatively be initialized with the .get classmethod:
soup = Soup.get(url)
