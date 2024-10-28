import requests
import logging
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#setup logging
logging.basicConfig(level=logging.INFO)

# Loading configuration from config.json
with open('config.json', 'r') as file:
    config = json.load(file)


api_key = os.getenv("OMDB_API_KEY")
search_keyword = config["search_keyword"]
base_url = config["base_url"]


def get_search_results(keyword, page=1):
    url = f"{base_url}?apikey={api_key}&s={search_keyword}&page={page}"
    response = requests.get(url)
    data = response.json()
    return data.get("Search", [])
# Check if the response contains search results

def get_movie_details(imdb_id):
    url = f"{base_url}?apikey={api_key}&i={imdb_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return response.json()

# Main script execution with pagination
page = 1
while True:
    # Calling the get_search_results passing the keyword and page
    search_results = get_search_results(search_keyword, page)
    if not search_results:
        logging.info(f"No more results on page {page}. Ending pagination.")
        break

    for result in search_results:
        try:
            # Here we call the get_movie_details passing the ID of the movie
            details = get_movie_details(result["imdbID"])
            if "Title" in details:
                logging.info(f"Retrieved details:{details}")
            else:
                logging.warning(f"No details found for {result['imdbID']}")
        except requests.RequestException as e:
            logging.error(f"Error retrieving details for {result['imdbID']}: {e}")
    page += 1 #Move to the next page