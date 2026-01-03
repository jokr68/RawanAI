"""
Tests for constants module.
"""
from src.rawanai.constants import (
    EMPTY_MESSAGE_RESPONSE,
    ERROR_MESSAGE_TEMPLATE,
    CHATBOT_ERROR_MESSAGE_TEMPLATE
)


def test_empty_message_response():
    """Test that empty message response is defined."""
    assert EMPTY_MESSAGE_RESPONSE is not None
    assert len(EMPTY_MESSAGE_RESPONSE) > 0
    assert isinstance(EMPTY_MESSAGE_RESPONSE, str)
    assert "قلبي" in EMPTY_MESSAGE_RESPONSE


def test_error_message_template():
    """Test that error message template is defined and can be formatted."""
    assert ERROR_MESSAGE_TEMPLATE is not None
    assert len(ERROR_MESSAGE_TEMPLATE) > 0
    
    # Test formatting
    formatted = ERROR_MESSAGE_TEMPLATE.format(error="test error")
    assert "test error" in formatted
    assert len(formatted) > len("test error")


def test_chatbot_error_message_template():
    """Test that chatbot error message template is defined and can be formatted."""
    assert CHATBOT_ERROR_MESSAGE_TEMPLATE is not None
    assert len(CHATBOT_ERROR_MESSAGE_TEMPLATE) > 0
    
    # Test formatting
    formatted = CHATBOT_ERROR_MESSAGE_TEMPLATE.format(error="test error")
    assert "test error" in formatted
    assert len(formatted) > len("test error")


def test_all_messages_are_arabic():
    """Test that all messages contain Arabic text."""
    # Check for Arabic characters (Unicode range)
    def has_arabic(text):
        return any('\u0600' <= c <= '\u06FF' for c in text)
    
    assert has_arabic(EMPTY_MESSAGE_RESPONSE)
    assert has_arabic(ERROR_MESSAGE_TEMPLATE)
    assert has_arabic(CHATBOT_ERROR_MESSAGE_TEMPLATE)
