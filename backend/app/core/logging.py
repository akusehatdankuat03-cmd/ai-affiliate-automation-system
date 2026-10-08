import logging
from logging.config import dictConfig

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {"format": "%(asctime)s %(levelname)s %(name)s %(message)s"}
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",
        }
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}

def configure_logging() -> None:
    dictConfig(LOGGING_CONFIG)

logger = logging.getLogger("affiliate_ai")
