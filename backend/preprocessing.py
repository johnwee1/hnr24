from PIL import Image
from PIL import ImageEnhance
import cv2
import os
import numpy as np
from deskew import Deskew

COMPRESSION_LEVEL = 3

# def convert_file(input_image_path):
#     # converts file from png to jpeg
#     filepath, filename = os.path.split(input_image_path)
#     filename, ext = os.path.split(filename)
#     if ext == ".png":
#         image = Image.open(input_image_path).convert("RGB")
#         image.save(os.path.join(filepath, f"{filename}.jpg"))
#         # OK so now a jpg is created. the old png is still sitting here, by the way. TODO


def convert_to_png(input_path, output_path=None):
    if output_path is None:
        path, ext = os.path.splitext(input_path)
        output_path = f"{path}.png"
    jpeg_image = cv2.imread(input_path)
    cv2.imwrite(
        output_path, jpeg_image, [int(cv2.IMWRITE_PNG_COMPRESSION), COMPRESSION_LEVEL]
    )


def preprocessing_cv2(input_image_path, override=False):
    """Preprocess an image by converting light-colored background to black and text to white."""
    input_image_path = os.path.join(os.path.dirname(__file__), input_image_path)
    # Read the image using OpenCV
    image = cv2.imread(input_image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Save the preprocessed image
    if override:
        output_image_path = input_image_path
    else:
        output_image_name, ext = os.path.splitext(input_image_path)
        output_image_path = f"{output_image_name}.png"
    cv2.imwrite(output_image_path, thresh)
    return input_image_path
