import time
import logging

class SessionKeeper:
    def __init__(self, session_timeout=300):
        self.session_timeout = session_timeout
        self.last_active = time.time()
        self.is_active = True
        self.logger = logging.getLogger(__name__)

    def update_activity(self):
        self.last_active = time.time()
        self.logger.info('Session activity updated.')

    def check_session(self):
        if time.time() - self.last_active > self.session_timeout:
            self.end_session()
        else:
            self.logger.info('Session is still active.')

    def end_session(self):
        self.is_active = False
        self.logger.warning('Session has ended due to timeout.')

    def reset_session(self):
        self.is_active = True
        self.last_active = time.time()
        self.logger.info('Session has been reset.')

    def get_session_status(self):
        return self.is_active

SessionKeeper().update_activity()
