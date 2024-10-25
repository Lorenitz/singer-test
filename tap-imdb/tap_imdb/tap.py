import requests
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#setup logging
logging.basicConfig(level=logging.INFO)

api_key = os.getenv("OMDB_API_KEY")
search_keyword = "adventure"


def get_search_results(keyword):
    url = f"https://www.omdbapi.com/?apikey={api_key}&s={search_keyword}"
    response = requests.get(url)
    data = response.json()
    return data.get("Search", [])
# Check if the response contains search results

def get_movie_details(imdb_id):
    url = f"https://www.omdbapi.com/?apikey={api_key}&i={imdb_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return response.json()

# Main script execution
search_results = get_search_results(search_keyword)
for result in search_results:
    try:
        details = get_movie_details(result["imdbID"])
        if "Title" in details:
            logging.info(f"Retrieved details:{details}")
        else:
            logging.warning(f"No details found for {result['imdbID']}")
    except requests.RequestException as e:
        logging.error(f"Error retrieving details for {result['imdbID']}: {e}")        