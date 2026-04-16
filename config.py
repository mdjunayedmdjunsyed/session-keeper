import json
import os

DEFAULT_CONFIG = {
    'username': 'guest',
    'session_timeout': 300,
    'auto_save': True
}

def load_config(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
            return {**DEFAULT_CONFIG, **config}
    return DEFAULT_CONFIG

if __name__ == '__main__':
    config = load_config('config.json')
    print(config)