from typing import Any, Optional

from aiogram import html, types
from beanie import Document, Indexed


class User(Document):
    user_id: Indexed(int)
    name: Optional[str] = None
    username: Optional[str] = None

    class Settings:
        name = "users"

    @classmethod
    async def set_user(cls, user: types.User, **kwargs: Any) -> "User":
        data = await cls.by_user_id(user.id)

        if data is None:
            if kwargs.get("name") is None:
                kwargs["name"] = html.quote(user.first_name)

            data = cls(user_id=user.id, username=user.username, **kwargs)
            await data.create()
        else:
            await data.set({cls.username: user.username, **kwargs})

        return data

    @classmethod
    async def by_user_id(cls, user_id: int) -> "User":
        return await cls.find_one(cls.user_id == user_id)

    @classmethod
    async def by_name(cls, name: str) -> "User":
        return await cls.find_one(cls.name == name)

    @classmethod
    async def by_username(cls, username: str) -> "User":
        return await cls.find_one(cls.username == username)
