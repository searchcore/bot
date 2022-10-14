from pathlib import Path
from typing import (
    Optional,
)

from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator


class LocaleLoader:
    def __init__(self, locales_folder: Path):
        self.locales_folder = locales_folder

    def get_content(self, locale: str) -> Optional[str]:
        with open(
            self.locales_folder / f"{locale}.ftl",
            "r",
            encoding='utf-8'
        ) as f:
            return f.read()


class Locale(FluentTranslator):
    """Facade for l10n, i18n and translation.
    Uses FluentTranslator at backend."""
    pass


class Localizator():
    """Pool of Locale objects."""
    def __init__(self, loader, locales_map: dict, default_locale='ru'):
        self.loader = loader
        self._map = locales_map
        self.default_locale = default_locale

        translators = []

        for lang in locales_map.keys():
            trans = FluentTranslator(
                lang,
                translator=FluentBundle.from_string(
                    lang,
                    self.loader.get_content(lang),
                    use_isolating=False,
                )
            )

            translators.append(trans)

        self.hub = TranslatorHub(
            locales_map,
            translators=translators,
            root_locale=default_locale,
        )

    def get_by_locale(self, locale: str) -> Locale:
        if locale not in self._map:
            return self.hub.get_translator_by_locale(
                self.default_locale
            )
        return self.hub.get_translator_by_locale(locale)
