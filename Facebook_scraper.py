import requests
from bs4 import BeautifulSoup


class FBGroupScraper:

    def __init__(self, group_id):
        self.group_id = group_id
        self.page_url = "https://mobile.facebook.com/groups/" + self.group_id
        self.page_content = ""


