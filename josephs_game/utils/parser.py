import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Load location data
location_data = load_data('path/to/location_data.json')
