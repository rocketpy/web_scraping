# Spidermon 
"""
Spidermon is an extension for Scrapy spiders.
The package provides useful tools for data validation, stats monitoring, and notification messages.
This way you leave the monitoring task to Spidermon and just check the reports/notifications.
"""

# Github:https://github.com/scrapinghub/spidermon
# Docs: https://spidermon.readthedocs.io/en/latest/installation.html

# Requirements: 
# Python 3.6, Python 3.7, Python 3.8 or Python 3.9

# pip install spidermon

"""
scrapy startproject tutorial
cd tutorial
scrapy genspider quotes quotes.toscrape.com
"""

# https://github.com/scrapinghub/spidermon/tree/master/examples/tutorial/tutorial/spiders
# tutorial/spiders/quotes.py
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('.quote'):
            yield {
                'quote': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'author_url': response.urljoin(
                    quote.css('.author a::attr(href)').get()),
                'tags': quote.css('.tag *::text').getall(),
            }

        yield scrapy.Request(
            response.urljoin(
                response.css('.next a::attr(href)').get()
            )
        )
