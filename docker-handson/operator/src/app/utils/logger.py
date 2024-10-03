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
    return logging.getLogger(name)
