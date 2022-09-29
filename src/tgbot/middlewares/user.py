from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Update, Message, CallbackQuery

from tgbot.services.repository import Repository
from tgbot.services.repository.models import User


class RegisterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any],
    ) -> Any:
        repo: Repository = data["repo"]

        _u = User(
            id=event.from_user.id,
            name=event.from_user.first_name,
            nickname=event.from_user.username,
            lang=event.from_user.language_code
        )

        if not repo.is_user_exists(_u):
            repo.create_user(_u)

        data['repo__user'] = _u

        return await handler(event, data)
