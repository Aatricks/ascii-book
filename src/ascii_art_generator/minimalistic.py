import cv2
import numpy as np
from PIL import Image
from rembg import remove


def create_background_mask(image, threshold=200):
    """Create a background mask using simple color-based segmentation."""
    grayscale_image = image.convert("L")
    mask = np.array(grayscale_image) > threshold
    return Image.fromarray(mask.astype(np.uint8) * 255, "L")

def emphasize_edges(image, background_mask, blur_kernel_size=5, edge_threshold=100):
    """Find and emphasize the edges of a subject in an image, including direction."""
    # Invert the background mask to get the subject mask
    subject_mask = 255 - np.array(background_mask)

    # Smooth the mask to reduce noise
    if blur_kernel_size > 0:
        if blur_kernel_size % 2 == 0:
            blur_kernel_size += 1
        subject_mask = cv2.GaussianBlur(subject_mask, (blur_kernel_size, blur_kernel_size), 0)

    # Use Sobel to get gradients
    sobel_x = cv2.Sobel(subject_mask, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(subject_mask, cv2.CV_64F, 0, 1, ksize=5)

    # Calculate gradient magnitude and direction
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    angle = np.arctan2(sobel_y, sobel_x) * 180 / np.pi

    # Normalize magnitude
    magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

    # Create an edge mask from magnitude
    edge_mask = (magnitude > edge_threshold).astype(np.uint8)

    # Quantize angle to 4 directions for edge characters matching ascii-view
    # 1: \, 2: _, 3: /, 4: |
    direction_map = np.zeros_like(angle, dtype=np.uint8)
    mask1 = ((22.5 <= angle) & (angle <= 67.5)) | ((-157.5 <= angle) & (angle <= -112.5))
    direction_map[mask1] = 3  # \
    mask2 = ((67.5 <= angle) & (angle <= 112.5)) | ((-112.5 <= angle) & (angle <= -67.5))
    direction_map[mask2] = 2  # _
    mask3 = ((112.5 <= angle) & (angle <= 157.5)) | ((-67.5 <= angle) & (angle <= -22.5))
    direction_map[mask3] = 1  # /
    direction_map[direction_map == 0] = 4  # |

    # Combine magnitude mask with direction map
    final_mask = direction_map * edge_mask

    return Image.fromarray(final_mask, "L")

def refine_mask(mask, dilation_kernel_size=3):
    """Refine a mask by applying dilation."""
    kernel = np.ones((dilation_kernel_size, dilation_kernel_size), np.uint8)
    dilated_mask = cv2.dilate(np.array(mask), kernel, iterations=1)
    return Image.fromarray(dilated_mask)

def remove_background_ml(image):
    """Remove the background from an image using a machine learning model."""
    return remove(image)
