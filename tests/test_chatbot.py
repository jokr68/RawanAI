"""
Tests for chatbot module.
"""
import pytest
from src.rawanai.chatbot import Chatbot


def test_chatbot_initialization():
    """Test chatbot initialization."""
    chatbot = Chatbot()
    assert chatbot is not None
    assert chatbot.system_prompt is not None


def test_clear_history():
    """Test clearing conversation history."""
    chatbot = Chatbot()
    result = chatbot.clear_history()
    assert result == []
    assert isinstance(result, list)


def test_process_message_empty(empty_history):
    """Test processing empty message."""
    chatbot = Chatbot()
    response = chatbot.process_message("", empty_history)
    assert response is not None
    assert "قلبي" in response or "شيء" in response


def test_process_message_whitespace(empty_history):
    """Test processing whitespace-only message."""
    chatbot = Chatbot()
    response = chatbot.process_message("   ", empty_history)
    assert response is not None
    assert len(response) > 0


def test_chatbot_has_system_prompt():
    """Test that chatbot has system prompt."""
    chatbot = Chatbot()
    assert hasattr(chatbot, 'system_prompt')
    assert len(chatbot.system_prompt) > 0
    assert "روان" in chatbot.system_prompt
