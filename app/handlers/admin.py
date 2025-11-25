"""
Админ-панель: /admin, выбор языка, раздела и редактирование текста.
"""

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from config import ADMIN_ID
from app.keyboards import admin_language_keyboard, admin_sections_keyboard, main_menu_keyboard
from app.localization import t
from app.services import get_section_text, resolve_user_lang, set_section_text
from app.states import AdminStates

router = Router()


def _is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID


def _section_human_name(section: str) -> str:
    mapping = {
        "about": "Обо мне",
        "services": "Услуги",
        "contacts": "Контакты",
        "socials": "Соцсети",
        "website": "Сайт",
    }
    return mapping.get(section, section)


@router.message(Command("admin"))
async def cmd_admin(message: Message) -> None:
    user = message.from_user
    lang_ui = resolve_user_lang(user)

    if not user or not _is_admin(user.id):
        await message.answer(t(lang_ui, "admin_access_denied"))
        return

    await message.answer(
        t(lang_ui, "admin_start"),
        reply_markup=admin_language_keyboard(),
    )


@router.callback_query(F.data.startswith("admin:lang:"))
async def admin_choose_lang(callback: CallbackQuery) -> None:
    user = callback.from_user
    lang_ui = resolve_user_lang(user)

    if not user or not _is_admin(user.id):
        await callback.answer()
        return

    _, _, lang_to_edit = callback.data.split(":", maxsplit=2)

    await callback.message.answer(
        text=(
            f"Язык текстов для редактирования: <b>{lang_to_edit}</b>\n\n"
            f"{t(lang_ui, 'admin_choose_section')}"
        ),
        reply_markup=admin_sections_keyboard(lang_to_edit),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("admin:edit:"))
async def admin_edit_section(callback: CallbackQuery, state: FSMContext) -> None:
    user = callback.from_user
    lang_ui = resolve_user_lang(user)

    if not user or not _is_admin(user.id):
        await callback.answer()
        return

    _, _, lang_to_edit, section = callback.data.split(":", maxsplit=3)
    current_text = get_section_text(section, lang_to_edit)

    await state.update_data(edit_lang=lang_to_edit, edit_section=section)
    await state.set_state(AdminStates.waiting_for_new_text)

    human = _section_human_name(section)
    await callback.message.answer(
        text=(
            f"Редактирование раздела: <b>{human}</b>\n"
            f"Язык: <b>{lang_to_edit}</b>\n\n"
            f"Текущий текст:\n\n{current_text}"
        )
    )
    await callback.message.answer(t(lang_ui, "admin_prompt_new_text"))
    await callback.answer()


@router.message(StateFilter(AdminStates.waiting_for_new_text))
async def admin_set_new_text(message: Message, state: FSMContext) -> None:
    user = message.from_user
    lang_ui = resolve_user_lang(user)

    data = await state.get_data()
    section = data.get("edit_section")
    lang_to_edit = data.get("edit_lang")

    if not section or not lang_to_edit:
        await state.clear()
        await message.answer("Что-то пошло не так, попробуй ещё раз /admin.")
        return

    content = message.html_text or message.text or ""
    set_section_text(section, lang_to_edit, content)
    await state.clear()

    await message.answer(
        t(lang_ui, "admin_text_updated"),
        reply_markup=main_menu_keyboard(lang_ui),
    )
