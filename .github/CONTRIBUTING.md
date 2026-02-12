# Contributing to RawanAI

Thank you for your interest in contributing to RawanAI! This document provides guidelines for contributing to the project.

## 🤖 GitHub Copilot Coding Agent

This repository is configured for use with [GitHub Copilot coding agent](https://docs.github.com/en/copilot/tutorials/coding-agent), which can autonomously work on issues when assigned.

### Copilot Instructions Structure

Our repository includes comprehensive instructions for Copilot:

- **`.github/copilot-instructions.md`** - Repository-wide guidelines covering project overview, code style, testing, and boundaries
- **`.github/instructions/python.instructions.md`** - Python backend specific guidelines (applies to `**/*.py`, `requirements.txt`)
- **`.github/instructions/frontend.instructions.md`** - Frontend/PWA specific guidelines (applies to `**/*.html`, `**/*.css`, `**/*.js`, `manifest.json`)
- **`.github/agents/my-agent.agent.md`** - Custom RawanAI Development Agent with specialized knowledge

### Assigning Issues to Copilot

1. Create a clear, well-scoped issue with:
   - Clear description of the problem or feature
   - Expected behavior or outcome
   - Any constraints or requirements
   - Acceptance criteria

2. Assign the issue to `@copilot` (requires write access to the repository)

3. Copilot will:
   - Create a new branch
   - Make the necessary changes
   - Create a pull request
   - Respond to review feedback

4. Review the PR carefully and provide feedback as needed

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ (for RawanAI backend)
- Modern web browser (for Lord'Os PWA)
- Git

### Setup for RawanAI Backend

```bash
# Clone the repository
git clone https://github.com/jokr68/RawanAI.git
cd RawanAI

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Access at http://localhost:7860
```

### Setup for Lord'Os PWA

```bash
# No installation needed! Just serve the files:
python3 -m http.server 8080

# Access at http://localhost:8080
# Open index.html in your browser
```

## 📋 Code Style Guidelines

### Python
- Follow PEP 8 conventions
- Use 4 spaces for indentation
- Keep Arabic content in strings, use English for variable names
- Add type hints where beneficial
- Write descriptive commit messages

### Frontend (HTML/CSS/JS)
- Use modern ES6+ JavaScript
- Follow mobile-first responsive design
- Maintain RTL support for Arabic text
- Keep dark theme aesthetic consistent
- Use semantic HTML5 elements

## 🧪 Testing

### Python Application
```bash
# Run the application and test manually
python app.py

# Test checklist:
# - Arabic text renders correctly (RTL)
# - روان's personality is consistent
# - Response time is acceptable
# - Memory usage is reasonable
```

### PWA Application
```bash
# Serve locally
python3 -m http.server 8080

# Test checklist:
# - Dark mode renders correctly
# - Glassmorphism effects work
# - Arabic text is RTL aligned
# - Mobile responsiveness works
# - PWA installs correctly
```

## 🌍 Bilingual Development

This is a **bilingual (Arabic/English) project**. When contributing:

1. **Preserve RTL Support**: All Arabic text must render right-to-left
2. **Maintain Character Personalities**:
   - **روان**: Sudanese, raised in Jeddah, Jeddah dialect
   - **مروى**: Najdi dialect, authentic Saudi expressions
3. **Test Both Languages**: Verify your changes work in Arabic and English
4. **Cultural Sensitivity**: Respect Saudi Arabian and Sudanese cultural contexts

## 🎨 Design Principles

### Dark Theme
- Primary background: `#0a0a0a` (very dark)
- Secondary background: `#1a1a1a` (dark gray)
- Accent colors: Purple shades (`#9c27b0`, `#4a148c`, `#311b92`)
- Text: White (`#ffffff`) with proper contrast

### Glassmorphism Effects
```css
.glass-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}
```

## 🚫 Boundaries

### Never Modify
- Copyright statements and IP rights declarations
- Character personalities and dialect specifications
- Core system prompts and AI personalities
- Model configurations without explicit requirements

### Always Preserve
- RTL support for Arabic text
- Dark theme aesthetics
- Mobile-first responsive design
- PWA offline functionality

## 📝 Commit Message Format

Use clear, descriptive commit messages:

```
feat: Add new feature description
fix: Fix bug description
docs: Update documentation
style: Code style changes (formatting, etc.)
refactor: Code refactoring
test: Add or update tests
chore: Maintenance tasks
```

Examples:
- `feat: Add file upload support to روان chatbot`
- `fix: Correct RTL alignment for Arabic text in Lord'Os`
- `docs: Update README with deployment instructions`

## 🔍 Pull Request Process

1. **Create a descriptive PR title** that summarizes the change
2. **Fill out the PR description** with:
   - What changed and why
   - How to test the changes
   - Screenshots (for UI changes)
   - Any breaking changes or migrations needed
3. **Ensure all checks pass** (if CI/CD is set up)
4. **Request review** from maintainers
5. **Respond to feedback** promptly

## 🛡️ Security

- Never commit secrets, API keys, or credentials
- Use `.env` files for sensitive configuration (not committed)
- Follow security best practices in instructions
- Report security vulnerabilities privately to the maintainer

## 📚 Additional Resources

- [GitHub Copilot Coding Agent Documentation](https://docs.github.com/en/copilot/tutorials/coding-agent)
- [GitHub Copilot Instructions Guide](https://design.dev/guides/copilot-instructions/)
- [Project README](../README.md)
- [Copilot Instructions](.github/copilot-instructions.md)

## 📧 Contact

**Developer & Creator**: أحمد بن محمد بن جمعان بن مبارك الدوسري  
**Copyright**: © 2025-2026 All rights reserved

For questions or suggestions, please open an issue on GitHub.

---

Thank you for contributing to RawanAI! 💜
