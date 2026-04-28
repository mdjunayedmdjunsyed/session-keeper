import json
import requests

class RobloxDataHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_user_data(self, user_id):
        response = requests.get(f'{self.base_url}/users/{user_id}/data')
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to fetch user data')

    def save_data_to_file(self, user_data, filename):
        with open(filename, 'w') as file:
            json.dump(user_data, file)

    def load_data_from_file(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def update_user_data(self, user_id, data):
        response = requests.put(f'{self.base_url}/users/{user_id}/data', json=data)
        return response.status_code == 204

# Example usage:
# handler = RobloxDataHandler('https://api.roblox.com')
# user_data = handler.fetch_user_data(123456)
# handler.save_data_to_file(user_data, 'user_data.json')
# loaded_data = handler.load_data_from_file('user_data.json')
# handler.update_user_data(123456, {'key': 'value'})