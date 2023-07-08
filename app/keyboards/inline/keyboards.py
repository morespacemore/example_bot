from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from fluentogram import TranslatorRunner

from .callback_data import EditLangCallback


def keyboard_edit_lang(l10n: TranslatorRunner) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text=l10n.button.lang.uk(),
        callback_data=EditLangCallback(lang="uk")
    )
    keyboard.button(
        text=l10n.button.lang.ru(),
        callback_data=EditLangCallback(lang="ru")
    )

    return keyboard.as_markup()
