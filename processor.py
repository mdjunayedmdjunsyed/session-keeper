import json
import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Log HTTP errors
    except requests.exceptions.RequestException as req_err:
        print(f'Request error occurred: {req_err}')  # Log request errors
    return None


def process_user_data(user_data):
    if not user_data:
        return 'No user data available'
    processed_data = {
        'username': user_data.get('username', 'Unknown'),
        'avatar_url': user_data.get('avatarUrl', ''),
        'status': 'active' if user_data.get('isActive', False) else 'inactive'
    }
    return json.dumps(processed_data)


def save_user_data_to_file(user_data, filename):
    with open(filename, 'w') as file:
        json.dump(user_data, file)


def load_user_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error loading user data: {e}')  # Error handling
        return None
