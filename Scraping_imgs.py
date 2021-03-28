import requests
import img2pdf


# scraping images and save to PDF file
def get_data():
    # need take Accept and User-agent from Networkfrom Inspector (Chrome Dev tools)
    headers = {"Accept": "..."
               "User=Agent": "..."
              }
           
    # start from main url
    # url = "https://"
    
    imgs_list = []  # use this list for img2pdf module
    #  using loop for urls
    for i in range(1, 101):  # 100 pages
        urls = f"https://.../{i}.jpg"  # or /{i}.html
        r = requests.get(url=url, headers=headers)
        resp = r.content
        
        # create new dir named Images and save scraped imgs to this dir
        with open(f"Images/{i}.jpg", "wb") as f:
            f.write(resp)
            imgs_list.append(f"Images/{i}.jpg")
            
            # checking in cmd a progress
            # print(f"Scraped {i} of 100 ")
            
    # creating PDF file        
    with open("File with images.pdf", "wb") as f:
        f.write(img2pdf.convert(imgs_list))
    
    
if __name__ == '__main__':
    get_data()
