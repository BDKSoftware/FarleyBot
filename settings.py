import os
from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv()

DiscordToken = os.getenv("DISCORD_API_TOKEN")


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s %(asctime)s %(module)-15s: %(message)s "
        },
        "standard": {
            "format": "%(levelname)-10s %(name)-15s: %(message)s "
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.StreamHandler",
        },
        "console2": {
            "level": "WARNING",
            "formatter": "standard",
            "class": "logging.StreamHandler",
        },
        "file": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.FileHandler",
            "filename": "logs/bot.log",
            "mode": "w",
        },

    },
    "loggers": {
        "bot": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "discord": {
            "handlers": ["console2, file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
