from aiogram.filters.callback_data import CallbackData


class EditLangCallback(CallbackData, prefix="edit_lang"):
    lang: str
