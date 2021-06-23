import csv
import requests
from bs4 import BeautifulSoup


# headrs = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0', 'accept': '*/*'}

headrs = {'Host': 'www...de',
          'If-None-Match': 'W/"2a07a-cNkp0k044NvAQTMhYpgDt4ar+KU"',
          'Referer': 'https://www..../results?animal_99=true',
          'TE': 'Trailers',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
          'X-API-Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjQ0Nzg1OTMsImlhdCI6MTYyNDQ3NzY5M30.1c_2SSqHH6URAOQig4Fzs-EbUrzD6o93LKdI4IXu9f8'
          'X-Site-ID': '1'
          }

# Take from: Inspector> Network> Headers> query string parameters
data = {
        }


def get_data(url, params=data):
    r = requests.get(url, headers=headrs, params=params)
    return r
  
 
if __name__ == '__main__':
    get_data()
    
    
