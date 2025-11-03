# Quick Start: Fix ASCII Brightness and Colors

**Date**: November 3, 2025
**Feature**: Fix ASCII Brightness and Colors

## Prerequisites

- Python 3.12+
- Virtual environment (recommended)
- Required packages: pillow, opencv-python, numpy

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ascii-book
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install pillow opencv-python numpy
   ```

## Basic Usage

### Command Line

1. **Generate ASCII art with brightness fix**:
   ```bash
   python src/ascii_generator.py input.png output.png
   ```

2. **Generate high-detail ASCII art**:
   ```bash
   python src/ascii_generator.py input.jpg output.jpg --density 2.0
   ```

3. **Generate minimalistic ASCII art**:
   ```bash
   python src/ascii_generator.py input.png output.png --minimalistic
   ```

### Testing Brightness Fix

1. **Compare brightness levels**:
   ```python
   from PIL import Image
   import numpy as np

   # Load images
   original = Image.open('input.png')
   ascii_art = Image.open('output.png')

   # Calculate mean brightness
   orig_mean = np.mean(np.array(original.convert('L')))
   ascii_mean = np.mean(np.array(ascii_art.convert('L')))

   print(f"Original brightness: {orig_mean}")
   print(f"ASCII brightness: {ascii_mean}")
   print(f"Difference: {abs(orig_mean - ascii_mean)}")
   ```

## Examples

### Brightness Comparison
- Input: `input.png` (original image)
- Output: `ascii_output.png` (ASCII art with corrected brightness)
- Validation: Mean brightness difference should be < 25.5 (10% of 255 range)

## Testing Brightness Fix

1. **Compare brightness levels**:
   ```bash
   python src/brightness_utils.py <original_image> <ascii_output>
   ```

   Expected: Brightness difference < 10%, Color difference < 25.5

## Examples

### Brightness Fix Validation
- Input: `input.png` (original image)
- Output: `ascii_output.png` (ASCII art with corrected brightness)
- Validation: Run brightness comparison tool - should show ✓ PASS

## Troubleshooting

- **Brightness still inaccurate**: Adjust brightness_factor in ASCIIGenerator (default 1.0)
- **Colors not matching**: Verify linear color space conversion in ascii_renderer.py
- **Background affecting measurement**: Ensure black background and exclude background pixels in calculations
- **Import errors**: Ensure all packages are installed
- **Memory issues**: Reduce image size or density for large images

## Development

- Run tests: `python -m unittest discover tests/`
- Validate fix: Use brightness_utils.py to compare before/after
- Adjust parameters: Modify brightness_factor in ascii_renderer.py for fine-tuning</content>
<parameter name="filePath">c:\Dev\ascii-g\specs\001-fix-ascii-brightness\quickstart.md