"""
Главное меню и выбор языка.
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.localization import t


def main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                text=t(lang, "btn_about"),
                callback_data="menu:about",
            ),
            InlineKeyboardButton(
                text=t(lang, "btn_services"),
                callback_data="menu:services",
            ),
        ],
        [
            InlineKeyboardButton(
                text=t(lang, "btn_contacts"),
                callback_data="menu:contacts",
            ),
            InlineKeyboardButton(
                text=t(lang, "btn_socials"),
                callback_data="menu:socials",
            ),
        ],
        [
            InlineKeyboardButton(
                text=t(lang, "btn_website"),
                callback_data="menu:website",
            ),
            InlineKeyboardButton(
                text=t(lang, "btn_feedback"),
                callback_data="menu:feedback",
            ),
        ],
        [
            InlineKeyboardButton(
                text=t(lang, "btn_language"),
                callback_data="menu:language",
            ),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def language_keyboard(current_lang: str | None = None) -> InlineKeyboardMarkup:
    ru_label = t("ru", "btn_lang_ru")
    en_label = t("en", "btn_lang_en")

    if current_lang == "ru":
        ru_label = "✅ " + ru_label
    elif current_lang == "en":
        en_label = "✅ " + en_label

    keyboard = [
        [
            InlineKeyboardButton(
                text=ru_label,
                callback_data="lang:ru",
            )
        ],
        [
            InlineKeyboardButton(
                text=en_label,
                callback_data="lang:en",
            )
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
