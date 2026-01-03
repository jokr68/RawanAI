"""
Test configuration and fixtures for RawanAI tests.
"""
import pytest
import sys
from pathlib import Path

# Add parent directory to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def sample_message():
    """Sample user message for testing."""
    return "مرحبا يا روان"


@pytest.fixture
def sample_history():
    """Sample conversation history for testing."""
    return [
        ("مرحبا", "مرحبا يا سيدي! 💜"),
        ("كيف حالك؟", "أنا بخير يا قلبي، الحمد لله 🔥"),
    ]


@pytest.fixture
def empty_history():
    """Empty conversation history for testing."""
    return []
