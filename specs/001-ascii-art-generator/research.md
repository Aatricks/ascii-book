# Research Findings: ASCII Art Generator

**Date**: November 3, 2025
**Feature**: ASCII Art Generator

## Research Tasks Completed

### Task 1: Image to ASCII Art Conversion Techniques

**Decision**: Use luminance-based character mapping with color overlay for high-quality ASCII art generation.

**Rationale**: 
- Luminance mapping provides good detail preservation by using character density to represent brightness levels
- Color overlay maintains gradients by sampling pixel colors and applying them to characters
- High character density (many characters per image) ensures detail retention
- Python Pillow library provides efficient image processing capabilities

**Alternatives Considered**:
- Pure color ASCII: Using colored characters without density mapping - rejected due to poor readability and detail loss
- Fixed character set: Using same character for all pixels - rejected as it loses too much visual information
- Vector-based ASCII: Converting to vector art first - rejected due to complexity and loss of photographic details

**Implementation Approach**:
- Convert image to grayscale for luminance values
- Map luminance ranges to ASCII characters by density (darkest to lightest)
- Sample original colors at character positions
- Render characters with corresponding colors to output image

### Task 2: Edge Detection for Minimalistic Mode

**Decision**: Use Canny edge detection with careful masking to emphasize edges without altering character interiors.

**Rationale**:
- Canny algorithm provides clean edge detection with good noise reduction
- Can apply edge enhancement only to detected edges, preserving internal character colors
- Python OpenCV provides robust Canny implementation
- Careful parameter tuning prevents detection of internal character features

**Alternatives Considered**:
- Sobel operator: Simpler but more noisy edges - rejected for quality
- Laplacian edge detection: Good for fine details but sensitive to noise - rejected
- Manual thresholding: Too simplistic for complex images - rejected

**Implementation Approach**:
- Apply Canny edge detection to input image
- Create edge mask
- For minimalistic mode: set non-edge areas to black, enhance edge areas
- Ensure color preservation in non-edge regions of characters

### Task 3: Analysis of Example Repository (ascii-view)

**Decision**: Study the ascii-view repository for color ASCII rendering techniques and output as image approach.

**Rationale**:
- Repository demonstrates outputting ASCII art as images rather than text
- Shows color handling in ASCII art
- Provides reference implementation for quality expectations
- Python-based, compatible with our tech stack

**Key Insights**:
- Uses image rendering for ASCII output (not text console)
- Employs color mapping techniques
- Demonstrates high-quality ASCII art generation
- Reference for user interface and output format

**Implementation Approach**:
- Adapt color mapping strategies from ascii-view
- Use similar image output methodology
- Reference quality benchmarks from the example

## Resolved Technical Unknowns

- **ASCII Character Density**: Use 80+ characters for high detail preservation
- **Color Mapping**: Sample colors at character centers, apply to entire character
- **Edge Detection Parameters**: Canny with sigma 1.0, thresholds 50-150 for clean edges
- **Output Format**: PNG/JPG images containing colored ASCII text
- **Performance Optimization**: Process images in tiles for large files

## Dependencies Confirmed

- Pillow: Image loading, processing, color manipulation
- OpenCV: Edge detection for minimalistic mode
- NumPy: Array operations for image data
- Jupyter: Interactive demo environment