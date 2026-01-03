"""
Tests for prompts module.
"""
from src.rawanai.prompts import get_system_prompt, SYSTEM_PROMPT


def test_system_prompt_exists():
    """Test that system prompt is defined."""
    assert SYSTEM_PROMPT is not None
    assert len(SYSTEM_PROMPT) > 0


def test_get_system_prompt():
    """Test get_system_prompt function."""
    prompt = get_system_prompt()
    assert prompt is not None
    assert len(prompt) > 0
    assert isinstance(prompt, str)


def test_system_prompt_contains_key_elements():
    """Test that system prompt contains key personality elements."""
    prompt = get_system_prompt()
    
    # Check for key elements
    assert "روان" in prompt
    assert "أحمد" in prompt
    assert "سكرتيرة" in prompt or "سكرتيره" in prompt
    assert "جداوية" in prompt or "جدة" in prompt


def test_system_prompt_stripped():
    """Test that get_system_prompt returns stripped text."""
    prompt = get_system_prompt()
    assert prompt == prompt.strip()
