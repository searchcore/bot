from aiogram import Router
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

from bot.services.locale import Locale
from bot.services.database.models import User
from bot.states.user import UserMain

router = Router()


@router.message(commands=['start'])
async def cmd_start(
    message: Message,
    db_user: User,
    dialog_manager: DialogManager,
    locale: Locale,
):
    await dialog_manager.start(
        UserMain.SOME_STATE,
        mode=StartMode.RESET_STACK
    )
