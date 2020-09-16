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
