---
applies_to:
  - "**/*.py"
  - "requirements.txt"
---

# Python Backend Instructions for RawanAI

## Overview

This file contains instructions specific to the Python backend of RawanAI, which powers the Gradio chatbot interface.

## Technology Stack

- **Framework**: Gradio 4.29.0
- **Model**: Microsoft Phi-3-mini-4k-instruct (HuggingFace Transformers)
- **Libraries**: torch, transformers, accelerate, sentencepiece
- **Deployment**: Hugging Face Spaces

## Code Style Guidelines

### Python Conventions
- Follow PEP 8 style guide
- Use 4 spaces for indentation
- Use descriptive variable names in English, but keep Arabic content in strings
- Add docstrings for functions (optional but recommended)

### Imports
- Group imports: standard library, third-party, local
- Use absolute imports

### Example:
\`\`\`python
import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Good variable naming
def chat_function(message, history):
    # Arabic content in strings is fine
    system_prompt = "أنتِ روان..."
\`\`\`

## Model Configuration

### Critical Settings
- **Model ID**: `microsoft/Phi-3-mini-4k-instruct`
- **Device Map**: `auto` (allows CPU/GPU flexibility)
- **torch_dtype**: `auto`
- **trust_remote_code**: `True`

### Generation Parameters
\`\`\`python
generation_args = {
    "max_new_tokens": 500,
    "return_full_text": False,
    "temperature": 0.7,
    "do_sample": True,
}
\`\`\`

**Do not modify these without testing**, as they affect response quality and speed.

## System Prompt (روان's Personality)

The `SYSTEM_PROMPT` variable defines روان's character:
- Sudanese origin, raised in Jeddah
- Jeddah dialect (لهجة جداوية)
- Friendly, professional, helpful
- Moderate emoji use (💜)

**Never remove or significantly alter** the core personality traits unless explicitly requested.

## Gradio Interface

### Theme
- Use purple color scheme (`primary_hue="purple"`)
- Dark background (`#1a1a1a`)
- RTL support for Arabic (`direction: rtl`)

### Components
- `gr.Chatbot`: Main chat display (height=500)
- `gr.Textbox`: User input with Arabic placeholder
- `gr.Button`: Clear chat functionality

### Custom CSS
Keep the dark purple aesthetic and RTL support in `custom_css`:
\`\`\`python
custom_css = """
body { background-color: #1a1a1a; color: #ffffff; direction: rtl; }
.message.user { background-color: #4a148c !important; }
.message.assistant { background-color: #311b92 !important; }
"""
\`\`\`

## Dependencies

### Adding New Packages
1. Check compatibility with Hugging Face Spaces
2. Add to `requirements.txt` with version pinning when necessary
3. Prefer lightweight alternatives
4. Test memory usage (Spaces has 16GB RAM limit)

### Current Dependencies
\`\`\`
gradio==4.29.0  # UI framework (pinned)
torch            # PyTorch (auto-latest)
transformers     # HuggingFace models
accelerate       # Model loading optimization
sentencepiece    # Tokenizer support
\`\`\`

## Testing

### Local Testing
\`\`\`bash
# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Access at http://localhost:7860
\`\`\`

### What to Test
1. **Arabic Input/Output**: Verify RTL rendering
2. **Response Quality**: Check if روان's personality is consistent
3. **Response Time**: Should be under 10 seconds on CPU
4. **Memory Usage**: Monitor RAM consumption
5. **Error Handling**: Test with empty messages, very long messages

## Performance Considerations

### Hugging Face Spaces Requirements
- Requires **CPU upgrade (2 vCPU, 16 GB RAM)** for optimal performance
- Model loads on startup (takes 1-2 minutes)
- Consider caching strategy for repeated queries

### Optimization Tips
- Use `torch_dtype="auto"` for automatic precision selection
- Keep `max_new_tokens` reasonable (500 is good balance)
- Consider adding response caching for common queries

## Common Tasks

### Modifying روان's Personality
Edit the `SYSTEM_PROMPT` variable:
\`\`\`python
SYSTEM_PROMPT = """
أنتِ "روان"، وكيلة ذكاء اصطناعي عامة للمساعدة اليومية.
# Add new traits here...
"""
\`\`\`

### Adjusting Response Length
Modify `max_new_tokens` in `generation_args`:
\`\`\`python
"max_new_tokens": 500,  # Increase for longer responses
\`\`\`

### Changing Temperature (Creativity)
Adjust `temperature` in `generation_args`:
\`\`\`python
"temperature": 0.7,  # Lower (0.5) = more focused, Higher (0.9) = more creative
\`\`\`

## Error Handling

### Common Issues
1. **Model Loading Failures**: Check internet connection and HF cache
2. **CUDA/Memory Errors**: Reduce batch size or use CPU-only
3. **Arabic Encoding Issues**: Ensure UTF-8 encoding in files

### Debugging
\`\`\`python
# Add logging
import logging
logging.basicConfig(level=logging.INFO)

# Check device
print(f"Using device: {model.device}")
\`\`\`

## Security Considerations

### Input Validation
- Gradio handles basic input sanitization
- روان's system prompt includes safety guidelines
- Consider adding content filtering for production

### Sensitive Data
- Do not log user messages in production
- Do not store conversation history permanently
- Respect privacy in system prompts

## Boundaries

### Do Not Change
- Model ID (microsoft/Phi-3-mini-4k-instruct)
- Core personality traits in SYSTEM_PROMPT
- RTL support and Arabic language handling
- Copyright statements

### Always Preserve
- Gradio interface responsiveness
- Arabic text rendering
- Dark purple theme
- روان's friendly, professional tone

## Questions Before Making Changes

1. Does this maintain روان's personality and dialect?
2. Is Arabic text still properly rendered (RTL)?
3. Does this work on Hugging Face Spaces (CPU/GPU auto)?
4. Is the response time still acceptable?
5. Are memory requirements still within 16GB limit?
