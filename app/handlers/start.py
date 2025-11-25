"""
/start и /menu
"""

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import PROFILE
from app.keyboards import main_menu_keyboard
from app.localization import t
from app.services import resolve_user_lang

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    lang = resolve_user_lang(message.from_user)

    if lang == "ru":
        header = f"<b>{PROFILE.full_name}</b>\n{PROFILE.title_ru}\n\n"
    else:
        header = f"<b>{PROFILE.full_name}</b>\n{PROFILE.title_en}\n\n"

    text = header + t(lang, "start_welcome")
    await message.answer(text=text, reply_markup=main_menu_keyboard(lang))


@router.message(Command("menu"))
async def cmd_menu(message: Message, state: FSMContext) -> None:
    await state.clear()
    lang = resolve_user_lang(message.from_user)
    await message.answer(
        text=t(lang, "menu_title"),
        reply_markup=main_menu_keyboard(lang),
    )
