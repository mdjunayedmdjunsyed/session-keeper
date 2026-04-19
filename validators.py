def is_valid_username(username):
    if not (3 <= len(username) <= 20):
        return False
    if not username.isalnum():
        return False
    return True


def is_valid_password(password):
    if len(password) < 6:
        return False
    if len(password) > 20:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    return True


def is_valid_email(email):
    import re
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.match(email_regex, email) is not None


def is_valid_age(age):
    return isinstance(age, int) and 13 <= age <= 100


def are_valid_inputs(username, password, email, age):
    return (is_valid_username(username) and
            is_valid_password(password) and
            is_valid_email(email) and
            is_valid_age(age))