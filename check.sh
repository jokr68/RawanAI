#!/bin/bash
# Quick check script for RawanAI

echo "RawanAI Quick Check"
echo "==================="
echo ""

echo "✓ Checking Python version..."
python --version

echo ""
echo "✓ Checking project structure..."
ls -la src/rawanai/

echo ""
echo "✓ Running tests..."
python -m pytest tests/ -v --tb=short

echo ""
echo "✓ Checking syntax..."
python -m py_compile app.py src/rawanai/*.py config/*.py

echo ""
echo "✓ Verification complete!"
