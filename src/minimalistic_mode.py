#!/usr/bin/env python3
"""
Minimalistic Mode Module for ASCII Art Generator.

Applies edge detection and background removal for minimalistic ASCII art.
"""

import cv2
import numpy as np
from PIL import Image


def apply_minimalistic_mode(image: Image.Image) -> tuple[Image.Image, np.ndarray]:
    """
    Apply minimalistic mode processing to an image.

    Sets background pixels to black and emphasizes edges without altering
    internal character colors.

    Args:
        image: Input PIL Image

    Returns:
        Tuple of (processed PIL Image, background mask as boolean array)
    """
    # Convert to numpy array
    img_array = np.array(image)

    # Convert to grayscale for edge detection
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Apply Canny edge detection with tuned parameters
    edges = cv2.Canny(gray, 50, 150)

    # Estimate background color from border pixels
    border_pixels = np.concatenate([
        img_array[0, :],      # top border
        img_array[-1, :],     # bottom border
        img_array[:, 0],      # left border
        img_array[:, -1]      # right border
    ])
    bg_color = np.median(border_pixels, axis=0).astype(np.uint8)

    # Create new image array for processing
    new_img = img_array.copy()

    # Create background mask
    height, width = img_array.shape[:2]
    bg_mask = np.zeros((height, width), dtype=bool)
    
    # Process each pixel
    for i in range(height):
        for j in range(width):
            pixel = img_array[i, j]
            # Calculate color distance to background
            color_distance = np.linalg.norm(pixel.astype(np.float32) - bg_color.astype(np.float32))

            # If pixel is close to background color, mark as background
            if color_distance < 50:  # threshold for background detection
                bg_mask[i, j] = True
                new_img[i, j] = [0, 0, 0]
            # If pixel is on an edge, emphasize it
            elif edges[i, j] > 0:
                # Amplify edge pixels by 100% while preserving color gradients
                new_img[i, j] = np.clip(pixel * 2.0, 0, 255).astype(np.uint8)

    return Image.fromarray(new_img), bg_mask