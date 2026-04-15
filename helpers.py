import json
from typing import Any, Dict, Union

class RobloxDataHandler:
    @staticmethod
    def load_data(file_path: str) -> Union[Dict[str, Any], None]:
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f'Error loading data: {e}')
            return None

    @staticmethod
    def save_data(file_path: str, data: Dict[str, Any]) -> bool:
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            return True
        except IOError as e:
            print(f'Error saving data: {e}')
            return False

    @staticmethod
    def update_data(file_path: str, updates: Dict[str, Any]) -> bool:
        data = RobloxDataHandler.load_data(file_path)
        if data is None:
            return False
        data.update(updates)
        return RobloxDataHandler.save_data(file_path, data)

    @staticmethod
    def get_value(data: Dict[str, Any], key: str, default: Any = None) -> Any:
        return data.get(key, default)

    @staticmethod
    def set_value(data: Dict[str, Any], key: str, value: Any) -> None:
        data[key] = value
