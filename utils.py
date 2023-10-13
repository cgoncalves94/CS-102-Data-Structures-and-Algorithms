import json
import os
import re
from sorts import quicksort, is_sorted, compare_by_key
from searches import binary_search

def get_file_path(filename):
    """Construct full file path for a given filename"""
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, filename)

def load_and_validate_restaurant_data(file_path):
    """Ensure the data is in the expected format and all required fields are present"""

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
    """Calculate and return the updated average rating for a restaurant based on its reviews"""

    all_ratings = [review['rating'] for review in restaurant['reviews']]
    new_average_rating = sum(all_ratings) / len(all_ratings)
    
    # Round the new average rating to one decimal place.
    return round(new_average_rating, 1)

def update_restaurant_data(restaurant, restaurant_data):
    """# Update the restaurant's data in the main data dictionary."""

    for key, value in restaurant_data.items():
        if value['name'] == restaurant['name']:
            restaurant_data[key] = restaurant

def handle_cuisine_search(restaurant_list):
    """
    Handles the search by cuisine type.
    """
    # Initialize an empty list to hold the filtered restaurants
    filtered_list = []
    
    # Get the cuisine type from the user
    cuisine_to_search = input("Enter the cuisine you're looking for: ").strip()

    # Check if the list is sorted by cuisine, if not, sort it
    if not is_sorted(restaurant_list, 'cuisine'):
        sorted_list = quicksort(restaurant_list, 0, len(restaurant_list) - 1, compare_by_key('cuisine'))
    else:
        sorted_list = restaurant_list

    # Perform binary search to find the first occurrence of the cuisine
    first_occurrence_idx = binary_search(sorted_list, cuisine_to_search, 'cuisine')
    
    # If no match found, return an empty list
    if first_occurrence_idx == -1:
        print(f"No restaurants found serving {cuisine_to_search} cuisine.")
        return []
        
    # Scan to the left and right of the first occurrence to collect all matching restaurants
    left, right = first_occurrence_idx, first_occurrence_idx
    while left >= 0 and sorted_list[left]['cuisine'] == cuisine_to_search:
        filtered_list.append(sorted_list[left])
        left -= 1
    while right < len(sorted_list) and sorted_list[right]['cuisine'] == cuisine_to_search:
        if right != first_occurrence_idx:  # Avoid adding the first occurrence twice
            filtered_list.append(sorted_list[right])
        right += 1

    # Display the search results
    display_search_results(filtered_list, cuisine_to_search)
    
    return filtered_list  # Return the filtered list at the end

def display_search_results(filtered_list, cuisine_to_search):
    """Display the search results, or indicate that no matches were found."""
    if not filtered_list:
        print(f"No restaurants found serving {cuisine_to_search} cuisine.")
        return

    print(f"Restaurants serving {cuisine_to_search} cuisine:")
    for i, restaurant in enumerate(filtered_list, 1):
        print(f"{i}. {restaurant['name']} ({restaurant['cuisine']})")
        print(f"   Location: {restaurant['location']}")
        print(f"   Rating: {restaurant['rating']}")
        print("   ---")

def collect_matching_cuisines(result, sorted_list, cuisine_to_search):
    """
    Collects all matching cuisines from the sorted list based on the binary search result.
    """
    matching_cuisines = []
    
    # Go left and right from the found index to collect all matching cuisines
    left, right = result, result
    while left >= 0 and sorted_list[left]['cuisine'] == cuisine_to_search:
        matching_cuisines.append(sorted_list[left])
        left -= 1
    
    while right < len(sorted_list) and sorted_list[right]['cuisine'] == cuisine_to_search:
        if sorted_list[right] not in matching_cuisines:  # Avoid duplicates
            matching_cuisines.append(sorted_list[right])
        right += 1
    
    return matching_cuisines

def get_valid_choice(prompt, min_value, max_value):
    """
    Get a valid integer input from the user within a specified range.
    """
    while True:
        try:
            choice = int(input(prompt))
            if min_value <= choice <= max_value:
                return choice
            else:
                print(f"Invalid choice. Must be between {min_value} and {max_value}.")
        except ValueError:
            print("Please enter a valid number.")

def get_valid_float(prompt, min_value, max_value):
    """
    Get a valid float input from the user within a specified range.
    """
    try:
        value = float(input(prompt))
        if min_value <= value <= max_value:
            return value
        else:
            print(f"Invalid input. Must be between {min_value} and {max_value}.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def capture_and_add_review(restaurant):
    """
    Captures a review and adds it to the given restaurant.
    """
    rating = get_valid_float("Your rating (1-5): ", 1, 5)
    if rating is not None:
        review_text = input("Your review: ")
        sanitized_review = sanitize_text(review_text)
        new_review = {"rating": rating, "text": sanitized_review}
        restaurant['reviews'].append(new_review)
        restaurant['rating'] = update_average_rating(restaurant)

def save_to_json(data, file_path):
    """Save updated restaurant data back to the JSON file."""

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def sanitize_text(text):
    """Sanitize user input text by removing special characters and stripping leading/trailing whitespaces"""
    
    # Remove any character that is not a word character or a space
    text = re.sub(r'[^\w\s,.!?-]', '', text)
    
    # Remove leading and trailing whitespaces
    text = text.strip()

    return text