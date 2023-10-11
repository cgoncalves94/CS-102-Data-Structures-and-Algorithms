import json
import os
from sorts import quicksort

current_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(current_dir, 'restaurant_data.json')

# Load restaurant data from JSON file into a dictionary
with open(data_file_path, 'r') as file:
    restaurant_data = json.load(file)
    
# Convert restaurant data to a list for easier sorting and searching
restaurant_list = list(restaurant_data.values())

def main_menu():
    # Display the main menu and capture user choice
    while True:
        print("Welcome to the Restaurant Recommendation Engine!")
        print("Please choose an option:")
        print("1. View Recommendations")
        print("2. Add Review")
        print("3. Search")
        print("4. Exit")
        choice = input("Your choice: ")
        
        if choice in ["1", "2", "3", "4"]:
            break  # Exit the loop if a valid option is chosen
        else:
            print("Invalid choice. Please try again.")
        
    if choice == "1":
        # Option to view restaurant recommendations
        view_recommendations()
    elif choice == "2":
        # Option to add a restaurant review
        add_review()
    elif choice == "3":
        # Option to search a restaurants based on a filter
        search_restaurants()
    elif choice == "4":
        # Exit application
        exit_app()

# Function to compare two restaurants based on a given criteria (e.g., rating, cuisine, location)
def compare_by(restaurant1, restaurant2, criteria):
    return restaurant1[criteria] > restaurant2[criteria]

# Function to display a list of restaurants in a readable format
# Enumerate through the list of restaurants and print details for each
def display_restaurants(restaurants):
    for i, restaurant in enumerate(restaurants, 1):
        print(f"{i}. {restaurant['name']} ({restaurant['cuisine']})")
        print(f"   Location: {restaurant['location']}")
        print(f"   Rating: {restaurant['rating']}")
        print("   ---")


def view_recommendations():
    while True:
        print("Choose the basis for sorting:")
        print("1. By Rating")
        print("2. By Cuisine")
        print("3. By Location")
        choice = input("Your choice: ")

        if choice in ["1", "2", "3"]:
            break  # Exit the loop if a valid option is chosen
        else:
            print("Invalid choice. Please try again.")
    
    if choice == "1":
        # Sort by rating 
        sorted_by_rating = quicksort(restaurant_list, 0, len(restaurant_list) - 1, lambda x, y: not compare_by(x, y, "rating"))
        print("Top restaurants by rating:")
        print(display_restaurants(sorted_by_rating))
        
    elif choice == "2":
        # Sort by cuisine alphabetically 
        sorted_by_cuisine = quicksort(restaurant_list, 0, len(restaurant_list) - 1, lambda x, y: compare_by(x, y, "cuisine"))
        print("Top restaurants by cuisine:")
        print(display_restaurants(sorted_by_cuisine))
        
    elif choice == "3":
        # Sort by location alphabetically 
        sorted_by_location = quicksort(restaurant_list, 0, len(restaurant_list) - 1, lambda x, y: compare_by(x, y, "location"))
        print("Top restaurants by ocation:")
        print(display_restaurants(sorted_by_location))



def add_review():
    '''
    Enable users to add reviews for restaurants.
    Update the restaurant's rating based on the new review.
    '''
    pass

def search_restaurants():
    '''
    Implement search by name, cuisine, or location.
    Extend Binary Search to include search by reviews,
    like finding all restaurants with reviews containing the word "excellent".
    '''
    pass

def exit_app():
    #exit
    pass


main_menu()