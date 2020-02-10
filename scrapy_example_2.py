#  in shell:  scrapy startproject name_project
#  cd name_project

#  creating a spider and URL
#  scrapy genspider name_spider blablabla.com/posts/

#  for run file with a our spider use:  scrapy crawl file_name

import scrapy


class MySpider(scrapy.Spider):
    name = "name of spider"  # here we can use file_name for name of spider !!!
    
    def start_requests(self):
        self.index = 0
        urls = [
            'http://blablabla.com/posts/',
        ]
        
        for url in urls:
            #  make a request to each url !!! 
            yield scrapy.Request(url=url, callback=self.parse)
            
            
    def parse(self, response):
        file_name = "response" + str(self.index)
        #  save response as a text file
        with open(file_name, 'wb') as f:        
            f.write(response.body)
        self.log('Saved file %s' % filename)
