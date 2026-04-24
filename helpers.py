import json
import os

def load_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found: {file_path}")
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

def save_config(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Config saved to {file_path}")

def format_timestamp(timestamp):
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')

def is_valid_user_id(user_id):
    return isinstance(user_id, int) and user_id > 0

def cleanup_data(data):
    if not isinstance(data, list):
        raise ValueError('Expected a list for cleanup')
    return [item for item in data if item is not None and item != '']  

