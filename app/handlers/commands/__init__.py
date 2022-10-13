from aiogram import Router


def setup_commands_routers() -> Router:
    from . import help, start

    router = Router()

    router.include_router(start.router)
    router.include_router(help.router)

    return router
