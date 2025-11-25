# app/database/__init__.py
from .db import init_db, get_connection

__all__ = ["init_db", "get_connection"]
