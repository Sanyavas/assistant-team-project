import logging

log_format = (
    "%(asctime)s [%(levelname)s] - %(name)s - %(funcName)15s:%(lineno)d - %(message)s"
)

file_handler = logging.FileHandler("data/application.logs")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(log_format))

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)
stream_handler.setFormatter(logging.Formatter(log_format))


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger
