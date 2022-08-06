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


# .find
# Use the .find method to target and extract HTML tags:
h1 = soup.find('h1')
print(h1)
# <h1 id="firstHeading" class="firstHeading" lang="en">Soup</h1>

# attrs=
# Use the attrs argument to isolate tags that contain specific HTML element attributes:
soup.find('div', attrs={'class': 'section-'})


# partial=
# Element attributes are partially matched by default. Turn this off by setting partial to False:

soup.find('div', {'class': 'soup'}, partial=False)

# mode=
# Override the mode argument {'auto', 'first', 'all'} to guarantee return behaviour:

print(soup.find('span', mode='first'))
# <span class="navbar-toggler-icon"></span>
len(soup.find('span', mode='all'))
# 8

dir()
# Soup objects have html, tag, attrs, and text attributes:

dir(h1)
# ['attrs', 'find', 'get', 'html', 'strip', 'tag', 'text']

print(h1.html)
# '<h1 id="firstHeading" class="firstHeading" lang="en">Soup</h1>'
print(h1.tag)
# h1
print(h1.attrs)
# {'id': 'firstHeading', 'class': 'firstHeading', 'lang': 'en'}
print(h1.text)
# Soup

