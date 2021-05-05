# library to generate user agent
from user_agent import generate_user_agent
import requests


proxies = {'http' : 'http://10.10.0.0:0000',  
          'https': 'http://120.10.0.0:0000'}

# generate a user agent
headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}

# headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'}
page_response = requests.get(page_link, timeout=5, headers=headers, proxies=proxies)


try:
    page_response = requests.get(page_link, timeout=5)
    if page_response.status_code == 200:
        # extract
    else:
        print(page_response.status_code)
        # notify, try again
except requests.Timeout as e:
    print("It is time to timeout")
    print(str(e))

