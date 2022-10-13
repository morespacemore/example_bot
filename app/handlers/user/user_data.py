from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from fluentogram import TranslatorRunner

from app.models import User

router = Router()


@router.message(Text(["👤 Профиль", "👤 Профіль"]))
async def profile(msg: Message, state: FSMContext, l10n: TranslatorRunner):
    await state.clear()

    data = await User.set_user(msg.from_user)
    await msg.answer(l10n.user.profile(id=data.user_id, name=data.name, username=str(data.username)))
