"""
app/states.py
Описание FSM-состояний бота.
"""

from aiogram.fsm.state import State, StatesGroup


class FeedbackStates(StatesGroup):
    waiting_for_message = State()


class AdminStates(StatesGroup):
    waiting_for_new_text = State()
