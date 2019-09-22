import csv
import time
import requests
from random import choice
from multiprocessing import Pool


proxs = {'https': 'http://'}

user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36']

headers = {'User-Agent': choice(user_agents)}

def get_html(url):
    sleep(1)  # 1 sec
    r = requests.get(url, verify=False, proxies=proxs, headers=headers, timeout=3)
    return r.text

def write_csv(data):
    with open('websites.csv', 'a') as f:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_page_data(text):
        data = text.strip().split('\n')[1:]  # data return a list

        for r in data:  # any r is a string
            columns = r.strip().split('\t')
            name = columns[0]
            url = columns[1]
            description = columns[2]
            traffic = columns[3]
            percent = columns[4]

            data = {'name': name,
                    'url': url,
                    'description': description,
                    'traffic': traffic,
                    'percent': percent
                    }
            write_csv(data)


def make_all(url):
    text = get_html(url)
    get_page_data(text)

def main():
    url = 'https://www...page={}'
    urls = [url.format(str(i)) for i in range(1, 6321)]  # pages

    with Pool(20) as p:  # pools is a process
        p.map(make_all, urls)  # p.map to every func make_all


if __name__ == '__main__':
    main()
