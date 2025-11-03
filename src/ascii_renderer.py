"""
ASCII art renderer for converting images to ASCII art.
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
from typing import Tuple
from ascii_chars import get_char_for_density


def srgb_to_linear(c: float) -> float:
    """Convert sRGB to linear color space."""
    c = c / 255.0
    if c <= 0.04045:
        return c / 12.92
    else:
        return ((c + 0.055) / 1.055) ** 2.4


def linear_to_srgb(c: float) -> float:
    """Convert linear to sRGB color space."""
    if c <= 0.0031308:
        return 12.92 * c * 255.0
    else:
        return (1.055 * (c ** (1/2.4)) - 0.055) * 255.0


class ASCIIGenerator:
    """
    Base class for ASCII art generation.
    """

    def __init__(self, char_width: int = 8, char_height: int = 12, brightness_factor: float = 1.0):
        """
        Initialize ASCII generator.

        Args:
            char_width: Width of each ASCII character in pixels
            char_height: Height of each ASCII character in pixels
            brightness_factor: Factor to adjust brightness (0.0-1.0, lower = darker)
        """
        self.char_width = char_width
        self.char_height = char_height
        self.brightness_factor = brightness_factor

    def image_to_ascii(self, img_array: np.ndarray, bg_mask: np.ndarray = None) -> Tuple[list, list]:
        """
        Convert image array to ASCII grid and color mappings.

        Args:
            img_array: 3D numpy array (height, width, 3) with RGB values
            bg_mask: Boolean array (height, width) - True for background pixels to skip

        Returns:
            Tuple of (ascii_grid, color_mappings)
            ascii_grid: 2D list of ASCII characters
            color_mappings: 2D list of RGB tuples
        """
        height, width = img_array.shape[:2]

        # Calculate ASCII grid dimensions
        ascii_width = width // self.char_width
        ascii_height = height // self.char_height

        ascii_grid = []
        color_mappings = []

        for y in range(ascii_height):
            ascii_row = []
            color_row = []

            for x in range(ascii_width):
                # Sample pixel block for this character position
                start_y = y * self.char_height
                end_y = min(start_y + self.char_height, height)
                start_x = x * self.char_width
                end_x = min(start_x + self.char_width, width)

                # Get pixel block
                pixel_block = img_array[start_y:end_y, start_x:end_x]

                # Convert to linear color space for accurate averaging
                linear_block = np.vectorize(srgb_to_linear)(pixel_block.astype(float))
                avg_linear = np.mean(linear_block, axis=(0, 1))
                
                # Apply brightness correction
                avg_linear *= self.brightness_factor
                
                # Convert back to sRGB for color mapping
                avg_color = np.vectorize(linear_to_srgb)(avg_linear).astype(int)
                avg_color = np.clip(avg_color, 0, 255)  # Ensure valid range
                color_row.append(tuple(avg_color))

                # Calculate luminance in linear space for accurate brightness perception
                luminance = np.dot(avg_linear, [0.2126, 0.7152, 0.0722])

                # Get ASCII character for this luminance
                # For minimalistic mode, if background (black), use space
                if np.all(avg_color == [0, 0, 0]):
                    char = ' '
                else:
                    char = get_char_for_density(luminance)
                ascii_row.append(char)

            ascii_grid.append(ascii_row)
            color_mappings.append(color_row)

        return ascii_grid, color_mappings

    def render_ascii_image(self, ascii_grid: list, color_mappings: list,
                          output_path: str, font_size: int = 10) -> None:
        """
        Render ASCII grid with colors to an image file.

        Args:
            ascii_grid: 2D list of ASCII characters
            color_mappings: 2D list of RGB tuples
            output_path: Path to save the output image
            font_size: Font size for ASCII characters
        """
        if not ascii_grid or not ascii_grid[0]:
            raise ValueError("ASCII grid is empty")

        ascii_height = len(ascii_grid)
        ascii_width = len(ascii_grid[0])

        # Calculate image dimensions
        img_width = ascii_width * self.char_width
        img_height = ascii_height * self.char_height

        # Create new image
        img = Image.new('RGB', (img_width, img_height), color='black')
        draw = ImageDraw.Draw(img)

        # Try to use a monospace font, fall back to default if not available
        try:
            font = ImageFont.truetype("DejaVuSansMono.ttf", font_size)
        except Exception:
            try:
                font = ImageFont.truetype("Courier New.ttf", font_size)
            except Exception:
                font = ImageFont.load_default()

        # Draw each character
        for y, (ascii_row, color_row) in enumerate(zip(ascii_grid, color_mappings)):
            for x, (char, color) in enumerate(zip(ascii_row, color_row)):
                # Position for this character
                pos_x = x * self.char_width
                pos_y = y * self.char_height

                # Draw the character with its color
                draw.text((pos_x, pos_y), char, fill=color, font=font)

        # Save the image
        img.save(output_path)