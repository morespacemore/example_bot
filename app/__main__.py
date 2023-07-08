import asyncio
import logging
from pathlib import Path

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import config
from app.handlers import error
from app.handlers.commands import setup_commands_routers
from app.handlers.user import setup_user_routers
from app.middlewares import DataMiddleware, L10nMiddleware, ThrottlingMiddleware
from app.models import __beanie_models__
from app.services import setup_fluent, setup_logger
from app.utils.commands import set_default_commands


async def main() -> None:
    setup_logger("WARNING")

    locales = Path(__file__).parent.joinpath("locales")
    fluent = setup_fluent(locales)

    mongodb = AsyncIOMotorClient(config.mongo_dsn)

    await init_beanie(
        database=mongodb[config.database_name],
        allow_index_dropping=True,
        document_models=__beanie_models__
    )

    bot = Bot(token=config.bot_token, parse_mode="HTML")

    if not config.redis_dsn:
        dp = Dispatcher(storage=MemoryStorage())
    else:
        dp = Dispatcher(storage=RedisStorage.from_url(config.redis_dsn))

    dp.message.filter(F.chat.type == "private")
    dp.update.outer_middleware(DataMiddleware(fluent))

    dp.message.middleware(ThrottlingMiddleware())
    dp.message.middleware(L10nMiddleware())
    dp.callback_query.middleware(L10nMiddleware())

    dp.include_router(setup_commands_routers())
    dp.include_router(setup_user_routers())
    dp.include_router(error.router)

    bot_info = await bot.get_me()
    await set_default_commands(bot, fluent)

    logging.warning("Bot startup")
    await bot.send_message(config.admin_id, "⚠️ Bot restarted ⚠️")

    try:
        logging.warning(f"Run polling for bot @{bot_info.username}")
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


asyncio.run(main())
