import asyncio
import logging

from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram_dialog import DialogRegistry

# Middlewares
from tgbot.middlewares.repo import RepoMiddleware
from tgbot.middlewares.user import RegisterMiddleware
from tgbot.middlewares.locale import LocaleMiddleware

# Routers
from tgbot.handlers.user import router as user_router

# Dialogs
from tgbot.handlers.dialog.user import dialog as user_dialog

# Config
from tgbot.config import BotConfig

# Services
from tgbot.services.locale import (
    Localizator,
    LocaleLoader
)
from tgbot.services.repository.repository import Database

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

BOTFOLDER = Path(__file__).parent


def _configure_fluent(locales_path):
    locales_map = {
        "ru": ("ru",),
    }
    loader = LocaleLoader(
        Path(locales_path),
    )
    return Localizator(loader, locales_map)


async def main():
    logger.warning("Starting bot")

    config = BotConfig(
        _env_file=BOTFOLDER / Path(".env")
    )

    storage = MemoryStorage()

    if config.redis_storage:
        # storage = RedisStorage()
        pass

    bot = Bot(token=config.token)
    dp = Dispatcher(storage=storage)
    database = Database(db_url=config.dsn, echo=config.echo)

    # Router
    reg = DialogRegistry(dp)
    reg.register(user_dialog)

    dp.include_router(user_router)

    fluent = _configure_fluent(config.locales_folder)

    # Middleware
    dp.update.outer_middleware.register(RepoMiddleware(db=database))
    dp.callback_query.outer_middleware.register(RepoMiddleware(db=database))
    dp.message.outer_middleware.register(RegisterMiddleware())
    dp.callback_query.outer_middleware.register(RegisterMiddleware())
    dp.message.outer_middleware.register(LocaleMiddleware(localizator=fluent))
    dp.callback_query.outer_middleware.register(LocaleMiddleware(localizator=fluent))

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await bot.session.close()


def cli():
    """Wrapper for command line, app's entry point"""
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")


if __name__ == '__main__':
    cli()
