import argparse
import os
import sys
from typing import Optional

import numpy as np
from PIL import Image

from . import conversion, minimalistic


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Convert images to ASCII art.")
    parser.add_argument("input_path", help="Path to the input image.")
    parser.add_argument("output_path", nargs='?', help="Path to save the output ASCII art image. If not provided, output to terminal.")
    parser.add_argument("-w", "--width", type=int, default=120, help="The desired width of the output image in characters.")
    parser.add_argument("-m", "--minimalistic", action="store_true", help="Enable minimalistic mode for subject isolation.")
    parser.add_argument("--bg-removal-method", choices=["simple", "ml"], default="ml", help="The method for background removal in minimalistic mode.")
    parser.add_argument("--ml-model", choices=["u2net", "u2netp", "u2net_human_seg", "u2net_cloth_seg", "silueta", "isnet-general-use", "isnet-anime", "sam", "birefnet-general", "birefnet-general-lite", "birefnet-portrait", "birefnet-dis", "birefnet-hrsod", "birefnet-cod", "birefnet-massive"], default="u2net", help="The ML model to use for background removal.")
    parser.add_argument("--dilation-kernel-size", type=int, default=1, help="The kernel size for dilation in background removal.")
    parser.add_argument("--blur-kernel-size", type=int, default=5, help="The kernel size for Gaussian blur on the subject mask.")
    parser.add_argument("--retro", action="store_true", help="Use retro color mode.")
    parser.add_argument("--bw", action="store_true", help="Use black and white mode.")
    parser.add_argument("--gamma", type=float, default=1.0, help="Gamma correction value for colors.")
    parser.add_argument("--brightness", type=float, default=1.0, help="Brightness adjustment factor.")
    parser.add_argument("--contrast", type=float, default=1.0, help="Contrast adjustment factor. ")
    parser.add_argument("--character-ratio", type=float, default=2.0, help="Height-to-width ratio for characters. Only for terminal output.")
    parser.add_argument("--max-height", type=int, default=48, help="Maximum height in characters. Only for terminal output.")
    return parser.parse_args()


def get_mask(image: Image.Image, args: argparse.Namespace) -> Optional[Image.Image]:
    """Generate a background mask based on the selected method."""
    if not args.minimalistic:
        return None

    if args.bg_removal_method == "simple":
        return minimalistic.create_background_mask(image)
    
    # ML method
    removed_bg_image = minimalistic.remove_background_ml(image, args.ml_model)
    # Extract alpha channel to create a mask where 0 (fully transparent) is background
    alpha = np.array(removed_bg_image.split()[-1])
    background_mask = Image.fromarray((alpha == 0).astype(np.uint8) * 255)
    return minimalistic.refine_mask(background_mask, args.dilation_kernel_size)


def main():
    args = parse_args()
    input_path = os.path.abspath(args.input_path)
    output_path = os.path.abspath(args.output_path) if args.output_path else None

    try:
        image = conversion.load_image(input_path)
        image = conversion.adjust_image(image, args.brightness, args.contrast, args.gamma)
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error loading image: {e}", file=sys.stderr)
        sys.exit(1)

    # Calculate target character ratio
    char_ratio = args.character_ratio if output_path is None else conversion.get_character_ratio()
    resized_image = conversion.resize_image(image, args.width, char_ratio)

    if output_path is None:
        # Terminal output
        conversion.print_ascii_art(resized_image, args.retro, args.bw, args.gamma)
        return

    # Image output
    ascii_chars = conversion.image_to_ascii_chars(resized_image)
    background_mask = get_mask(resized_image, args)
    
    output_image = conversion.draw_ascii_art(
        resized_image, 
        ascii_chars, 
        background_mask=background_mask, 
        use_retro=args.retro, 
        use_bw=args.bw, 
        gamma=args.gamma
    )

    try:
        output_image.save(output_path)
    except IOError as e:
        print(f"Error saving output file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

