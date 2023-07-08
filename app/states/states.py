from aiogram.fsm.state import State, StatesGroup


class EditLang(StatesGroup):
    get_lang = State()
