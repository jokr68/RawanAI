"""
Tests for chatbot module.
"""
import pytest


def test_chatbot_initialization():
    """Test chatbot initialization."""
    from src.rawanai.chatbot import Chatbot
    chatbot = Chatbot()
    assert chatbot is not None
    assert chatbot.system_prompt is not None


def test_clear_history():
    """Test clearing conversation history."""
    from src.rawanai.chatbot import Chatbot
    chatbot = Chatbot()
    result = chatbot.clear_history()
    assert result == []
    assert isinstance(result, list)


def test_process_message_empty():
    """Test processing empty message."""
    from src.rawanai.chatbot import Chatbot
    chatbot = Chatbot()
    empty_history = []
    response = chatbot.process_message("", empty_history)
    assert response is not None
    assert "قلبي" in response or "شيء" in response


def test_process_message_whitespace():
    """Test processing whitespace-only message."""
    from src.rawanai.chatbot import Chatbot
    chatbot = Chatbot()
    empty_history = []
    response = chatbot.process_message("   ", empty_history)
    assert response is not None
    assert len(response) > 0


def test_chatbot_has_system_prompt():
    """Test that chatbot has system prompt."""
    from src.rawanai.chatbot import Chatbot
    chatbot = Chatbot()
    assert hasattr(chatbot, 'system_prompt')
    assert len(chatbot.system_prompt) > 0
    assert "روان" in chatbot.system_prompt
