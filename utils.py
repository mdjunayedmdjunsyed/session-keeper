import json
import os

def load_json(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} not found")
    with open(file_path, 'r') as f:
        return json.load(f)


def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def is_valid_user(user):
    return isinstance(user, dict) and 'username' in user and 'id' in user


def format_username(username):
    if not isinstance(username, str):
        raise ValueError("Username must be a string")
    return username.strip().lower()


def create_user_dict(username, user_id):
    formatted_username = format_username(username)
    return { 'username': formatted_username, 'id': user_id }