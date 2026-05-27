import logging
import sys
from typing import Any


class Log:
    @classmethod
    def _log(cls, level: int, message: str, *args: Any, **kwargs: Any) -> None:
        logging.log(level, message, *args, **kwargs)

    @classmethod
    def info(cls, message: str, *args: Any, **kwargs: Any) -> None:
        cls._log(logging.INFO, message, *args, **kwargs)

    @classmethod
    def debug(cls, message: str, *args: Any, **kwargs: Any) -> None:
        cls._log(logging.DEBUG, message, *args, **kwargs)

    @classmethod
    def error(cls, message: str, *args: Any, **kwargs: Any) -> None:
        cls._log(logging.ERROR, message, *args, **kwargs)

    @classmethod
    def init(cls) -> None:
        """
        Initialize logging

        Default logging level is INFO
        Enables DEBUG mode if `-debug` is passed in command-line arguments.
        """
        log_level = logging.INFO

        if "-debug" in sys.argv:
            log_level = logging.DEBUG

        log_format = "%(levelname)s: %(message)s"
        logging.basicConfig(level=log_level, format=log_format)
