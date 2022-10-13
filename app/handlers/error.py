import logging

from aiogram import Router
from aiogram.types.error_event import ErrorEvent

router = Router()


@router.errors()
async def error_handler(exception: ErrorEvent):
    logging.error(f'{exception.exception}. Update: {exception.update.dict()}')
