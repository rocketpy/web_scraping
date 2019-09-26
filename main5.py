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
    
"""
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool()

pool = ThreadPool(4) # Sets the pool size to 4
"""

"""
import urllib2
from multiprocessing.dummy import Pool as ThreadPool

urls = [
	'http://www.python.org',
	'http://www.python.org/about/',
	'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
	'http://www.python.org/doc/',
	'http://www.python.org/download/',
	'http://www.python.org/getit/',
	'http://www.python.org/community/',
	'https://wiki.python.org/moin/',
	'http://planet.python.org/',
	'https://wiki.python.org/moin/LocalUserGroups',
	'http://www.python.org/psf/',
	'http://docs.python.org/devguide/',
	'http://www.python.org/community/awards/'
	# etc.. 
	]

# Make the Pool of workers
pool = ThreadPool(4)

# Open the urls in their own threads
# and return the results
results = pool.map(urllib2.urlopen, urls)

#close the pool and wait for the work to finish 
pool.close()
pool.join()
"""

# examples with a many sizes of Pool
"""
results = []
for url in urls:
	result = urllib2.urlopen(url)
	results.append(result)
#  4 Pool
pool = ThreadPool(4)
results = pool.map(urllib2.urlopen, urls)

# 8 Pool
pool = ThreadPool(8)
results = pool.map(urllib2.urlopen, urls)

# 13 Pool
pool = ThreadPool(13)
results = pool.map(urllib2.urlopen, urls)
"""
