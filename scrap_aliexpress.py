import scrapy


class AliexpressSpider(scrapy.Spider):
    name = 'aliexpress'
    allowed_domains = ['aliexpress.com']
    start_urls = ['https://www.aliexpress.com/category/.../.html',
                 'https://www.aliexpress.com/category/...']


    def parse(self, response):
        print("procesing : " + response.url)
        product_name = response.css('.product::text').extract()
        price_range = response.css('.value::text').extract()
        orders = response.xpath("//em[@title='Total Orders']/text()").extract()
        company_name = response.xpath("//a[@class='store $p4pLog']/text()").extract()

        data = zip(product_name, price_range, orders, company_name)

        for item in data:
            scraped_info = {
                'page':response.url,
                'product_name' : item[0], 
                'price_range' : item[1],
                'orders' : item[2],
                'company_name' : item[3],
            }

            yield scraped_info
