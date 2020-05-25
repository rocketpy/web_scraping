import requests
import pandas as pd
fro bs4 import BeautifulSoup


URL = "..."  # page must have a some table !!!

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find('table', {'class': 'class_name'}).tbody  # tbody is a tag

rows = table.find_all('tr')
columns = [i.text.replace('\n', '') for i in rows[0].find_all('th')]

df = pd.DataFrame(columns=columns)

for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    
    if len(tds) == 4:
        values = [tds[0].text, tds[1].text, '', tds[2].text, tds[3].text.replace('\n', '').replace('\xx', '')]
    else:
        values = [td.text.replace('\n', '').replace('\xx', '') for td in tds]  # use replace for cleaning a text
        
    df = df.append(pd.Series(values, index=columns), ignore_index=True)
    df.to_csv(r'path to directory', 'file_name.csv', index=False)
    

