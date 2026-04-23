import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='session_keeper.log', max_bytes=5*1024*1024, backup_count=3):
    logger = logging.getLogger('session_keeper')
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # Creating a directory for logs if it doesn't exist
        os.makedirs('logs', exist_ok=True)
        handler = RotatingFileHandler(os.path.join('logs', log_file), maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

logger = setup_logger()
logger.info('Logger setup complete.')