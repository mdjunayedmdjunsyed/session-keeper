def validate_session_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if not user_input.isalnum():
        raise ValueError('Input must be alphanumeric')
    return True


def main_loop():
    while True:
        user_input = input('Enter session ID: ')
        try:
            validate_session_input(user_input)
            print(f'Session ID is valid: {user_input}')
            # Process the valid session further
        except ValueError as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main_loop()