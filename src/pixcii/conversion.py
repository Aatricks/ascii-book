import colorsys

from PIL import Image, ImageDraw, ImageEnhance, ImageFont
from tqdm import tqdm

ASCII_CHARS = " `.:-,';_~/\\\"^><i=!*r+I)(lj?t1}{vf7z|LJcx[]TsYyoFa2#nuZVek3XC4A5PhESU0bpdqK69HORwG8D&gmQ%B$NWM@"

def get_character_ratio():
    font_size = 10
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    bbox = font.getbbox("A")
    char_width = bbox[2] - bbox[0]
    char_height = bbox[3] - bbox[1]
    return char_height / char_width

def get_luminance(pixel: tuple) -> float:
    """Calculate normalized luminance (0.0 to 1.0) from a pixel."""
    if len(pixel) >= 3:
        return (0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]) / 255
    return pixel[0] / 255

def get_ascii_char(luminance: float) -> str:
    """Map normalized luminance to an ASCII character."""
    index = int(luminance * (len(ASCII_CHARS) - 1))
    return ASCII_CHARS[min(index, len(ASCII_CHARS) - 1)]

def get_processed_color(pixel: tuple, use_retro: bool = False, use_bw: bool = False) -> tuple:
    """Apply retro or black-and-white processing to a pixel color."""
    if use_bw:
        gray = int(get_luminance(pixel) * 255)
        return (gray, gray, gray)
    
    if use_retro:
        return get_retro_color(pixel)
    
    if len(pixel) >= 3:
        return (int(pixel[0]), int(pixel[1]), int(pixel[2]))
    
    val = int(pixel[0])
    return (val, val, val)

def load_image(path: str) -> Image.Image:
    """Load an image from a file path."""
    image = Image.open(path)
    return image.convert("RGB")

def adjust_image(image: Image.Image, brightness: float = 1.0, contrast: float = 1.0, gamma: float = 1.0) -> Image.Image:
    """Adjust brightness, contrast, and gamma of the image."""
    if gamma != 1.0:
        image = Image.eval(image, lambda x: int(((x / 255) ** (1 / gamma)) * 255))
    
    if brightness != 1.0:
        image = ImageEnhance.Brightness(image).enhance(brightness)
    
    if contrast != 1.0:
        image = ImageEnhance.Contrast(image).enhance(contrast)
    
    return image

def resize_image(image: Image.Image, new_width: int = 120, character_ratio: float = 1.0) -> Image.Image:
    """Resize an image to a new width, maintaining aspect ratio with character ratio."""
    width, height = image.size
    new_height = int(new_width * height / (character_ratio * width))
    return image.resize((new_width, new_height))

def get_retro_color(pixel: tuple) -> tuple:
    """Get retro quantized color."""
    h, s, v = colorsys.rgb_to_hsv(pixel[0] / 255, pixel[1] / 255, pixel[2] / 255)
    # Quantize hue to 6 intervals (60 degrees each)
    h = round(h * 6) / 6
    # Saturation threshold
    s = 0.0 if s < 0.25 else 1.0
    # Value is always full for retro effect
    r, g, b = colorsys.hsv_to_rgb(h, s, 1.0)
    return (int(r * 255), int(g * 255), int(b * 255))

def image_to_ascii_chars(image: Image.Image) -> str:
    """Convert an image to a list of ASCII characters based on brightness."""
    width, height = image.size
    chars = []
    for y in tqdm(range(height), desc="Converting image to ASCII characters"):
        for x in range(width):
            pixel = image.getpixel((x, y))
            chars.append(get_ascii_char(get_luminance(pixel)))
    return "".join(chars)

def draw_ascii_art(
    image: Image.Image,
    ascii_chars: str,
    background_mask: Image.Image = None,
    use_retro: bool = False,
    use_bw: bool = False,
    gamma: float = 1.0
) -> Image.Image:
    """Draw the ASCII art on a new image canvas with color."""
    width, height = image.size
    font_size = 10
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    bbox = font.getbbox("A")
    char_width = bbox[2] - bbox[0]
    char_height = bbox[3] - bbox[1]
    
    output_image = Image.new("RGB", (width * char_width, height * char_height), "black")
    draw = ImageDraw.Draw(output_image)

    mask_data = background_mask.getdata() if background_mask else None

    for i, char in tqdm(enumerate(ascii_chars), desc="Drawing ASCII art", total=len(ascii_chars)):
        if mask_data and mask_data[i] > 0:
            continue

        x, y = i % width, i // width
        pixel = image.getpixel((x, y))
        color = get_processed_color(pixel, use_retro, use_bw)
        draw.text((x * char_width, y * char_height), char, font=font, fill=color)

    return output_image

def print_ascii_art(
    image: Image.Image,
    use_retro: bool = False,
    use_bw: bool = False,
    gamma: float = 1.0
) -> None:
    """Print ASCII art to terminal with color."""
    width, height = image.size

    for y in tqdm(range(height), desc="Printing ASCII art"):
        line = []
        for x in range(width):
            pixel = image.getpixel((x, y))
            lum = get_luminance(pixel)
            char = get_ascii_char(lum)
            r, g, b = get_processed_color(pixel, use_retro, use_bw)
            line.append(f"\x1b[38;2;{r};{g};{b}m{char}")
        print("".join(line))
    print("\x1b[0m", end="")

