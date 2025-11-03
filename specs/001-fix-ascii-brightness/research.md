# Research Findings: Fix ASCII Brightness and Colors

**Date**: November 3, 2025
**Feature**: Fix ASCII Brightness and Colors

## Research Tasks Completed

### Task 1: Causes of Brightness Inaccuracy in ASCII Art Generation

**Decision**: Implement gamma-corrected luminance calculation and area-averaged color sampling.

**Rationale**:
- Current linear luminance mapping doesn't account for human brightness perception (gamma ~2.2)
- Single-point color sampling at character centers misses color gradients within character blocks
- Over-brightening occurs because ASCII characters are perceived brighter than their pixel values suggest

**Alternatives Considered**:
- Character set optimization: Using different ASCII characters - rejected because the issue is in calculation, not character choice
- Histogram equalization: Automatic brightness adjustment - rejected as it would alter the artistic intent
- Fixed gamma values: Hard-coded gamma correction - rejected in favor of configurable approach

**Implementation Approach**:
- Apply gamma correction (γ=2.2) to luminance values before character mapping
- Sample colors by averaging over the entire character block area
- Add brightness calibration factor for fine-tuning

### Task 2: Best Practices for Color Calibration in Image Processing

**Decision**: Use CIE L*a*b* color space for accurate color difference measurement and sRGB gamma correction.

**Rationale**:
- CIE L*a*b* provides perceptually uniform color differences (delta E)
- sRGB gamma correction ensures colors match display standards
- Color averaging prevents artifacts from single-pixel sampling

**Alternatives Considered**:
- HSV color space: Good for hue/saturation but less accurate for brightness perception
- RGB averaging: Simple but doesn't account for perceptual uniformity
- No gamma correction: Maintains original colors but doesn't fix brightness perception

**Implementation Approach**:
- Convert RGB to linear color space for averaging
- Apply sRGB gamma correction before output
- Calculate mean color levels for validation testing

## Resolved Technical Unknowns

- **Brightness Calculation**: Use gamma-corrected luminance: L = (0.299*R + 0.587*G + 0.114*B)^(1/2.2)
- **Color Sampling**: Average RGB values over character block, then apply gamma correction
- **Validation Method**: Compare mean RGB values between original and ASCII output
- **Calibration Factor**: Add adjustable brightness multiplier (default 0.8-0.9)

## Dependencies Confirmed

- Pillow: For image processing and color space conversions
- NumPy: For efficient array operations and averaging
- OpenCV: Already available for any additional processing if needed</content>
<parameter name="filePath">c:\Dev\ascii-g\specs\001-fix-ascii-brightness\research.md