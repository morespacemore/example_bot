from cachetools import TTLCache

from app.config import config

throttling_cache = TTLCache(maxsize=10_000, ttl=config.throttling_rate)
