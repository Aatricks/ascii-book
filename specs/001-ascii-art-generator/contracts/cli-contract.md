# CLI Contracts: ASCII Art Generator

**Date**: November 3, 2025
**Feature**: ASCII Art Generator

## CLI Interface Specification

Following constitution principle II. CLI Interface, all functionality is exposed via command-line interface with stdin/args input and stdout output.

### Command: ascii-generator

**Purpose**: Generate ASCII art from input image

**Usage**:
```
python src/ascii_generator.py <input_image> <output_image> [options]
```

**Parameters**:
- `input_image`: Path to input image file (required)
- `output_image`: Path to output image file (required)
- `--minimalistic`: Enable minimalistic mode (optional)
- `--char-width`: Width of each ASCII character in pixels (default: 8)
- `--char-height`: Height of each ASCII character in pixels (default: 12)
- `--density`: Character density multiplier (default: 1.0, higher = more detail)

**Input**: Image file path via command line argument

**Output**: 
- Success: Creates output image file, returns exit code 0
- Error: Prints error message to stderr, returns exit code 1

**Examples**:
```bash
# Basic ASCII art generation
python src/ascii_generator.py input.png output.png

# High-density ASCII art
python src/ascii_generator.py input.jpg output.jpg --density 2.0

# Minimalistic mode
python src/ascii_generator.py input.png output.png --minimalistic
```

### Error Handling

- Invalid input file: "Error: Input file not found or unreadable"
- Unsupported format: "Error: Unsupported image format. Supported: PNG, JPG, BMP, GIF"
- Output path issues: "Error: Cannot write to output path"
- Processing errors: "Error: Failed to process image: [details]"

### Data Formats

**Input**: Standard image files (binary)

**Output**: Image file containing ASCII art (binary)

**Logs**: Human-readable text to stdout/stderr, structured JSON available with --json flag