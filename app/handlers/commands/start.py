from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from fluentogram import TranslatorHub, TranslatorRunner

from app.keyboards.inline import EditLangCallback, keyboard_set_lang
from app.keyboards.reply import keyboard_main_menu
from app.models import User

router = Router()


class SetLang(StatesGroup):
    get_lang = State()


@router.message(Command("start"))
async def bot_start(msg: Message, state: FSMContext, l10n: TranslatorRunner):
    await state.clear()

    await User.set_user(msg.from_user)

    await state.set_state(SetLang.get_lang)
    await msg.answer(l10n.lang.set(), reply_markup=keyboard_set_lang(l10n))


@router.callback_query(SetLang.get_lang, EditLangCallback.filter())
async def set_lang(call: CallbackQuery, state: FSMContext, callback_data: EditLangCallback, fluent: TranslatorHub):
    await state.clear()

    data = await User.by_user_id(call.from_user.id)
    await data.set({User.lang: callback_data.lang})

    l10n = fluent.get_translator_by_locale(callback_data.lang)

    await call.message.delete()
    await call.answer()

    await call.message.answer(l10n.bot.welcome_message(), reply_markup=keyboard_main_menu(l10n))
