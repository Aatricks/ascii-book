#!/usr/bin/env python3
"""
Demo script showing brightness and color correction techniques for ASCII art.
"""

import numpy as np
from PIL import Image
from image_enhancement import (
    gamma_correction, histogram_equalization, adaptive_histogram_equalization,
    white_balance, calculate_image_metrics, enhance_for_ascii
)
from ascii_renderer import ASCIIGenerator
from image_processor import get_image_array

def demo_enhancements(input_path: str, output_prefix: str = "demo"):
    """
    Demonstrate various enhancement techniques on an image.

    Args:
        input_path: Path to input image
        output_prefix: Prefix for output files
    """
    print("Loading image...")
    original = Image.open(input_path)

    print("Applying different enhancement techniques...")

    # Technique 1: Gamma correction
    gamma_corrected = gamma_correction(original, gamma=1.5)
    gamma_corrected.save(f"{output_prefix}_gamma.png")
    print("✓ Gamma correction applied (gamma=1.5)")

    # Technique 2: Histogram equalization
    hist_eq = histogram_equalization(original)
    hist_eq.save(f"{output_prefix}_hist_eq.png")
    print("✓ Histogram equalization applied")

    # Technique 3: CLAHE
    clahe = adaptive_histogram_equalization(original)
    clahe.save(f"{output_prefix}_clahe.png")
    print("✓ CLAHE applied")

    # Technique 4: White balance
    wb = white_balance(original)
    wb.save(f"{output_prefix}_white_balance.png")
    print("✓ White balance applied")

    # Technique 5: Comprehensive enhancement
    enhanced = enhance_for_ascii(original)
    enhanced.save(f"{output_prefix}_enhanced.png")
    print("✓ Comprehensive enhancement applied")

    # Calculate metrics
    print("\nCalculating quality metrics...")
    techniques = [
        ("Gamma Correction", gamma_corrected),
        ("Histogram Equalization", hist_eq),
        ("CLAHE", clahe),
        ("White Balance", wb),
        ("Comprehensive Enhancement", enhanced)
    ]

    print(f"{'Technique':<25} {'MSE':<12} {'PSNR':<8} {'Correlation':<12}")
    print("-" * 60)

    for name, img in techniques:
        metrics = calculate_image_metrics(original, img)
        print(f"{name:<25} {metrics['MSE']:<12.2f} {metrics['PSNR']:<8.2f} {metrics['Correlation']:<12.4f}")

    return enhanced

def demo_ascii_comparison(input_path: str):
    """
    Compare ASCII art generation with and without enhancement.

    Args:
        input_path: Path to input image
    """
    print("\n" + "="*50)
    print("ASCII Art Generation Comparison")
    print("="*50)

    original = Image.open(input_path)
    enhanced = enhance_for_ascii(original)

    # Create ASCII generators
    generator = ASCIIGenerator()

    print("Generating ASCII art from original image...")
    orig_array = get_image_array(original)
    orig_ascii, orig_colors = generator.image_to_ascii(orig_array)

    print("Generating ASCII art from enhanced image...")
    enh_array = get_image_array(enhanced)
    enh_ascii, enh_colors = generator.image_to_ascii(enh_array)

    # Render to images
    generator.render_ascii_image(orig_ascii, orig_colors, "ascii_original.png")
    generator.render_ascii_image(enh_ascii, enh_colors, "ascii_enhanced.png")

    print("✓ ASCII art generated and saved")
    print("  - ascii_original.png: From original image")
    print("  - ascii_enhanced.png: From enhanced image")

    # Compare brightness distributions
    orig_brightness = np.mean(orig_array, axis=(0, 1))
    enh_brightness = np.mean(enh_array, axis=(0, 1))

    print("\nBrightness comparison:")
    print(f"Original RGB: {orig_brightness}")
    print(f"Enhanced RGB: {enh_brightness}")
    print(f"Brightness change: {np.mean(enh_brightness) - np.mean(orig_brightness):.2f}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python demo_enhancements.py <input_image>")
        print("Example: python demo_enhancements.py input.png")
        sys.exit(1)

    input_path = sys.argv[1]

    try:
        # Run enhancement demo
        enhanced = demo_enhancements(input_path)

        # Run ASCII comparison
        demo_ascii_comparison(input_path)

        print("\n" + "="*50)
        print("Demo completed! Check the generated PNG files.")
        print("For ASCII art, use: python src/ascii_generator.py input.png output.png --enhance")
        print("="*50)

    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)