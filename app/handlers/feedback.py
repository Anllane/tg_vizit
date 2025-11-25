"""
Обратная связь: /cancel и приём текста от пользователя.
"""

import logging

from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import ADMIN_ID
from app.keyboards import main_menu_keyboard
from app.localization import t
from app.services import resolve_user_lang, save_feedback
from app.states import FeedbackStates

router = Router()


@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    lang = resolve_user_lang(message.from_user)
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(t(lang, "cancel_no_state"))
        return

    await state.clear()
    await message.answer(
        t(lang, "cancel_done"),
        reply_markup=main_menu_keyboard(lang),
    )


@router.message(StateFilter(FeedbackStates.waiting_for_message))
async def handle_feedback(message: Message, state: FSMContext, bot) -> None:
    lang = resolve_user_lang(message.from_user)
    save_feedback(message, lang)

    user = message.from_user
    if user and ADMIN_ID:
        username = f"@{user.username}" if user.username else "—"
        full_name = user.full_name or "—"

        admin_text = (
            "📩 <b>Новая заявка / сообщение от пользователя</b>\n\n"
            f"ID: <code>{user.id}</code>\n"
            f"Имя: {full_name}\n"
            f"Username: {username}\n"
            f"Язык: {lang}\n\n"
            f"Текст сообщения:\n{message.text or message.caption or ''}"
        )

        try:
            await bot.send_message(chat_id=ADMIN_ID, text=admin_text)
        except Exception as e:
            logging.exception("Не удалось отправить сообщение админу: %s", e)

    await state.clear()
    await message.answer(
        t(lang, "feedback_thanks"),
        reply_markup=main_menu_keyboard(lang),
    )
