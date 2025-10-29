import data_fetcher

# Function definitions

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

    # Check for characteristics
    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet", "N/A")
    if diet != "N/A":
        html_card += f'<strong>Diet:</strong> {diet}<br/>'

    # Check for locations
    locations = animal_obj.get("locations", [])
    if locations:
        html_card += f'<strong>Location:</strong> {locations[0]}<br/>'

    # Check for type (class) in taxonomy
    taxonomy = animal_obj.get("taxonomy", {})
    type_ = taxonomy.get("class", "N/A")
    if type_ != "N/A":
        html_card += f'<strong>Type:</strong> {type_}<br/>'

    # Close the paragraph and list item tags
    html_card += '</p>'
    html_card += '</li>'

    # Return the complete HTML string
    return html_card


# Main Script

# 1. Get user input for the animal name
animal_name = input("Enter a name of an animal: ")

# 2. Fetch Animal Data using the data_fetcher module
# This one line REPLACES the entire API request and try/except block
animals_data = data_fetcher.fetch_data(animal_name)

# 3. Read the HTML template file
try:
    with open('animals_template.html', 'r', encoding='utf-8') as file:
        template_content = file.read()
except FileNotFoundError:
    print("Error: animals_template.html not found.")
    exit()

# 4. Generate the HTML for all animals
animals_info_string = ""
if animals_data:  # Only generate if data was successfully fetched
    for animal in animals_data:
        animals_info_string += serialize_animal(animal)
else:
    # Show a message if no data was fetched or found
    animals_info_string = f"<p>No animal data found for '{animal_name}'.</p>"

# 5. Replace the placeholder in the template
final_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_info_string)

# 6. Write the final content to a new HTML file
try:
    with open('animals.html', 'w', encoding='utf-8') as file:
        file.write(final_html_content)
    print("Website was successfully generated to the file animals.html.")
except IOError as e:
    print(f"Error writing to animals.html: {e}")