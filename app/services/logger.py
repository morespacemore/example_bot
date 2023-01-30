import logging
from typing import Union


def setup_logger(level: Union[int, str]) -> None:
    logging.basicConfig(
        level=logging.getLevelName(level),
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(filename="journal.log", mode="a", encoding="utf-8")
        ],
        format="%(asctime)s | %(levelname)s | %(name)s:%(funcName)s:%(lineno)d - %(message)s"
    )
