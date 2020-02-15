#  in shell:  scrapy startproject name_project
#  cd name_project

#  creating a spider and URL
#  scrapy genspider name_spider blablabla.com/posts/

#  for run file with a our spider use:  scrapy crawl file_name
"""
#  use a specific proxy for that URL we can pass it as a meta parameter
def start_requests(self):
    for url in self.start_urls:
        return Request(url=url, callback=self.parse,
                       headers={"User-Agent": "My UserAgent"},
                       meta={"proxy": "http://191.175.1.1:8050"})
"""

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
        
#  for taking url of imgs  use:
#  response.xpath(‘//a/@href’)

def imgs_to_html(img_url):
  return '<img width=\'30%\' height=\'30%\' src=\''+ img_url +'\' > </img><br/> '

def parse(self, response):
        final = ''
        for i in response.xpath('//a/@href'):
            img_url = i.extract()
            if img_url.endswith('.jpg') or img_url.endswith('.png'):
                final += imgs_to_html(img_url)
                # print(img_url) 
        with open('images.html', 'a') as links:
            links.write(final)
        links.close()
