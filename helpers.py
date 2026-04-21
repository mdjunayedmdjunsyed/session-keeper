from typing import List, Dict, Any


def format_user_data(user_id: int, username: str, attributes: Dict[str, Any]) -> str:
    """
    Formats user data for display.

    Args:
        user_id (int): The ID of the user.
        username (str): The username of the user.
        attributes (Dict[str, Any]): A dictionary of user attributes.

    Returns:
        str: A formatted string representing the user's information.
    """
    attributes_str = ', '.join(f'{key}: {value}' for key, value in attributes.items())
    return f'User [{user_id}] - {username} | Attributes: {attributes_str}'


def filter_users(users: List[Dict[str, Any]], min_age: int) -> List[Dict[str, Any]]:
    """
    Filters users by minimum age.

    Args:
        users (List[Dict[str, Any]]): A list of user dictionaries.
        min_age (int): The minimum age for users to be included.

    Returns:
        List[Dict[str, Any]]: A list of users who meet the age criteria.
    """
    return [user for user in users if user.get('age', 0) >= min_age]


def extract_usernames(users: List[Dict[str, Any]]) -> List[str]:
    """
    Extracts usernames from a list of user dictionaries.

    Args:
        users (List[Dict[str, Any]]): A list of user dictionaries.

    Returns:
        List[str]: A list of usernames.
    """
    return [user['username'] for user in users if 'username' in user]
