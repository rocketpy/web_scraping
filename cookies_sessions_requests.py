import requests


#  how take cookies ??? 
# 1. open dev. console on website , 2. go to Networks , 3. go to Headers , here we can take a cookies 

session = requests.Session()

#  create a cookies jar for contain a cookies
jar = requests.cookies.RequestsCookieJar()

r = session.get("URL")

# r = requests.get("URL")

#  get cookies from Request Headers and take part like : chat_session=

