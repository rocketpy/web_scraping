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


# Case 2: SearchGraph using Mixed Models
# We use Groq for the LLM and Ollama for the embeddings.

from scrapegraphai.graphs import SearchGraph


# Define the configuration for the graph
graph_config = {
    "llm": {
        "model": "groq/gemma-7b-it",
        "api_key": "GROQ_API_KEY",
        "temperature": 0
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",  # set ollama URL arbitrarily
    },
    "max_results": 5,
}

# Create the SearchGraph instance
search_graph = SearchGraph(
    prompt="List me all the traditional recipes from Chioggia",
    config=graph_config
)

# Run the graph
result = search_graph.run()
# print(result)


# Case 3: SpeechGraph using OpenAI
# You just need to pass the OpenAI API key and the model name.

from scrapegraphai.graphs import SpeechGraph


graph_config = {
    "llm": {
        "api_key": "OPENAI_API_KEY",
        "model": "gpt-3.5-turbo",
    },
    "tts_model": {
        "api_key": "OPENAI_API_KEY",
        "model": "tts-1",
        "voice": "alloy"
    },
    "output_path": "audio_summary.mp3",
}
