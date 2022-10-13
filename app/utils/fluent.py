from pathlib import Path

from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub


def setup_fluent(locales: Path) -> TranslatorHub:
    return TranslatorHub(
        locales_map={
            "ru": ("ru", "uk"),
            "uk": ("uk", "ru")
        },
        translators=[
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale="ru", use_isolating=False,
                    filenames=[str(path) for path in locales.joinpath("ru").glob("*.ftl")]
                )
            ),
            FluentTranslator(
                locale="uk",
                translator=FluentBundle.from_files(
                    locale="uk", use_isolating=False,
                    filenames=[str(path) for path in locales.joinpath("uk").glob("*.ftl")]
                )
            )
        ],
        root_locale="ru"
    )
