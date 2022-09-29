from aiogram_dialog import DialogManager
from tgbot.services.locale import Locale

from aiogram_dialog.widgets.text import Text
from aiogram_dialog.widgets.when import (
    WhenCondition,
)


class LocaleText(Text):
    def __init__(
        self,
        i18n_var_name: str,
        when: WhenCondition = None,
        localizator_name='locale',
        **kwargs,
    ):
        super().__init__(when=when)
        self.v_name = i18n_var_name
        self._kwargs = kwargs
        self._l_name = localizator_name

    async def _render_text(
            self, data: dict, manager: DialogManager,
    ) -> str:
        mw_d = manager.data
        locale: Locale = mw_d.get(self._l_name)

        for k, v in self._kwargs.items():
            try:
                self._kwargs[k] = v.format_map(data)
            except KeyError:
                pass

        return locale.get(self.v_name, **self._kwargs)
