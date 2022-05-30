from requests_html import HTMLSession

session = HTMLSession()
res = session.get('https://...')
print(res)



