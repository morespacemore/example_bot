import logging

from aiogram import Router
from aiogram.types import ErrorEvent

router = Router()


@router.errors()
async def error_handler(event: ErrorEvent):
    logging.error("Exception: %r. Update: %r", event.exception, event.update)
