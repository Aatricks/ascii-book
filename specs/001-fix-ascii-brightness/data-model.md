# Data Model: Fix ASCII Brightness and Colors

**Date**: November 3, 2025
**Feature**: Fix ASCII Brightness and Colors

## Entities

### Input Image
- **Purpose**: Source image for ASCII art generation
- **Attributes**:
  - `width`: Integer - Image width in pixels
  - `height`: Integer - Image height in pixels
  - `mode`: String - Color mode (RGB, RGBA, etc.)
  - `pixels`: Array - Pixel data as RGB tuples
  - `mean_brightness`: Float - Average brightness level (0-255)
  - `color_histogram`: Dict - RGB color distribution

### ASCII Output Image
- **Purpose**: Generated ASCII art with corrected brightness and colors
- **Attributes**:
  - `width`: Integer - Output width in pixels
  - `height`: Integer - Output height in pixels
  - `ascii_grid`: 2D Array - ASCII characters used
  - `color_mappings`: Dict - Color data for each character position
  - `mean_brightness`: Float - Average brightness level (should match input within tolerance)
  - `brightness_correction_factor`: Float - Applied correction factor

## Relationships

- **Input Image** → **ASCII Output Image**: One-to-one transformation
- **Validation**: Compare `mean_brightness` between input and output

## Validation Rules

- **Brightness Accuracy**: |input.mean_brightness - output.mean_brightness| < 25.5 (10% of 255)
- **Color Preservation**: RGB values maintain relative proportions
- **No Data Loss**: All input pixels contribute to output</content>
<parameter name="filePath">c:\Dev\ascii-g\specs\001-fix-ascii-brightness\data-model.md