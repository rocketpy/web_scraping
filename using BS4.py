import requests
from bs4 import BeautifulSoup


"""
proxies = {
  'http': 'http://here proxy place',
  'https': 'http://',
}

requests.get('http://example.org', proxies=proxies)
"""

result = requests.get('https://www.whitehouse.gov/briefings-statements/')  # get data
src = result.content
soup = BeautifulSoup(src, 'lxml')
urls = []

for h2_tag in soup.find('h2'):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

print(urls)

"""
links = soup.find_all('a')  # method find_all return LIST

for link in links:
    if 'About' in link.text:
        print(link)
        print(link.attrs['href'])

print(result.status_code)
print(result.headers)
"""