import json
import os
import re

def get_file_path(filename):
    """Construct full file path for a given filename"""
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def load_and_validate_restaurant_data(file_path):
    """Load and validate restaurant data from a JSON file."""

    if not os.path.exists(file_path):
        print("Error: Data file not found.")
        return None

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return None

    if not isinstance(data, dict):  
        print("Error: Data should be a dictionary.")
        return None

    # Additional validation for each restaurant data entry if needed
    for key, entry in data.items():
        if not isinstance(entry, dict):
            print(f"Error: The entry for {key} should be a dictionary.")
            return None

    return data

def load_and_convert_data_to_list():
    """Load and validate restaurant data, then convert it to a list for easier manipulation."""

    # Use the utility function to get the full path of the data file
    data_file_path = get_file_path('restaurant_data.json')  # Replaced multiple lines with a single function call
    
    # Load and validate the restaurant data
    restaurant_data = load_and_validate_restaurant_data(data_file_path)
    
    if restaurant_data is None:
        print("Failed to load restaurant data.")
        return None  # Handle the error as needed
    else:
        print("Successfully loaded restaurant data.")
        
        # Convert the restaurant data to a list for easier manipulation.
        restaurant_list = list(restaurant_data.values())
        
        return restaurant_list, restaurant_data, data_file_path

def compare_by(restaurant1, restaurant2, criteria):
    """Compare two dictionaries by a given field"""

    return restaurant1[criteria] > restaurant2[criteria]

def display_restaurants(restaurants):
    '''Function to display a list of restaurants in a readable format'''
    
    # Enumerate through the list of restaurants and print details for each
    for i, restaurant in enumerate(restaurants, 1):
        print(f"{i}. {restaurant['name']} ({restaurant['cuisine']})")
        print(f"   Location: {restaurant['location']}")
        print(f"   Rating: {restaurant['rating']}")
        print("   ---")

def update_average_rating(restaurant):
    """Update the average rating of a restaurant based on its reviews."""

    all_ratings = [review['rating'] for review in restaurant['reviews']]
    new_average_rating = sum(all_ratings) / len(all_ratings)
    
    # Round the new average rating to one decimal place.
    return round(new_average_rating, 1)

def update_restaurant_data(restaurant, restaurant_data):
    """Update the main restaurant_data dictionary with the updated restaurant data."""

    for key, value in restaurant_data.items():
        if value['name'] == restaurant['name']:
            restaurant_data[key] = restaurant

def save_to_json(data, file_path):
    """Save updated restaurant data back to the JSON file."""

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def sanitize_text(text):
    """Sanitize user input text by escaping special characters."""
    
    # Remove any character that is not a word character or a space
    text = re.sub(r'[^\w\s,.!?-]', '', text)
    
    # Remove leading and trailing whitespaces
    text = text.strip()

    return text