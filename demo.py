#!/usr/bin/env python3
"""
Demonstration of the Photo Upscaler CLI with custom naming
"""

import subprocess
import sys
import os
from pathlib import Path

def demo_custom_naming():
    """Demonstrate custom naming feature"""
    print("🖼️  Photo Upscaler CLI - Custom Naming Demo")
    print("=" * 50)
    
    # Clear output folder first
    output_folder = Path('output')
    if output_folder.exists():
        for file in output_folder.glob('*'):
            file.unlink()
        print("Cleared output folder")
    
    # Run upscaler with custom name
    print("\n1. Running with custom name 'enhanced_photo':")
    cmd = [
        sys.executable, 'upscaler.py',
        '--custom-name', 'enhanced_photo',
        '--scale', '3.0',
        '--method', 'lanczos'
    ]
    
    # Use expect to automatically answer 'y' to the confirmation prompt
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input='y\n')
    
    print(stdout)
    if stderr:
        print("Errors:", stderr)
    
    # List output files
    print("\n2. Files created:")
    for file in sorted(output_folder.glob('*')):
        print(f"   - {file.name}")
    
    print("\n✓ Demo complete!")

if __name__ == '__main__':
    demo_custom_naming()
