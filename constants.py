class Constants:
    ROBLOX_API_URL = 'https://api.roblox.com/'
    SESSION_TIMEOUT = 3600  # seconds
    MAX_RETRIES = 5
    USER_AGENT = 'SessionKeeper/1.0'
    HEADERS = {
        'User-Agent': USER_AGENT,
        'Accept': 'application/json'
    }
    ASSETS_FOLDER = './assets/'
    LOG_FILE = './logs/session_keeper.log'
    ERROR_MESSAGES = {
        'session_expired': 'Session has expired, please login again.',
        'invalid_credentials': 'Invalid username or password.',
        'connection_error': 'Failed to connect to Roblox API.'
    }
