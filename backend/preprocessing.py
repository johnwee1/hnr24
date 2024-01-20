from PIL import Image
from PIL import ImageEnhance
import os


def convert_file(input_image_path):
    filepath, filename = os.path.split(input_image_path)
    filename, ext = os.path.split(filename)
    if ext == ".png":
        image = Image.open(input_image_path).convert("RGB")
        image.save(os.path.join(filepath, f"{filename}.jpg"))
        # OK so now a jpg is created. the old png is still sitting here, by the way. TODO


def preprocessing(input_image_path):
    # changes images to grayscale
    # Open the image file
    original_image = Image.open(input_image_path)
    grayscale_image = original_image.convert("L")

    enhancer = ImageEnhance.Contrast(grayscale_image)
    contrast_factor = 1.8  # >=1 means increased contrast
    contrast_img = enhancer.enhance(contrast_factor)

    # Save the preprocessed image
    contrast_img.save(input_image_path)


def preprocessing_cv2(input_image_path):
    # Read the image using OpenCV
    original_image = cv2.imread(input_image_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Increase contrast using histogram equalization
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    contrast_img = clahe.apply(grayscale_image)

    # Save the preprocessed image
    cv2.imwrite(input_image_path, contrast_img)


# def run_function(ls, function):
#     res = []
#     for i in ls:
#         res.append(function(i))
#     return res


# run_function(images, preprocessing)
