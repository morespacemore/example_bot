from aiogram import Router


def setup_user_routers() -> Router:
    from . import user_data

    router = Router()

    router.include_router(user_data.router)

    return router
