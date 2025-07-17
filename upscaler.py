#!/usr/bin/env python3
"""
Photo Upscaler CLI - A command line tool for upscaling photos
"""

import os
import sys
import click
from PIL import Image
import cv2
import numpy as np
from pathlib import Path
import shutil


class PhotoUpscaler:
    """Main class for handling photo upscaling operations"""
    
    def __init__(self, input_folder="input", output_folder="output"):
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
        
        # Create folders if they don't exist
        self.input_folder.mkdir(exist_ok=True)
        self.output_folder.mkdir(exist_ok=True)
    
    def get_image_files(self):
        """Get all supported image files from input folder"""
        image_files = []
        for file_path in self.input_folder.iterdir():
            if file_path.is_file() and file_path.suffix.lower() in self.supported_formats:
                image_files.append(file_path)
        return sorted(image_files)
    
    def upscale_image(self, image_path, scale_factor=2, method='lanczos'):
        """Upscale an image using specified method"""
        try:
            with Image.open(image_path) as img:
                # Get original dimensions
                width, height = img.size
                
                # Calculate new dimensions
                new_width = int(width * scale_factor)
                new_height = int(height * scale_factor)
                
                # Choose resampling method
                if method == 'lanczos':
                    resampling = Image.LANCZOS
                elif method == 'bicubic':
                    resampling = Image.BICUBIC
                elif method == 'bilinear':
                    resampling = Image.BILINEAR
                else:
                    resampling = Image.LANCZOS
                
                # Upscale the image
                upscaled_img = img.resize((new_width, new_height), resampling)
                
                return upscaled_img
                
        except Exception as e:
            click.echo(f"Error upscaling {image_path}: {str(e)}", err=True)
            return None
    
    def generate_output_filename(self, base_name, extension):
        """Generate output filename with incremental numbering if file exists"""
        counter = 1
        output_path = self.output_folder / f"{base_name}{extension}"
        
        while output_path.exists():
            output_path = self.output_folder / f"{base_name}_{counter}{extension}"
            counter += 1
        
        return output_path
    
    def process_images(self, scale_factor=2, method='lanczos', custom_name=None):
        """Process all images in the input folder"""
        image_files = self.get_image_files()
        
        if not image_files:
            click.echo("No image files found in the input folder.")
            return
        
        click.echo(f"Found {len(image_files)} image(s) to process.")
        
        for i, image_path in enumerate(image_files):
            click.echo(f"Processing {image_path.name}...")
            
            # Upscale the image
            upscaled_img = self.upscale_image(image_path, scale_factor, method)
            
            if upscaled_img is None:
                continue
            
            # Determine output filename
            if custom_name and i == 0:
                # Use custom name for first image
                base_name = custom_name
            elif custom_name:
                # Use custom name with incremental number for subsequent images
                base_name = f"{custom_name}_{i}"
            else:
                # Use original filename with _upscaled suffix
                base_name = f"{image_path.stem}_upscaled"
            
            extension = image_path.suffix
            output_path = self.generate_output_filename(base_name, extension)
            
            # Save the upscaled image
            try:
                upscaled_img.save(output_path, quality=95)
                click.echo(f"✓ Saved: {output_path.name}")
            except Exception as e:
                click.echo(f"✗ Error saving {output_path.name}: {str(e)}", err=True)
        
        click.echo(f"\nProcessing complete! Check the '{self.output_folder}' folder.")


@click.command()
@click.option('--input-folder', '-i', default='input', 
              help='Input folder containing images to upscale (default: input)')
@click.option('--output-folder', '-o', default='output', 
              help='Output folder for upscaled images (default: output)')
@click.option('--scale', '-s', default=2.0, type=float,
              help='Scale factor for upscaling (default: 2.0)')
@click.option('--method', '-m', default='lanczos',
              type=click.Choice(['lanczos', 'bicubic', 'bilinear']),
              help='Upscaling method (default: lanczos)')
@click.option('--custom-name', '-n', default=None,
              help='Custom base name for output files')
@click.option('--prompt-name', '-p', is_flag=True,
              help='Prompt for custom filename during execution')
def main(input_folder, output_folder, scale, method, custom_name, prompt_name):
    """
    Photo Upscaler CLI - Upscale photos from input folder to output folder
    
    This tool will:
    1. Read all supported image files from the input folder
    2. Upscale them using the specified method and scale factor
    3. Save them to the output folder with optional custom naming
    """
    
    click.echo("🖼️  Photo Upscaler CLI")
    click.echo("=" * 50)
    
    # Initialize upscaler
    upscaler = PhotoUpscaler(input_folder, output_folder)
    
    # Check if input folder has images
    image_files = upscaler.get_image_files()
    if not image_files:
        click.echo(f"No image files found in '{input_folder}' folder.")
        click.echo("Please add some images to the input folder and try again.")
        return
    
    # Display current settings
    click.echo(f"Input folder: {input_folder}")
    click.echo(f"Output folder: {output_folder}")
    click.echo(f"Scale factor: {scale}x")
    click.echo(f"Method: {method}")
    click.echo(f"Images found: {len(image_files)}")
    
    # Handle custom naming
    if prompt_name:
        custom_name = click.prompt("\nEnter custom base name for output files (or press Enter to use original names)", 
                                 default="", show_default=False)
        if not custom_name.strip():
            custom_name = None
    
    if custom_name:
        click.echo(f"Using custom base name: {custom_name}")
    
    # Confirm before processing
    if not click.confirm("\nProceed with upscaling?"):
        click.echo("Operation cancelled.")
        return
    
    # Process images
    click.echo("\nStarting upscaling process...")
    upscaler.process_images(scale, method, custom_name)


if __name__ == '__main__':
    main()
