"""
Клавиатуры для админ-панели.
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.localization import t


def admin_language_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                text=t("ru", "btn_lang_ru"),
                callback_data="admin:lang:ru",
            )
        ],
        [
            InlineKeyboardButton(
                text=t("en", "btn_lang_en"),
                callback_data="admin:lang:en",
            )
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def admin_sections_keyboard(lang_to_edit: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                text="Обо мне",
                callback_data=f"admin:edit:{lang_to_edit}:about",
            ),
            InlineKeyboardButton(
                text="Услуги",
                callback_data=f"admin:edit:{lang_to_edit}:services",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Контакты",
                callback_data=f"admin:edit:{lang_to_edit}:contacts",
            ),
            InlineKeyboardButton(
                text="Соцсети",
                callback_data=f"admin:edit:{lang_to_edit}:socials",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Сайт",
                callback_data=f"admin:edit:{lang_to_edit}:website",
            ),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
