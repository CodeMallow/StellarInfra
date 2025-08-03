import sys
import logging


def get_logger(file_path, logger_name,  console_level=logging.DEBUG, file_level=logging.INFO):
    #adopt from chat-gpt

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # master level: allow all through to handlers
    logger.handlers.clear()  # prevent duplicate handlers on re-run

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    file_handler = logging.FileHandler(file_path)
    file_handler.setLevel(file_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger