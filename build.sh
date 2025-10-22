#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
echo "=== Starting build process ==="
echo "Python version: $(python --version)"

# Upgrade pip and build tools
echo "=== Upgrading pip and build tools ==="
pip install --upgrade pip setuptools wheel

pip install -r requirements.txt

echo "=== Build process completed ==="