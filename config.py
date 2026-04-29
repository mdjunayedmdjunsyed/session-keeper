import json
import os

DEFAULT_CONFIG = {
    'game_id': 123456,
    'session_timeout': 300,
    'max_players': 10,
    'log_level': 'INFO'
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as f:
                user_config = json.load(f)
            return {**DEFAULT_CONFIG, **user_config}
        return DEFAULT_CONFIG

    def get(self, key, default=None):
        return self.config.get(key, default)

    def save(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.config)