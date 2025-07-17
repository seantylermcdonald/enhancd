#!/usr/bin/env python3
"""
Setup script for Photo Upscaler CLI
"""

import os
import subprocess
import sys
from pathlib import Path

def create_folders():
    """Create necessary folders"""
    folders = ['input', 'output']
    for folder in folders:
        Path(folder).mkdir(exist_ok=True)
        print(f"✓ Created/verified folder: {folder}")

def install_requirements():
    """Install required packages"""
    try:
        print("Installing required packages...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✓ All packages installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing packages: {e}")
        return False
    return True

def main():
    print("🖼️  Photo Upscaler CLI Setup")
    print("=" * 40)
    
    # Create folders
    create_folders()
    
    # Install requirements
    if install_requirements():
        print("\n✓ Setup complete!")
        print("\nUsage:")
        print("1. Place your images in the 'input' folder")
        print("2. Run: python upscaler.py")
        print("3. Check the 'output' folder for upscaled images")
        print("\nFor more options: python upscaler.py --help")
    else:
        print("\n✗ Setup failed. Please check the error messages above.")

if __name__ == '__main__':
    main()
