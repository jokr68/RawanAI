"""
RawanAI - Your Secretary
A sophisticated AI chatbot with Rawan's personality.

Copyright © 2025 Ahmed bin Mohammed bin Jum'an bin Mubarak Al-Dosari
All rights reserved.
"""

__version__ = "1.0.0"
__author__ = "Ahmed bin Mohammed bin Jum'an bin Mubarak Al-Dosari"

# Note: Lazy imports to avoid loading heavy dependencies at import time
# Import model_manager only when needed to avoid torch import errors in tests

__all__ = [
    "chatbot",
    "model_manager",
    "create_interface",
    "launch_interface",
]


def __getattr__(name):
    """Lazy loading of heavy modules."""
    if name == "chatbot":
        from src.rawanai.chatbot import chatbot
        return chatbot
    elif name == "model_manager":
        from src.rawanai.model import model_manager
        return model_manager
    elif name == "create_interface":
        from src.rawanai.ui import create_interface
        return create_interface
    elif name == "launch_interface":
        from src.rawanai.ui import launch_interface
        return launch_interface
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
