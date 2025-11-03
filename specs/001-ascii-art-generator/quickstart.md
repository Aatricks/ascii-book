# Quick Start: ASCII Art Generator

**Date**: November 3, 2025
**Feature**: ASCII Art Generator

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

1. **Generate standard ASCII art**:
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

### Jupyter Notebook Demo

1. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```

2. **Open the demo notebook**:
   - Navigate to `notebooks/demo.ipynb`
   - Run cells to see interactive ASCII art generation

## Examples

### Standard Mode
- Input: `input.png` (photograph)
- Output: `ascii_output.png` (image with colored ASCII characters)

### Minimalistic Mode
- Input: `portrait.jpg` (person on background)
- Output: `minimalistic_output.png` (black background, emphasized character edges)

## Troubleshooting

- **Import errors**: Ensure all packages are installed
- **Memory issues**: Reduce image size or density for large images
- **Quality issues**: Increase density parameter for more detail
- **Edge artifacts**: Adjust minimalistic mode parameters if needed

## Development

- Run tests: `python -m unittest discover tests/`
- Add new features: Follow the spec in `specs/001-ascii-art-generator/spec.md`