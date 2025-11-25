from .start import router as start_router
from .menu import router as menu_router
from .language import router as language_router
from .feedback import router as feedback_router
from .admin import router as admin_router

__all__ = [
    "start_router",
    "menu_router",
    "language_router",
    "feedback_router",
    "admin_router",
]
