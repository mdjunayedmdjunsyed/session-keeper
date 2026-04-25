class SessionError(Exception):
    """Exception raised for session-related errors."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class UserNotFoundError(SessionError):
    """Exception raised when a user is not found in the session."""
    def __init__(self, user_id: str) -> None:
        message = f'User with ID {user_id} not found in the session.'
        super().__init__(message)

class SessionExpiredError(SessionError):
    """Exception raised when a session has expired."""
    def __init__(self, session_id: str) -> None:
        message = f'Session with ID {session_id} has expired.'
        super().__init__(message)

class InvalidSessionError(SessionError):
    """Exception raised for invalid session attempts."""
    def __init__(self, session_id: str) -> None:
        message = f'Session with ID {session_id} is invalid.'
        super().__init__(message)
