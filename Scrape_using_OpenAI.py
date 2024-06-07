# Scrape the Web with entities extraction using OpenAI Function

# https://github.com/trancethehuman/entities-extraction-web-scraper


# Example
# Define the schema of the website you want to scrape in schemas.py (Pydantic class or dictionary are both fine):

class SchemaNewsWebsites(BaseModel):
    news_headline: str
    news_short_summary: str
  
# To start scraping, in main.py, run something like this:

asyncio.run(scrape_with_playwright(
        url="https://www.bbc.com",
        tags=["span"],
        schema_pydantic=SchemaNewsWebsites
    ))
