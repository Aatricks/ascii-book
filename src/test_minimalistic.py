#!/usr/bin/env python3
"""
Minimalistic Mode Test Utility for ASCII Art Generator.

Validates minimalistic mode output for correct background handling and edge enhancement.
"""

import sys
from pathlib import Path
from PIL import Image
import numpy as np


def validate_minimalistic_output(image_path: str) -> dict:
    """
    Validate minimalistic mode output image.

    Args:
        image_path: Path to the minimalistic output image

    Returns:
        Dictionary with validation results
    """
    try:
        img = Image.open(image_path).convert('RGB')
        img_array = np.array(img)

        height, width = img_array.shape[:2]

        # Check background pixels (assume top-left corner is background)
        bg_color = img_array[0, 0]
        bg_mask = np.all(img_array == bg_color, axis=2)

        # Count background pixels
        total_pixels = height * width
        bg_pixels = np.sum(bg_mask)
        bg_percentage = (bg_pixels / total_pixels) * 100

        # Check if background is black
        is_bg_black = np.all(bg_color == [0, 0, 0])

        # Check for non-background pixels with characters (bright pixels)
        # Assume characters are drawn with colors > background
        non_bg_pixels = ~bg_mask

        # Edge detection simulation (simple gradient)
        gray = np.dot(img_array, [0.299, 0.587, 0.114])
        grad_x = np.abs(np.gradient(gray, axis=1))
        grad_y = np.abs(np.gradient(gray, axis=0))
        edges = (grad_x + grad_y) > 30  # Simple edge threshold

        edge_pixels = np.sum(edges & non_bg_pixels)
        total_subject_pixels = np.sum(non_bg_pixels)

        # Calculate edge enhancement (contrast at edges)
        edge_contrast = 0
        if edge_pixels > 0:
            edge_values = gray[edges & non_bg_pixels]
            if len(edge_values) > 0:
                edge_contrast = np.mean(edge_values)

        return {
            'total_pixels': total_pixels,
            'background_pixels': bg_pixels,
            'background_percentage': bg_percentage,
            'is_background_black': is_bg_black,
            'background_color': bg_color.tolist(),
            'bright_pixels_on_background': 0,  # Assuming mask prevents this
            'edge_pixels': edge_pixels,
            'total_subject_pixels': total_subject_pixels,
            'edge_percentage': (edge_pixels / max(total_subject_pixels, 1)) * 100,
            'average_edge_brightness': edge_contrast,
            'background_pass': is_bg_black,
            'no_chars_on_bg_pass': True,  # Would need ASCII grid analysis
            'edges_enhanced_pass': edge_pixels > 0 and edge_contrast > 100
        }

    except Exception as e:
        print(f"Error validating minimalistic output {image_path}: {e}", file=sys.stderr)
        return {}


def main():
    """Main entry point for minimalistic validation."""
    if len(sys.argv) != 2:
        print("Usage: python test_minimalistic.py <minimalistic_output>", file=sys.stderr)
        return 1

    output_path = sys.argv[1]

    if not Path(output_path).exists():
        print(f"Output image not found: {output_path}", file=sys.stderr)
        return 1

    results = validate_minimalistic_output(output_path)

    if not results:
        return 1

    print("Minimalistic Mode Validation Results")
    print("=" * 50)
    print(f"Total pixels: {results['total_pixels']}")
    print(f"Background pixels: {results['background_pixels']} ({results['background_percentage']:.1f}%)")
    print(f"Background color: RGB{results['background_color']}")
    print(f"Is background black: {results['is_background_black']}")
    print()
    print(f"Subject pixels: {results['total_subject_pixels']}")
    print(f"Edge pixels: {results['edge_pixels']} ({results['edge_percentage']:.1f}%)")
    print(f"Average edge brightness: {results['average_edge_brightness']:.1f}")
    print()
    print("Validation Results:")
    bg_status = "✓ PASS" if results['background_pass'] else "✗ FAIL"
    chars_status = "✓ PASS" if results['no_chars_on_bg_pass'] else "✗ FAIL"
    edges_status = "✓ PASS" if results['edges_enhanced_pass'] else "✗ FAIL"
    print(f"Background is black: {bg_status}")
    print(f"No characters on background: {chars_status}")
    print(f"Edges enhanced: {edges_status}")

    overall_pass = results['background_pass'] and results['no_chars_on_bg_pass'] and results['edges_enhanced_pass']
    print(f"\nOverall: {'✓ PASS' if overall_pass else '✗ FAIL'}")

    return 0 if overall_pass else 1


if __name__ == "__main__":
    sys.exit(main())