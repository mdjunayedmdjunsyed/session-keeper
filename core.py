import json
import requests

class RobloxDataHandler:
    BASE_URL = 'https://api.roblox.com/'

    @staticmethod
    def fetch_user_data(user_id):
        """Fetch user data from Roblox API by user ID."""
        response = requests.get(f'{RobloxDataHandler.BASE_URL}users/{user_id}')
        if response.status_code != 200:
            raise Exception('Failed to fetch data')
        return response.json()

    @staticmethod
    def fetch_game_data(game_id):
        """Fetch game data from Roblox API by game ID."""
        response = requests.get(f'{RobloxDataHandler.BASE_URL}games/{game_id}/data')
        if response.status_code != 200:
            raise Exception('Failed to fetch game data')
        return response.json()

    @staticmethod
    def get_user_friends(user_id):
        """Fetch friends list for a given user ID."""
        response = requests.get(f'{RobloxDataHandler.BASE_URL}users/{user_id}/friends')
        if response.status_code != 200:
            raise Exception('Failed to fetch friends')
        return response.json()  

    @staticmethod
    def save_data_to_json(data, filename):
        """Save data to a JSON file."""
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)