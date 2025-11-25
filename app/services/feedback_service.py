"""
app/services/feedback_service.py
Сохранение заявок (обратной связи).
"""

from __future__ import annotations

from datetime import datetime

from aiogram.types import Message

from app.database import get_connection


def save_feedback(message: Message, lang: str) -> None:
    """
    Сохраняет заявку / сообщение обратной связи в БД.
    """
    user = message.from_user
    if user is None:
        return

    text = message.text or message.caption or ""
    username = f"@{user.username}" if user.username else None
    full_name = user.full_name

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO feedbacks (user_id, username, full_name, message, lang, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            user.id,
            username,
            full_name,
            text,
            lang,
            datetime.now().isoformat(timespec="seconds"),
        ),
    )
    conn.commit()
    conn.close()
