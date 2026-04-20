import logging
import os
from logging.handlers import RotatingFileHandler

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILE = 'session_keeper.log'
MAX_BYTES = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3


def setup_logger():
    logger = logging.getLogger('session_keeper')
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        handler = RotatingFileHandler(LOG_FILE, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

logger = setup_logger()