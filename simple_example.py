import csv
import requests
from bs4 import BeautifulSoup


def get_data():
    resp = requests..get(https://...)
    soup = BeautifulSoup(resp.content, 'html.parser')
    data = soup.find('a', {'href': '...').text
    return data


def get_data_api():
    resp = requests..get(https://.../api/...)
    data = resp.json()
    value = [x for x in data['Data'] if x['User']['Name'] == 'John'][0]
    return value['User']['Name']


url = requests.get('http:// .com').text
soup = BeautifulSoup(url, 'lxml')

with open('cms_scrape.csv', 'w'):
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)
    print()
    csv_writer.writerow([headline, summary, yt_link])

    
if __name__=='__main__':
    print('Resault is :', get_data())
    print('Resault is :', get_data_api())
    
