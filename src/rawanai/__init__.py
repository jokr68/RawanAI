"""
RawanAI - Your Secretary
A sophisticated AI chatbot with Rawan's personality.

Copyright © 2025 Ahmed bin Mohammed bin Jum'an bin Mubarak Al-Dosari
All rights reserved.
"""

__version__ = "1.0.0"
__author__ = "Ahmed bin Mohammed bin Jum'an bin Mubarak Al-Dosari"

from src.rawanai.chatbot import chatbot
from src.rawanai.model import model_manager
from src.rawanai.ui import create_interface, launch_interface

__all__ = [
    "chatbot",
    "model_manager",
    "create_interface",
    "launch_interface",
]
