import json
import http.client

class RobloxDataHandler:
    BASE_URL = 'https://data.roblox.com'
    
    @staticmethod
    def fetch_data(api_endpoint):
        conn = http.client.HTTPSConnection('data.roblox.com')
        conn.request('GET', api_endpoint)
        response = conn.getresponse()
        return json.loads(response.read())
    
    @staticmethod
    def format_user_data(user_data):
        formatted = {
            'id': user_data['UserId'],
            'name': user_data['Username'],
            'friends_count': user_data['FriendCount'],
            'is_online': user_data['IsOnline']
        }
        return json.dumps(formatted, indent=4)
    
    @classmethod
    def get_user_info(cls, user_id):
        api_endpoint = f'/users/{user_id}'
        user_data = cls.fetch_data(api_endpoint)
        return cls.format_user_data(user_data)

# Example usage
if __name__ == '__main__':
    user_info = RobloxDataHandler.get_user_info(123456)
    print(user_info)