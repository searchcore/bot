from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Update, Message, CallbackQuery

from bot.services.database.models import User


class RegisterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any],
    ) -> Any:
        session = data["session"]

        _u = User(
            id=event.from_user.id,
            name=event.from_user.first_name,
            nickname=event.from_user.username,
            lang=event.from_user.language_code
        )

        if not User.is_exists(session, _u):
            User.create(session, _u)

        data['db_user'] = _u

        return await handler(event, data)
