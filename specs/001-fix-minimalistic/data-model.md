# Data Model: Fix Minimalistic Mode

**Date**: November 3, 2025
**Feature**: Fix Minimalistic Mode

## Entities

### Background Mask
- **Purpose**: Identifies pixels that should be background (black, no characters)
- **Attributes**:
  - `mask`: 2D boolean array - True for background pixels
  - `background_color`: RGB tuple - detected background color
  - `threshold`: Float - color distance threshold for classification

### Edge Mask
- **Purpose**: Identifies pixels that are subject edges for enhancement
- **Attributes**:
  - `edges`: 2D boolean array - True for edge pixels
  - `enhancement_factor`: Float - contrast boost for edges

### Minimalistic Output
- **Purpose**: Final ASCII art with black background and enhanced edges
- **Attributes**:
  - `ascii_grid`: 2D array - characters (empty strings for background)
  - `color_mappings`: 2D array - colors (black for background, enhanced for edges)
  - `background_pixels`: Integer - count of background pixels
  - `edge_pixels`: Integer - count of enhanced edge pixels

## Relationships

- **Background Mask** → **Minimalistic Output**: Determines where no characters are rendered
- **Edge Mask** → **Minimalistic Output**: Determines where colors are enhanced
- **Input Image** → **Background Mask**: Source for background detection

## Validation Rules

- **Background Purity**: All background pixels must be RGB(0,0,0) in output
- **No Background Characters**: ASCII grid must have empty strings for background positions
- **Edge Enhancement**: Edge pixels must have higher contrast than original
- **Internal Preservation**: Non-edge subject pixels unchanged from standard mode</content>
<parameter name="filePath">c:\Dev\ascii-g\specs\001-fix-minimalistic\data-model.md