from utils import sanitize_text, compare_by, display_restaurants, load_and_convert_data_to_list, update_average_rating, update_restaurant_data, save_to_json
from sorts import quicksort


def main_menu():
    """Display the main menu and handle user input."""

    while True:
        # Print the available options
        print("Welcome to the Restaurant Recommendation Engine!")
        print("1. View Recommendations")
        print("2. Add a Review")
        print("3. Search Restaurants")
        print("4. Exit")

        # Capture the user's choice and validate it
        try:
            choice = int(input("Your choice: ")) # Capture user choice for menu option.
            if choice in [1, 2, 3, 4]:
                # Process the user's choice
                if choice == 1:
                    view_recommendations()
                elif choice == 2:
                    add_review()
                elif choice == 3:
                    search_restaurants()
                else:
                    print("Thank you for using the Restaurant Recommendation Engine. Goodbye!")
                    exit()
                break
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError:
            print("\nPlease enter a valid number.")

def view_recommendations():
    """Display recommendations based on selected criteria."""

    # Map user choice to sorting criteria
    criteria_map = {
        1: "rating",
        2: "cuisine",
        3: "location"
    }
    while True:
        # Present sorting options to the user
        print("Choose the basis for recommendations:")
        print("1. By Rating")
        print("2. By Cuisine")
        print("3. By Location")
        try:
            # Capture and validate user choice
            choice = int(input("Your choice: "))
            if choice in criteria_map.keys():
                # Determine the criterion for sorting
                criterion = criteria_map[choice]

                # Define comparison function with 'criterion' as a default argument
                def comparison_function(x, y, criterion=criterion):
                    if criterion == "rating":
                        return not compare_by(x, y, criterion)
                    return compare_by(x, y, criterion)

                # Sort the restaurant list based on the chosen criterion.   
                sorted_list = quicksort(restaurant_list, 0, len(restaurant_list) - 1, comparison_function)

                # Display sorted list
                print(f"Top restaurants by {criterion}:")
                display_restaurants(sorted_list) # Display the sorted list of restaurants
                post_recommendation_menu()
                break
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError:
            print("\nPlease enter a valid number.")

def post_recommendation_menu():
    """Handle post-recommendation actions like going back to the main menu or adding a review."""

    while True:
        print("What would you like to do next?")
        print("1. Go back to main menu")
        print("2. Add a review for a listed restaurant")
        print("3. Exit")
        
        try:
            choice = int(input("Your choice: "))
            
            if choice == 1:
                # Call the function that displays the main menu
                main_menu()
                break
            elif choice == 2:
                # Call the function to add a review
                add_review()
                break
            elif choice == 3:
                print("Thank you for using the Restaurant Recommendation Engine. Goodbye!")
                exit()
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError:
            print("\nPlease enter a valid number.")

def add_review():
    """Add a review to a selected restaurant and update its rating."""

    while True:  # Loop to keep asking for a valid restaurant choice
        try:
            choice = int(input("Choose a restaurant to review: ")) # Capture the user's choice for the restaurant to review.
            if 1 <= choice <= len(restaurant_list):
                restaurant = restaurant_list[choice - 1]
                break  # Exit the loop as a valid restaurant has been chosen
            else:
                print("\nInvalid choice.")
        except ValueError:
            print("\nPlease enter a valid number.")
    try:
        rating = float(input("Your rating (1-5): ")) # Capture the user's rating.
        if 1 <= rating <= 5:
            review_text = input("Your review: ")
            sanitized_review = sanitize_text(review_text)
            new_review = {"rating": rating, "text": sanitized_review}
            restaurant['reviews'].append(new_review)
        else:
            print("\nInvalid rating. Must be between 1 and 5.")
            return
    except ValueError:
        print("\nPlease enter a valid rating.")
        return

    restaurant['rating'] = update_average_rating(restaurant)
    update_restaurant_data(restaurant, restaurant_data)
    save_to_json(restaurant_data, data_file_path)  # Save the updated data back to JSON file

def search_restaurants():
    '''
    Implement search by name, cuisine, or location.
    Extend Binary Search to include search by reviews,
    like finding all restaurants with reviews containing the word "excellent".
    '''
    pass


if __name__ == "__main__":
    restaurant_list, restaurant_data, data_file_path = load_and_convert_data_to_list()

    if restaurant_list:
        main_menu()
    else:
        print("Program terminated due to data loading failure.")
