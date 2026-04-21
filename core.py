import sys

class SessionKeeper:
    def __init__(self):
        self.active_sessions = []

    def start_session(self, session_id):
        if self.validate_input(session_id):
            self.active_sessions.append(session_id)
            print(f'Session {session_id} started.')
        else:
            print(f'Invalid session ID: {session_id}')

    def stop_session(self, session_id):
        if session_id in self.active_sessions:
            self.active_sessions.remove(session_id)
            print(f'Session {session_id} stopped.')
        else:
            print(f'Session {session_id} not found.')

    def validate_input(self, session_id):
        return isinstance(session_id, str) and len(session_id) > 0

    def process_sessions(self, session_ids):
        for session_id in session_ids:
            self.start_session(session_id)

if __name__ == '__main__':
    keeper = SessionKeeper()
    keeper.process_sessions(sys.argv[1:])
