from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject
from fluentogram import TranslatorHub

from app.models import User


class L10nMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        from_user: types.User = event.from_user
        fluent: TranslatorHub = data["fluent"]

        user_data = await User.by_user_id(from_user.id) or await User.set_user(from_user)
        lang = user_data.lang or from_user.language_code

        data["l10n"] = fluent.get_translator_by_locale(lang)
        return await handler(event, data)
