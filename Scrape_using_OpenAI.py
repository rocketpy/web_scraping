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

"""
Setup
1. Create a new Python virtual environment
python -m venv virtual-env or python3 -m venv virtual-env (Mac)

py -m venv virtual-env (Windows 11)

2. Activate virtual environment
.\virtual-env\Scripts\activate (Windows)

source virtual-env/bin/activate (Mac)

3. Install dependencies using Poetry
Run poetry install --sync or poetry install

4. Install playwright
playwright install
5. Create a new .env file to store OpenAI's API key
OPENAI_API_KEY=XXXXXX
Usage
Run locally
python main.py
"""
