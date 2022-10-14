from aiogram import Router
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

from bot.services.locale import Locale
from bot.services.repository.user import User
from bot.states.user import UserMain

router = Router()


@router.message(commands=['start'])
async def cmd_start(
    message: Message,
    repo__user: User,
    dialog_manager: DialogManager,
    locale: Locale,
):
    await dialog_manager.start(
        UserMain.SOME_STATE,
        data=locale,
        mode=StartMode.RESET_STACK
    )
