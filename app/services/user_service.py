"""
app/services/user_service.py
Работа с пользователями и языком интерфейса.
"""

from __future__ import annotations

from typing import Optional

from aiogram.types import User

from app.database import get_connection
from app.localization import DEFAULT_LANG, SUPPORTED_LANGS


def _get_user_lang_from_db(user_id: int) -> Optional[str]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT lang FROM users WHERE user_id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return row["lang"]
    return None


def set_user_lang(user_id: int, lang: str) -> None:
    """
    Сохраняем выбранный пользователем язык в БД.
    """
    if lang not in SUPPORTED_LANGS:
        lang = DEFAULT_LANG

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO users (user_id, lang)
        VALUES (?, ?)
        ON CONFLICT(user_id) DO UPDATE SET lang = excluded.lang
        """,
        (user_id, lang),
    )
    conn.commit()
    conn.close()


def resolve_user_lang(user: Optional[User]) -> str:
    """
    Определяем язык пользователя:
    1) если есть в БД – берём его;
    2) иначе смотрим language_code Telegram;
    3) иначе – русский по умолчанию.
    """
    if user is None:
        return DEFAULT_LANG

    db_lang = _get_user_lang_from_db(user.id)
    if db_lang in SUPPORTED_LANGS:
        return db_lang

    code = (user.language_code or "").lower()
    if code.startswith("ru"):
        return "ru"
    return "en"
