#!/usr/bin/env python3
"""
Brightness Test Utility for ASCII Art Generator.

Compares brightness and color accuracy between original and ASCII output images.
"""

import sys
from pathlib import Path
from PIL import Image
import numpy as np


def calculate_mean_brightness(image_path: str) -> float:
    """
    Calculate the mean brightness of an image, excluding background pixels.

    Args:
        image_path: Path to the image file

    Returns:
        Mean brightness value (0-255) of non-background pixels
    """
    try:
        img = Image.open(image_path).convert('L')  # Convert to grayscale
        img_array = np.array(img)
        
        # Exclude black background pixels (assume background is 0-10)
        non_background = img_array > 10
        
        if np.any(non_background):
            return np.mean(img_array[non_background])
        else:
            return 0.0
    except Exception as e:
        print(f"Error calculating brightness for {image_path}: {e}", file=sys.stderr)
        return 0.0


def calculate_mean_color(image_path: str) -> tuple[float, float, float]:
    """
    Calculate the mean RGB color of an image, excluding background pixels.

    Args:
        image_path: Path to the image file

    Returns:
        Tuple of mean R, G, B values (0-255) of non-background pixels
    """
    try:
        img = Image.open(image_path).convert('RGB')
        img_array = np.array(img)
        
        # Exclude black background pixels
        # Consider pixel as background if all RGB < 10
        non_background = np.max(img_array, axis=2) > 10
        
        if np.any(non_background):
            # Average only non-background pixels
            masked = img_array[non_background]
            return tuple(np.mean(masked, axis=0))
        else:
            return (0.0, 0.0, 0.0)
    except Exception as e:
        print(f"Error calculating mean color for {image_path}: {e}", file=sys.stderr)
        return (0.0, 0.0, 0.0)


def compare_images(original_path: str, ascii_path: str) -> dict:
    """
    Compare brightness and colors between original and ASCII images.

    Args:
        original_path: Path to original image
        ascii_path: Path to ASCII output image

    Returns:
        Dictionary with comparison results
    """
    orig_brightness = calculate_mean_brightness(original_path)
    ascii_brightness = calculate_mean_brightness(ascii_path)

    orig_color = calculate_mean_color(original_path)
    ascii_color = calculate_mean_color(ascii_path)

    brightness_diff = abs(orig_brightness - ascii_brightness)
    brightness_diff_percent = (brightness_diff / 255.0) * 100

    color_diff = tuple(abs(o - a) for o, a in zip(orig_color, ascii_color))
    max_color_diff = max(color_diff)

    return {
        'original_brightness': orig_brightness,
        'ascii_brightness': ascii_brightness,
        'brightness_difference': brightness_diff,
        'brightness_diff_percent': brightness_diff_percent,
        'original_color': orig_color,
        'ascii_color': ascii_color,
        'color_differences': color_diff,
        'max_color_diff': max_color_diff,
        'brightness_pass': brightness_diff_percent < 10.0,  # 10% tolerance
        'color_pass': max_color_diff < 25.5  # 10% of 255
    }


def main():
    """Main entry point for brightness comparison."""
    if len(sys.argv) != 3:
        print("Usage: python test_brightness.py <original_image> <ascii_image>", file=sys.stderr)
        return 1

    original_path = sys.argv[1]
    ascii_path = sys.argv[2]

    if not Path(original_path).exists():
        print(f"Original image not found: {original_path}", file=sys.stderr)
        return 1

    if not Path(ascii_path).exists():
        print(f"ASCII image not found: {ascii_path}", file=sys.stderr)
        return 1

    results = compare_images(original_path, ascii_path)

    print("Brightness and Color Comparison Results")
    print("=" * 50)
    print(f"Original brightness: {results['original_brightness']:.2f}")
    print(f"ASCII brightness:    {results['ascii_brightness']:.2f}")
    print(f"Brightness difference: {results['brightness_difference']:.2f} ({results['brightness_diff_percent']:.1f}%)")
    print()
    print(f"Original mean color: R={results['original_color'][0]:.1f}, G={results['original_color'][1]:.1f}, B={results['original_color'][2]:.1f}")
    print(f"ASCII mean color:    R={results['ascii_color'][0]:.1f}, G={results['ascii_color'][1]:.1f}, B={results['ascii_color'][2]:.1f}")
    print(f"Color differences:   R={results['color_differences'][0]:.1f}, G={results['color_differences'][1]:.1f}, B={results['color_differences'][2]:.1f}")
    print(f"Max color difference: {results['max_color_diff']:.1f}")
    print()
    print("Validation Results:")
    brightness_status = "✓ PASS" if results['brightness_pass'] else "✗ FAIL"
    color_status = "✓ PASS" if results['color_pass'] else "✗ FAIL"
    print(f"Brightness (< 10% diff): {brightness_status}")
    print(f"Color accuracy (< 25.5 diff): {color_status}")

    overall_pass = results['brightness_pass'] and results['color_pass']
    print(f"\nOverall: {'✓ PASS' if overall_pass else '✗ FAIL'}")

    return 0 if overall_pass else 1


if __name__ == "__main__":
    sys.exit(main())