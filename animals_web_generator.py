import requests
import json

# Constants for API access
API_KEY = "rkw1LvTjt+16MeGrEOvFzg==Whn03X2JW8DjG60q" # Replace with your actual key
REQUESTED_URL = "https://api.api-ninjas.com/v1/animals"

def serialize_animal(animal_obj):
    """ Takes a single animal dictionary and returns a formatted HTML card string. """
    # Start the HTML card with the opening list item tag
    html_card = '<li class="cards__item">'

    # Add the title div - Check API response for the correct key (likely 'name')
    # Use .get() for safety in case the key is missing
    name = animal_obj.get("name", "N/A")
    html_card += f'<div class="card__title">{name}</div>'

    # Add the paragraph for all the details
    html_card += '<p class="card__text">'

    # Adapt these to match the API Ninja response structure!
    # Example: API might have 'characteristics' dictionary with 'diet' inside,
    # or 'diet' might be a top-level key. Use .get() chained for nested data.
    characteristics = animal_obj.get("characteristics", {}) # Get characteristics dict or empty dict
    diet = characteristics.get("diet", "N/A")
    if diet != "N/A":
        html_card += f'<strong>Diet:</strong> {diet}<br/>'

    # Location might be a list or a single string in the API response
    locations = animal_obj.get("locations", []) # Get locations list or empty list
    if locations: # Check if the list is not empty
        # Assuming locations is a list of strings
        location = locations[0]
        html_card += f'<strong>Location:</strong> {location}<br/>'

    # 'Type' might be under characteristics or top-level
    type_ = characteristics.get("type", "N/A") # Check within characteristics first
    if type_ == "N/A":
         type_ = animal_obj.get("taxonomy", {}).get("class", "N/A") # Example fallback: check taxonomy.class

    if type_ != "N/A":
        html_card += f'<strong>Type:</strong> {type_}<br/>'

    # Close the paragraph and list item tags
    html_card += '</p>'
    html_card += '</li>'

    # Return the complete HTML string for this one card
    return html_card

# Main Script

# 1. Get user input for the animal name
# This replaces the old ANIMAL_TO_SEARCH = "Fox" constant
animal_to_search = input("Enter a name of an animal: ") # Milestone 2

# 2. Fetch Animal Data from API Ninja API
print(f"Fetching data for '{animal_to_search}' from API Ninja...")
animals_data = [] # Initialize as empty list

# Prepare parameters and headers for the API request
params_data = {"name": animal_to_search} # Use the variable from user input
request_headers = {"X-Api-Key": API_KEY}

try:
    # Make the GET request
    response = requests.get(REQUESTED_URL, params=params_data, headers=request_headers)
    response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
    animals_data = response.json() # Parse the JSON response

    if not animals_data:
        print(f"No animals found matching '{animal_to_search}'.")
    else:
        print(f"Successfully fetched {len(animals_data)} result(s).")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
except json.JSONDecodeError:
    print("Error parsing JSON response from API.")
    print(f"Raw response text (first 200 chars): {response.text[:200]}...")

# 3. Read the HTML template file
try:
    with open('animals_template.html', 'r', encoding='utf-8') as file:
        template_content = file.read()
except FileNotFoundError:
    print("Error: animals_template.html not found.")
    exit()

# 4. Generate the HTML for all animals
animals_info_string = ""
if animals_data: # Only generate if data was successfully fetched
    for animal in animals_data:
        animals_info_string += serialize_animal(animal)
else:
    # Show a message if no data was fetched or found
    animals_info_string = f"<p>No animal data found for '{animal_to_search}'.</p>"

# 5. Replace the placeholder in the template
final_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_info_string)

# 6. Write the final content to a new HTML file
try:
    with open('animals.html', 'w', encoding='utf-8') as file:
        file.write(final_html_content)
    # Changed the final print message to match the example
    print("Website was successfully generated to the file animals.html.")
except IOError as e:
    print(f"Error writing to animals.html: {e}")