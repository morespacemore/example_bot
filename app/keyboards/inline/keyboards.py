from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from fluentogram import TranslatorRunner

from app.keyboards.inline.callback_data import EditLangCallback


def keyboard_edit_lang(l10n: TranslatorRunner) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text=l10n.button.lang.ru.true(),
        callback_data=EditLangCallback(lang="ru")
    )
    keyboard.button(
        text=l10n.button.lang.uk.true(),
        callback_data=EditLangCallback(lang="uk")
    )

    return keyboard.as_markup()
