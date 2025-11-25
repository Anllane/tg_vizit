"""
Выбор языка: /language + callback lang:ru/en
"""

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import language_keyboard, main_menu_keyboard
from app.localization import SUPPORTED_LANGS, t
from app.services import resolve_user_lang, set_user_lang

router = Router()


@router.message(Command("language"))
async def cmd_language(message: Message) -> None:
    lang = resolve_user_lang(message.from_user)
    await message.answer(
        text=t(lang, "language_choose"),
        reply_markup=language_keyboard(lang),
    )


@router.callback_query(F.data.startswith("lang:"))
async def language_chosen(callback: CallbackQuery) -> None:
    _, lang_code = callback.data.split(":", maxsplit=1)
    if lang_code not in SUPPORTED_LANGS:
        await callback.answer()
        return

    set_user_lang(callback.from_user.id, lang_code)

    text = t(lang_code, "language_saved")
    await callback.message.answer(
        text=text,
        reply_markup=main_menu_keyboard(lang_code),
    )
    await callback.answer()
