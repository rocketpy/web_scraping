from requests_html import HTMLSession
from requests_html import AsyncHTMLSession


session = HTMLSession()
req = session.get('https://...')

asession = AsyncHTMLSession()
async def get_pythonorg():
          r = await asession.get('https://...')
          return r

async def get_reddit():
    r = await asession.get('https://reddit.com/')
    return r

async def get_google():
          r = await asession.get('https://google.com/')
          return r

results = asession.run(get_pythonorg, get_reddit, get_google)
#  check the requests all returned a 200 (success) code
#  [<Response [200]>, <Response [200]>, <Response [200]>]

for result in results:
    print(result.html.url)

#  grab a list of all links
lnks = r.html.links

#  select an element with a CSS selector
about = r.html.find('#about', first=True)

#  grab an element's text contents
print(about.text)

#  introspect an element's attributes
print(about.attrs)

#  render out an element's HTML
print(about.html)
