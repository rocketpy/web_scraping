# pip install Scrapy
# pip install pymongo

# to start a new Scrapy project: scrapy startproject project_name
# to start first spider: cd project_name
#                        scrapy genspider example example.com

# working with items: https://doc.scrapy.org/en/1.0/topics/items.html


import scrapy
from scrapy.item import Item, Field


class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
    

    
# need create a file called project_spider.py in the “spiders” directory.
from scrapy import Spider


class ProjectSpider(Spider):
    name = "Some_name"
    allowed_domains = ["blablabla.com"]
    start_urls = ["http://...",
                 ]

