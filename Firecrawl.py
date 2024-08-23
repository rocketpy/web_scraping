# Firecrawl - Crawl and convert any website into LLM-ready markdown or structured data. 
# The Firecrawl Python SDK is a library that allows you to easily scrape and crawl websites, and output the data in a format ready for use with language models (LLMs). 


# https://github.com/mendableai/firecrawl
# https://github.com/mendableai/firecrawl-py


# [OLD] Firecrawl Python SDK

"""
Installation
To install the Firecrawl Python SDK, you can use pip:

pip install firecrawl-py


Usage

Get an API key from firecrawl.dev
Set the API key as an environment variable named FIRECRAWL_API_KEY or pass it as a parameter to the FirecrawlApp class.
Here's an example of how to use the SDK:

from firecrawl import FirecrawlApp

# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key='your_api_key')

# Scrape a single URL
url = 'https://mendable.ai'
scraped_data = app.scrape_url(url)

# Crawl a website
crawl_url = 'https://mendable.ai'
crawl_params = {
    'crawlerOptions': {
        'excludes': ['blog/*'],
        'includes': [], # leave empty for all pages
        'limit': 1000,
    }
}

crawl_result = app.crawl_url(crawl_url, params=crawl_params)
"""
