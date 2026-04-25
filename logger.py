import logging
from logging.handlers import RotatingFileHandler

class LoggerSetup:
    def __init__(self, log_file='app.log', max_bytes=5*1024*1024, backup_count=3):
        self.logger = logging.getLogger('SessionKeeper')
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        self.handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_debug(self, message):
        self.logger.debug(message)

if __name__ == '__main__':
    logger = LoggerSetup()  
    logger.log_info('Logger initialized')
    logger.log_warning('This is a warning message')
    logger.log_error('An error occurred')
    logger.log_debug('Debug information here')