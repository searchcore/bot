from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Update

from tgbot.services.repository import Database, Repository


class RepoMiddleware(BaseMiddleware):
    def __init__(self, db: Database) -> None:
        self.db = db

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:

        with self.db.new_session() as session:
            data["repo"]: Repository = Repository(session)

            await handler(event, data)

            data["repo"].commit_pending()
