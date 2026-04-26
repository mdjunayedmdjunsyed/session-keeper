import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='session_keeper.log', max_size=5 * 1024 * 1024, backup_count=3):
    logger = logging.getLogger('session_keeper')
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info('Logger setup complete')
    return logger

# Example usage: 
# if __name__ == '__main__':
#     log = setup_logger()
#     log.info('This is an example log message.')