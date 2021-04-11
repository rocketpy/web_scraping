import json 

p = driver.find_element_by_tag_name("...").text
data = json.loads(p)
print(data)


# or
import requests

url = 'https://...'
find = '...'  

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

response = requests.get(url, headers=headers).json()
data = response['data']

for el in data:
    if el['alt'] == find:
        id_key = el['id']
        image_url = el['image_url']
        alt = el['alt']
        print (el)

        
# or
import requests, json

url = "https://..."
response = requests.get(url)
json_value = response.json()
alt = json_value['alt']
