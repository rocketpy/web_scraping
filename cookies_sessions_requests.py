import json
import requests


#  how take cookies ??? 
# 1. open dev. console on website , 2. go to Networks , 3. go to Headers , here we can take a cookies 

session = requests.Session()

#  get cookies from Request Headers and take part like : chat_session=value

#  create a cookies jar for contain a cookies
jar = requests.cookies.RequestsCookieJar()

cookie_name = "chat_session"
cookie_value = "some value"

jar.set("cookie_name", "cookie_value")

session.cookies = jar

r = session.get("URL")

js = json.loads(r.text)
print(js['HTML'][0])

# r = requests.get("URL")
