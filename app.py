import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(current_dir, 'restaurant_data.json')

with open(data_file_path, 'r') as file:
    restaurant_data = json.load(file)


# Print the details of the first restaurant to verify
print(restaurant_data.get("1"))
