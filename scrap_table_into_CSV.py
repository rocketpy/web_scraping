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



