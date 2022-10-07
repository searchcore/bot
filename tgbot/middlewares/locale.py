from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Update, Message, CallbackQuery

from tgbot.services.locale import (
    Localizator,
    Locale
)


class LocaleMiddleware(BaseMiddleware):
    def __init__(self, localizator: Localizator):
        self._loc: Localizator = localizator

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any],
    ) -> Any:

        user_lang = event.from_user.language_code

        _locale: Locale = self._loc.get_by_locale(user_lang)

        data["locale"] = _locale

        return await handler(event, data)
