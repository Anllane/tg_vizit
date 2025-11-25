"""
config.py
Глобальная конфигурация бота.

Все секреты берём из .env / переменных окружения.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent

# Загружаем .env
load_dotenv(BASE_DIR / ".env")


# === Секреты и параметры ===

BOT_TOKEN: str | None = os.getenv("BOT_TOKEN")

try:
    ADMIN_ID: int = int(os.getenv("ADMIN_ID", "0"))
except ValueError:
    ADMIN_ID = 0

DB_PATH: str = os.getenv("DATABASE_PATH", str(BASE_DIR / "bot.db"))


@dataclass(frozen=True)
class Profile:
    """
    Профиль владельца визитки.
    Можно смело поменять под себя.
    """

    full_name: str
    title_ru: str
    title_en: str


PROFILE = Profile(
    full_name="**** ********",
    title_ru="Разработчик Telegram-ботов и web-сервисов",
    title_en="Telegram bot & web developer",
)


# === Тексты разделов по умолчанию (могут меняться через админку) ===

DEFAULT_SECTION_TEXTS = {
    "ru": {
        "about": (
            "👋 Привет! Меня зовут ****, я занимаюсь разработкой Telegram-ботов, "
            "web-сервисов и автоматизацией процессов.\n\n"
            "Помогаю бизнесу упрощать рутину, собирать заявки и делать удобные "
            "цифровые инструменты под задачи."
        ),
        "services": (
            "💼 <b>Мои услуги</b>\n\n"
            "• Разработка Telegram-ботов под ключ\n"
            "• Приём заявок и уведомления в Telegram\n"
            "• Интеграция с Google Sheets / CRM\n"
            "• Простые web-лендинги\n"
            "• Консультации по автоматизации\n"
        ),
        "contacts": (
            "📞 <b>Контакты</b>\n\n"
            "Телефон: <code>+7 999 000-00-00</code>\n"
            "E-mail: <code>example@mail.ru</code>\n"
            "Город: Москва\n"
        ),
        "socials": (
            "📱 <b>Социальные сети</b>\n\n"
            "• Telegram: @Mzerat1\n"
            "• VK: vk.com/username\n"
            "• Instagram*: instagram.com/username\n\n"
            "<i>*Запрещённая в РФ организация, 18+</i>"
        ),
        "website": (
            "🌐 <b>Сайт</b>\n\n"
            "Мой сайт: https://example.com\n\n"
            "Можно перейти по ссылке прямо из этого сообщения."
        ),
    },
    "en": {
        "about": (
            "👋 Hi! My name is Ivan. I build Telegram bots, web services and "
            "automation tools.\n\n"
            "I help businesses collect leads, simplify routine tasks and create "
            "useful digital tools."
        ),
        "services": (
            "💼 <b>Services</b>\n\n"
            "• Telegram bots from scratch\n"
            "• Lead collection and notifications\n"
            "• Integration with Google Sheets / CRM\n"
            "• Simple landing pages\n"
            "• Automation consulting\n"
        ),
        "contacts": (
            "📞 <b>Contacts</b>\n\n"
            "Phone: <code>+7 999 000-00-00</code>\n"
            "E-mail: <code>example@mail.ru</code>\n"
            "City: Moscow\n"
        ),
        "socials": (
            "📱 <b>Social media</b>\n\n"
            "• Telegram: @Mzerat1\n"
            "• VK: vk.com/username\n"
            "• Instagram*: instagram.com/username\n\n"
        ),
        "website": (
            "🌐 <b>Website</b>\n\n"
            "My website: https://example.com\n\n"
            "You can open the link directly from this message."
        ),
    },
}
