.PHONY: help install install-dev test lint format clean run verify docker-build docker-run

help:
	@echo "RawanAI Development Commands"
	@echo "============================"
	@echo "make install      - Install production dependencies"
	@echo "make install-dev  - Install development dependencies"
	@echo "make test         - Run tests"
	@echo "make lint         - Run linting checks"
	@echo "make format       - Format code with black and isort"
	@echo "make clean        - Clean build artifacts and cache"
	@echo "make run          - Run the application"
	@echo "make verify       - Verify installation"
	@echo "make docker-build - Build Docker image"
	@echo "make docker-run   - Run with Docker Compose"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v

test-coverage:
	pytest tests/ --cov=src --cov-report=html --cov-report=term

lint:
	@echo "Running flake8..."
	flake8 src/ tests/ config/ app.py
	@echo "Linting passed!"

format:
	@echo "Formatting with black..."
	black src/ tests/ config/ app.py
	@echo "Sorting imports with isort..."
	isort src/ tests/ config/ app.py
	@echo "Formatting complete!"

clean:
	@echo "Cleaning build artifacts..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache .coverage htmlcov/ build/ dist/
	@echo "Clean complete!"

run:
	python app.py

verify:
	python verify_installation.py

docker-build:
	docker build -t rawanai:latest .

docker-run:
	docker-compose up -d

docker-stop:
	docker-compose down
