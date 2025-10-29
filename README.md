zootopia-api-project

Description

This project generates a simple HTML webpage displaying information about animals based on user input. Unlike the original Zootopia project which used a static JSON file, this version dynamically fetches animal data in real-time from the API Ninja Animals API.

The project demonstrates:

Interacting with an external API using Python's requests library.

Handling API keys via headers.

Parsing JSON responses.

Generating HTML content dynamically based on API data.

Basic project structure with separation of concerns (data fetching vs. HTML generation).

Features

Prompts the user to enter an animal name.

Fetches data for the specified animal from the API Ninja Animals API.

Generates an animals.html file displaying the fetched animal(s) information in styled cards.

Handles cases where no animals are found or API errors occur.

Technology Used

Python 3: Core programming language.

Requests Library: For making HTTP requests to the API.

HTML: For the structure of the generated webpage.

CSS: (Assumed from original Zootopia project) For styling the webpage. Included within animals_template.html.

Setup and Installation

Clone the Repository:

git clone <your-repository-url>
cd zootopia-api-project


Install Dependencies:
Make sure you have Python 3 installed. Then, install the required library:

pip install -r requirements.txt


Add Your API Key:

Open the data_fetcher.py file.

Find the line API_KEY = "YOUR_API_KEY_HERE" (or similar).

Replace "YOUR_API_KEY_HERE" with your actual API key obtained from API Ninja.

Usage

Navigate to the project directory in your terminal.

Run the main script:

python animals_web_generator.py


The script will prompt you to enter an animal name.

After fetching the data, it will create (or overwrite) an animals.html file in the same directory.

Open the animals.html file in your web browser to view the results.

File Structure

data_fetcher.py: Contains the logic for interacting with the API Ninja Animals API. Includes the fetch_data function.

animals_web_generator.py: The main script. Handles user input, calls the data fetcher, and generates the final HTML file using the template. Contains the serialize_animal function.

animals_template.html: The HTML template file with CSS styles and the __REPLACE_ANIMALS_INFO__ placeholder.

requirements.txt: Lists the required Python libraries (requests).

animals.html: (Generated file) The final webpage displaying the animal data.

README.md: This file.
