from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update
from fluentogram import TranslatorHub


class DataMiddleware(BaseMiddleware):
    def __init__(self, fluent: TranslatorHub) -> None:
        self.fluent = fluent

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        data["fluent"] = self.fluent

        return await handler(event, data)
