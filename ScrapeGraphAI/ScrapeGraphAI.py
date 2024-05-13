# ScrapeGraphAI - is a web scraping python library that uses LLM and direct graph logic to create scraping pipelines for websites, documents and XML files.

# https://github.com/VinciGit00/Scrapegraph-ai


# pip install scrapegraphai

# you will also need to install Playwright for javascript-based scraping:
# playwright install


# Case 1: SmartScraper using Local Models
# Remember to have Ollama installed and download the models using the ollama pull command.


from scrapegraphai.graphs import SmartScraperGraph


graph_config = {
    "llm": {
        "model": "ollama/mistral",
        "temperature": 0,
        "format": "json",  # Ollama needs the format to be specified explicitly
        "base_url": "http://localhost:11434",  # set Ollama URL
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",  # set Ollama URL
    },
    "verbose": True,
}

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the projects with their descriptions",
    # also accepts a string with the already downloaded HTML code
    source="https://perinim.github.io/projects",
    config=graph_config
)

result = smart_scraper_graph.run()
# print(result)
