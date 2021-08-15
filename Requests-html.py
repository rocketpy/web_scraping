# Requests-HTML: HTML Parsing for Humans


# PyPi: https://pypi.org/project/requests-html/
# Github: https://github.com/psf/requests-html

# pip install requests-html

"""
This library intends to make parsing HTML (e.g. scraping the web) as simple and intuitive as possible.
If you’re interested in financially supporting Kenneth Reitz open source, consider visiting this link.
Your support helps tremendously with sustainability of motivation, as Open Source is no longer part of my day job.

When using this library you automatically get:

    Full JavaScript support!
    CSS Selectors (a.k.a jQuery-style, thanks to PyQuery).
    XPath Selectors, for the faint at heart.
    Mocked user-agent (like a real web browser).
    Automatic following of redirects.
    Connection–pooling and cookie persistence.
    The Requests experience you know and love, with magical parsing abilities.
    Async Support
"""

# Make a GET request:

from requests_html import HTMLSession


session = HTMLSession()
r = session.get('https://')


# Try async and get some sites at the same time:
from requests_html import AsyncHTMLSession


asession = AsyncHTMLSession()

async def get_pythonorg():
    r = await asession.get('https://')

async def get_reddit():
    r = await asession.get('https://')

async def get_google():
    r = await asession.get('https://')

result = session.run(get_pythonorg, get_reddit, get_google)
 

