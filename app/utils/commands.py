from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats
from fluentogram import TranslatorHub


async def set_default_commands(bot: Bot, fluent: TranslatorHub) -> None:
    l10n = fluent.get_translator_by_locale("ru")

    commands = [
        BotCommand(command="start", description=l10n.command.start()),
        BotCommand(command="help", description=l10n.command.help()),
    ]
    await bot.set_my_commands(commands, BotCommandScopeAllPrivateChats())
