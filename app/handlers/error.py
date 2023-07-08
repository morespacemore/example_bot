import logging

from aiogram import Bot, Router
from aiogram.types import ErrorEvent, FSInputFile

from app.config import config

router = Router()


@router.errors()
async def error_handler(event: ErrorEvent, bot: Bot):
    logging.error("Exception: %r. Update: %r", event.exception, event.update)

    await bot.send_document(
        chat_id=config.admin_id, document=FSInputFile("journal.log"),
        caption='An error was detected, more detailed information in the log.'
    )
