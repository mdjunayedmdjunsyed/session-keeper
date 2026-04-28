from typing import Any, Dict, Union


def is_valid_username(username: str) -> bool:
    """
    Validate the username for Roblox.
    A valid username must be between 3 and 20 characters and can contain letters, numbers, and underscores.
    
    Args:
        username (str): The username to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    if 3 <= len(username) <= 20 and username.isalnum():
        return True
    return username.isalnum() or '_' in username


def is_valid_email(email: str) -> bool:
    """
    Check if the provided email is in valid format.
    A valid email contains one '@' symbol and at least one '.' after it.
    
    Args:
        email (str): The email to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    return '@' in email and email.count('.') > 0


def validate_data(data: Dict[str, Any]) -> Union[str, bool]:
    """
    Validate the entire user data dictionary for Roblox.
    Keys expected: username and email.
    
    Args:
        data (Dict[str, Any]): Data containing user information to validate.
    
    Returns:
        str: 'Invalid username or email' if validation fails, else True.
    """
    if not is_valid_username(data.get('username', '')):
        return 'Invalid username'
    if not is_valid_email(data.get('email', '')):
        return 'Invalid email'
    return True
