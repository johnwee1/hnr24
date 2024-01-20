from tesserocr import PyTessBaseAPI
from PIL import Image
from PIL import ImageEnhance
import os

images = ["sample_7.jpeg"]


def convert_file(input_image_path):
    filepath, filename = os.path.split(input_image_path)
    filename, ext = os.path.split(filename)
    if ext == ".jpeg":
        ext = ".jpg"
    elif ext == ".png":
        image = Image.open(input_image_path).convert("RGB")
    image.save(os.path.join(filepath, f"{filename}{ext}"))


def preprocessing(input_image_path):
    # changes images to grayscale
    # Open the image file
    original_image = Image.open(input_image_path)

    # Convert the image to grayscale
    grayscale_image = original_image.convert("L")

    enhancer = ImageEnhance.Contrast(grayscale_image)

    # Adjust the contrast factor (1.0 means no change, values above 1.0 increase contrast)
    contrast_factor = 2  # You can adjust this value based on your preference
    contrast_img = enhancer.enhance(contrast_factor)

    # Save the preprocessed image
    contrast_img.save(input_image_path)


# def run_function(ls, function):
#     res = []
#     for i in ls:
#         res.append(function(i))
#     return res


# run_function(images, preprocessing)

PyTessBaseAPI(path="tessdata_best")
with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(img)
        text = api.GetUTF8Text()
        print(text)
        print(len(text))
        print(api.AllWordConfidences())
# api is automatically finalized when used in a with-statement (context manager).
# otherwise api.End() should be explicitly called when it's no longer needed.
