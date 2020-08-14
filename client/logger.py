import os
import sys
import logging
    

def setup_logger(log_name, log_file, *, log_level=logging.INFO, log_mod='w'):
    """To setup manny loggers"""
    log_format = '[%(asctime)s] %(levelname)s | %(message)s'
    logging.basicConfig(level=log_level, format=log_format)
    logger = logging.getLogger(log_name)

    # Save logs to file
    log_file = f'{os.path.dirname(os.path.abspath(__file__))}/{log_file}'
    log_file = logging.FileHandler(log_file, log_mod)
    log_file.setFormatter(logging.Formatter(log_format))
    log_file.setLevel(log_level)
    logger.addHandler(log_file)

    return logger
