"""
Configuration management for RawanAI application.
Handles environment variables and application settings.
"""
import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class ModelConfig:
    """Configuration for the AI model."""
    model_id: str = "microsoft/Phi-3-mini-4k-instruct"
    max_new_tokens: int = 500
    temperature: float = 0.7
    do_sample: bool = True
    device_map: str = "auto"
    torch_dtype: str = "auto"
    trust_remote_code: bool = True


@dataclass
class AppConfig:
    """General application configuration."""
    app_title: str = "❤️ RawanAI - Your Secretary"
    app_description: str = "نظام ذكاء اصطناعي متطور بشخصية روان - السودانية الجداوية الدلوعة"
    chat_height: int = 500
    theme_primary_hue: str = "purple"
    enable_queue: bool = True
    debug: bool = False


@dataclass
class Config:
    """Main configuration class."""
    model: ModelConfig
    app: AppConfig
    
    @classmethod
    def from_env(cls) -> "Config":
        """Load configuration from environment variables."""
        model_config = ModelConfig(
            model_id=os.getenv("MODEL_ID", "microsoft/Phi-3-mini-4k-instruct"),
            max_new_tokens=int(os.getenv("MAX_NEW_TOKENS", "500")),
            temperature=float(os.getenv("TEMPERATURE", "0.7")),
            do_sample=os.getenv("DO_SAMPLE", "true").lower() == "true",
        )
        
        app_config = AppConfig(
            debug=os.getenv("DEBUG", "false").lower() == "true",
        )
        
        return cls(model=model_config, app=app_config)


# Global configuration instance
config = Config.from_env()
