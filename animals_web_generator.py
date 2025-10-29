import json


# --- Function Definitions ---

def load_data(file_path):
    """ Loads a JSON file from the given path. """
    with open(file_path, "r", encoding='utf-8') as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """ Takes a single animal dictionary and returns a formatted HTML card string. """

    # Start the HTML card with the opening list item tag
    html_card = '<li class="cards__item">'

    # Add the title div
    html_card += f'<div class="card__title">{animal_obj["name"]}</div>'

    # Add the paragraph for all the details
    html_card += '<p class="card__text">'

    # Add each detail, checking if it exists first
    if 'diet' in animal_obj['characteristics']:
        diet = animal_obj['characteristics']['diet']
        html_card += f'<strong>Diet:</strong> {diet}<br/>'

    if 'locations' in animal_obj and animal_obj['locations']:
        location = animal_obj['locations'][0]
        html_card += f'<strong>Location:</strong> {location}<br/>'

    if 'type' in animal_obj['characteristics']:
        type_ = animal_obj['characteristics']['type']
        html_card += f'<strong>Type:</strong> {type_}<br/>'

    # Close the paragraph and list item tags
    html_card += '</p>'
    html_card += '</li>'

    # Return the complete HTML string for this one card
    return html_card


# --- Main Script ---

# 1. Load the animal data from the JSON file
animals_data = load_data('animals_data.json')

# 2. Read the HTML template file
with open('animals_template.html', 'r', encoding='utf-8') as file:
    template_content = file.read()

# 3. Generate the HTML for all animals by looping and calling our function
animals_info_string = ""
for animal in animals_data:
    animals_info_string += serialize_animal(animal)

# 4. Replace the placeholder in the template with our generated string
final_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_info_string)

# 5. Write the final content to a new HTML file
with open('animals.html', 'w', encoding='utf-8') as file:
    file.write(final_html_content)

print("Successfully created animals.html!")