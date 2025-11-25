"""
app/database/db.py
Простая обёртка над sqlite3: инициализация и подключение.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from config import DB_PATH


def get_connection() -> sqlite3.Connection:
    """
    Возвращает новое подключение к SQLite.
    Для маленького бота это нормально делать на каждый запрос.
    """
    path = Path(DB_PATH)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """
    Создаёт таблицы, если их ещё нет.
    """
    conn = get_connection()
    cur = conn.cursor()

    # Пользователи и их выбранный язык
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            lang    TEXT NOT NULL
        )
        """
    )

    # Заявки / сообщения обратной связи
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS feedbacks (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id    INTEGER NOT NULL,
            username   TEXT,
            full_name  TEXT,
            message    TEXT,
            lang       TEXT,
            created_at TEXT
        )
        """
    )

    # Тексты разделов (редактируются в админке)
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS texts (
            section TEXT NOT NULL,
            lang    TEXT NOT NULL,
            content TEXT NOT NULL,
            PRIMARY KEY (section, lang)
        )
        """
    )

    conn.commit()
    conn.close()
