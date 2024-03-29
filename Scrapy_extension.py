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
        
        
#  Enabling Spidermon
# To enable Spidermon in your project, include the following lines in your Scrapy project settings.py file:


SPIDERMON_ENABLED = True

EXTENSIONS = {
    'spidermon.contrib.scrapy.extensions.Spidermon': 500,
}


# tutorial/monitors.py
from spidermon import Monitor, MonitorSuite, monitors


@monitors.name('Item count')
class ItemCountMonitor(Monitor):

    @monitors.name('Minimum number of items')
    def test_minimum_number_of_items(self):
        item_extracted = getattr(
            self.data.stats, 'item_scraped_count', 0)
        minimum_threshold = 10

        msg = 'Extracted less than {} items'.format(
            minimum_threshold)
        self.assertTrue(
            item_extracted >= minimum_threshold, msg=msg
        )

class SpiderCloseMonitorSuite(MonitorSuite):

    monitors = [
        ItemCountMonitor,
    ]
    
# Item validation
import scrapy


class QuoteItem(scrapy.Item):
    quote = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()
    tags = scrapy.Field()

    
# modify the spider code to use the newly defined item
import scrapy
from tutorial.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('.quote'):
            item = QuoteItem(
                quote=quote.css('.text::text').get(),
                author=quote.css('.author::text').get(),
                author_url=response.urljoin(
                    quote.css('.author a::attr(href)').get()
                ),
                tags=quote.css('.tag *::text').getall()
            )
            yield item

        yield scrapy.Request(
            response.urljoin(
                response.css('.next a::attr(href)').get()
            )
        )

        
# create our schematics model in validators.py
from schematics.models import Model
from schematics.types import URLType, StringType, ListType


class QuoteItem(Model):
    quote = StringType(required=True)
    author = StringType(required=True)
    author_url = URLType(required=True)
    
    
# # tutorial/settings.py
ITEM_PIPELINES = {
    'spidermon.contrib.scrapy.pipelines.ItemValidationPipeline': 800,
}

SPIDERMON_VALIDATION_MODELS = (
    'tutorial.validators.QuoteItem',
)

    tags = ListType(StringType)
