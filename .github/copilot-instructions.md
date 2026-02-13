# Copilot Instructions for RawanAI

## Project Overview

RawanAI is a bilingual (Arabic/English) AI assistant project with two main components:
1. **RawanAI General Agent**: A Python/Gradio-based chatbot using Microsoft Phi-3-Mini model
2. **Lord'Os AI System**: A Progressive Web App (PWA) with a desktop and mobile interface

## Developer Information

**Developer & Creator**: أحمد بن محمد بن جمعان بن مبارك الدوسري  
**Copyright**: © 2025-2026 All rights reserved

## General Guidelines

### Language and Communication
- This is a **bilingual project** - maintain both Arabic and English in documentation
- Use Arabic (RTL) for UI elements and user-facing content
- Use English for technical documentation and code comments when appropriate
- Keep Arabic text properly formatted with RTL support

### Code Style
- **Python**: Follow PEP 8 conventions
- **JavaScript**: Use modern ES6+ syntax
- **HTML/CSS**: Maintain semantic HTML and organized CSS
- Keep code clean, readable, and well-documented

### Project Structure
\`\`\`
RawanAI/
├── app.py              # Gradio chatbot application (Python)
├── requirements.txt    # Python dependencies
├── index.html         # Lord'Os PWA interface
├── style.css          # PWA styling (Dark mode, Glassmorphism)
├── brain.js           # Lord'Os AI logic
├── manifest.json      # PWA manifest
└── .github/           # GitHub configuration
    ├── copilot-instructions.md
    ├── instructions/   # Scoped instructions
    └── agents/        # Custom agents
\`\`\`

### Testing and Validation
- Test Python changes with: `python app.py` (local testing)
- Test PWA changes by opening `index.html` in a browser or using `python3 -m http.server 8080`
- Always verify Arabic text rendering (RTL support)
- Check mobile responsiveness for PWA changes

### Dependencies
- Do not add new dependencies unless absolutely necessary
- When adding Python packages, update `requirements.txt`
- Prefer lightweight libraries compatible with Hugging Face Spaces

### Deployment Targets
- **RawanAI Agent**: Hugging Face Spaces (Gradio)
- **Lord'Os PWA**: Netlify, GitHub Pages, or Vercel
- Keep deployment configurations minimal and portable

## Key Features to Preserve

### RawanAI Agent
- Character: "روان" - Sudanese origin, raised in Jeddah
- Dialect: Gentle, professional Jeddah dialect
- Model: Microsoft Phi-3-Mini-4k-instruct
- UI: Dark purple theme with Arabic RTL support

### Lord'Os System
- Character: "مروى مسلم الدوسري" - Najdi dialect AI agent
- Features: Behavioral analysis, lifestyle patterns, personal wellness
- Design: Dark mode with Glassmorphism effects
- Technology: PWA with offline capabilities

## Boundaries

### Do Not Modify
- Copyright statements and IP rights declarations
- Character personalities and dialect specifications
- Core system prompts and AI personalities
- Model configurations without explicit requirements

### Always Maintain
- RTL support for Arabic text
- Dark theme aesthetics
- Mobile-first responsive design
- PWA offline functionality

## Common Tasks

### Adding Features
1. Check if it fits the project scope (general AI assistance)
2. Maintain bilingual support
3. Test on both desktop and mobile
4. Update relevant documentation

### Bug Fixes
1. Reproduce the issue
2. Fix with minimal changes
3. Test in both languages
4. Verify UI/UX consistency

### UI Changes
1. Maintain dark purple theme
2. Ensure RTL support for Arabic
3. Test mobile responsiveness
4. Keep Glassmorphism effects consistent

## Build and Run Commands

### Python Application
\`\`\`bash
# Install dependencies
pip install -r requirements.txt

# Run locally (requires GPU/CPU upgrade for optimal performance)
python app.py

# The app will start on http://localhost:7860 (default Gradio port)
\`\`\`

### PWA Application
\`\`\`bash
# Simple HTTP server
python3 -m http.server 8080

# Then open: http://localhost:8080
\`\`\`

## Questions to Ask Before Changes

1. Does this maintain bilingual support (Arabic/English)?
2. Is RTL rendering preserved for Arabic text?
3. Are character personalities and dialects maintained?
4. Is the dark theme aesthetic preserved?
5. Does this work on both desktop and mobile?
6. Are copyright notices intact?

## Additional Notes

- Hugging Face Spaces requires CPU upgrade (2 vCPU, 16 GB RAM) for optimal RawanAI performance
- Lord'Os is designed to work offline as a PWA
- Both components should remain lightweight and fast
- Respect cultural context of Saudi Arabian and Sudanese dialects
