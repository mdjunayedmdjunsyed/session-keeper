import robloxapi
from constants import BASE_URL

class SessionKeeper:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = None

    def login(self):
        self.session = robloxapi.login(self.username, self.password)
        return self.session

    def keep_alive(self):
        if self.session:
            response = robloxapi.keep_session_alive(self.session)
            return response
        raise Exception('No active session')

    def logout(self):
        if self.session:
            robloxapi.logout(self.session)
            self.session = None
        else:
            raise Exception('No active session to logout')

if __name__ == '__main__':
    keeper = SessionKeeper('user@example.com', 'password')
    keeper.login()
    keeper.keep_alive()
    keeper.logout()