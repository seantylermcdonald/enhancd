# Photo Upscaler CLI

A command-line tool for upscaling photos with customizable naming and output options.

## Features

- **Batch Processing**: Upscale multiple images at once
- **Multiple Upscaling Methods**: Lanczos, Bicubic, and Bilinear
- **Custom Naming**: Prompt for custom filenames or use original names
- **Auto-numbering**: Automatically append numbers to avoid filename conflicts
- **Flexible Scale Factors**: Any scale factor (2x, 3x, 1.5x, etc.)
- **Multiple Format Support**: JPEG, PNG, BMP, TIFF, WebP

## Installation

1. Clone or download this project
2. Run the setup script:
   ```bash
   python setup.py
   ```

This will:
- Install required dependencies (Pillow, Click, OpenCV, NumPy)
- Create `input` and `output` folders

## Usage

### Basic Usage

1. Place your images in the `input` folder
2. Run the upscaler:
   ```bash
   python upscaler.py
   ```

### Advanced Options

```bash
# Custom scale factor
python upscaler.py --scale 3.0

# Different upscaling method
python upscaler.py --method bicubic

# Custom input/output folders
python upscaler.py --input-folder /path/to/images --output-folder /path/to/output

# Prompt for custom filename
python upscaler.py --prompt-name

# Use predefined custom name
python upscaler.py --custom-name "upscaled_photo"
```

### Command Options

- `--input-folder, -i`: Input folder containing images (default: input)
- `--output-folder, -o`: Output folder for upscaled images (default: output)
- `--scale, -s`: Scale factor for upscaling (default: 2.0)
- `--method, -m`: Upscaling method (lanczos, bicubic, bilinear)
- `--custom-name, -n`: Custom base name for output files
- `--prompt-name, -p`: Prompt for custom filename during execution

## Examples

### Example 1: Basic upscaling with 2x scale
```bash
python upscaler.py
```

### Example 2: Custom naming with prompting
```bash
python upscaler.py --prompt-name
```
When prompted, enter a custom name like "enhanced_photo". The output files will be:
- `enhanced_photo.jpg`
- `enhanced_photo_1.jpg`
- `enhanced_photo_2.jpg`
- etc.

### Example 3: High-quality 4x upscaling
```bash
python upscaler.py --scale 4.0 --method lanczos
```

### Example 4: Batch processing with custom folders
```bash
python upscaler.py -i /home/user/photos -o /home/user/upscaled -s 3.0
```

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- WebP (.webp)

## File Naming

The tool handles file naming intelligently:

1. **Original naming**: `photo.jpg` → `photo_upscaled.jpg`
2. **Custom naming**: `photo.jpg` → `custom_name.jpg`
3. **Multiple files with custom naming**:
   - First file: `custom_name.jpg`
   - Second file: `custom_name_1.jpg`
   - Third file: `custom_name_2.jpg`
   - etc.

## Requirements

- Python 3.6+
- Pillow (PIL)
- Click
- OpenCV
- NumPy

## License

MIT License - Feel free to use and modify as needed.
