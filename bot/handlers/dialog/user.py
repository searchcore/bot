from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const
from aiogram_dialog import Dialog, DialogManager

from bot.services.integration import LocaleText
from bot.states.user import UserMain


async def get_data(dialog_manager: DialogManager, **kwargs):
    mw_d = dialog_manager.data

    data = dict()
    data['user_name'] = mw_d.get('repo__user').name

    return data


main_window = Window(
    LocaleText('welcome', user='@{user_name}'),
    Button(Const("Useless button"), id="nothing"),
    state=UserMain.SOME_STATE,
    getter=get_data
)

dialog = Dialog(main_window)
