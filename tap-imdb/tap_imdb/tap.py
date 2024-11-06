import requests
import logging
import os
import json
import sys
import singer
from dotenv import load_dotenv
from utils import get_env, get_config


class TapIMDB():
    base_url = ''
    api_key = ''

    def load_config(self, filename):
        # Check if a config filename is passed as an argument
        # Load configuration from the specified file
        config_path = os.path.join(os.getcwd(), filename)

        with open(config_path, 'r') as file:
            return json.load(file)
        
    def get_argument(self, names, argv):
        # This function return the value for the argument of the givin name
        # Example: --port 80 (calling get_argument(["--port"], argv) will return 80)
        for i, arg in enumerate(argv):
            if arg in names:
                return argv[i+1]
            
    def get_search_results(self, keyword, page=1):
        url = f"{self.base_url}?apikey={self.api_key}&s={keyword}&page={page}"
        response = requests.get(url)
        data = response.json()
        return data.get("Search", [])
    # Check if the response contains search results

    def get_movie_details(self, imdb_id):
        url = f"{self.base_url}?apikey={self.api_key}&i={imdb_id}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return response.json()

    def run(self):
        # how to get a specific place in a array, this + 1
        # Check if the config file was provided as an argument
        if len(sys.argv) > 1:
            filename = self.get_argument(["-c", "--config"], sys.argv)
        else:
            # If not provided, raise an erro or set a default file
            raise ValueError("Please provide a configuration filename as an argument")

        # Load configuration
        try:
            config = self.load_config(filename)
            search_keyword = config["search_keyword"]
            base_url = config["base_url"]
        except KeyError as e:
            print(f"Missing configuration key: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Failed to load config: {e}")
            sys.exit(1)


        # Load environment variables from .env file
        load_dotenv()

        # Get key from environment
        self.api_key = get_env("OMDB_API_KEY")

        #setup logging
        logging.basicConfig(level=logging.INFO)


        search_keyword = get_config("search_keyword", config)
        self.base_url = get_config("base_url", config)


        # Define schema for the output
        schema = {
            "properties": {
                "Title": {"type": "string"},
                "Year": {"type": "string"},
                "Rated": {"type": "string"},
                "Released": {"type": "string"},
                "Runtime": {"type": "string"},
                "Genre": {"type": "string"},
                "Director": {"type": "string"},
                "Writer": {"type": "string"},
                "Actors": {"type": "string"},
                "Plot": {"type": "string"},
                "Language": {"type": "string"},
                "Country": {"type": "string"},
                "Awards": {"type": "string"},
                "Poster": {"type": "string"},
                "imdbRating": {"type": "string"},
                "imdbVotes": {"type": "string"},
                "imdbID": {"type": "string"},
                "Type": {"type": "string"},
            },
            "type": "object",
        }

        # Main script execution with pagination
        page = 1

        # Emit the schema to the terminal
        singer.write_schema('movies', schema, 'Title')
        #singer.write_records('movies', [{'Title': 'string', 'Year' : 'String'}])

        while True:
            # Calling the get_search_results passing the keyword and page
            search_results = self.get_search_results(search_keyword, page)
            if not search_results:
                logging.info(f"No more results on page {page}. Ending pagination.")
                break

            for result in search_results:
                try:
                    # Here we call the get_movie_details passing the ID of the movie
                    details = self.get_movie_details(result["imdbID"])
                    if "Title" in details:
                        logging.info(f"Retrieved details:{details}")
                        singer.write_records('movies', [details])
                    else:
                        logging.warning(f"No details found for {result['imdbID']}")
                except requests.RequestException as e:
                    logging.error(f"Error retrieving details for {result['imdbID']}: {e}")
            page += 1 #Move to the next page