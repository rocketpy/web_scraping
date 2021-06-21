import queue
import requests
from bs4 import BeautifulSoup


URL = ''

proxies = {'http': 'http://',
           'https': 'http://'
           }

def get_proxie(url):
    return requests.get(url, proxies=proxies)


def get_data(data):
    soup = BeautifulSoup(data, "html.parser")


if __name__=='__main__':
    queue = queue.Queue()
       
