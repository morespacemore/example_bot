from typing import Any, Optional

from aiogram import html, types
from beanie import Document, Indexed
from beanie.operators import Set


class User(Document):
    user_id: Indexed(int)
    name: Optional[str] = None
    username: Optional[str] = None
    lang: Optional[str] = None

    class Settings:
        name = "users"

    @classmethod
    async def set_user(cls, user: types.User, **kwargs: Any) -> "User":
        data = await cls.find_one(cls.user_id == user.id)

        if data is None:
            kwargs["name"] = html.quote(user.first_name)

            data = cls(user_id=user.id, username=user.username, **kwargs)
            await data.create()
        else:
            await data.update(Set({cls.username: user.username, **kwargs}))

        return data

    @classmethod
    async def by_user_id(cls, user_id: int) -> Optional["User"]:
        return await cls.find_one(cls.user_id == user_id)

    @classmethod
    async def by_username(cls, username: str) -> Optional["User"]:
        return await cls.find_one(cls.username == username)
