from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_default_commands(bot: Bot) -> None:
    private_commands = [
        BotCommand(command="start", description="Перезапустить бота"),
        BotCommand(command="help", description="Помощь")
    ]
    await bot.set_my_commands(private_commands, scope=BotCommandScopeAllPrivateChats())
