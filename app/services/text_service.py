"""
app/services/text_service.py
Тексты разделов: чтение и обновление.
"""

from __future__ import annotations

from config import DEFAULT_SECTION_TEXTS
from app.database import get_connection
from app.localization import DEFAULT_LANG


def get_section_text(section: str, lang: str) -> str:
    """
    Возвращает текст раздела с учётом языка.
    Если в БД нет – берём дефолт, сохраняем и возвращаем.
    """
    if lang not in DEFAULT_SECTION_TEXTS:
        lang = DEFAULT_LANG

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT content FROM texts WHERE section = ? AND lang = ?",
        (section, lang),
    )
    row = cur.fetchone()

    if row:
        conn.close()
        return row["content"]

    # Нет в БД – подставляем дефолт
    default_lang_dict = DEFAULT_SECTION_TEXTS.get(lang) or DEFAULT_SECTION_TEXTS[DEFAULT_LANG]
    default_content = default_lang_dict.get(section, "")

    cur.execute(
        """
        INSERT INTO texts (section, lang, content)
        VALUES (?, ?, ?)
        ON CONFLICT(section, lang) DO UPDATE SET content = excluded.content
        """,
        (section, lang, default_content),
    )
    conn.commit()
    conn.close()
    return default_content


def set_section_text(section: str, lang: str, content: str) -> None:
    """
    Обновляет текст раздела (используется админ-панелью).
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO texts (section, lang, content)
        VALUES (?, ?, ?)
        ON CONFLICT(section, lang) DO UPDATE SET content = excluded.content
        """,
        (section, lang, content),
    )
    conn.commit()
    conn.close()
