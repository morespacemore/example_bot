import logging
from typing import Union

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record) -> None:
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_logger(level: Union[int, str]) -> None:
    logging.basicConfig(
        level=logging.getLevelName(level),
        handlers=[
            InterceptHandler(),
            logging.FileHandler(filename="bot.log", mode="a", encoding="utf-8")
        ],
        format="%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s"
    )
