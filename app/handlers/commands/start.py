from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from fluentogram import TranslatorHub, TranslatorRunner

from app.keyboards.inline import EditLangCallback, keyboard_edit_lang
from app.keyboards.reply import keyboard_main_menu
from app.models import User
from app.states import EditLang

router = Router()


@router.message(Command("start"))
async def bot_start(msg: Message, state: FSMContext, l10n: TranslatorRunner):
    await state.clear()
    data = await User.set_user(msg.from_user)

    if data.lang is None:
        await state.set_state(EditLang.get_lang)
        await msg.answer(l10n.edit.lang.choose(), reply_markup=keyboard_edit_lang(l10n))
    else:
        await msg.answer(l10n.bot.welcome_message(), reply_markup=keyboard_main_menu(l10n))


@router.callback_query(EditLang.get_lang, EditLangCallback.filter())
async def edit_lang(
    call: CallbackQuery, state: FSMContext, callback_data: EditLangCallback, fluent: TranslatorHub
):
    await state.clear()
    l10n = fluent.get_translator_by_locale(callback_data.lang)

    data = await User.set_user(call.from_user, lang=callback_data.lang)
    await call.message.delete()

    await call.message.answer(l10n.bot.welcome_message(), reply_markup=keyboard_main_menu(l10n))
    await call.answer()
