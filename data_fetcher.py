import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


# Constants for API access
API_KEY = os.getenv('API_KEY')
REQUESTED_URL = "https://api.api-ninjas.com/v1/animals"

# Function definition

def fetch_data(animal_name):
    """
    Fetches the animals data from the API Ninja API for the given 'animal_name'.
    Returns: a list of animals (dictionaries) if successful,
    or an empty list if an error occurs or no animals are found.

    """

    print(f"Fetching data for '{animal_name}' from API Ninja...")
    animals_data = []  # Default to an empty list

    # Prepare parameters and headers for the API request
    params_data = {"name": animal_name}
    request_headers = {"X-Api-Key": API_KEY}

    try:
        # Make the GET request
        response = requests.get(REQUESTED_URL, params=params_data, headers=request_headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        animals_data = response.json()  # Parse the JSON response

        if not animals_data:
            print(f"No animals found matching '{animal_name}'.")
        else:
            print(f"Successfully fetched {len(animals_data)} result(s).")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
    except json.JSONDecodeError:
        print("Error parsing JSON response from API.")

    # Return the fetched data (or the empty list)
    return animals_data