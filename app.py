from utils import get_valid_choice, capture_and_add_review, handle_cuisine_search, compare_by, display_restaurants, load_and_convert_data_to_list, update_restaurant_data, save_to_json
from sorts import quicksort


def main_menu():
    """Display the main menu and handle user input."""

    while True:
        # Print the available options
        print("\nWelcome to the Restaurant Recommendation Engine!")
        print("1. View Recommendations")
        print("2. Add a Review")
        print("3. Search Restaurants")
        print("4. Exit")

        # Capture the user's choice and validate it
        try: # Using try-except to validate user input is a number
            choice = int(input("Your choice: ")) # Capture user choice for menu option.
            if choice in [1, 2, 3, 4]:
                # Process the user's choice
                if choice == 1: # If choice is 1, view restaurant recommendations
                    view_recommendations()
                elif choice == 2: # If choice is 2, add review
                    add_review()
                elif choice == 3: # If choice is 3, search restaurants
                    search_menu()
                else:
                    print("Thank you for using the Restaurant Recommendation Engine. Goodbye!")
                    exit() # Exit the application

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
        print("\nChoose the basis for recommendations:")
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
                print(f"\nTop restaurants by {criterion}:")
                display_restaurants(sorted_list) # Display the sorted list of restaurants
                post_menu()
                break
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError:
            print("\nPlease enter a valid number.")

def post_menu(restaurants_to_review=None):
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
                add_review(restaurants_to_review)
                break
            elif choice == 3:
                print("Thank you for using the Restaurant Recommendation Engine. Goodbye!")
                exit()
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError:
            print("\nPlease enter a valid number.")

def add_review(restaurants_to_review=None):
    """
    Add a review to a selected restaurant and update its rating.
    """
    if restaurants_to_review is None:
        restaurants_to_review = restaurant_list

    restaurant_choice = get_valid_choice("Choose a restaurant to review: ", 1, len(restaurants_to_review))
    restaurant = restaurants_to_review[restaurant_choice - 1]
    
    capture_and_add_review(restaurant)
    
    update_restaurant_data(restaurant, restaurant_data)
    save_to_json(restaurant_data, data_file_path)

def search_menu():
    """ Displays the search menu and handles the user's choice."""
    while True:
        print("You can search restaurants by:")
        print("1. Cuisine")
        print("2. Go back to main menu")
        
        try:
            choice = int(input("Your choice: "))
            if choice in [1, 2]:
                if choice == 1:
                    filtered_list = handle_cuisine_search(restaurant_list)  # Call the handler function for cuisine search
                    # Assuming search_results contain the filtered list of restaurants
                    post_menu(filtered_list)
                elif choice == 2:
                    main_menu()
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    

if __name__ == "__main__":
    restaurant_list, restaurant_data, data_file_path = load_and_convert_data_to_list()

    if restaurant_list:
        main_menu()
    else:
        print("Program terminated due to data loading failure.")
