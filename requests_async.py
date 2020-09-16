from requests_html import HTMLSession
from requests_html import AsyncHTMLSession


session = HTMLSession()
req = session.get('https://...')

asession = AsyncHTMLSession()
async def get_pythonorg():
          r = await asession.get('https://...')
          return r

    
