"""
bot.py
Точка входа для Меню-Бота Визитки.

Запуск из корня проекта:
    python bot.py
"""

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN, ADMIN_ID
from app.database import init_db
from app.handlers import (
    admin_router,
    feedback_router,
    language_router,
    menu_router,
    start_router,
)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
    )

    if not BOT_TOKEN:
        raise RuntimeError(
            "Не указан BOT_TOKEN. Добавь его в .env (BOT_TOKEN=...)"
        )

    if not ADMIN_ID:
        logging.warning(
            "ADMIN_ID не указан или равен 0 — админ-панель и пересылка заявок админу "
            "работать не будут."
        )

    # Инициализация базы
    init_db()

    # Создаём бота с настройкой parse_mode для aiogram 3.7+
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher(storage=MemoryStorage())

    # Подключаем все роутеры
    dp.include_router(start_router)
    dp.include_router(language_router)
    dp.include_router(menu_router)
    dp.include_router(feedback_router)
    dp.include_router(admin_router)

    logging.info("Меню-бот визитка запущен. Нажми Ctrl+C для остановки.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
