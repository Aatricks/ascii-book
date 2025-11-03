#!/usr/bin/env python3
"""
ASCII Art Generator - Main CLI script.

Converts images to high-quality colorized ASCII art.
"""

import argparse
import sys
from pathlib import Path

from image_processor import load_image, validate_image_dimensions, get_image_array
from ascii_renderer import ASCIIGenerator
from minimalistic_mode import apply_minimalistic_mode


def main():
    """Main entry point for the ASCII art generator."""
    parser = argparse.ArgumentParser(
        description="Convert images to high-quality colorized ASCII art"
    )
    parser.add_argument(
        "input_image",
        help="Path to input image file"
    )
    parser.add_argument(
        "output_image",
        help="Path to output image file"
    )
    parser.add_argument(
        "--char-width",
        type=int,
        default=8,
        help="Width of each ASCII character in pixels (default: 8)"
    )
    parser.add_argument(
        "--char-height",
        type=int,
        default=12,
        help="Height of each ASCII character in pixels (default: 12)"
    )
    parser.add_argument(
        "--density",
        type=float,
        default=1.0,
        help="Character density multiplier (default: 1.0, higher = more detail)"
    )
    parser.add_argument(
        "--minimalistic",
        action="store_true",
        help="Enable minimalistic mode for edge emphasis"
    )

    args = parser.parse_args()

    try:
        # Validate input file
        input_path = Path(args.input_image)
        if not input_path.exists():
            print(f"Error: Input file '{args.input_image}' does not exist", file=sys.stderr)
            return 1

        output_path = Path(args.output_image)

        # Load and validate image
        print(f"Loading image: {args.input_image}")
        img = load_image(str(input_path))
        validate_image_dimensions(img)

        # Apply minimalistic mode if requested
        if args.minimalistic:
            print("Applying minimalistic mode...")
            img, bg_mask = apply_minimalistic_mode(img)
        else:
            bg_mask = None

        # Get image array
        img_array = get_image_array(img)

        # Create ASCII generator with adjusted density
        char_width = int(args.char_width * args.density)
        char_height = int(args.char_height * args.density)
        generator = ASCIIGenerator(char_width=char_width, char_height=char_height)

        # Generate ASCII art
        print("Generating ASCII art...")
        ascii_grid, color_mappings = generator.image_to_ascii(img_array, bg_mask)

        # Render to image
        print(f"Saving ASCII art to: {args.output_image}")
        generator.render_ascii_image(ascii_grid, color_mappings, str(output_path))

        print("ASCII art generation completed successfully!")
        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())