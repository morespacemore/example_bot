from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from fluentogram import TranslatorHub

from app.models import User


class L10nMiddleware(BaseMiddleware):
    def __init__(self, l10n: TranslatorHub) -> None:
        self.l10n = l10n

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user_data = await User.by_user_id(event.from_user.id)

        if user_data is None or user_data.lang is None:
            lang = event.from_user.language_code
        else:
            lang = user_data.lang

        data["fluent"] = self.l10n
        data["l10n"] = self.l10n.get_translator_by_locale(lang)

        return await handler(event, data)
