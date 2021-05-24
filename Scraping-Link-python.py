#  Scraping-Link - A Python module for Web Scraping with Scraping.link, you will be able to scrape any website and solves typical blocking complications.

# PyPi:  https://pypi.org/project/scraping-link/
# Github: https://github.com/nicolasmarin/scraping-link-python

# pip install scraping-link


# This module can be used to web scraping - Extract HTML content.

from scraping_link import ScrapingLinkRequest


url = "https://parascrapear.com/"
apikey = "YOUR_API"

r = ScrapingLinkRequest.scrape(url, apikey)
print(r.text)

