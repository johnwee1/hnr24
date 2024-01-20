import cv2
import os
import numpy as np

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
    # this isn't used.
    if output_path is None:
        # If output path is not specified, set output path as the filename, which should be save.png
        path, ext = os.path.splitext(input_path)
        output_path = f"{path}.png"
    jpeg_image = cv2.imread(input_path)
    cv2.imwrite(
        output_path, jpeg_image, [int(cv2.IMWRITE_PNG_COMPRESSION), COMPRESSION_LEVEL]
    )


def preprocessing_cv2(image_content, override=False):
    """Preprocess an image by converting light-colored background to black and text to white."""

    image = cv2.imdecode(np.frombuffer(image_content, np.uint8), cv2.IMREAD_COLOR)
    print(f"image type = {type(image)}")
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image = cv2.GaussianBlur(image, (9, 9), 0)
    # image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    return image
