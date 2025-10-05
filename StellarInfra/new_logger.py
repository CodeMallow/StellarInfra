import sys
import time
import logging

start_time = 0

def get_logger(file_path, logger_name,  console_level=logging.INFO, file_level=logging.DEBUG):
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
    global start_time
    start_time = time.time()
    return logger

class SecondsFormatter(logging.Formatter):
    "from chatGPT"
    def format(self, record):
        global start_time
        now_time = time.time()
        # add relative seconds field
        record.relativeSeconds = now_time - start_time
        return super().format(record)
    

def set_logger_time(logger: logging.Logger, mode:str):
    if mode == 'abs':
        new_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    else:
        new_formatter = SecondsFormatter(
            '%(relativeSeconds).3f - %(name)s - %(levelname)s - %(message)s',
        )
    for handler in logger.handlers:
        handler.setFormatter(new_formatter)