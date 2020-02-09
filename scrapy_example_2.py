#  in shell:  scrapy startproject name_project
#  cd name_project

#  creating a spider and URL
#  scrapy genspider name_spider blablabla.com/posts/

import scrapy


class MySpider(scrapy.Spider):
    name = "name of spider"
    
    def start_requests(self):
        self.index = 0
        urls = [
            'http://blablabla.com/posts/',
        ]
        
        for url in urls:
            #  make a request to each url !!! 
            yield scrapy.Request(url=url, callback=self.parse)
