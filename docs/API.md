# RawanAI API Documentation

## Overview

RawanAI is a modular chatbot application with a personality-driven AI assistant named Rawan.

## Project Structure

```
RawanAI/
├── app.py                 # Main application entry point
├── config/                # Configuration management
│   ├── __init__.py
│   └── config.py         # Configuration classes
├── src/
│   └── rawanai/          # Main application package
│       ├── __init__.py
│       ├── chatbot.py    # Chatbot logic
│       ├── model.py      # AI model management
│       ├── prompts.py    # System prompts
│       └── ui.py         # Gradio user interface
├── tests/                # Test files
├── requirements.txt      # Production dependencies
└── requirements-dev.txt  # Development dependencies
```

## Core Modules

### Configuration (`config/config.py`)

Manages application configuration with environment variable support.

#### Classes

**ModelConfig**
- `model_id`: str - AI model identifier
- `max_new_tokens`: int - Maximum tokens to generate
- `temperature`: float - Sampling temperature
- `do_sample`: bool - Enable sampling

**AppConfig**
- `app_title`: str - Application title
- `app_description`: str - Application description
- `chat_height`: int - Chat interface height
- `theme_primary_hue`: str - UI theme color

**Config**
- Main configuration container
- `from_env()`: Load config from environment variables

### Model Management (`src/rawanai/model.py`)

Handles AI model loading and text generation.

#### ModelManager Class

**Methods:**
- `load_model()`: Load the AI model and tokenizer
- `generate_response(messages, custom_args)`: Generate response from messages
- `is_loaded()`: Check if model is loaded

### Chatbot (`src/rawanai/chatbot.py`)

Manages conversation logic and message processing.

#### Chatbot Class

**Methods:**
- `process_message(message, history)`: Process user message and generate response
- `clear_history()`: Clear conversation history

### User Interface (`src/rawanai/ui.py`)

Creates and manages the Gradio web interface.

**Functions:**
- `create_interface()`: Create Gradio interface
- `launch_interface(demo, **kwargs)`: Launch the interface
- `respond(message, chat_history)`: Handle user input

### Prompts (`src/rawanai/prompts.py`)

Defines system prompts and personality.

**Functions:**
- `get_system_prompt()`: Get the system prompt for Rawan's personality

## Usage Examples

### Basic Usage

```python
from src.rawanai.model import model_manager
from src.rawanai.ui import create_interface, launch_interface

# Load model
model_manager.load_model()

# Create and launch interface
demo = create_interface()
launch_interface(demo)
```

### Custom Configuration

```python
import os
os.environ['MAX_NEW_TOKENS'] = '300'
os.environ['TEMPERATURE'] = '0.8'

from config.config import Config
config = Config.from_env()
```

### Using Chatbot Directly

```python
from src.rawanai.chatbot import chatbot

history = []
response = chatbot.process_message("مرحبا يا روان", history)
print(response)
```

## Environment Variables

Configure the application with these environment variables:

- `MODEL_ID`: AI model identifier (default: microsoft/Phi-3-mini-4k-instruct)
- `MAX_NEW_TOKENS`: Maximum tokens to generate (default: 500)
- `TEMPERATURE`: Sampling temperature (default: 0.7)
- `DO_SAMPLE`: Enable sampling (default: true)
- `DEBUG`: Enable debug mode (default: false)

## Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_config.py

# Run with coverage
pytest --cov=src --cov-report=html
```

## Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d

# Build manually
docker build -t rawanai .
docker run -p 7860:7860 rawanai
```
