#!/bin/bash

# Photo Upscaler CLI - Easy run script

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found. Running setup..."
    python3 setup.py
fi

# Activate virtual environment and run the upscaler
source .venv/bin/activate
python upscaler.py "$@"
