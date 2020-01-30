import scrapy
from urllib.parse import urljoin


class MySpider(scrapy.Spider):
    name = "some_name"  # spider name
    start_urls = ['http://.com']
    
    def parse(self, response):
        for post_link in response.xpath('//div[@class="post mb-2"]/h2/a/@href').extract():
            url = urljoin(response.url, post_link)
            print(url)
