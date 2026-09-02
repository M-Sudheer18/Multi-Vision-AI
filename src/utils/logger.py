import logging
import sys
from src.config.settings import settings

# configures a standardized, professional logger
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    # Prevent Duplicate Logs
    if not logger.handlers:
        # set the logging level based on settings
        log_level = logging.DEBUG if settings.DEBUG else logging.INFO
        logger.setLevel(log_level)

        # Direct the Logs to the Terminal
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)

        # Column Aligned Format Logs
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(module)s:%(lineno)d | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        # logs don't propagate up to the root logger and print twice
        logger.propagate = False
    return logger