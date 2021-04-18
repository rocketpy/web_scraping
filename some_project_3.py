import requests
from bs4 import BeautifulSoup


persons_url_list = []

# preparing url's for parsing  
for i in range(0, 800, 20):
    url = f'https://www.../page={i}'
    req = requests.get(url)
    result = req.content
    
    soup = BeautifulSoup(result, 'lxml')
    persons = soup.find_all(class_='class_name')
    
    for person in persons:
        person_page_url = person.get('href')
        persons_url_list.append(person_page_url)
    
with open('persons_url_list.txt', 'a') as file:
    for line in persons_url_list:
        file.write(f'{line}\n')
