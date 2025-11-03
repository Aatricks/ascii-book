"""
Image processing utilities for ASCII art generator.
"""

from PIL import Image
import numpy as np


def load_image(image_path: str) -> Image.Image:
    """
    Load an image from file path.

    Args:
        image_path: Path to the image file

    Returns:
        PIL Image object

    Raises:
        FileNotFoundError: If image file doesn't exist
        ValueError: If image format is unsupported
    """
    try:
        img = Image.open(image_path)
        # Convert to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')
        return img
    except FileNotFoundError:
        raise FileNotFoundError(f"Image file not found: {image_path}")
    except Exception as e:
        raise ValueError(f"Unsupported image format or corrupted file: {e}")


def validate_image_dimensions(img: Image.Image, max_size: tuple = (4096, 4096)) -> None:
    """
    Validate image dimensions.

    Args:
        img: PIL Image object
        max_size: Maximum allowed dimensions (width, height)

    Raises:
        ValueError: If image is too large
    """
    if img.width > max_size[0] or img.height > max_size[1]:
        raise ValueError(f"Image too large: {img.size}. Maximum allowed: {max_size}")


def get_image_array(img: Image.Image) -> np.ndarray:
    """
    Convert PIL image to numpy array.

    Args:
        img: PIL Image object

    Returns:
        3D numpy array (height, width, 3) with RGB values
    """
    return np.array(img)