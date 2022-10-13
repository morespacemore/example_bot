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
from app.middlewares import L10nMiddleware, ThrottlingMiddleware
from app.models import __beanie_models__
from app.utils.commands import set_commands
from app.utils.fluent import setup_fluent
from app.utils.logger import setup_logger


async def main():
    setup_logger("WARNING")

    locales = Path(__file__).parent.joinpath("locales")
    l10n = setup_fluent(locales)

    client = AsyncIOMotorClient(config.mongodb_dsn)

    await init_beanie(
        database=client.example_bot,
        document_models=__beanie_models__
    )

    bot = Bot(token=config.bot_token, parse_mode="HTML")

    if not config.redis_dsn:
        dp = Dispatcher(storage=MemoryStorage())
    else:
        dp = Dispatcher(storage=RedisStorage.from_url(config.redis_dsn))

    dp.message.filter(F.chat.type == "private")

    dp.message.middleware(ThrottlingMiddleware())
    dp.message.middleware(L10nMiddleware(l10n))
    dp.callback_query.middleware(L10nMiddleware(l10n))

    dp.include_router(setup_commands_routers())
    dp.include_router(setup_user_routers())
    dp.include_router(error.router)

    await set_commands(bot)
    user = await bot.get_me()

    logging.warning("Start bot")
    await bot.send_message(config.admin_id, "Бот перезапущен 📡")

    try:
        logging.warning(f"Run polling for bot @{user.username}")
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        client.close()
        await bot.session.close()


asyncio.run(main())
