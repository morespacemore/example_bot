from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from fluentogram import TranslatorRunner


def keyboard_main_menu(l10n: TranslatorRunner) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()

    keyboard.button(text=l10n.button.profile())

    return keyboard.as_markup(resize_keyboard=True)
