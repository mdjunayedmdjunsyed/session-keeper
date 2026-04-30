import re

def validate_username(username):
    if not isinstance(username, str) or not username:
        raise ValueError('Username must be a non-empty string.')
    if len(username) < 3 or len(username) > 20:
        raise ValueError('Username must be between 3 and 20 characters.')
    if not re.match('^[a-zA-Z0-9_]*$', username):
        raise ValueError('Username can only contain letters, numbers, and underscores.')
    return True

def validate_session_duration(duration):
    if not isinstance(duration, int) or duration <= 0:
        raise ValueError('Session duration must be a positive integer.')
    return True

class SessionKeeper:
    def __init__(self, username, session_duration):
        validate_username(username)
        validate_session_duration(session_duration)
        self.username = username
        self.session_duration = session_duration
        self.active = False

    def start_session(self):
        self.active = True
        print(f'Session for {self.username} started for {self.session_duration} minutes.')

    def end_session(self):
        self.active = False
        print(f'Session for {self.username} ended.')
