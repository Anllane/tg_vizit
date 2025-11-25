"""
Обработка нажатий в главном меню: разделы, язык, обратная связь.
"""

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.keyboards import language_keyboard, main_menu_keyboard
from app.localization import t
from app.services import get_section_text, resolve_user_lang
from app.states import FeedbackStates

router = Router()


@router.callback_query(F.data.startswith("menu:"))
async def menu_callback(callback: CallbackQuery, state: FSMContext) -> None:
    lang = resolve_user_lang(callback.from_user)
    action = callback.data.split(":", maxsplit=1)[1]

    # Обратная связь
    if action == "feedback":
        await state.set_state(FeedbackStates.waiting_for_message)
        await callback.message.answer(t(lang, "feedback_intro"))
        await callback.answer()
        return

    # Выбор языка
    if action == "language":
        await callback.message.answer(
            text=t(lang, "language_choose"),
            reply_markup=language_keyboard(lang),
        )
        await callback.answer()
        return

    # Разделы
    if action in {"about", "services", "contacts", "socials", "website"}:
        text = get_section_text(action, lang)
    else:
        text = t(lang, "menu_title")

    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=main_menu_keyboard(lang),
        )
    except Exception:
        await callback.message.answer(
            text=text,
            reply_markup=main_menu_keyboard(lang),
        )

    await callback.answer()
