# Research Findings: Fix Minimalistic Mode

**Date**: November 3, 2025
**Feature**: Fix Minimalistic Mode

## Research Tasks Completed

### Task 1: Background Detection Techniques

**Decision**: Use border pixel sampling with color distance thresholding to detect background areas.

**Rationale**:
- Border pixels reliably represent background for centered subjects
- Color distance thresholding handles slight variations in background color
- Simple and effective for typical use cases (subject on uniform background)

**Alternatives Considered**:
- Flood fill from corners: Too sensitive to subject proximity to borders
- K-means clustering: Overkill for simple background detection
- Histogram analysis: May fail with complex images

**Implementation Approach**:
- Sample pixels from image borders
- Calculate median color as background reference
- Use Euclidean distance in RGB space for background classification

### Task 2: Preventing Characters on Background

**Decision**: Create background mask and skip character rendering for background pixels.

**Rationale**:
- Direct masking prevents any characters on background areas
- Maintains clean black background as specified
- Preserves subject rendering integrity

**Alternatives Considered**:
- Post-processing removal: Complex and error-prone
- Conditional rendering: Less efficient than masking
- Alpha channel masking: Unnecessary for RGB images

**Implementation Approach**:
- Generate binary mask of background pixels
- Skip ASCII grid population for masked areas
- Ensure renderer respects the mask

### Task 3: Edge Enhancement Without Internal Alteration

**Decision**: Apply contrast enhancement only to detected edge pixels, preserve original colors elsewhere.

**Rationale**:
- Canny edge detection provides clean edge identification
- Selective enhancement maintains internal color integrity
- Contrast amplification creates visible edge emphasis

**Alternatives Considered**:
- Global contrast adjustment: Affects entire image including internals
- Edge thickening: May create artifacts
- Color shifting: Alters the artistic intent

**Implementation Approach**:
- Detect edges using Canny algorithm
- Apply contrast boost factor to edge pixels only
- Keep non-edge pixels unchanged

## Resolved Technical Unknowns

- **Background Detection**: Sample border pixels, median color, distance threshold 50
- **Character Prevention**: Binary mask, skip rendering for background pixels
- **Edge Enhancement**: Canny edges, 20% contrast boost on edge pixels only
- **Color Preservation**: Process edges separately from color mapping

## Dependencies Confirmed

- Pillow: For image processing and border sampling
- OpenCV: For Canny edge detection
- NumPy: For efficient array operations and masking</content>
<parameter name="filePath">c:\Dev\ascii-g\specs\001-fix-minimalistic\research.md