"""
ASCII character constants for art generation.
Characters ordered from darkest to lightest for density mapping.
"""

# ASCII characters ordered by visual density (darkest to lightest)
ASCII_CHARS = "@%#*+=-:. "

# Character density weights (0-255, where 0 is darkest)
DENSITY_MAP = {
    '@': 0,    # Darkest
    '%': 32,
    '#': 64,
    '*': 96,
    '+': 128,
    '=': 160,
    '-': 192,
    ':': 224,
    '.': 240,
    ' ': 255   # Lightest
}

# Number of characters for high-density mapping
NUM_CHARS = len(ASCII_CHARS)

def get_char_for_density(density: float) -> str:
    """
    Get ASCII character for a given density value.

    Args:
        density: Float between 0.0 (darkest) and 1.0 (lightest)

    Returns:
        ASCII character
    """
    if density < 0.0:
        density = 0.0
    elif density > 1.0:
        density = 1.0

    # Map density to character index
    index = int(density * (NUM_CHARS - 1))
    return ASCII_CHARS[index]