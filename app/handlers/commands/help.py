from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from fluentogram import TranslatorRunner

from app.config import config

router = Router()


@router.message(Command("help"))
async def bot_help(msg: Message, state: FSMContext, l10n: TranslatorRunner):
    await state.clear()
    await msg.answer(l10n.help(admin_username=config.admin_username))
