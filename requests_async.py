from requests_html import HTMLSession


session = HTMLSession()
req = session.get('https://...')
