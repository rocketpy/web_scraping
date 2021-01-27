import csv
import time
import requests
from random import choice
from bs4 import BeautifulSoup


proxies = {'http': 'http:// ... ',
           'https': 'http:// ... '}

headers = {'User-Agent': choice(useragents)}

def get_html(url):
    #time.sleep(3)
    proxy = {'http': 'http://' + proxies} 
    useragent = {'User-Agent': choice(useragents)} 
    r = requests.get(url, headers=headers, timeout=3)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('div', id='home-welcome').find('header').find('h1').text
    return h1

def main():
    url = 'https://... .org/'
    print(get_data(get_html(url)))
    
useragents = ['Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US)',
              'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)']


"""
import csv
import pandas
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict


page = requests.get("https://www...")
soup = BeautifulSoup(page.content,"html.parser")

name = soup.find("div",{"class":"name"})
# name = soup.find("div",{"class":"name"}).text.replace("\n","").strip()   it's a full path

player_ids = pandas.read_csv("player_ids.csv")
ids = player_ids["Ids"]

base_url = "https://www..."

player_list = []

for pages in ids:
    d=OrderedDict()
    print(base_url+str(pages)+"/profile.html")
    request = requests.get(base_url+str(pages)+"/profile.html")
    content = request.content
    soup = BeautifulSoup(content,"html.parser")
    d['Name'] = soup.find("div",{"class":"name"}).text.replace("\n","").strip()
    d['Country'] = soup.find("div",{"class":"country"}).text.replace("\n","").strip()
    d['Role'] = soup.find("div",{"class":"role"}).text.replace("\n","").strip()
    d['Age'] = soup.find("div",{"class":"profile-number"}).text.replace("\n","").strip()
    d['Height(cm)'] = soup.find_all("div",{"class":"profile-number"})[1].text.replace("\n","").strip()
    d['International Caps'] = soup.find_all("div",{"class":"profile-number"})[2].text.replace("\n","").strip()
    d['International Goals'] = soup.find_all("div",{"class":"profilenumber"})[3].text.replace("\n","").strip()

player_list.append(d)
df = pandas.DataFrame(player_list)
df.to_csv('Players_info.csv', index = False)
print("Success \n")

# print(soup.prettify())

"""
    
if __name__ == '__main__':
    main()
 
