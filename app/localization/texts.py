"""
app/localization/texts.py
Локализованные строки интерфейса (RU/EN).
"""

from __future__ import annotations

DEFAULT_LANG = "ru"
SUPPORTED_LANGS = ("ru", "en")

TEXTS = {
    "ru": {
        "start_welcome": "Добро пожаловать в меню-бот визитку 👇",
        "menu_title": "Главное меню 👇",
        "feedback_intro": (
            "✉️ <b>Обратная связь</b>\n\n"
            "Опиши свой вопрос, идею или задачу одним сообщением.\n"
            "Я получу его и отвечу, как только смогу.\n\n"
            "Если передумал — отправь /cancel."
        ),
        "feedback_thanks": (
            "✅ Спасибо! Твоё сообщение отправлено.\n"
            "Я свяжусь с тобой, как только смогу."
        ),
        "cancel_no_state": "Сейчас нет активного действия, которое можно отменить.",
        "cancel_done": "Действие отменено. Возвращаю в главное меню 👇",
        "language_choose": "🌐 Выбери язык интерфейса",
        "language_saved": "✅ Язык интерфейса переключён на русский.",
        "btn_about": "ℹ️ Обо мне",
        "btn_services": "💼 Услуги",
        "btn_contacts": "📞 Контакты",
        "btn_socials": "📱 Соцсети",
        "btn_website": "🌐 Сайт",
        "btn_feedback": "✉️ Обратная связь",
        "btn_language": "🌐 Язык",
        "btn_lang_ru": "🇷🇺 Русский",
        "btn_lang_en": "🇬🇧 English",
        "admin_access_denied": "У тебя нет прав администратора.",
        "admin_start": (
            "🛠 <b>Админ-панель</b>.\n"
            "Сначала выбери язык разделов, который хочешь отредактировать."
        ),
        "admin_choose_section": "Выбери раздел для редактирования:",
        "admin_prompt_new_text": (
            "Пришли новый текст одним сообщением. Текущий текст выше."
        ),
        "admin_text_updated": "✅ Текст раздела обновлён.",
    },
    "en": {
        "start_welcome": "Welcome to the business-card menu bot 👇",
        "menu_title": "Main menu 👇",
        "feedback_intro": (
            "✉️ <b>Feedback</b>\n\n"
            "Describe your question or task in a single message.\n"
            "I'll receive it and get back to you.\n\n"
            "If you changed your mind — send /cancel."
        ),
        "feedback_thanks": (
            "✅ Thank you! Your message has been sent.\n"
            "I'll contact you as soon as I can."
        ),
        "cancel_no_state": "There is no active action to cancel.",
        "cancel_done": "Action cancelled. Back to the main menu 👇",
        "language_choose": "🌐 Choose interface language",
        "language_saved": "✅ Interface language set to English.",
        "btn_about": "ℹ️ About me",
        "btn_services": "💼 Services",
        "btn_contacts": "📞 Contacts",
        "btn_socials": "📱 Socials",
        "btn_website": "🌐 Website",
        "btn_feedback": "✉️ Feedback",
        "btn_language": "🌐 Language",
        "btn_lang_ru": "🇷🇺 Russian",
        "btn_lang_en": "🇬🇧 English",
        "admin_access_denied": "You are not an administrator.",
        "admin_start": (
            "🛠 <b>Admin panel</b>.\n"
            "First choose the language of the sections you want to edit."
        ),
        "admin_choose_section": "Choose a section to edit:",
        "admin_prompt_new_text": (
            "Send the new text in a single message. The current text is shown above."
        ),
        "admin_text_updated": "✅ Section text updated.",
    },
}


def t(lang: str, key: str) -> str:
    """
    Удобный хелпер для получения текста по ключу с запасным вариантом.
    """
    lang_dict = TEXTS.get(lang) or TEXTS[DEFAULT_LANG]
    return lang_dict.get(key) or TEXTS[DEFAULT_LANG].get(key, key)
