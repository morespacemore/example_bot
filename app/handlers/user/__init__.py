from aiogram import Router


def setup_user_routers() -> Router:
    from . import profile

    router = Router()

    router.include_router(profile.router)

    return router
