from typing import Optional

from pydantic import BaseSettings, MongoDsn, RedisDsn


class Settings(BaseSettings):
    database_name: str
    bot_token: str
    mongo_dsn: MongoDsn
    redis_dsn: Optional[RedisDsn]
    bot_id: int
    bot_username: str
    admin_id: int
    admin_username: str
    rate_limit: float = 0.5
    datetime_format: str = "%d.%m.%Y %H:%M"
    timezone: str = "Europe/Moscow"
    short_datetime_format: str = "%d.%m.%Y"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()
