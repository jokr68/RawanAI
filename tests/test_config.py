"""
Tests for configuration module.
"""
import pytest
import os
from config.config import Config, ModelConfig, AppConfig


def test_model_config_defaults():
    """Test ModelConfig default values."""
    config = ModelConfig()
    assert config.model_id == "microsoft/Phi-3-mini-4k-instruct"
    assert config.max_new_tokens == 500
    assert config.temperature == 0.7
    assert config.do_sample is True


def test_app_config_defaults():
    """Test AppConfig default values."""
    config = AppConfig()
    assert "RawanAI" in config.app_title
    assert config.chat_height == 500
    assert config.theme_primary_hue == "purple"
    assert config.debug is False


def test_config_from_env(monkeypatch):
    """Test loading configuration from environment variables."""
    # Set environment variables
    monkeypatch.setenv("MODEL_ID", "test-model")
    monkeypatch.setenv("MAX_NEW_TOKENS", "300")
    monkeypatch.setenv("TEMPERATURE", "0.5")
    monkeypatch.setenv("DEBUG", "true")
    
    config = Config.from_env()
    
    assert config.model.model_id == "test-model"
    assert config.model.max_new_tokens == 300
    assert config.model.temperature == 0.5
    assert config.app.debug is True


def test_config_structure():
    """Test Config class structure."""
    config = Config.from_env()
    assert hasattr(config, 'model')
    assert hasattr(config, 'app')
    assert isinstance(config.model, ModelConfig)
    assert isinstance(config.app, AppConfig)
