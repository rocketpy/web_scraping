import requests


def get_data():
    # need take Accept and User-agent from Networkfrom Inspector (Chrome Dev tools)
    headers = {"Accept": "..."
               "User=Agent": "..."
              }
           
    # start from main url
    # url = "https://"
           
    #  using loop for urls
    for i in range(1, 100):
        urls = f"https://.../{i}.jpg"  # or /{i}.html
        r = requests.get(url=url, headers=headers)
        resp = r.content
        
        # create new dir named Images and save scraped imgs to this dir
        with open(f"Images/{i}.jpg", "wb") as f:
            f.write(resp)
            # checking in cmd a progress
            # print(f"Scraped {i} of 100 ")

if __name__ == '__main__':
    get_data()
