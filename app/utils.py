import cv2
import numpy as np
import pandas as pd
from PIL import Image

def process_image(img_array, canny_threshold1, canny_threshold2):
    # Ensure the image has 3 channels (RGB) before converting to grayscale
    if len(img_array.shape) == 2:  # Image is already grayscale
        gray = img_array
    elif len(img_array.shape) == 3 and img_array.shape[2] == 4:  # Image has an alpha channel
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    else:  # Standard RGB image
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Histogram Equalization
    equalized = cv2.equalizeHist(gray)

    # Noise Reduction (Gaussian Blur)
    blurred = cv2.GaussianBlur(equalized, (5, 5), 0)

    # Edge Detection with Adjustable Thresholds
    edges = cv2.Canny(blurred, canny_threshold1, canny_threshold2)

    # Adaptive Thresholding for Segmentation
    adaptive_thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    return gray, equalized, blurred, edges, adaptive_thresh

def save_image(image_array, filename):
    """ Saves the processed image as a PNG file. """
    image = Image.fromarray(image_array)
    image.save(filename)
    return filename

def convert_to_bytes(filename):
    """ Converts the image file to bytes for download. """
    with open(filename, "rb") as img_file:
        return img_file.read()

def get_image_metadata(image, img_array):
    """ Extracts metadata and returns it as a DataFrame with string values to prevent Arrow errors. """
    metadata = {
        "Property": ["Width", "Height", "Format", "Channels"],
        "Value": [str(image.width), str(image.height), str(image.format), str(img_array.shape[2] if len(img_array.shape) == 3 else 1)]
    }
    return pd.DataFrame(metadata)
