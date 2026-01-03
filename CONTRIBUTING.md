# Contributing to RawanAI

Thank you for your interest in contributing to RawanAI! This document provides guidelines for contributing to the project.

## Copyright Notice

This project is copyrighted by Ahmed bin Mohammed bin Jum'an bin Mubarak Al-Dosari © 2025. All rights reserved. Please review the license terms before contributing.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jokr68/RawanAI.git
   cd RawanAI
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Code Style

We follow these conventions:
- Use Black for code formatting: `black .`
- Use isort for import sorting: `isort .`
- Use flake8 for linting: `flake8`
- Use type hints where appropriate

## Testing

Run tests with pytest:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=src --cov-report=html
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Run tests and linting
5. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

## Code Review

All submissions require review. We use GitHub pull requests for this purpose.

## Questions?

If you have questions, please open an issue on GitHub.
