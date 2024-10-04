from logging import Logger, _nameToLevel
import logging
import os

def set_log_level() -> int:
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()

    return _nameToLevel[log_level]


logging.basicConfig(level=set_log_level(), format='%(asctime)s [%(levelname)s, %(name)s]:%(message)s')

def get_logger(name: str) -> Logger:
    """
    Get a logger instance with the specified name.

    Args:
        name (str): The name of the logger.

    Returns:
        Logger: The logger instance.

    """
    file_handler = logging.FileHandler('logs/operator.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s, %(name)s]:%(message)s'))
    stream_handler = logging.StreamHandler()
    logger = logging.getLogger(name)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
