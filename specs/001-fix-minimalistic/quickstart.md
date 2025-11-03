# Quick Start: Fix Minimalistic Mode

**Date**: November 3, 2025
**Feature**: Fix Minimalistic Mode

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

3. **Generate fixed minimalistic ASCII art**:
   ```bash
   python src/ascii_generator.py input.png output.png --minimalistic
   ```

### Testing Minimalistic Fix

1. **Visual inspection**:
   - Background should be pure black with no characters
   - Subject edges should be emphasized
   - Internal subject colors unchanged

2. **Automated validation**:
   ```bash
   python src/test_minimalistic.py <minimalistic_output>
   ```

   Expected: ✓ PASS for all criteria

## Examples

### Minimalistic Mode Fix
- Input: `portrait.jpg` (girl on gray background)
- Output: `minimalistic_output.png` (black background, no characters on background, emphasized edges)
- Validation: Background RGB(0,0,0), no ASCII on background areas, edges visually enhanced

## Troubleshooting

- **Background not black**: Check border pixel sampling in minimalistic_mode.py
- **Characters on background**: Verify background mask application
- **Edges not emphasized**: Check edge detection parameters
- **Import errors**: Ensure all packages are installed
- **Memory issues**: Reduce image size or density for large images

## Development

- Run tests: `python -m unittest discover tests/`
- Validate fix: Visual inspection of minimalistic output
- Add new features: Follow the spec in `specs/001-fix-minimalistic/spec.md`</content>
<parameter name="filePath">c:\Dev\ascii-g\specs\001-fix-minimalistic\quickstart.md